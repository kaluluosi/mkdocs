# 更新说明

---


## 升级

升级MkDocs到最新版本，请使用pip：

```bash
pip install -U mkdocs
```

可使用`mkdocs --version`来确定当前已安装的版本：

```console
$ mkdocs --version
mkdocs, version 1.5.0 from /path/to/mkdocs (Python 3.10)
```

## 维护团队

MkDocs团队的现任和前任成员。
* [@tomchristie](https://github.com/tomchristie/)
* [@d0ugal](https://github.com/d0ugal/)
* [@waylan](https://github.com/waylan/)
* [@oprypin](https://github.com/oprypin/)
* [@ultrabug](https://github.com/ultrabug/)

## 版本 1.5.2 (2023-08-02)

*   Bugfix (1.5.0中的回归): 恢复`--no-livereload`的功能。(#3320)

*   Bugfix (1.5.0中的回归): 新的页面标题检测有时会无法删除锚链接-修复一下这个问题。 (#3325)

*   部分恢复1.5版API：`extra_javascript` 项将再次主要是字符串，并且仅在额外的`script`功能被使用时才为`ExtraStringValue`。插件可以自由地向`config.extra_javascript`追加字符串，但是在读取值时，它们仍然必须确保将其视为`str（value）`，以防它是`ExtraScriptValue`项。要查询`.type`等属性，您需要先检查`isinstance`。静态类型检查将引导您在其中进行。(#3324)

请参见[提交日志](https://github.com/mkdocs/mkdocs/compare/1.5.1...1.5.2)。

## 版本 1.5.1 (2023-07-28)

*   Bugfix (1.5.0中的回归): 使`ExtraScriptValue`可以视为路径。这使得某些插件仍然可以使用，尽管有破坏性的更改。*   Bugfix （1.5.0中的回归）：避免用3个冲突文件（例如' index.html`，`index.md`和`README.md`)导致错误(#3314)

请参见[提交日志](https://github.com/mkdocs/mkdocs/compare/1.5.0...1.5.1)。

## 版本 1.5.0 (2023-07-26)

### 新命令 `mkdocs get-deps`

该命令会猜测MkDocs网站所需的Python依赖项，以便构建。它只需打印需要安装的PyPI软件包。在终端中，它可以直接与安装命令结合使用，如下所示：

```bash
pip install $(mkdocs get-deps)
```

理念是在运行此命令后，您可以直接跟随 `mkdocs build` 命令，它几乎总是“正常工作”，无需考虑要安装的依赖关系。它的工作原理是通过扫描 `mkdocs.yml 中的' themes:`， `plugins:` 和` markdown_extensions:` 项，并根据大型已知项目目录列表进行反向查找。当然，您可以使用一个“virtualenv”来使用这样的命令。另请注意，对于需要稳定性的环境（例如CI），直接以这种方式安装依赖项不是很可靠，因为会破坏依赖项固定。该命令允许覆盖使用哪个配置文件（而不是当前目录中的m `kdocs.yml`）以及使用哪个项目目录列表（而不是从默认位置下载它）。请参见[`mkdocs get-deps --help`](../user-guide/cli.md#mkdocs-get-deps)。上下文：#3205

### MkDocs具有官方的插件目录

请查看<https://github.com/mkdocs/catalog>并将所有通用插件、主题和扩展添加到其中，以便可以通过`mkdocs get-deps`进行查找。这被重命名为“best-of-mkdocs”并收到了重大更新。除了pip安装命令之外，该页面现在还显示了添加插件所需的配置样板。### 扩展验证链接

#### 验证的Markdown中的链接

> 正如您可能已经知道的，对于Markdown，MkDocs实际上只识别导致另一个物理`*.md`文档（或媒体文件）的相对链接。这是一个好的惯例，因为然后源页面也可以在没有MkDocs的情况下自由浏览，例如GitHub。MkDocs知道在输出中应该将这些`* .md`链接转换为适当的`* .html`，并且如果此类链接实际上没有导向现有文件，则始终会告诉您。然而，链接的检查非常松散，有许多让步。例如，链接以`/`（“绝对”）开头以及链接以`/`结尾的链接保持不变，没有显示任何警告，这使得此类非常脆弱的链接混入了网站源文件：链接当前可能正常工作，但是没有得到验证并且令人困惑，需要使用`use_directory_urls`启用额外的级别的`..`。现在，除了检查相对链接之外，MkDocs还会为未识别的链接类型（包括绝对链接）打印`INFO`消息。它们看起来像这样：

```text
INFO - Doc file 'example.md' contains an absolute link '/foo/bar/', it was left as is.Did you mean `foo/bar.md'?```

如果您不想进行任何更改，甚至`INFO`消息，希望恢复到MkDocs 1.4的安静状态，请将以下配置添加到`mkdocs.yml`中（**不**建议使用）：

```yaml
validation:
  absolute_links: ignore
  unrecognized_links: ignore
```

如果你想让它们打印`WARNING`消息并导致`mkdocs build --strict`失败，你应该将它们配置为`warn`。请查看[**documentation**](../user-guide/configuration.md#validation)，以了解实际建议的设置和更多详细信息。上下文：#3283

#### 在nav中验证链接

现在，在[`nav`配置](../user-guide/configuration.md#nav)中的文档链接也具有可以配置的验证功能，尽管默认情况下没有更改。您可以启用未在nav中的文件的验证。例如：

```yaml
validation:
  nav:
    omitted_files: warn
    absolute_links: warn
```

如果我们想要在文件夹中的某些页面没有列在“nav”配置中的情况下打印出警告信息，那么可以这样做：

```text
INFO - The following pages exist in the docs directory, but are not included in the "nav" configuration: ...
```

请参见[**documentation**](../user-guide/configuration.md#validation)。上下文：#3283, #1755

#### 标记为“不在nav中”

有一个新的配置`not_in_nav`。它使您可以将特定的文件模式标记为免于上述“omitted_files”警告类型；对于它们不会再打印任何消息。 （作为推论，将此配置设置为 `*` 等同于完全忽略 `omitted_files`）。如果您通常喜欢这些关于从nav中遗漏的文件的警告，但仍有一些页面，您明知道从nav中排除了这些页面，只是想构建和复制它们。除了上述“not_in_nav”配置之外，还可以使用一种类似于gitignore的模式。请参见下一节，以了解另一种需要使用此类配置的说明。请参见[**documentation**](../user-guide/configuration.md#not_in_nav)。上下文：#3224, #1888

### 排除文档文件

有一个新的配置`exclude_docs`，告诉MkDocs忽略位于`docs_dir`下的某些文件，并将它们不作为构建的一部分复制到`site`。历史上，MkDocs一直会忽略以句点开头的文件名，那就是全部。现在都可以进行配置，可以取消忽略这些，或者忽略更多模式的文件。 `exclude_docs`配置遵循[.gitignore模式格式](https://git-scm.com/docs/gitignore#_pattern_format)，并指定为多行YAML字符串。例如：

```yaml
exclude_docs: |
  *.py               # Excludes e.g.docs/hooks/foo.py
  /drafts            # Excludes e.g.docs/drafts/hello.md
  /requirements.txt  # Excludes docs/requirements.txt
```

链接的验证（以上述方式描述）也会受到`exclude_docs`的很好的，我理解了你的要求。请您发送英文markdown文档给我，我会尽快将其翻译为中文。