# 主题本地化

在你喜欢的语言中显示你的主题。

---

注意：
主题本地化仅翻译主题本身的文本元素（如“下一页”和“上一页”链接），而不是你文档的实际内容。如果你想创建多语言文档，你需要将本地化主题与第三方国际化/本地化插件结合使用。

## 安装

为使主题本地化正常工作，必须使用支持主题本地化的主题并安装 `mkdocs[i18n]` 以启用i18n（国际化）支持：

```bash
pip install mkdocs[i18n]
```

## 支持的语言环境

在大多数情况下，你的语言环境是根据你的语言的[ISO-639-1]（2字母）缩写来指定的。但是，语言环境也可能包括一个地域（或区域或县）代码。必须用下划线分隔语言和地域。例如，英语的一些可能的语言环境包括 `en`, `en_AU`, `en_GB` 和 `en_US`。

有关你正在使用的主题支持的语言环境列表，请参见该主题的文档。

- [mkdocs](choosing-your-theme.md#mkdocs-locale)
- [readthedocs](choosing-your-theme.md#readthedocs-locale)

警告：
如果你配置一个主题尚不支持的语言环境，MkDocs 将回退到主题的默认语言环境。

## 使用说明

为指定MkDocs应使用的语言环境，请将 [theme] 配置选项的 [locale] 参数设置为适当的代码。

例如，要在法语中构建 `mkdocs` 主题，你将在 `mkdocs.yml` 配置文件中使用以下内容：

```yaml
theme:
  name: mkdocs
  locale: fr
```

## 贡献主题翻译

如果主题尚未翻译成你的语言，请使用 [翻译指南]（Translation Guide）贡献翻译。

[翻译指南]: ../dev-guide/translations.md
[locale]: configuration.md#locale
[theme]: configuration.md#theme
[ISO-639-1]: https://en.wikipedia.org/wiki/ISO_639-1