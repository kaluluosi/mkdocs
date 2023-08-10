# 选择你的主题

选择和配置一个主题。---

MkDocs 包含两种内置主题 ([mkdocs](#mkdocs) 和 [readthedocs](#readthedocs))，下面将进行文档记录。然而，也有许多 [第三方主题] 可供选择。为选择主题，在你的 `mkdocs.yml` 配置文件中设置 [theme] 配置选项。

```yaml
theme:
  name: readthedocs
```

## mkdocs

默认主题，它是一个自定义 [Bootstrap] 主题，支持MkDocs的几乎所有功能。![mkdocs](../img/mkdocs.png)

除了默认的[主题配置选项][theme]外，`mkdocs`主题还支持以下选项：

*   __`highlightjs`__: 使用 [highlight.js] JavaScript 库在代码块中启用源代码的高亮显示。默认值为 `True` 。
*   __`hljs_style`__: highlight.js 库提供了79种不同的 [样式]（颜色变化），用于突出显示代码块中的源代码。将其设置为所需样式的名称。默认值为 `github` 。
*   __`hljs_languages`__: 默认情况下，highlight.js 仅支持23种常见语言。在此处列出其他语言，以包含对它们的支持。

```yaml
theme:
  name: mkdocs
  highlightjs: true
  hljs_languages:
    - yaml
    - rust
```

*   __`analytics`__: 定义分析服务的配置选项。目前，仅通过 `gtag` 选项支持 Google Analytics v4。
*   __`gtag`__: 要启用 Google Analytics，请设置为使用 `G-` 格式的 Google Analytics v4 跟踪 ID。请参阅 Google 的文档，了解如何[为网站和/或应用设置分析(GA4)][setup-GA4]或[升级到 Google Analytics 4 属性][upgrade-GA4]。

```yaml
    theme:
      name: mkdocs
      analytics:
        gtag: G-ABC123
```
当设置为默认值（`null`）时，禁用 Google Analytics。

*   __`shortcuts`__: 定义键盘快捷键。

```yaml
theme:
  name: mkdocs
  shortcuts:
    help: 191    # ?next: 78     # n
    previous: 80 # p
    search: 83   # s
```

所有值都必须是数字键代码。最好使用所有键盘都有的键。你可以使用 <https://keycode.info/> 来确定给定的键的键码。

*   __`help`__: 显示一个显示键盘快捷键的帮助弹出窗口。默认值为 `191`（`?`）。
*   __`next`__: 导航到“下一个”页面。默认值为 `78`（`n`）。
*   __`previous`__: 导航到“上一个”页面。默认值为 `80`（`p`）。
*   __`search`__: 显示搜索弹出窗口。默认值为 `83`（`s`）。

*   __`navigation_depth`__: 侧边栏中导航树的最大深度。默认值为 `2`。
*   __`nav_style`__: 这调整顶部导航栏的视觉样式；默认情况下，它设置为 `primary`（默认值），但也可以设置为 `dark` 或 `light`。

```yaml
theme:
  name: mkdocs
  nav_style: dark
```

*   __`locale`__{ #mkdocs-locale }: 用于构建主题的区域设置（语言/位置）。如果你的语言环境还没有得到支持，它将返回到默认值。此主题支持以下位置设置：

    * `en` : 英语（默认值）
    * (查看现有目录 `mkdocs/themes/mkdocs/locales/*/` 的列表)

    更多信息请参见[主题本地化]指南。

## readthedocs

与[Read the Docs]服务使用的默认主题的克隆版，提供与其父主题相同的受限功能集。与其父主题一样，仅支持两个层级的导航。![ReadTheDocs](../img/readthedocs.png)

除了默认的[主题配置选项][theme]外，`readthedocs` 主题还支持以下选项：

*   __`highlightjs`__: 使用 [highlight.js] JavaScript 库在代码块中启用源代码的高亮显示。默认值为 `True`。
*   __`hljs_languages`__: 默认情况下，highlight.js 仅支持23种常见语言。在此处列出其他语言，以包含对它们的支持。 

```yaml
theme:
  name: readthedocs
  highlightjs: true
  hljs_languages:
    - yaml
    - rust
```

*   __`analytics`__: 定义分析服务的配置选项。
*   __`gtag`__: 要启用 Google Analytics，请设置为使用 `G-` 格式的 Google Analytics v4 跟踪 ID。请参阅 Google 的文档，了解如何[为网站和/或应用设置分析(GA4)][setup-GA4]或[升级到 Google Analytics 4 属性][upgrade-GA4]。

```yaml
    theme:
      name: readthedocs
      analytics:
        gtag: G-ABC123
```

当设置为默认值（`null`）时，禁用 Google Analytics。

*   __`anonymize_ip`__：要为 Google Analytics 启用匿名 IP 地址，请设置为 `True`。默认值为 `False`。
*   __`include_homepage_in_sidebar`__：在侧边栏菜单中列出主页。由于 MkDocs 要求主页列在 `nav` 配置选项中，因此此设置允许在侧边栏中包含或排除主页。请注意，网站名称/标志始终链接到主页。默认值为 `True`。
*   __`prev_next_buttons_location`__：一个值为 `bottom`、`top`、`both` 或 `none` 的设置，相应地显示“下一页”和“上一页”按钮。默认值时 `bottom`。 
*   __`navigation_depth`__：侧边栏中导航树的最大深度。默认值为 `4`。
*   __`collapse_navigation`__：仅在当前页面的侧栏中包含该页面的名称部分标题。默认值为 `True`。
*   __`titles_only`__：仅在侧栏中包括页面标题，不包括所有页面的名称部分标题。默认值为 `False`。
*   __`sticky_navigation`__：如果为 True，则使侧栏随着页面内容的滚动而滚动。默认值为 `True`。
*   __`locale`__{ #readthedocs-locale }: 使用于构建主题的区域设置（语言/位置）。如果你的语言环境还没有得到支持，它将返回到默认值。此主题支持以下位置设置：

    * `en` : 英语（默认值）
    * (查看现有目录 `mkdocs/themes/readthedocs/locales/*/` 的列表)

    更多信息请参见[主题本地化]指南。

*   __`logo`__：要在项目上设置标识而不是纯文本 `site_name`，请将此变量设置为图像的位置。默认值为 `null`。

## 第三方主题

第三方主题列表，可以在社区维基页面和 [排名目录][catalog] 上找到。如果你已经创建了自己的主题，请将它们添加到那里。[第三方主题]: #第三方主题
[theme]: configuration.md#theme
[Bootstrap]: https://getbootstrap.com/
[highlight.js]: https://highlightjs.org/
[styles]: https://highlightjs.org/static/demo/
[setup-GA4]: https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319
[upgrade-GA4]: https://support.google.com/analytics/answer/9744165?hl=en&ref_topic=9303319
[Read the Docs]: https://readthedocs.org/
[community wiki]: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[catalog]: https://github.com/mkdocs/catalog#-theming
[主题本地化]: localizing-your-theme.md