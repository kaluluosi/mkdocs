# 主题开发

创建和分发自定义主题的指南。

注意：
如果您正在寻找现有的第三方主题，它们列在[社区Wiki页面][community wiki]和 [MkDocs项目目录][catalog]中。如果您想分享自己创作的主题，请在那里列出。
当创建一个新主题时，您可以按照这个指南的步骤从头开始创建，或者您可以下载 `mkdocs-basic-theme` 作为一个基本但完整的主题，并包含所有必要的样板文件。**您可以在 [GitHub][basic theme] 找到该基础主题**。它在代码中包含了详细的注释，以描述不同的特性及其用法。

[community wiki]: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[catalog]: https://github.com/mkdocs/catalog#-theming
[basic theme]: https://github.com/mkdocs/mkdocs-basic-theme

## 创建自定义主题

自定义主题所需的最少条件是在一个目录中放置一个 `main.html` [Jinja2 模板文件]，该目录不是 [docs_dir] 的子目录。
在 `mkdocs.yml` 中，将 [`theme.custom_dir`][custom_dir] 选项设置为包含 `main.html` 的目录的路径。该路径应与配置文件的相对路径一致。
例如，给定此示例项目布局：

```text
mkdocs.yml
docs/
    index.md
    about.md
custom_theme/
    main.html
    ...
```

...可在 `mkdocs.yml` 中包含以下设置以使用自定义主题目录：
```yaml
theme:
  name: null
  custom_dir: 'custom_theme/'
```

> 注意：
通常在构建自己的自定义主题时，`theme.[name]` 配置设置应被设置为 'null'。然而，如果将 `theme.[custom_dir]` 配置值与现有主题结合使用，则可用于仅替换内置主题中的特定部分。
例如，对于上面的布局，如果将 `name: "mkdocs"`，则在主题目录中的 `main.html` 文件将替换 `mkdocs` 主题中的同名文件，但否则 `mkdocs` 主题将保持不变。如果您想对现有主题进行小的调整，这很有用。
有关更具体的信息，请参阅[自定义主题]。

<!-- -->
> 警告：
主题在 `theme.custom_dir` 中存在时定义在 `mkdocs_theme.yml` 文件中的主题[配置]不会被加载。
当整个主题存在于 `theme.custom_dir` 中并且 `theme.name` 被设置为 'null' 时，则必须在 `mkdocs.yml` 文件的 [theme] 配置选项中定义整个主题配置。
然而，在打包主题进行分发时，使用 `theme.name` 配置选项进行加载时，则需要一个 `mkdocs_theme.yml` 文件。

[Jinja2 模板文件]: https://jinja.palletsprojects.com/
[custom_dir]: ../user-guide/configuration.md#custom_dir
[name]: ../user-guide/configuration.md#name
[docs_dir]: ../user-guide/configuration.md#docs_dir
[configuration]: #theme-configuration
[packaged]: #packaging-themes
[theme]: ../user-guide/configuration.md#theme
[自定义主题]: ../user-guide/customizing-your-theme.md#using-the-theme-custom_dir

## 基础主题

最简单的 `main.html` 文件如下：

```django
<!DOCTYPE html>
<html>
  <head>
    <title>{% if page.title %}{{ page.title }} - {% endif %}{{ config.site_name }}</title>
    {%- for path in config.extra_css %}
      <link href="{{ path | url }}" rel="stylesheet">
    {%- endfor %}
  </head>
  <body>
    {{ page.content }}

    {%- for script in config.extra_javascript %}
      {{ script | script_tag }}
    {%- endfor %}
  </body>
</html>
```

从 `mkdocs.yml` 中指定内容插入到此主题和正常 HTML 文件一样，可以引入样式表和脚本。NavBar 和目录也可以自动生成并包含进来，分别使用 `nav` 和 `toc` 对象。
如果您想编写自己的主题，建议从一个 [内置主题] 开始，并相应地进行修改。

注意：
MkDocs 使用 [Jinja] 作为其模板引擎，您可以访问 Jinja 的所有强大功能，包括 [模板继承]。
您可能会注意到，随 MkDocs 一起提供的主题广泛使用模板继承和块，允许用户轻松覆盖主题 [custom_dir] 中的模板的小块和片段。因此，内置主题是用 `base.html` 文件实现的，而 `main.html` 扩展了 `base.html`。
尽管这不是必需的，但鼓励第三方模板作者遵循类似的模式，并可能希望定义内置主题中使用的相同块 [blocks]，以保持一致性。

[Jinja]: https://jinja.palletsprojects.com/
[模板继承]: https://jinja.palletsprojects.com/en/latest/templates/#template-inheritance
[blocks]: ../user-guide/customizing-your-theme.md#overriding-template-blocks
[内置主题]: ../user-guide/customizing-your-theme.md#built-in-themes

### 从配置中获取 CSS 和 JavaScript

MkDocs 定义了顶级配置 [extra_css] 和 [extra_javascript]。它们都是文件列表。主题必须包含 HTML，以链接这些配置中的项目，否则配置将无法正常工作。您可以在[基础主题示例]中看到一个推荐的方式来呈现这两者的内容。

> 新增：**自 MkDocs 1.5 版本更改：**
>
> `config.extra_javascript` 列表的项过去是简单字符串，现在变成了具有以下字段的对象：`path`、`type`、`async`、`defer`。
> 在这个版本中，MkDocs 还增加了 [`script_tag` 过滤器](#script_tag)。
>
> 示例的旧样式是：
> ```django
>   {%- for path in extra_javascript %}
>     <script src="{{ path }}"></script>
>   {%- endfor %}
> ```
> 这个旧样式甚至使用了不推荐的顶级 `extra_javascript` 列表。请始终使用 `config.extra_javascript`。
> 因此，一种略微更新的方法是：
> ```django
>   {%- for path in config.extra_javascript %}
>     <script src="{{ path | url }}"></script>
>   {%- endfor %}
> ```
> >? 示例中说的新增用法为：
> > ```django
> >   {%- for script in config.extra_javascript %}
> >     {{ script | script_tag }}
> >   {%- endfor %}
> > ```
>
> 如果您希望在保持主题与旧版 MkDocs 兼容的同时，能够使用新的自定义内容，请使用以下代码片段：
>
> > 示例：**向后兼容的样式**
> >
> > ```django
> >   {%- for script in config.extra_javascript %}
> >     {%- if script.path %}  {# 检测到 MkDocs 1.5+，其拥有 `script.path` 和 `script_tag` #}
> >       {{ script | script_tag }}
> >     {%- else %}  {# 向后兼容 - 直接检查文件名 #}
> >       <script src="{{ script | url }}"{% if script.endswith(".mjs") %} type="module"{% endif %}></script>
> >     {%- endif %}
> >   {%- endfor %}
> > ```

[extra_css]:../user-guide/configuration.md#extra_css
[extra_javascript]:../user-guide/configuration.md#extra_javascript
[基础主题示例]: #基础主题

## 主题文件

主题以某种方式特殊对待各种文件。所有其他文件都只是从主题目录复制到 `site_dir` 中的相同路径。例如，图像和 CSS 文件没有特殊意义，将原样复制。但是，请注意，如果用户提供具有相同路径的文件，则用户的文件将替换主题文件。

### 模板文件

任何具有 `.html` 扩展名的文件都被视为模板文件，不会从主题目录或任何子目录复制。同时，任何在 [static_templates] 中列出的文件都视为模板，无论其文件扩展名如何。

[static_templates]: #static_templates

### 主题元文件

还会忽略打包主题所需的各种文件，具体来说，是 `mkdocs_theme.yml` 配置文件和任何 Python 文件。

### 点文件

主题作者可以通过用一个点开始的文件或目录名，明确地强制 MkDocs 忽略文件。以下任何文件都将被忽略：

```text
.ignored.txt
.ignored/file.txt
foo/.ignored.txt
foo/.ignored/file.txt
```

### 文档文件

所有文档文件都将被忽略。特别是，将忽略使用任何由 MkDocs 支持的文件扩展名的 Markdown 文件。此外，忽略了可能存在于主题目录中的任何 README 文件。

## 模板变量

每个主题的模板都是使用模板上下文生成的。这些变量可用于主题。上下文根据正在构建的模板而异。目前模板使用全局上下文或页面特定上下文。全局上下文用于不表示单个 Markdown 文档的 HTML 页面，例如 404.html 页面或 search.html。

### 全局上下文

下列变量对于任何模板都是全局可用的。

#### config

`config` 变量是从 `mkdocs.yml` 配置文件生成的 MkDocs 配置对象的实例。您可以使用任何配置选项，但一些常用的选项包括：

* [config.site_name](../user-guide/configuration.md#site_name)：站点名称。
* [config.site_url](../user-guide/configuration.md#site_url)：站点 URL。
* [config.site_author](../user-guide/configuration.md#site_author)：站点作者。
* [config.site_description](../user-guide/configuration.md#site_description)：站点说明。
* [config.theme.locale](../user-guide/configuration.md#locale)（参见下文的 [主题配置]）。
* [config.extra_javascript](../user-guide/configuration.md#extra_javascript)：额外的 JavaScript 文件。
* [config.extra_css](../user-guide/configuration.md#extra_css)：额外的 CSS 文件。
* [config.repo_url](../user-guide/configuration.md#repo_url)：源代码库的 URL。
* [config.repo_name](../user-guide/configuration.md#repo_name)：源代码库名称。
* [config.google_analytics](../user-guide/configuration.md#google_analytics)：Google Analytics ID。

#### nav

`nav` 变量用于为文档创建导航。`nav` 对象是 [nav] 配置 setting 定义的 [导航对象][navigation objects] 的一个可迭代对象。

[nav]: ../user-guide/configuration.md#nav
[navigation objects]: #navigation-objects

::: mkdocs.structure.nav.Navigation
    options:
        show_root_heading: false
        show_root_toc_entry: true
        members: []
        heading_level: 4

除了迭代的 [导航对象][navigation objects]，`nav` 对象还包含以下属性：

::: mkdocs.structure.nav.Navigation.homepage
    options:
        show_root_full_path: false
        heading_level: 5

::: mkdocs.structure.nav.Navigation.pages
    options:
        show_root_full_path: false
        heading_level: 5

请注意，这个列表并不一定是所有站点页面的完整列表，因为它不包含未在导航中包含的页面。此列表与用于所有“下一页”和“上一页”链接的页面列表和顺序相匹配。要列出所有页面，请使用 [pages](#pages) 模板变量。

##### Nav 示例

以下示例显示前两个层次的目录结构。

```django
{% if nav|length > 1 %}
    <ul>
    {% for nav_item in nav %}
        {% if nav_item.children %}
            <li>{{ nav_item.title }}
                <ul>
                {% for nav_item in nav_item.children %}
                    <li class="{% if nav_item.active %}current{% endif %}">
                        <a href="{{ nav_item.url|url }}">{{ nav_item.title }}</a>
                    </li>
                {% endfor %}
                </ul>
            </li>
        {% else %}
            <li class="{% if nav_item.active %}current{% endif %}">
                <a href="{{ nav_item.url|url }}">{{ nav绝对地址被原样传递。如果URL是相对的，而模板上下文包括一个页面对象，那么URL将相对于页面对象返回。否则，URL将附带[base_url]({#base_url})前缀返回。

```django
<a href="{{ page.url|url }}">{{ page.title }}</a>
```

### tojson

安全地将Python对象转换为JavaScript脚本中的值。

```django
<script>
    var mkdocs_page_name = {{ page.title|tojson|safe }};
</script>
```

### script_tag

新功能：自1.5版本起使用。

将[extra_javascript]中的项目转换为`<script>`标签，其中考虑了所有[此配置的自定义]，并内置了[`|url`]({#url})行为的等效项。请参阅[基本主题]中如何使用它。

## 搜索和主题

自MkDocs版本0.17起，通过`search`插件向MkDocs添加了客户端搜索支持。主题需要提供一些东西供插件与主题一起使用。虽然`search`插件默认情况下已激活，用户可以禁用插件，主题应该考虑这一点。建议主题模板使用下面的插件检查将搜索特定标记包装进去：

```django
{% if 'search' in config.plugins %}
    search stuff here...
{% endif %}
```

在其最基本的功能中，搜索插件将简单地提供一个索引文件，该文件不超过包含所有页面内容的JSON文件。主题需要在客户端执行自己的搜索功能。然而，通过一些设置和必要的模板，该插件可以提供基于[lunr.js]的完整功能的客户端搜索工具。下面的HTML需要添加到该主题中，以使提供的JavaScript能够正确加载搜索脚本，并从当前页中的搜索结果创建相对链接。

```django
<script>var base_url = {{ base_url|tojson }};</script>
```

使用正确配置的设置，模板中的以下HTML将向您的主题添加完整的搜索实现。

```django
<h1 id="search">Search Results</h1>

<form action="search.html">
  <input name="q" id="mkdocs-search-query" type="text" >
</form>

<div id="mkdocs-search-results">
  Sorry, page not found.</div>
```

插件中的JavaScript通过查找上述HTML中使用的特定ID来工作。用户为用户键入搜索查询的表单输入必须使用`id="mkdocs-search-query"`进行标识，并且将结果放置的div必须使用`id="mkdocs-search-results"`进行标识。插件支持在[主题的配置文件](`mkdocs_theme.yml`)中设置以下选项:

### include_search_page

确定搜索插件是否希望主题通过位于`search/search.html`的模板提供专用搜索页面。当`include_search_page`设置为`true`时，将构建并在`search/search.html`中提供搜索模板。该方法由`readthedocs`主题使用。当`include_search_page`设置为`false`或未定义时，期望该主题提供其他显示搜索结果的机制。例如，`mkdocs`主题通过模态方式在任何页面上显示结果。### search_index_only

确定搜索插件是否应仅生成搜索索引还是完整的搜索解决方案。当`search_index_only`设置为`false`时，搜索插件通过添加具有较低优先级的自己的`templates`目录（比主题低）并向`extra_javascript`配置设置添加其脚本来修改Jinja环境。当`search_index_only`设置为`true`或未定义时，搜索插件不会对Jinja环境进行任何修改。使用提供的索引文件的完整解决方案是主题的责任。搜索索引写入[site_dir]中的JSON文件`search/search_index.json`。文件中包含的JSON对象可以包含最多三个对象。```json
{
    config: {...},
    docs: [...],
    index: {...}
}
```

如果存在，则`config`对象包含在用户的`mkdocs.yml`配置文件中为插件定义的配置选项的键/值对。`config`对象是MkDocs版本*1.0*的新功能。`docs`对象包含文档对象列表。每个文档对象由`location`（URL）、`title`和可以用于创建搜索索引和/或显示搜索结果的`text`组成。如果存在，则`index`对象包含预构建索引，可为较大站点提供性能改进。请注意，只有当用户显式启用了[prebuild_index]配置选项时，才会创建预构建的索引。主题应该预计索引不存在，但可以选择在可用时使用索引。`index`对象是MkDocs版本*1.0*的新功能。[Jinja2 template]: https://jinja.palletsprojects.com/
[built-in themes]: https://github.com/mkdocs/mkdocs/tree/master/mkdocs/themes
[主题的配置文件]: #主题配置
[lunr.js]: https://lunrjs.com/
[site_dir]: ../user-guide/configuration.md#site_dir
[prebuild_index]: ../user-guide/configuration.md#prebuild_index
[Jinja's default filters]: https://jinja.palletsprojects.com/en/latest/templates/#builtin-filters

## 打包主题

MkDocs使用[Python packaging]来分发主题，其中有一些要求。有关包含一个主题的包的示例，请参见[MkDocs Bootstrap主题]，有关包含许多主题的包的示例，请参见[MkDocs Bootswatch主题]。

注意:不必严格打包主题，因为整个主题可以包含在`custom_dir`中。如果您创建了“一次性主题”。但是，如果您打算分发您的主题供他人使用，则打包主题具有某些优点。通过打包您的主题，您的用户可以更轻松地安装它，他们可以依赖于定义的默认[configuration]，然后他们可以利用[custom_dir]来调整您的主题以更好地符合其需求。[Python packaging]: https://packaging.python.org/en/latest/
[MkDocs Bootstrap theme]: https://mkdocs.github.io/mkdocs-bootstrap/
[MkDocs Bootswatch theme]: https://mkdocs.github.io/mkdocs-bootswatch/

### 包装布局

以下布局建议用于主题。该目录处于顶层目录中，称为`MANIFEST.in`和`setup.py`旁边的主题目录，其包含一个空的`__init__.py`文件，一个主题配置文件（`mkdocs_theme.yml`）以及您的模板和媒体文件。

```text
.|-- MANIFEST.in
|-- theme_name
|   |-- __init__.py
|   |-- mkdocs_theme.yml
|   |-- main.html
|   |-- styles.css
`-- setup.py
```

在`MANIFEST.in`文件中，应包含以下内容，但应将`theme_name`更新为包括任何额外文件扩展名的内容。

```text
recursive-include theme_name *.ico *.js *.css *.png *.html *.eot *.svg *.ttf *.woff
recursive-exclude * __pycache__
recursive-exclude * *.py[co]
```

`setup.py`应包括以下文本，其中包含下面讲述的修改。

```python
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="mkdocs-themename",
    version=VERSION,
    url='',
    license='',
    description='',
    author='',
    author_email='',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'themename = theme_name',
        ]
    },
    zip_safe=False
)
```

填写URL、许可证、描述、作者和作者电子邮件地址。名称应遵循`mkdocs-themename`约定（如`mkdocs-bootstrap`和`mkdocs-bootswatch`），以MkDocs开头，使用连字符分隔单词，包括您的主题名称。文件的大部分内容可以不编辑。我们还需要更改最后一个部分entry_points。这是MkDocs找到您包含在包中的主题的方式。左侧的名称是用户将在其mkdocs.yml中使用的名称，右侧是包含主题文件的目录。您在本节开头创建的目录应该包含所有其他主题文件的主要文件main.html。至少，它必须包含主题的`main.html`。**必须**还包括一个名为`__init__.py`的文件，该文件应为空文件，该文件告诉Python该目录是软件包。### 主题配置

打包主题需要包含一个名为`mkdocs_theme.yml`的配置文件，该文件位于模板文件的根目录中。文件应该包含主题的默认配置选项。但是，如果该主题未提供配置选项，则仍需要该文件，并且可以留空。不需要一个名为`mkdocs_theme.yml`的未打包的主题文件，因为该文件不会从`theme.custom_dir`中加载。主题作者可以定义任何认为必要的任意选项，并且这些选项将在模板中可用于控制行为。例如，主题可能希望使侧边栏是可选的，并在`mkdocs_theme.yml`文件中包括以下内容：

```yaml
show_sidebar: true
```

然后，在模板中，可以引用该配置选项：

```django
{% if config.theme.show_sidebar %}
<div id="sidebar">...</div>
{% endif %}
```

用户可以在其项目的`mkdocs.yml`配置文件中覆盖此默认值：

```yaml
theme:
  name: themename
  show_sidebar: false
```

除了主题定义的任意选项外，MkDocs定义了一些特殊选项，它们会改变其行为：

> BLOCK:
>
> #### locale
>
> 此选项镜像了主题配置选项中的[开关]。如果`mkdocs_theme.yml`文件中未定义此值，并且用户在`mkdocs.yml`中未设置它，则它将默认为`en`（英语）。该值应与主题中使用的文本匹配（例如，“上一个”和“下一个”链接），并应作为`<html>`标记的`lang`属性的值使用。有关详细信息，请参见[支持主题本地化/翻译](#支持主题本地化/翻译)。
> 请注意，在配置验证期间，提供的字符串会转换为`Locale`对象。该对象包含`Locale.language`和`Locale.territory`属性，并且将在模板中作为字符串解析。因此，以下内容将正常工作：
>
> ```html
> <html lang="{ config.theme.locale }">
> ```
>
> 如果语言设置为`fr_CA`（加拿大法语），则上面的模板将呈现为：
>
> ```html
> <html lang="fr_CA">
> ```
>
> 如果您不想包括领域属性，则直接引用`language`属性：
>
> ```html
> <html lang="{ config.theme.locale.language }">
> ```
>
> 那将呈现为：
>
> ```html
> <html lang="fr">
> ```
>
> #### static_templates
>
> 此选项镜像了主题配置中的[开关]，并允许设置一些默认值。请注意，虽然用户可以向此列表添加模板，但用户不能删除包含在主题配置中的模板。
> #### extends
>
> 定义此主题所继承的父主题。该值应为父主题的固定字符串名称。适用正常[Jinja继承规则]。插件还可以定义一些选项，允许主题通知插件它希望使用哪些插件选项。请参见任何您希望在主题中支持的插件的文档。### 分发主题

按照上述更改，您的主题现在应该准备安装了。这可以使用pip完成，如果仍在setup.py所在目录中，则可以使用`pip install .`。大多数Python软件包，包括MkDocs，在PyPI上分发。为此，您应该运行以下命令。

```bash
python setup.py register
```

如果您还没有设置帐户，则会提示您创建一个。有关详细信息，请参见官方Python打包文档[Packaging and Distributing Projects]。[Packaging and Distributing Projects]: https://packaging.python.org/en/latest/distributing/

## 支持主题本地化/翻译

虽然内置主题提供了在模板中[本地化/翻译]的支持，但自定义主题和第三方主题可能选择不支持。无论如何，`theme`配置选项中的[`locale`](#locale)设置始终存在，其他部分依赖于它。因此，建议所有第三方主题使用相同的设置来指定语言，而不考虑它们用于翻译的系统。以这种方式，无论用户选择哪个主题，都将体验到一致的行为。

翻译管理方法由主题的开发人员决定。然而，如果主题开发人员选择使用内置主题使用的机制，则以下各节概述如何启用和使用MkDocs使用的相同命令。

[本地化/翻译]: ../user-guide/localizing-your-theme.md

### 使用本地化/翻译命令

警告:
由于默认情况下[pybabel]未安装，并且大多数用户不会安装pybabel，请确保已安装必要的依赖项（使用`pip install mkdocs[i18n]`）。否则，主题开发人员和/或翻译人员应确保已安装必要的依赖项。

翻译命令应从主题的工作树的根目录中调用。有关MkDocs用于翻译内置主题的工作流程的概述，请参见Contributing Guide的相应[部分]和[Translation Guide]。

[pybabel]: https://babel.pocoo.org/en/latest/setup.html
[部分]: ../about/contributing.md#submitting-changes-to-the-builtin-themes
[Translation Guide]: translations.md

### 示例自定义主题的本地化/翻译工作流程

请按照[MkDocs基本主题][basic theme]的示例，随时添加任何翻译。通过在HTML源中使用`{% trans %}`和`{% endtrans %}`包装文本来编辑模板，如下所示：

```diff
--- a/basic_theme/base.html
+++ b/basic_theme/base.html
@@ -88,7 +88,7 @@

 <body>

-  <h1>This is an example theme for MkDocs.</h1>
+  <h1>{% trans %}This is an example theme for MkDocs.{% endtrans %}</h1>

   <p>
     It is designed to be read by looking at the theme HTML which is heavily
```

然后，按照[翻译指南]的常规方式启动翻译工作。### 与主题一起打包翻译

当`extract_messages`命令创建的可移植对象模板（`pot`）文件和`init_catalog`和`update_catalog`命令创建的可移植对象(`po`)文件用于创建和编辑翻译时，它们不直接用于MkDocs并且不需要包含在主题的打包版本中。当MkDocs使用翻译构建站点时，它只使用指定语言的二进制`mo`文件。因此，在[打包主题]时，请确保在“wheels”中包含它，使用`MANIFEST.in`文件或其他方式。然后，在构建Python软件包之前，您将希望确保针对每种语言的二进制`mo`文件是最新的，通过为每种语言运行`compile_catalog`命令来完成。

MkDocs希望二进制`mo`文件位于`locales/<locale>/LC_MESSAGES/messages.mo`，该文件由`compile_catalog`命令自动执行。有关详细信息，请参见[Testing theme translations]。请注意:
如我们的[Translation Guide]中所述，MkDocs项目已选择包含[pybabel]为我们的代码存储库中的`pot`和`po`文件，但未包含`mo`文件。这需要我们始终