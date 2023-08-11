# 选择你的主题

选择并配置一个主题。

---

MkDocs包括了两个内置主题([mkdocs](#mkdocs)和[readthedocs](#readthedocs))，就像下方所记录的一样。然而，也有许多[第三方主题]可供选择。

要选择一个主题，在你的`mkdocs.yml`配置文件中设置[theme]配置选项。

```yaml
theme:
  name: readthedocs
```

## mkdocs

默认主题，构建为一个自定义Bootstrap主题，支持MkDocs的几乎所有特性。

![mkdocs](../img/mkdocs.png)

除了默认的[theme configuration options][theme]之外，`mkdocs`主题还支持以下选项：

*   __`highlightjs`__：使用[highlight.js JavaScript library]对代码块中的源代码进行语法高亮。默认：`True`。

*   __`hljs_style`__：highlight.js库提供了79种不同的[样式]（颜色变化）来高亮代码块中的源代码。将其设置为所需样式的名称。默认：`github`。

*   __`hljs_languages`__：默认情况下，highlight.js仅支持23种常用语言。在这里列出其他语言以支持它们。

```yaml
theme:
  name: mkdocs
  highlightjs: true
  hljs_languages:
    - yaml
    - rust
```

*   __`analytics`__：定义分析服务的配置选项。目前，仅通过`gtag`选项支持Google Analytics v4。

    *   __`gtag`__：要启用Google Analytics，请设置为使用`G-`格式的Google Analytics v4跟踪ID。请参阅Google的文档以[设置网站和/或应用的分析(GA4)][setup-GA4]或[升级到Google Analytics 4属性][upgrade-GA4]。

```yaml
theme:
  name: mkdocs
  analytics:
    gtag: G-ABC123
```

当设置为默认（即 `null` ）时，将禁用网站的Google Analytics。

*   __`shortcuts`__：定义快捷键。

```yaml
theme:
  name: mkdocs
  shortcuts:
    help: 191    # ?
    next: 78     # n
    previous: 80 # p
    search: 83   # s
```

所有值都必须是数字键代码。最好使用所有键盘都可用的键。您可以使用<https://keycode.info/>来确定给定键的键代码。

*   __`help`__：显示一个帮助模态框，列出快捷键。默认：`191`（&quest;）

*   __`next`__：导航到下一页。默认：`78`（n）

*   __`previous`__：导航到上一页。默认：`80`（p）

*   __`search`__：显示搜索模态框。默认：`83`（s）

*   __`navigation_depth`__：侧边栏中导航树的最大深度。默认：`2`。

*   __`nav_style`__：这调整了顶部导航栏的可视样式；默认情况下，它设置为`primary`（默认值），但也可以设置为`dark`或`light`。

```yaml
theme:
  name: mkdocs
  nav_style: dark
```

*   __`locale`__{#mkdocs-locale }：用于构建主题的区域设置（语言/位置）。如果您的语言环境尚不受支持，则会回退到默认设置。

此主题支持以下区域设置：

* `en`：英文（默认）
* （查看现有目录的列表`mkdocs/themes/mkdocs/locales/*/`）

有关详细信息，请参见[本地化您的主题]指南。

## readthedocs

Read the Docs服务使用的默认主题的克隆版，提供与其父主题相同的受限功能集。与其父主题一样，仅支持两个级别的导航。

![ReadTheDocs](../img/readthedocs.png)

除了默认的[theme configuration options][theme]之外，`readthedocs`主题还支持以下选项：

*   __`highlightjs`__：使用[highlight.js JavaScript library]对代码块中的源代码进行语法高亮。默认：`True`。

*   __`hljs_languages`__：默认情况下，highlight.js仅支持23种常用语言。在这里列出其他语言以支持它们。

```yaml
theme:
  name: readthedocs
  highlightjs: true
  hljs_languages:
    - yaml
    - rust
```

*   __`analytics`__：定义分析服务的配置选项。

    *   __`gtag`__：要启用Google Analytics，请设置为使用`G-`格式的Google Analytics v4跟踪ID。请参阅Google的文档以[设置网站和/或应用的分析(GA4)][setup-GA4]或[升级到Google Analytics 4属性][upgrade-GA4]。

```yaml
theme:
  name: readthedocs
  analytics:
    gtag: G-ABC123
```

当设置为默认（即 `null` ）时，将禁用网站的Google Analytics。

*   __`include_homepage_in_sidebar`__：在侧边栏菜单中列出主页。由于MkDocs要求在`nav`配置选项中列出主页，因此此设置允许从侧栏中包括或排除主页。请注意，站点名称/徽标始终链接到主页。默认为：`True`。

*   __`prev_next_buttons_location`__： `bottom`，`top`，`both`或`none`中的一个。相应地显示“下一个”和“上一个”按钮。默认值为：`bottom`。

*   __`navigation_depth`__：侧边栏中导航树的最大深度。默认：`4`。

*   __`collapse_navigation`__：仅在当前页面的侧边栏中包括页面部分标题。默认：`True`。

*   __`titles_only`__：仅在侧栏中包括页面标题，而不包括所有页面的部分标题。默认：`False`。

*   __`sticky_navigation`__：如果为True，则导致侧栏在滚动页面时与主页面内容一起滚动。默认：`True`。

*   __`locale`__{ #readthedocs-locale }：用于构建主题的区域设置（语言/位置）。如果您的语言环境尚不受支持，则会回退到默认设置。

此主题支持以下区域设置：

* `en`：英文（默认）
* （查看现有目录的列表`mkdocs/themes/readthedocs/locales/*/`）

有关详细信息，请参见[本地化您的主题]指南。

*   __`logo`__：要在项目中设置一个徽标，而不是纯文本`site_name`，请将此变量设置为图像的位置。默认值为：`null`。

## 第三方主题

第三方主题的列表可以在[社区维基]页面和[名录][catalog]中找到。如果您创建了自己的主题，请将它们添加到那里。

[third party themes]: #third-party-themes
[theme]: configuration.md#theme
[Bootstrap]: https://getbootstrap.com/
[highlight.js JavaScript library]: https://highlightjs.org/
[样式]: https://highlightjs.org/static/demo/
[setup-GA4]: https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319
[upgrade-GA4]: https://support.google.com/analytics/answer/9744165?hl=en&ref_topic=9303319
[Read the Docs]: https://readthedocs.org/
[社区维基]: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[catalog]: https://github.com/mkdocs/catalog#-theming
[localizing your theme]: localizing-your-theme.md