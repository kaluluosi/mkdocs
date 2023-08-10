# 翻译

主题本地化指南。---

MkDocs提供的[内置主题]支持翻译。这是面向翻译人员的指南，说明了为贡献新的翻译和/或更新现有翻译所需遵循的流程。有关修改现有主题的指导，请参见[贡献指南][更新主题]。要启用特定的翻译，请查看您在[用户指南][内置主题]中使用的特定主题的文档。对于第三方主题的翻译，请参见这些主题的文档。为了让第三方主题使用MkDocs的翻译工具和方法，必须正确[配置]该主题以使用这些工具。注意：翻译仅适用于主题模板中包含的文本，例如“下一个”和“上一个”链接。页面的Markdown内容没有被翻译。如果您希望创建多语言文档，请将主题本地化与第三方国际化/本地化插件相结合。[内置主题]：../ user-guide / choosing-your-theme.md [更新主题]：../ about / contributing.md＃提交内置主题更改 [配置]：themes.md＃supporting-theme-localizationtranslation

## 本地化工具先决条件

主题本地化使用[babel]项目生成和编译本地化文件。您需要从您的本地机器的git工作树中使用翻译命令。有关如何[进行开发安装]和[提交拉取请求]的指示，请参阅[贡献指南]。本文档中的说明假定您正在使用正确配置的开发环境。确保环境中已安装翻译要求：

```bash
pip install mkdocs[i18n]
```

[小屋]：https://babel.pocoo.org/en/latest/cmdline.html [贡献指南]：../ about / contributing.md [安装开发]：../ about / contributing.md＃安装开发 [提交拉取请求]：../ about / contributing.md#submitting-pull-requests

## 在主题中添加语言翻译

如果您最喜欢的语言区域设置尚未受到内置主题（`mkdocs`和`readthedocs`）的支持，则可以按照以下步骤轻松贡献翻译。以下是您需要做的概要：

1。[分叉和克隆MkDocs存储库]（＃fork-and-clone-the-mkdocs-repository）然后[安装用于开发的MkDocs]（../ about / contributing.md＃安装用于开发）以添加和测试翻译。2。[初始化新的本地化目录]（＃initializing-the-localization-catalogs）以使用您的语言（如果已存在区域设置的翻译，请按照[更新主题本地化文件]的说明。）3。[为每个本地化目录中的文本占位符添加翻译]（＃translating-the-mkdocs-themes）。4。[本地服务和测试]翻译后的语言的主题（＃testing-theme-translations）。5。[更新有关已翻译主题的支持文档]（＃updating-them-documentation）。6。通过拉取请求贡献翻译（＃contributing-translations）。注意：翻译语言环境通常使用[ISO-639-1]（2个字母）语言代码进行标识。虽然还支持地域/地区/县代码，但只有在完成了通用语言翻译并且区域方言需要使用与通用语言翻译不同的术语时，才应添加特定于位置的翻译。[ISO-639-1]：https://en.wikipedia.org/wiki/ISO_639-1

### Fork和克隆MkDocs库

在接下来的步骤中，您将使用MkDocs存储库的分支。请遵循[分叉和克隆MkDocs存储库]的说明。要测试翻译，您还需要从您的分支[为开发安装MkDocs]。###初始化本地化目录

每个主题的模板都包含已提取为可移植对象模板（`messages.pot`）文件的文本占位符，该文件位于每个主题的文件夹中。初始化目录包括运行一个命令，该命令将为所需的语言创建目录结构，并从主题的POT文件派生可移植对象（`messages.po`）文件。在主题的每个目录上使用`init_catalog`命令，并提供适当的语言代码（`-l<language>`）。这个语言代码几乎总是只有两个小写字母，比如说`sv`，但在某些情况下它需要进一步进行模糊分辨。见：

* [内置主题的已翻译语言]（../ user-guide / choosing-your-theme.md#mkdocs-locale）
* [ISO 639语言清单]（https://www.localeplanet.com/icu/iso639.html）
* [语言子标记注册表]（https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry）

特别是，要知道`pt`语言应该由`pt_PT`和`pt_BR`进行歧义消除，是因为* Language subtag register *页面包含您搜索`pt-`，而`s`应保持为`s`，因为该页面并不包含`sv-`。所以，如果我们选择西班牙语（`es`）作为示例语言代码，在两个内置主题中添加其翻译，则运行以下命令：

```bash
pybabel init --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l es
pybabel init --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l es
```

以上命令将创建以下文件结构：

```text
mkdocs/themes/mkdocs/locales
├── es
│   └── LC_MESSAGES
│       └── messages.po
```

现在您可以进行下一步并为本地化的目录中的每个文本占位符[添加翻译]。＃在翻译的目录中添加翻译

如果主题的`messages.pot`模板文件自您的语言环境的`messages.po`上次更新以来进行[更新]，请按照以下步骤更新主题的`messages.po`文件：

1。[更新主题的翻译目录]（＃updating-the-translation-catalogs），刷新每个主题的可翻译文本占位符。2。在每个“messages.po”目录文件语言上[翻译]（＃translating-the-mkdocs-themes）新添加的可翻译文本占位符。3。[本地服务和测试]已翻译的语言的主题（＃testing-theme-translations）。4。通过拉取请求[贡献翻译]（＃contributing-translations）。###更新翻译目录

在为您希望为其提供翻译的每种语言方案做出更改后，应完成此步骤。为了更新两个内置主题的`fr`翻译目录，请使用以下命令：

```bash
pybabel update --ignore-obsolete --update-header-comment --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l fr
pybabel updatexxx --ignore-obsolete --update-header-comment --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l fr
```

现在，您可以转到下一步并[添加翻译]以适合本地化目录中更新的文本占位符。[添加翻译]：＃在翻译的目录中添加翻译

###翻译MkDocs主题

现在，您的本地化`messages.po`文件已经准备就绪，您只需要为每个文件中的每个`msgid`项目中的每个`msgstr`项目添加翻译。```text
msgid "Next"
msgstr "Siguiente"
```

警告：
不要修改`msgid`，因为它对所有翻译通用。只需在`msgstr`项目中添加其翻译即可。完成所有在`po`文件中列出的术语的翻译后，您将需要[测试本地化的主题]（＃testing-theme-translations）。###测试主题翻译

要测试已翻译的主题，您首先需要将主题的`messages.po`文件编译为`messages.mo`文件。以下命令将为两个内置主题编译`es`翻译：

```bash
pybabel compile --statistics --directory mkdocs/themes/mkdocs/locales -l es
pybabel compile --statistics --directory mkdocs/themes/readthedocs/locales -l es
```

上述命令的结果如下文件结构：

```text
mkdocs/themes/mkdocs/locales
├── es
│   └── LC_MESSAGES
│       ├── messages.mo
│       └── messages.po
```

请注意，编译后的`messages.mo`文件是基于您刚刚编辑的`messages.po`文件生成的。然后，在项目根目录下修改`mkdocs.yml`文件以测试新的和/或更新的语言环境：

```yaml
theme:
  name: mkdocs
  locale: es
```

最后，运行`mkdocs serve`以查看您的主题的新本地化版本。>注意：
生成和发布过程会处理所有区域设置，将所有区域设置分配给最终用户，因此您只需要担心贡献实际的文本翻译`messages.po`文件（git会忽略其他文件）。>
在完成测试后，请务必在提交更改之前撤消`mkdocs.yml`文件中的`locale`设置更改。##更新主题文档

页面[选择您的主题]（../user-guide/choosing-your-theme.md）会自动更新，其中包含所有可用的语言环境选项。##贡献翻译

现在是您为该项目[做出贡献]（../about/contributing.md）的好时节。谢谢！