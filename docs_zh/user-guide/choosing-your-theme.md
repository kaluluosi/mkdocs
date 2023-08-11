# 选择主题

选择和配置主题。

---

MkDocs包含两个内置主题（[mkdocs](#mkdocs)和[readthedocs](#readthedocs)），如下所述文档。 然而，还有许多[第三方主题]可供选择。

要选择主题，请在`mkdocs.yml`的配置文件中设置 [theme] 配置选项。

```yaml
theme:
  name: readthedocs
```

## mkdocs

默认主题，建立在定制的[Bootstrap]主题之上，支持MkDocs的几乎所有功能。

![mkdocs](../img/mkdocs.png)

除了默认的[主题配置选项][theme]之外，`mkdocs`主题还支持以下选项：

*   __`highlightjs`__ : 启用其使用[highlight.js] JavaScript库高亮显示代码块中的源代码。默认值为`True`。

*   __`hljs_style`__ : `highlight.js`库提供了79种不同的[样式]（颜色变化）用于高亮显示代码块中的源代码。将其设置为所需样式的名称即可。默认值为`github`。

*   __`hljs_languages`__ : 默认情况下，`highlight.js`仅支持23种常见语言。在此列出其他语言，以包括对其的支持。

    ```yaml
    theme:
      name: mkdocs
      highlightjs: true
      hljs_languages:
        - yaml
        - rust
    ```

*   __`analytics`__ : 定义分析服务的配置选项。目前，只有通过`gtag`选项支持Google Analytics v4。

    *   __`gtag`__ : 要启用Google Analytics，请设置为使用`G-`格式的Google Analytics v4跟踪ID。请参见Google的文件以了解有关为网站和/或应用程序设置分析（GA4）的信息或升级到Google Analytics 4属性的信息[为网站和/或应用程序设置分析（GA4）]和[升级到Google Analytics 4属性][upgrade-GA4]。

        ```yaml
        theme:
          name: mkdocs
          analytics:
            gtag: G-ABC123
        ```

        当设置为默认值（`null`）时，则禁用Google Analytics。

*   __`shortcuts`__ : 定义键盘快捷键。

    ```yaml
    theme:
      name: mkdocs
      shortcuts:
        help: 191    # ?
        next: 78     # n
        previous: 80 # p
        search: 83   # s
    ```

    所有值都必须是数字键代码。最好使用所有键盘都有的按键。您可以使用<https://keycode.info/>来确定给定键的键代码。

    *   __`help`__ : 显示列表键盘快捷方式的帮助模态框。默认值为`191` (&quest;)。

    *   __`next`__ : 导航到“下一页”。默认值为`78`（n）。

    *   __`previous`__ : 导航到“上一页”。默认值为`80`（p）。

    *   __`search`__ : 显示搜索模态框。默认值为`83`（s）。

*   __`navigation_depth`__ : 侧边栏中导航树的最大深度。默认值为`2`。

*   __`nav_style`__ : 这会将顶部导航栏的视觉样式调整为默认的`primary`（默认），但也可以设置为`dark`或`light`。

    ```yaml
    theme:
      name: mkdocs
      nav_style: dark
    ```

*   __`locale`__{ #mkdocs-locale } : 用于构建主题的区域设置（语言/位置）。如果您的区域设置尚未受支持，则将其回退到默认设置。

    此主题支持以下语言环境：

    * `en`：英语（默认）
    * （查看现有目录`mkdocs / themes / mkdocs / locales / * /`的列表）

    有关更多信息，请参见[本地化主题]指南。

## readthedocs

默认主题的克隆版，由[Read the Docs]服务使用，提供与其父主题相同的受限功能集。与其父主题一样，仅支持两个级别的导航。

![ReadTheDocs](../img/readthedocs.png)

除了默认的[主题配置选项][theme]之外，`readthedocs`主题还支持以下选项：

*   __`highlightjs`__ : 启用其使用[highlight.js] JavaScript库高亮显示代码块中的源代码。默认值为`True`。

*   __`hljs_languages`__ : 默认情况下，`highlight.js`仅支持23种常见语言。在此列出其他语言，以包括对其的支持。

    ```yaml
    theme:
      name: readthedocs
      highlightjs: true
      hljs_languages:
        - yaml
        - rust
    ```

*   __`analytics`__ : 定义分析服务的配置选项。

    *   __`gtag`__ : 要启用Google Analytics，请设置为使用`G-`格式的Google Analytics v4跟踪ID。请参见Google的文件以了解有关为网站和/或应用程序设置分析（GA4）的信息或升级到Google Analytics 4属性的信息[为网站和/或应用程序设置分析（GA4）]和[升级到Google Analytics 4属性][upgrade-GA4]。

        ```yaml
        theme:
          name: readthedocs
          analytics:
            gtag: G-ABC123
        ```

        当设置为默认值（`null`）时，则禁用Google Analytics。

    *   __`anonymize_ip`__ : 要对Google Analytics启用匿名IP地址，请将其设置为`True`。默认值为`False`。

*   __`include_homepage_in_sidebar`__ : 在侧边栏菜单中列出主页。由于MkDocs要求主页列在`nav`配置选项中，因此此设置允许在侧边栏中包括或排除主页。请注意，网站名称/标志始终链接到主页。默认值为`True`。

*   __`prev_next_buttons_location`__ : 其中之一：`bottom`，`top`，`both`或`none`。相应地显示``下一页''和``上一页''按钮。默认值为`bottom`。

*   __`navigation_depth`__ : 侧边栏中导航树的最大深度。默认值为`4`。

*   __`collapse_navigation`__ : 仅将当前页面的页面部分标题包括在侧边栏中。默认值为`True`。

*   __`titles_only`__ : 仅在侧边栏中包括页面标题，不包括所有页面的所有部分标题。默认值为`False`。

*   __`sticky_navigation`__ : 如果为True，则使侧边栏随着滚动页面而滚动主页面内容。默认值为`True`。

*   __`locale`__{ #readthedocs-locale } : 用于构建主题的区域设置（语言/位置）。如果您的区域设置尚未受支持，则将其回退到默认设置。

    此主题支持以下语言环境：

    * `en`：英语（默认）
    * （查看现有目录`mkdocs / themes / readthedocs / locales / * /`的列表）

    有关更多信息，请参见[本地化主题]指南。

*   __`logo`__ : 要在项目上设置标志而不是纯文本`site_name`，请将此变量设置为您的图像位置。默认值为`null`。

## 第三方主题

可在社区维基页面上找到[第三方主题]的列表和[等级目录][catalog]。如果您自己创建了，请将其添加到此处。

[third party themes]: #third-party-themes
[theme]: configuration.md#theme
[Bootstrap]: https://getbootstrap.com/
[highlight.js]: https://highlightjs.org/
[styles]: https://highlightjs.org/static/demo/
[setup-GA4]: https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319
[upgrade-GA4]: https://support.google.com/analytics/answer/9744165?hl=en&ref_topic=9303319
[Read the Docs]: https://readthedocs.org/
[community wiki]: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[catalog]: https://github.com/mkdocs/catalog#-theming
[localizing your theme]: localizing-your-theme.md