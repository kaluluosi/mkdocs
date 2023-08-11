# 翻译

主题本地化指南。

---

MkDocs提供的[内置主题]支持翻译。本指南面向译者，记录了为添加新的翻译和/或更新现有翻译所需的流程。关于修改现有主题的指南，请参见[Contributing Guide][update themes]。要启用特定翻译，请参阅[用户指南][built-in themes]中使用的特定主题的文档。有关第三方主题的翻译，请参见这些主题的文档。为了让第三方主题使用MkDocs的翻译工具和方法，该主题必须正确[配置]来使用这些工具。

注意:
翻译仅适用于主题模板中包含的文本，例如“next”和“previous”链接。页面的Markdown内容不会被翻译。如果您希望创建多语言文档，请将主题本地化与第三方国际化/本地化插件相结合使用。

[built-in themes]: ../user-guide/choosing-your-theme.md
[update themes]: ../about/contributing.md#submitting-changes-to-the-builtin-themes
[configured]: themes.md#supporting-theme-localizationtranslation

## 本地化工具先决条件

主题本地化使用[babel]项目生成和编译本地化文件。您需要在本地计算机上使用git工作树才能使用翻译命令。

请参见[Contributing Guide]，了解如何[安装开发环境]和[提交拉取请求]。本文档中的说明假定您正在使用正确配置的开发环境工作。

确保在您的环境中安装了翻译要求：

```bash
pip install mkdocs[i18n]
```

[babel]: https://babel.pocoo.org/en/latest/cmdline.html
[Contributing Guide]: ../about/contributing.md
[Install for Development]: ../about/contributing.md#installing-for-development
[Submit a Pull Request]: ../about/contributing.md#submitting-pull-requests

## 将语言翻译添加到主题

如果您最喜欢的语言语言环境尚未受到内置主题（`mkdocs`和`readthedocs`）的支持，则可以按照以下步骤轻松地通过添加翻译来做出贡献。

以下是您需要执行的快速摘要：

1. [分叉和克隆MkDocs存储库]（#fork-and-clone-the-mkdocs-repository），然后[安装MkDocs进行开发]（../about/contributing.md#installing-for-development）以添加和测试翻译。
2. [初始化新的本地化目录]（#initializing-the-localization-catalogs）适合您的语言（如果您的地区语言环境已经存在翻译，请按照[更新主题本地化文件]的说明进行操作）。
3. [为本地化的目录一次添加一个翻译]（#translating-the-mkdocs-themes）每个文本占位符。
4. [本地化服务并测试]（#testing-theme-translations）翻译后的语言。
5. [更新有关已翻译主题支持的文档]（#updating-theme-documentation）。
6. [通过拉取请求]（#contributing-translations）贡献您的翻译。

注意:
通常使用[ISO-639-1]（2个字母）的语言代码标识翻译语言环境。虽然也支持区域/地区/县代码，但是只有在完成了通用语言翻译并且地区方言需要使用与通用语言翻译不同的术语时，才应添加特定地区的翻译。

[ISO-639-1]：https://en.wikipedia.org/wiki/ISO_639-1

### 分叉和克隆MkDocs存储库

在以下步骤中，您将使用MkDocs存储库的分支。遵循说明[分叉和克隆MkDocs)存储库](../about/contributing.md#installing-for-development)。

要测试翻译，您还需要从您的分支[安装MkDocs进行开发]。

### 初始化的本地化目录

每个主题的模板都包含已提取到可移植对象模板（“messages.pot”）文件中的文本占位符，该文件位于每个主题的文件夹中。

初始化目录包括运行一个命令，该命令将为所需语言创建目录结构，并从主题的pot文件派生一个可移植对象（"messages.po"）文件。

在每个主题的目录中使用“init_catalog”命令，并提供适当的语言代码（"-l <语言>"）。

语言代码几乎总是只有两个小写字母，例如`sv`，但在某些情况下需要进一步消除歧义。

见：

* [已翻译内置主题的语言]（../user-guide/choosing-your-theme.md # mkdocs-locale）
* [ISO 639语言列表]（https://www.localeplanet.com/icu/iso639.html）
* [语言子标记注册表]（https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry）

特别是，要了解`pt`语言应该恰当地将其作为`pt_PT`和`pt_BR`进行区分的方式是* Language subtag registry *页面中包含`pt-`，如果搜索该页面，就会发现。而“sv”应保持为“sv”，因为该页面不包含“sv-”。

因此，如果我们选择`es`（西班牙语）作为示例语言代码，在两个内置主题中都为其添加翻译，请运行以下命令：

```bash
pybabel init --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l es
pybabel init --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l es
```

上面的命令将创建以下文件结构：

```text
mkdocs/themes/mkdocs/locales
├── es
│   └── LC_MESSAGES
│       └── messages.po
```

现在可以继续下一步并为本地化的目录中的每个文本占位符添加翻译。

## 更新主题翻译

如果此主题的“messages.pot”模板文件自上次更新您的语言环境的“messages.po”文件以来已[更新] [update themes]，则按照以下步骤更新主题的“messages.po”文件：

1. [更新主题的本地化目录]（#updating-the-translation-catalogs）以刷新每个主题的可翻译文本占位符。
2. 在每个`messages.po`目录文件语言上[翻译]（#translating-the-mkdocs-themes）新添加的可翻译文本占位符。
3. [本地化服务并测试]（#testing-theme-translations）翻译后的主题语言。
4. [通过拉取请求贡献您的翻译]（#contributing-translations）。

### 更新翻译目录

只要安装主题的模板已经[更新] [update themes]为您希望为其做出贡献的每种语言，就应完成此步骤。

要更新两种内置主题的“fr”翻译目录，请使用以下命令：

```bash
pybabel update --ignore-obsolete --update-header-comment --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l fr
pybabel update --ignore-obsolete --update-header-comment --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l fr
```

现在可以继续下一步，并为每个本地化目录中已更新的文本占位符添加[翻译]。

[添加翻译]：#translating-the-mkdocs-themes

### 翻译MkDocs主题

由于您的本地化`messages.po`文件已准备好，因此您只需要在文件中为每个`msgstr`项目添加翻译，以至于为每个`msgid`项目添加翻译。

```text
msgid "Next"
msgstr "Siguiente"
```

警告:
不要修改`msgid`，因为它通常适用于所有翻译。只需在`msgstr`项目中添加其翻译即可。

完成所有列在“po”文件中的术语翻译后，您将要[测试本地化主题]（#testing-theme-translations）。

### 测试主题翻译

要测试使用翻译的主题，请首先将主题的“messages.po”文件编译为“messages.mo”文件。以下命令将编译两种内置主题的“es”翻译：

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

请注意，已编译的“messages.mo”文件是基于您刚刚编辑的“messages.po”文件生成的。

然后修改项目根目录中的“mkdocs.yml”文件，以测试新的本地化和/或更新的语言环境：

```yaml
theme:
  name: mkdocs
  locale: es
```

最后，运行“mkdocs serve”以查看主题的新本地化版本。

> 注意：
> 构建和发布过程负责编译和分发
> 所有语言环境供最终用户使用，因此您只需要担心贡献实际文本翻译`messages.po`文件
> （其余内容将被git忽略）。
>
> 在完成测试工作后，请务必在提交更改之前撤消`mkdocs.yml`文件中`locale`设置的更改。

## 更新主题文档

页面[选择您的主题]（../user-guide/choosing-your-theme.md）会自动更新，以根据所有可用的本地环境选项更新。

## 贡献翻译

现在到了[贡献]（../about/contributing.md）您的美好工作的时候了
该项目。谢谢！