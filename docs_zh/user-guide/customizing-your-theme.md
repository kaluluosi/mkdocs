# 定制主题

修改主题以适应您的需求。

如果您想对现有主题进行调整，那么无需从头开始创建自己的主题。对于仅需一些 CSS 和/或 JavaScript 的小型调整，您可以使用 [docs_dir]。然而，对于更复杂的自定义，包括覆盖模板，您需要使用主题的 [custom_dir] 设置。

## 使用 docs_dir

可以使用 [extra_css] 和 [extra_javascript] 配置选项来进行现有主题的调整和自定义。要使用这些功能，您只需要在 [文档目录] 中包含 CSS 或 JavaScript 文件。例如，要更改文档中标题的颜色，创建一个名为 `style.css` 的文件，将其放置在与文档 Markdown 同级的目录中，在该文件中添加以下 CSS：

```css
h1 {
  color: red;
}
```

然后将其添加到 `mkdocs.yml` 中：

```yaml
extra_css:
  - style.css
```

进行这些更改后，在运行 `mkdocs serve` 时应该可以看到更新，如果您已经运行了 `mkdocs serve`，您将会看到 CSS 更改自动被捡起并更新文档。

注意：

任何额外的 CSS 或 JavaScript 文件将在页面内容之后添加到生成的 HTML 文档中。如果您想要包括 JavaScript 库，则可以通过使用主题的 [custom_dir] 来包括库。

## 使用主题 custom_dir

[`theme.custom_dir`] 配置选项可用于指向一个文件夹，其中的文件会覆盖父级主题中的文件。父级主题将是在 [`theme.name`] 配置选项中定义的主题。与父主题中同名的 `custom_dir` 中的任何文件都将替换父主题中同名的文件。在 `custom_dir` 中的任何其他文件都将添加到父级主题中。`custom_dir` 的内容应反映父主题的目录结构。您可以包括模板、JavaScript 文件、CSS 文件、图像、字体或任何包括在主题中的媒体。

注意：

为使其正常工作，必须将 `theme.name` 设置为已知的已安装主题。如果 `name` 设置为 `null`（或未定义），则没有要覆盖的主题，`custom_dir` 的内容必须是一个完整的独立主题。有关更多信息，请参阅 [主题开发人员指南][custom theme]。

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

要覆盖该主题中包含的任何文件，请在您的 `docs_dir` 旁边创建一个新目录：

```bash
mkdir custom_theme
```

然后将您的 `mkdocs.yml` 配置文件指向新目录：

```yaml
theme:
  name: mkdocs
  custom_dir: custom_theme/
```

要覆盖 404 错误页面（"文件未找到"），请将名为 `404.html` 的新模板文件添加到 `custom_theme` 目录中。有关可以包含在模板中的信息，请查看 [主题开发人员指南][custom theme]。要覆盖标签图标，可以在 `custom_theme/img/favicon.ico` 中添加新的图标文件。要包括 JavaScript 库，请将该库复制到 `custom_theme/js/` 目录下。

现在，您的目录结构应如下所示：

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

父主题中包括的任何文件（在 `name` 中定义）但未包含在 `custom_dir` 中的文件仍将被使用。`custom_dir` 将仅覆盖/替换父级主题中的文件。如果您想要删除文件或从头开始构建主题，则应查看[主题开发人员指南][custom theme]。

### 覆盖模板块

内置主题在模板块中实现了其许多部分，这些模板块可以单独覆盖在 `main.html` 模板中定义。只需要在您的 `custom_dir` 中创建一个 `main.html` 模板文件，在该文件中定义替换块。只需确保 `main.html` 扩展了 `base.html`。例如，要更改 MkDocs 主题的标题，您的替换的 `main.html` 模板将包含以下内容：

```django
{% extends "base.html" %}

{% block htmltitle %}
<title>修改后的标题</title>
{% endblock %}
```

在上面的示例中，您自定义的 `main.html` 文件中定义的 `htmltitle` 块将用于替换父级主题中默认定义的 `htmltitle` 块。只要这些块在父级中定义，您可以重新定义尽可能多的块。例如，您可以将 Google Analytics 脚本替换为其他服务的脚本，或者将搜索功能替换为您自己的功能。您需要查阅您正在使用的父主题，以确定可用于覆盖的块。MkDocs 和 ReadTheDocs 主题提供以下块：

- `site_meta`：包含文档头中的元标记。
- `htmltitle`：包含文档头中的页面标题。
- `styles`：包含样式表的链接标记。
- `libs`：包含页面头中包括的 JavaScript 库（jQuery 等）。
- `scripts`：包含页面加载后应执行的 JavaScript 脚本。
- `analytics`：包含分析脚本。
- `extrahead`：一个在`<head>`标记中插入自定义标记/脚本等的空块。
- `site_name`：包含导航栏中的站点名称。
- `site_nav`：包含导航栏的站点导航。
- `search_button`：包含导航栏中的搜索框。
- `next_prev`：包含导航栏中的下一页和上一页按钮。
- `repo`：包含导航栏中的存储库链接。
- `content`：包含页面内容和页面的目录。
- `footer`：包含页面的页脚。

您可能需要查看源模板文件，以确保您的修改与站点的结构兼容。有关您可以在自定义块中使用的变量列表，请参阅[模板变量][Template Variables]。要获取有关块的更完整说明，请参阅[Jinja 文档][Jinja documentation]。

### 结合 custom_dir 和模板块

将 JavaScript 库添加到 `custom_dir` 中将使其可用，但不会将其包含在 MkDocs 生成的页面中。因此，需要将文件夹中的库链接到 HTML 中。以上面的目录结构为例（截断）：

```nohighlight
- docs/
- custom_theme/
  - js/
    - somelib.js
- config.yml
```

需要将 `custom_theme/js/somelib.js` 文件的链接添加到模板中。由于`somelib.js` 是 JavaScript 库，因此它将逻辑上进入到 `libs` 块。但是，仅包括新脚本的新 `libs` 块将替换父模板中定义的块，并将删除父模板中指向库的链接。为了避免打破模板，可以使用 [super block] 并在其中使用 `super` 调用该块。例如：

```django
{% extends "base.html" %}

{% block libs %}
    {{ super() }}
    <script src="{{ base_url }}/js/somelib.js"></script>
{% endblock %}
```

请注意，使用 [base_url] 模板变量，以确保链接始终相对于当前页面。现在，生成的页面将包括指向库 provided template 的链接以及包含在 `custom_dir` 中的库的链接。对于包括在 `custom_dir` 中的任何其他 CSS 文件，也需要执行相同的操作。

[custom theme]: ../dev-guide/themes.md
[extra_css]: ./configuration.md#extra_css
[extra_javascript]: ./configuration.md#extra_javascript
[documentation directory]: ./configuration.md#docs_dir
[custom_dir]: ./configuration.md#custom_dir
[name]: ./configuration.md#name
[mkdocs]: ./choosing-your-theme.md#mkdocs
[browse source]: https://github.com/mkdocs/mkdocs/tree/master/mkdocs/themes/mkdocs
[Template Variables]: ../dev-guide/themes.md#template-variables
[Jinja documentation]: https://jinja.palletsprojects.com/en/latest/templates/#template-inheritance
[super block]: https://jinja.palletsprojects.com/en/latest/templates/#super-blocks
[base_url]: ../dev-guide/themes.md#base_url