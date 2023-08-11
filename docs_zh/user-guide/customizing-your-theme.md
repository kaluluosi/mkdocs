# 自定义主题

修改主题以满足您的需求。

---

如果您想对现有主题进行一些修改，那么无需从头创建自己的主题。对于只需要一些CSS和/或JavaScript的较小修改，您可以[使用docs_dir](#using-the-docs_dir)。然而，对于更复杂的自定义，包括覆盖模板，则需要使用主题custom_dir设置。

## 使用docs_dir

`extra_css`和`extra_javascript`配置选项可用于对现有主题进行微调和自定义。要使用它们，您只需在[文档目录]中包含CSS或JavaScript文件即可。

例如，要更改文档中标题的颜色，请创建一个名为（例如）`style.css`的文件，并将其放在文档Markdown旁边。在该文件中添加以下CSS。

```css
h1 {
   color: red;
}
```

然后将其添加到 `mkdocs.yml`：

```yaml
extra_css:
  - style.css
```

在进行这些更改后，当您运行`mkdocs serve`时，它们应该会在文档中可见，如果已经运行它，则应该看到自动捕获了CSS更改并更新了文档。

注意：
任何额外的CSS或JavaScript文件都将在页面内容后添加到生成的HTML文档中。如果您要包含JavaScript库，可能最好使用主题[custom_dir]。

## 使用主题custom_dir

`theme.custom_dir`配置选项可用于指向一个文件目录，其中的文件覆盖父主题中的文件。父主题将是在`theme.name`配置选项中定义的主题。`custom_dir`中具有与父主题中同名的文件的任何文件都将替换父主题中同名的文件。`custom_dir`中的任何其他文件都将添加到父主题中。`custom_dir`的内容应该与父主题的目录结构相同。您可以包括主题中包含的模板，JavaScript文件，CSS文件，图像，字体或任何其他媒体。

注意：
为此正常工作，必须将 `theme.name` 设置为已知的已安装主题。如果`name`设置为`null`（或未定义），则没有主题可用于覆盖，`custom_dir`的内容必须是完整的，独立的主题。有关更多信息，请参阅[主题开发人员指南][自定义主题]。

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

要覆盖该主题中包含的任何文件，请在 `docs_dir` 旁边创建一个新目录：

```bash
mkdir custom_theme
```

然后将您的 `mkdocs.yml` 配置文件指向新目录：

```yaml
theme:
  name: mkdocs
  custom_dir: custom_theme/
```

要覆盖404错误页面（“文件未找到”），请向 `custom_theme` 目录添加一个名为`404.html`的新模板文件。有关可以包含在模板中的内容的信息，请参阅[主题开发人员指南][自定义主题]。

要覆盖favicon，请在`custom_theme / img / favicon.ico`处添加新的图标文件。

要包含JavaScript库，请将库复制到`custom_theme / js /`目录中。

您的目录结构现在应如下所示：

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
父主题中包含的任何文件（在`name`中定义）但未包含在`custom_dir`中的文件仍将被使用。`custom_dir`仅覆盖/替换父主题中的文件。如果您想要删除文件或从头构建主题，则应查看[主题开发人员指南][自定义主题]。

### 覆盖模板块

内置主题实现了许多模板块内的部分，这些模板块可以单独在 `main.html`模板 中覆盖。只需在 `custom_dir` 中创建一个`main.html`模板文件，然后在该文件中定义替换块即可。只需要确保`main.html`扩展到 `base.html`。例如，要更改MkDocs主题的标题，您的替换`main.html`模板将包含以下内容：

```django
{% extends "base.html" %}
{% block htmltitle %}
<title>Custom title goes here</title>
{% endblock %}
```

在上面的示例中，定义在自定义的`main.html`文件中的`htmltitle`块将替换父模板中定义的默认`htmltitle`块。您可以重新定义任意数量的块，只要这些块在父项中定义即可。例如，您可以将Google Analytics脚本替换为不同服务的脚本或将搜索功能替换为自己的功能。您将需要查看您使用的父主题，以确定可用于覆盖哪些块。 MkDocs和ReadTheDocs主题提供以下块：

* `site_meta`：包含文档头中的元标记。
* `htmltitle`：包含文档头中的页面标题。
* `styles`：包含样式表的链接标记。
* `libs`：包含页面标题中包含的JavaScript库（jQuery等）的库。
* `scripts`：包含页面加载后应执行的JavaScript脚本。
* `analytics`：包含分析脚本。
* `extrahead`：在`<head> `中插入自定义标签/脚本等的空块。
* `site_name`：包含导航栏中的站点名称。
* `site_nav`：包含导航栏中的站点导航。
* `search_button`：包含导航栏中的搜索框。
* `next_prev`：包含导航栏中的上一页和下一页按钮。
* `repo`：包含导航栏中的存储库链接。
* `content`：包含页面内容和目录。
* `footer`：包含页面页脚。

您可能需要查看源模板文件，以确保您的修改与站点结构兼容。有关您可以在自定义块中使用的变量列表，请参阅 [模板变量]。

### 组合custom_dir和模板块

向`custom_dir`添加JavaScript库将使其可用，但不会将其包含在MkDocs生成的页面中。因此，需要在HTML中添加从库到链接。

从上面的目录结构开始（截断）：

```nohighlight
- docs/
- custom_theme/
  - js/
    - somelib.js
- config.yml
```

需要将 `custom_theme/js/somelib.js` 文件的链接添加到模板中。由于 `somelib.js` 是JavaScript库，因此逻辑上应该放在 `libs` 块中。但是，仅包含新脚本的新`libs`块将替换在父模板中定义的块和任何链接到父模板中库的链接。为了避免破坏模板，可以使用超级块与块内的`超级函数`：

```django
{% extends "base.html" %}

{% block libs %}
    {{ super() }}
    <script src="{{ base_url }}/js/somelib.js"></script>
{% endblock %}
```

请注意，[base_url] 模板变量用于确保链接始终与当前页面相关。

现在，生成的页面将包括对模板提供的库的链接以及包含在 `custom_dir` 中的库的链接。对于包含在 `custom_dir` 中的任何其他 CSS 文件，也会需要相同的操作。

[自定义主题]:../dev-guide/themes.md
[extra_css]:./configuration.md#extra_css
[extra_javascript]:./configuration.md#extra_javascript
[文档目录]:./configuration.md#docs_dir
[custom_dir]:./configuration.md#custom_dir
[name]:./configuration.md#name
[mkdocs]:./choosing-your-theme.md#mkdocs
[浏览源代码]:https://github.com/mkdocs/mkdocs/tree/master/mkdocs/themes/mkdocs
[模板变量]:../dev-guide/themes.md#template-variables
[Jinja documentation]:https://jinja.palletsprojects.com/en/latest/templates/#template-inheritance
[超级函数]:https://jinja.palletsprojects.com/en/latest/templates/#super-blocks
[base_url]:../dev-guide/themes.md#base_url