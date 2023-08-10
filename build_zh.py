import shutil
import glob
import os
import openai
import nltk
from tqdm import trange
import logging
from contextlib import contextmanager

nltk.download("punkt")

logging.basicConfig(filename="translate.log", filemode='w', level=logging.INFO)
log = logging.getLogger("translate")


openai.api_key = "f6438b715aa8473f917b5fe5968db5c3"
openai.api_base = "https://dxgpt.openai.azure.com/"
openai.api_type = "azure"
openai.api_version = "2023-05-15"

DOCS_PATH = "docs"
DOCS_BAK_PATH = "docs_bak"
DOCS_ZH_PATH = "docs_zh"

START_PROMPT = """
    你现在是一个markdown文档翻译器，我先面会把整个英文markdown文档发送给你，你按照原来的markdown的格式翻译成中文返回给我。不要破坏markdown语法，不要将用中文全角标点，继续沿用英文标点。
    """
DEPLOYMENT_NAME = "dxgpt35"
MAX_TOKENS = 4000


@contextmanager
def start_translate():
    if not os.path.exists(DOCS_ZH_PATH):
        shutil.copytree(DOCS_PATH, DOCS_ZH_PATH)
    yield


def to_segment(doc: str):
    sents = nltk.sent_tokenize(doc)

    current_seg = ""
    token_counter = 0
    for sent in sents:
        tokens = nltk.word_tokenize(sent)
        if token_counter + len(tokens) >= MAX_TOKENS:
            yield current_seg
            current_seg = ""
            token_counter = 0
        else:
            token_counter += len(tokens)
            current_seg += sent

    yield current_seg


def translate(doc_path: str):
    try_times = 0
    max_try_times = 5
    total_txt = ""
    with open(doc_path, encoding='utf-8') as f:
        doc = f.read()
        segs = to_segment(doc)
        for seg in segs:
            while try_times < max_try_times:
                try:
                    response = openai.ChatCompletion.create(
                        engine=DEPLOYMENT_NAME,
                        messages=[
                            {"role": "system", "content": START_PROMPT},
                            {"role": "user", "content": seg},
                        ],
                    )
                    txt = response['choices'][0]['message']['content']
                    total_txt += txt
                    break
                except Exception as e:
                    try_times += 1
                    print(e, type(e))
                    print(doc_path, "翻译失败")
                    return None

        return total_txt


def is_translated(doc_path: str):
    with open("translate.log") as f:
        logs = f.read()
        return doc_path in logs


with start_translate():
    print("开始翻译...")

    doc_paths = glob.glob("docs_zh/**/*.md", recursive=True)

    for index in trange(len(doc_paths)):
        doc_path = doc_paths[index]

        if is_translated(doc_path):
            continue

        translated_doc = translate(doc_path)

        if translated_doc is None:
            continue

        with open(doc_path, mode='w', encoding='utf-8') as f:
            f.write(translated_doc)
            log.info(doc_path)
            print(doc_path, "翻译结束")

    print("翻译结束")
