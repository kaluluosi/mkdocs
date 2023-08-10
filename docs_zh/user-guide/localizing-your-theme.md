# 本地化你的主题

在你钟意的语言中展示你的主题。

注意：
主题本地化只翻译主题本身的文字元素（如“下一页”和“上一页”链接），而不是你的文档实际内容。如果你想创建多语言文档，你需要将本地化主题与第三方国际化/本地化插件结合使用。

## 安装

为了使主题本地化生效，你必须使用支持该功能并安装了`mkdocs [i18n]`的主题：

```bash
pip install mkdocs[i18n]
```

## 支持的语言环境

在大多数情况下，使用 [ISO-639-1]（2 个字母）缩写来指定语言环境。然而，语言环境可能还包括领土（或地区或国家）代码。语言和领土之间必须使用下划线分隔。例如，英语的一些可能的语言环境包括 `en`、`en_AU`、`en_GB` 和 `en_US`。有关所使用主题支持的语言环境列表，请参阅该主题的文档。

- [mkdocs](choosing-your-theme.md#mkdocs-locale)
- [readthedocs](choosing-your-theme.md#readthedocs-locale)

警告：
如果你配置了一个未被所使用的主题支持的语言环境，MkDocs 将使用主题的默认语言环境。

## 用法

要指定 MkDocs 应使用的语言环境，请将 [theme] 配置选项的 [locale] 参数设置为相应的代码。例如，要在法语中构建“mkdocs”主题，你应该在你的 `mkdocs.yml` 配置文件中使用下列命令：

```yaml
theme:
  name: mkdocs
  locale: fr
```

## 贡献主题翻译

如果一个主题没有被翻译成你的语言，请随时使用[翻译指南]进行贡献。

[翻译指南]: ../dev-guide/translations.md
[locale]: configuration.md#locale
[theme]: configuration.md#theme
[ISO-639-1]: https://en.wikipedia.org/wiki/ISO_639-1