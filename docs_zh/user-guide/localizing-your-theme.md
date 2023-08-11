# 本地化您的主题

在您喜欢的语言下展示您的主题。

---

注：
主题本地化只翻译主题本身的文本元素（如“下一页”和“上一页”链接），而不是您的文档的实际内容。
如果您希望创建多语言文档，您需要将此处描述的主题本地化与第三方国际化/本地化插件相结合。

## 安装

要使主题本地化工作，您必须使用支持它的主题，并通过安装`mkdocs[i18n]`启用`i18n`（国际化）支持：

```bash
pip install mkdocs[i18n]
```

## 支持的语言环境

在大多数情况下，语言环境由您的语言的[ISO-639-1]（2字母）缩写来指定。然而，语言环境还可能包括领土（或区域或国家）代码。语言和领土必须用下划线分隔。例如，英语的一些可能的语言环境包括`en`，`en_AU`，`en_GB`和`en_US`。

有关主题支持的语言环境列表，请参阅该主题的文档。

- [mkdocs](choosing-your-theme.md#mkdocs-locale)
- [readthedocs](choosing-your-theme.md#readthedocs-locale)

警告：
如果您配置了主题尚不支持的语言环境，则MkDocs将退回到主题的默认语言环境。

## 使用方法

为了指定MkDocs应该使用的本地环境，请将[theme]配置选项的[locale]参数设置为相应的代码。

例如，要在法语下构建`mkdocs`主题，您可以在您的`mkdocs.yml`配置文件中使用以下内容：

```yaml
theme:
  name: mkdocs
  locale: fr
```

## 贡献主题翻译

如果某个主题尚未翻译为您的语言，请随时使用[翻译指南]进行翻译。

[翻译指南]: ../dev-guide/translations.md
[locale]: configuration.md#locale
[theme]: configuration.md#theme
[ISO-639-1]: https://en.wikipedia.org/wiki/ISO_639-1