# 翻译

主题本地化指南。

---

MkDocs提供的[内置主题]支持翻译。本文档是为翻译者制作的，记录了投稿新翻译和/或更新现有翻译的流程。有关修改现有主题的指导，请参见[贡献指南][更新主题]。要启用特定的翻译，请参阅您在[用户指南][内置主题]中使用的特定主题的文档。有关第三方主题的翻译，请参见这些主题的文档。为了让第三方主题使用MkDocs的翻译工具和方法，该主题必须正确地[配置]以利用这些工具。

注意：
翻译仅适用于主题模板中包含的文本，例如“下一页”和“上一页”链接。页面的Markdown内容不会被翻译。如果您希望创建多语言文档，请将主题本地化与第三方国际化/本地化插件相结合。

[内置主题]：../用户指南/选择您的主题.md
[更新主题]：../关于/贡献.md＃提交更改到内置主题
[配置]：主题.md＃支持主题本地化翻译

## 本地化工具先决条件

主题本地化使用[babel]项目生成和编译本地化文件。您需要从本地机器上的git工作树上工作，以使用翻译命令。

有关如何[安装开发]程序并[提交拉取请求]的说明，请参见[贡献指南]。本文档中的说明假定您正在使用正确配置的开发环境。

确保在环境中安装了翻译要求：

““ ”bash
pip install mkdocs[i18n]
““”

[babel]：https://babel.pocoo.org/en/latest/cmdline.html
[Contributing Guide]：../about/contributing.md
[安装开发]：“../about/contributing.md＃installing-for-development”
[提交拉取请求]：“../about/contributing.md＃submitting-pull-requests”

## 将语言翻译添加到主题

如果您最喜欢的语言环境尚未支持内置主题（mkdocs和readthedocs之一或两者），则可以按照以下步骤轻松贡献翻译。

这是您需要做的简要总结：

1. [Fork and clone the MkDocs repository] （＃fork-and-clone-the-mkdocs-repository）然后[安装MkDocs进行开发]（../ about / contributing.md＃installing-for-development）以添加和测试翻译。
2. [Initialize new localization catalogs]（# initializing-the-localization-catalogs），为您的语言准备一个便携式对象，如果您的语言环境已经有翻译，请按照[更新主题本地化文件]的说明操作。
3. [为本地化目录中的每个文本占位符添加翻译]（＃translating-the-mkdocs-themes）。
4. [本地提供和测试]（# testing-theme-translations）您的语言的翻译主题。
5. [更新文档]（＃updating-theme-documentation）有关每个翻译主题支持的翻译的文档。
6. [通过拉取请求贡献您的翻译]（＃contributing-translations）。

注意：
翻译区域通常使用[ISO-639-1]（2个字符）语言代码来标识。虽然也支持领土/地区/县代码，但应仅在完成常规语言翻译并且区域方言需要使用与一般语言翻译不同的术语时添加。

[ISO-639-1]：https://en.wikipedia.org/wiki/ISO_639-1

### Fork and clone the MkDocs repository

在接下来的步骤中，您将使用MkDocs存储库的副本。请按照说明进行操作[关于贡献]来[forking and cloning the MkDocs repository]。

要测试翻译，您还需要从您的fork [安装MkDocs进行开发]。

### 初始化本地化目录

每个主题的模板都包含已提取为便携式对象模板（messages.pot）文件的文本占位符，该文件位于每个主题的文件夹中。

初始化目录包括运行命令，该命令将为所需语言创建目录结构，并准备从主题的“pot”文件派生的可便携式对象（“messages.po”）文件。

在每个主题的目录上使用“init_catalog”命令，并提供适当的语言代码（“-l＆lt; language>”）。

语言代码通常只有两个小写字母，例如“sv”，但在某些情况下，它需要进一步阐明。

看：

*[内置主题的已翻译语言]（../user-guide/choosing-your-theme.md#mkdocs-locale）
* [ISO 639语言列表]（https://www.localeplanet.com/icu/iso639.html）
* [语言子标记注册表]（https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry）

特别是，要知道“pt”语言应该解释为“pt_PT”和“pt_BR”的方法是搜索“Language subtag registry”页面中是否包含“pt-”。而“sv”应保持为“sv”，因为该页面不包含“sv-”。

因此，如果我们选择将“es”（西班牙语）作为示例语言代码，为内置主题添加该语言的翻译，可以运行以下命令：

““ ”bash
pybabel init --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l es
pybabel init --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l es
““”

以上命令将创建如下文件结构：

““ ”text
mkdocs/themes/mkdocs/locales
├─es
│ └─LC_MESSAGES
│ └─messages.po
““”

您现在可以继续进行下一步，并[在本地化目录中的每个文本占位符中添加翻译]。

## 更新主题翻译

如果自上次更新了主题的“messages.pot”模板文件以来已更新了主题的“messages.po”，则请按照以下步骤更新主题的“messages.po”文件：

1. [更新主题的翻译目录]（# updating-the-translation-catalogs），以刷新每个主题的可翻译文本占位符。
2. [翻译]（#translating-the-mkdocs-themes）新添加的可翻译文本占位符在每个“messages.po”目录文件语言上。
3. [测试并测试]（# testing-theme-translations）您的语言的翻译主题。
4. [通过拉取请求捐赠]（＃contributing-translations）您的翻译。

### 更新翻译目录

此步骤应在主题模板为您希望为其贡献翻译的每个语言更改后完成。

要更新内置主题的两个目录的“fr”翻译目录，请使用以下命令：

““ ”bash
pybabel update --ignore-obsolete --update-header-comment --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l fr
pybabel update --ignore-obsolete --update-header-comment --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l fr
““”

您现在可以继续进行下一步，并[添加翻译]以本地化目录中每个更新文本占位符的翻译。

[添加翻译]：＃translating-the-mkdocs-themes

### 翻译MkDocs主题

现在，您的本地化“messages.po”文件已准备就绪，您只需为每个文件中的每个“msgid”项添加“msgstr”项中的翻译即可。

““ ”text
msgid “Next”
msgstr“Siguiente”
““”

警告：
不要修改msgid，因为它对所有翻译通用。只需在msgstr项中添加其翻译。

完成翻译po文件中列出的所有术语后，您将要[测试本地化主题]（＃testing-theme-translations）。

### 测试主题翻译

要测试有翻译的主题，您需要首先将主题的“messages.po”文件编译为“messages.mo”文件。以下命令将编译两个内置主题的“es”翻译：

““ ”bash
pybabel compile --statistics --directory mkdocs/themes/mkdocs/locales -l es
pybabel compile --statistics --directory mkdocs/themes/readthedocs/locales -l es
““”

以上命令会产生以下文件结构：

““ ”text
mkdocs/themes/mkdocs/locales
├─es
│ └─LC_MESSAGES
│ ├──messages.mo
│ └─messages.po
““”

请注意，编译的“messages.mo”文件是根据您刚编辑的“messages.po”文件生成的。

然后，修改项目根目录中的“mkdocs.yml”文件，以测试新的和/或更新的语言环境：

““ ”yaml
主题：
  名字：mkdocs
  locale：es
““”

最后，运行“mkdocs serve”，查看主题的新本地化版本。

>注意：
>构建和发布过程负责编译和分发
>所有语言环境给最终用户，因此您只需要关注
>实际文本翻译`messages.po`文件（其余git被忽略）。
>
>完成测试后，请记得撤消更改
>Mkdocs.yml文件中的“locale”设置，然后提交
>更改。

## 更新主题文档

[选择您的主题]页面更新为所有可用的语言环境。

## 捐赠翻译

现在是时候为您的项目做出贡献了。谢谢！