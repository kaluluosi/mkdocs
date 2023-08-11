# 自定义主题

修改主题以满足您的需求。

---

如果您想对现有主题进行一些微调，则无需从头创建自己的主题。对于仅需要一些 CSS 和/或 JavaScript 的小调整，您可以使用 [docs_dir](#using-the-docs_dir)。然而，对于更复杂的自定义，包括覆盖模板，您将需要使用主题的 [custom_dir](#using-the-theme-custom_dir) 设置。

## 使用 docs_dir

[extra_css] 和 [extra_javascript] 配置选项可用于对现有主题进行微调和自定义。要使用这些选项，您只需要在 [文档目录] 中包含 CSS 或 JavaScript 文件即可。

例如，要更改文档中标题的颜色，请创建一个名为（例如）`style.css` 的文件，并将其放在与文档 Markdown 相邻的位置。在该文件中添加以下 CSS。

```css
h1 {
  color: red;
}
```

然后将其添加到 `mkdocs.yml` 文件中：

```yaml
extra_css:
  - style.css
```

进行这些更改后，当您运行 `mkdocs serve` 时，应该可以看到它们。如果已经在运行它，请查看是否自动捕获了 CSS 更改并更新了文档。

注意：
任何额外的 CSS 或 JavaScript 文件都将在页面内容后添加到生成的 HTML 文档中。如果您想要包含 JavaScript 库，则可以使用主题 [custom_dir] 来包含该标准库。

## 使用主题的 custom_dir

[`theme.custom_dir`][custom_dir] 配置选项可用于指向一个包含覆盖父主题文件的文件目录。父主题将是在 [`theme.name`][name] 配置选项中定义的主题。在具有与父主题相同名称的文件的 `custom_dir` 中的任何文件都将替换父主题中相同名称的文件。`custom_dir` 中的任何其他文件都将添加到父主题中。`custom_dir` 的内容应该跟父主题的目录结构相同。您可以包含模板，JavaScript 文件，CSS 文件，图像，字体或包括主题中的任何其他媒体

注意：
要使用这个功能，`theme.name` 设置必须设置为已知的已安装主题。如果 `name` 设置为 `null`（或未定义），那么没有要覆盖的主题，`custom_dir` 的内容必须是一个完整的，独立的主题。有关详细信息，请参阅[主题开发人员指南][custom theme]。

例如，[mkdocs] 主题（[浏览源代码]）包含以下目录结构（部分）：

```nohighlight
- css\
- fonts\
- img\
  - favicon.ico
  - grid.png
- js\
- 404.html
- base.html
- content.html
- nav-sub.html
- nav.html
- toc.html
```

要覆盖该主题中包含的任何文件，请在 `docs_dir` 旁边创建一个名为 `custom_theme` 的新目录：

```bash
mkdir custom_theme
```

然后将 `mkdocs.yml` 配置文件指向新目录：

```yaml
theme:
  name: mkdocs
  custom_dir: custom_theme/
```

要覆盖 404 错误页面（“文件未找到”），请在 `custom_theme` 目录中添加一个名为 `404.html` 的新模板文件。有关模板中可以包含的内容，请查看[主题开发人员指南][custom theme]。

要覆盖网站图标，请将一个新的图标文件添加到 `custom_theme/img/favicon.ico`。

要包含 JavaScript 库，请将库复制到 `custom_theme/js/` 目录中。

现在您的目录结构应如下所示：

```nohighlight
- docs/
  - index.html
- custom_theme/
  - img/
    - favicon.ico
  - js/
    - somelib.js
  - 404.html
- config.yml
```

注意：
父主题中包含的任何未包含在 `custom_dir` 中的文件仍将被使用。`custom_dir` 将仅覆盖/替换父主题中的文件。如果您想要删除文件或从头开始构建一个主题，则应该查看 [主题开发人员指南][custom theme]。

### 覆盖模板块

内置主题在模板块内实现其许多部分，这些模板块可以单独在 `main.html` 模板中被覆盖。只需在 `custom_dir` 中创建一个 `main.html` 模板文件，并在其中定义替换块即可。只要 `main.html` 扩展了 `base.html`。例如，要更改 MkDocs 主题的标题，您的更换 `main.html` 模板将包含以下内容：

```django
{% extends "base.html" %}

{% block htmltitle %}
<title>Custom title goes here</title>
{% endblock %}
```

在上面的示例中，您自定义的 `main.html` 文件中定义的 `htmltitle` 块将用于替换父级中定义的默认 `htmltitle` 块。您可以重新定义所有您想要的块，只要这些块在父级中定义即可。例如，您可以将 Google Analytics 脚本替换为不同服务的脚本或使用自己的搜索替换搜索功能。您将需要查看您正在使用的父主题，以确定可以覆盖的块。MkDocs 和 ReadTheDocs 主题提供以下块：

* `site_meta`：包含文档 head 中的元标签。
* `htmltitle`：包含文档 head 中的页面标题。
* `styles`：包含样式表的链接标记。
* `libs`：包含页面头部中包含的 JavaScript 库（jQuery 等）。
* `scripts`：包含页面加载后应执行的 JavaScript 脚本。
* `analytics`：包含数据分析脚本。
* `extrahead`：位于 `<head>` 中的一个空块，用于插入自定义标签/脚本等。
* `site_name`：包含导航栏中的站点名称。
* `site_nav`：包含导航栏中的网站导航。
* `search_button`：在导航栏中包含搜索框。
* `next_prev`：包含导航栏中的下一个和上一个按钮。
* `repo`：包含导航栏中的存储库链接。
* `content`：包含页面内容和目录。
* `footer`：包含页面页脚。

您可能需要查看源模板文件，以确保您的修改与站点的结构兼容。查看[模板变量]以获取可在自定义块中使用的变量列表。有关块的更完整说明，请查阅 [Jinja 文档]。

### 合并 custom_dir 和 模板块

将 JavaScript 库添加到 `custom_dir` 中将使其可用，但不会在 MkDocs 生成的页面中包含它。因此，需要从 HTML 中添加该库的链接。

使用上面的目录结构（缩短）：

```nohighlight
- docs/
- custom_theme/
  - js/
    - somelib.js
- config.yml
```

需要从模板添加到 `custom_theme/js/somelib.js` 文件中的链接。由于 `somelib.js` 是 JavaScript 库，它会合理地放在 `libs` 块中。然而，一个新的 `libs` 块仅包含新脚本，将替换父模板中定义的块和任何链接到模板中的库的链接将被删除。为了避免破坏模板，可以使用带有 `super` 的 [super 块]：


```django
{% extends "base.html" %}

{% block libs %}
    {{ super() }}
    <script src="{{ base_url }}/js/somelib.js"></script>
{% endblock %}
```

请注意，使用 [base_url] 模板变量以确保链接始终是相对于当前页面的。

现在生成的页面将包括模板提供的库的链接以及包含在 `custom_dir` 中的库的链接。任何包含在 `custom_dir` 中的其他 CSS 文件都需要执行相同的操作。

[custom theme]: ../dev-guide/themes.md
[extra_css]: ./configuration.md#extra_css
[extra_javascript]: ./configuration.md#extra_javascript
[documentation directory]: ./configuration.md#docs_dir
[custom_dir]: ./configuration.md#custom_dir
[name]: ./configuration.md#name
[mkdocs]: ./choosing-your-theme.md#mkdocs
[browse source]: https://github.com/mkdocs/mkdocs/tree/master/mkdocs/themes/mkdocs
[模板变量]: ../dev-guide/themes.md#template-variables
[Jinja 文档]: https://jinja.palletsprojects.com/en/latest/templates/#template-inheritance
[super 块]: https://jinja.palletsprojects.com/en/latest/templates/#super-blocks
[base_url]: ../dev-guide/themes.md#base_url