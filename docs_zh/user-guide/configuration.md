# 配置

所有可用配置设置的指南。

---

## 介绍

项目设置默认使用名为 `mkdocs.yml` 的项目目录中的 YAML 配置文件进行配置。您可以指定另一个路径，方法是使用 `-f`/`--config-file` 参数（参见 `mkdocs build --help`）。

至少，此配置文件必须包含 `site_name`。所有其他设置都是可选的。

## 项目信息

### `site_name`

这是一个 **必需的设置**，应是一个字符串，用作项目文档的主标题。例如：

```yaml
site_name: Marshmallow Generator
```

在渲染主题时，此设置将作为 `site_name` 上下文变量传递。

### `site_url`

设置站点的规范化URL。这将在每个HTML页面的 `head` 部分添加具有 `canonical` URL 的 `link` 标记。如果MkDocs网站的 `root` 在域的子目录中，确保在该设置中包括该子目录（例如 `https://example.com/foo/`）。

此设置还用于 `mkdocs serve`：服务器将挂载到 URL 的路径组件上，例如 `some/page.md` 将从 `http://127.0.0.1:8000/foo/some/page/` 提供，以模拟预期的远程布局。

**默认值**：`null`

### `repo_url`

设置一个链接到您的存储库（GitHub、Bitbucket、GitLab 等）的URL，用于每个页面。

```yaml
repo_url: https://github.com/example/repository/
```

**默认值**：`null`

### `repo_name`

当设置时，在每个页面上为您的存储库提供链接的名称。

**默认值**：如果 `repo_url` 匹配这些域名，则为 “GitHub”、 “Bitbucket” 或 “GitLab”，否则为来自 `repo_url` 的主机名。

### `edit_uri`

当直接查看页面时从基本 `repo_url` 计算的文档目录的路径，考虑存储库主机的具体情况（例如 GitHub、Bitbucket 等等）、分支和文档目录本身。MkDocs 连接 `repo_url` 和 `edit_uri`，并将页面的输入路径附加到其后。

当设置并且如果您的主题支持它时，将为您的源存储库中的页面提供直接链接。这使查找和编辑页面的源文件变得更加容易。如果未设置 `repo_url`，则忽略此选项。在某些主题上，设置此选项可能导致在存储库链接的位置使用编辑链接。其他主题可能显示两个链接。

`edit_uri`支持查询 (`?`) 和片段 (`#`) 字符。对于使用查询或片段访问文件的存储库主机，可能会设置 `edit_uri` 如下（请注意URI中的 `?` 和 `#` …）。

```yaml
# 查询字符串示例
edit_uri: '?query=root/path/docs/'
```

```yaml
# 路径片段示例
edit_uri: '#root/path/docs/'
```

对于其他存储库主机，请简单地指定到文档目录的相对路径。

```yaml
# 查询字符串示例
edit_uri: root/path/docs/
```

例如，具有此配置：

```yaml
repo_url: https://example.com/project/repo
edit_uri: blob/main/docs/
```

意味着名为 'foo/bar.md' 的页面的编辑链接将带到：<https://example.com/project/repo/blob/main/docs/foo/bar.md>

`edit_uri` 实际上可以只是绝对 URL 而不一定是相对于 `repo_url` 的路径，因此可以实现相同的结果：

```yaml
edit_uri: https://example.com/project/repo/blob/main/docs/
```

要获得更大的灵活性，请参见下面的 [edit_uri_template](#edit_uri_template)。

> 注意：
> 在一些已知的主机上（特别是 GitHub、Bitbucket 和 GitLab），`edit_uri`是从 'repo_url' <repo_url> 中派生出来，无需手动设置。只需定义一个 `repo_url` 将自动填充 `edit_uri` 配置设置。
>
> 例如，对于托管在 GitHub 或 GitLab 上的存储库，`edit_uri` 会自动设置为 `edit/master/docs/` （请注意 `edit` 路径和 `master` 分支）。
>
> 对于名为 Bitbucket 的存储库，等效的 `edit_uri` 将自动设置为 `src/default/docs/`（请注意 `src` 路径和 `default` 分支）。
>
> 要使用与默认 URI 不同的 URI（例如不同的分支），只需将 `edit_uri` 设置为所需的字符串。如果您不想在页面上显示任何 “编辑 URL 链接”，请将 `edit_uri` 设置为空字符串以禁用自动设置。

警告：在 GitHub 和 GitLab 上，使用默认的 "编辑" 路径（`edit/master/docs/`）将示例在在线编辑器中打开页面。这个功能需要用户拥有并登录到 GitHub/GitLab 账户。否则，用户将被重定向到登录/注册页面。或者，使用 "blob" 路径（`blob/master/docs# MkDocs配置文件指南

欢迎来到MkDocs的配置文件指南。使用此指南，你可以了解与MkDocs构建文档站点有关的所有配置选项和设置。本指南作为官方文档的一部分，记录了MkDocs在处理配置文件和其他设置时所采用的标准。

## 标准配置选项

MkDocs预定义了许多配置选项，以确保运行MkDocs时可以使用关键选项的默认值。本节中提供了完整的，预定义的配置选项清单，以及用于自定义配置选项的相关说明和建议。

以下是MkDocs中可用的标准配置选项的清单：

### `site_name`

用于指定站点的名称，通常出现在每个页面的标题栏中。它可以是一个字符串，也可以是多国语言的语言文件，类似于[MkDocs主题](../dev-guide/themes.md)。以下是一个基本示例：

```yaml
site_name: My Docs
```

以下是使用语言文件的示例：

```yaml
site_name: !lang my_docs
```

在上面的示例中，`my_docs`是一个语言文件，应该放置在主题语言目录的根目录中。

### `site_description`

用于指定站点的描述，通常会出现在页面的元描述标记中（如果定义的话）。它既可以是字符串，也可以是HTML。以下是一个基本示例：

```yaml
site_description: My documentation site
```

在上面的示例中，值是一个字符串。如果你想显示有样式的富文本，可以定义HTML：

```yaml
site_description: <em>My</em> documentation site
```

### `site_author`

用于指定站点的作者（或列出所有作者，以及每个页面的单个作者）。例如：

```yaml
site_author: John Doe
```

或者，对于多个作者的列表：

```yaml
site_author:
  - John Doe
  - Jane Smith
```

或者，对于每个页面的单个作者定义：

```yaml
pages:
  - Home: index.md
  - About: about.md
    author: John Doe
```

在上面的例子中，`About`页面的作者将是`John Doe`。

### `site_url`

用于指定站点的URL。它用于`sitemap.xml`和`robots.txt`文件中。例如：

```yaml
site_url: https://example.com
```

如果没有指定端口，则可以省略这个值的http/https前缀：

```yaml
site_url: example.com
```

并且，如果将`site_url`设为''（空字符串），则会使用MkDocs在本地服务器上访问时自动识别的值（如果已检测到），这个值不能倍用于生成`sitemap.xml`文件。

当你在本地开发站点时，可以采用相对URL代替完整URL：

```yaml
site_url: ''
```

在这种情况下，MkDocs在生成的URL中使用相对URL。

### `repo_url`

将此设置为repo的URL。如果设置了这个选项，MkDocs将在每个页面中包含一个`Edit`链接。例如：

```yaml
repo_url: https://github.com/user/repo/
```

Edit链接将指向具有基础URL的组合：`{repo_url}/edit/{branch}/{filename}`。如果不指定仓库的分支，请将它留空。如果想链接到页面所在分支的Github Pages站点, 请添加"blob/master"作为repo_url的路径, 参见:

```yaml
repo_url: https://github.com/user/repo/blob/master
```

这将导致页面的URL修改为：`https://github.com/user/repo/blob/master/{filename}`。在GitHub的发布页面中为您的用户提供一个界面，以便贡献和提取GitHub项目。

### `repo_name`

用于指定库名称，将在一些主题的选项卡或页脚中使用。例如：

```yaml
repo_name: my-docs
```

### `edit_uri`

用于指定页面的编辑URL模板。它被用于使用其他源管理器的用户。模板中的`{filename}`部分将被替换为当前页面的文件名。例如：

```yaml
edit_uri: "https://github.com/user/repo/edit/branch/docs/{filename}.md"
```

### `docs_dir`

指定文档源文件的文件夹。如果你在文档编写时使用标准的文件夹结构，这将很有用。例如：

```yaml
docs_dir: docs
```

如果您的文档在站点同级别下，建议留空。通常MkDocs会自动发现文件夹结构。

### `site_dir`

用于指定存储生成文档的目标路径。默认情况下，文档将放置在`site`文件夹中。例如:

```yml
site_dir: ../build/docs
```

在上面的例子中，生成的文件放置在`../build/docs`中。

### `theme`

用于指定主题。此配置选项可以是字符串或字典。如果是字符串，则表示主题名称（模板网站上可用的名称）。如果是字典，它将解析为包含以下键值对的字典：

* `name` (required): 主题名称。
* `custom_dir`: 主题要求的自定义文件目录。
* `dirs`: 自定义子目录路径。
* `static_templates`: 如果设置为`true`，则在主题目录中首先查找静态模板。
* `locale`: 指定选定语言主题的位置。

以下是一个基本示例：

```yaml
theme: readthedocs
```

以下是字典格式的示例：

```yaml
theme:
  name: material
  custom_dir: mymaterial
  dirs:
    assets: assets
    templates: _templates
```

如果要使用本地主题，则可以将`theme_dir`选项指向该主题的路径. 注意这里不包括主题名称。

```yaml
theme_dir: ../my-material-theme
theme:
  name: material
```

除了内置主题之外，你还可以创建自己的主题。[这里](../dev-guide/themes.md)提供了有关如何创建你自己的主题的详细信息。

注：`default`主题不需要定义，因为它是默认的主题，这个主题可以在[选择你的主题](choosing-your-theme.md)中进一步了解。

### `theme_color`

的主题颜色。在移动设备上，Chrome和Firefox将在浏览器的地址栏中显示这种颜色。如果用户将站点添加到主屏幕，则可用于提供应用程序的样式。例如:

```yaml
theme_color: pink
```

### `logo`

用于指定站点的标志文件或图像文件路径。默认情况下，在所有页面的左上角将始终显示站点名称。如果配置为文件路径，则使用指定的文件表示默认情况下会显示出来的站点名称。例如：

```yaml
logo: img/my_logo.png
```

上面的示例中，`my_logo.png`是存储在`/docs/img/`目录中的图像文件。

### `favicon`

用于指定站点的favicon文件路径。如果指定了favicon，MkDocs会自动生成`favicon.ico`，并在每个页面的页面头部覆盖默认favicon。例如：

```yaml
favicon: img/favicon.png
```

在上面的示例中，favicon的图像文件应该存储在`/docs/img/`中。

### `extra_css`

用于指定一个CSS文件，该文件将被注入到每个页面的页面头部中。例如：

```yaml
extra_css: css/my_custom_style.css
```

在上面的示例中，`my_custom_style.css`是一个存储在`/docs/css/`目录中的自定义CSS文件。

### `extra_javascript`

用于指定包含任意JavaScript代码的JavaScript文件或URL。它将被注入到每个页面的页面底部。例如：

```yaml
extra_javascript: js/my_custom_script.js
```

在上面的示例中，`my_custom_script.js`是一个存储在`/docs/js/`目录中的自定义JavaScript文件。

### `markdown_extensions`

用于指定Markdown扩展。除了标准的Markdown，Python Markdown提供了许多扩展，而MkDocs可以使用[常见的扩展](https://python-markdown.github.io/extensions/)和[pymdownx扩展](https://facelessuser.github.io/pymdown-extensions/)。此外，Python Markdown Wiki中还有更多[扩展](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions)供选择。以下是一个具有多个扩展的完整示例：

```yaml
markdown_extensions:
  - footnote
  - codehilite:
      linenums: true
  - extra
  - smarty:
      curly_dashes: true
```

### `plugins`

用于指定[MkDocs插件](../dev-guide/plugins.md)。插件可用于添加额外的功能，如搜索，自定义选项卡和自定义CSS文件等等。在此处指定的每个插件的特定配置详细信息将取决于该插件。

参见[可用插件目录](https://github.com/mkdocs/catalog)。

以下是一个具有多个插件的完整示例：

```yaml
plugins:
  - search
  - mkdocs-minify-plugin
```

### `nav`

用于定义站点的导航结构和页面。在基础形式中，这是一个页面名称和标题的字典，或者是一个页面名称和一个子字典的组合。子字典可用于表示单个页面的配置。例如：

```yaml
nav:
  - Home: index.md
  - User Guide:
    - Writing your docs: writing-your-docs.md
    - Configuring pages: configuring-pages.md
    - Customizing your theme: customizing-your-theme.md
```

在上面的例子中，`User Guide`被视为一个包含子页面的页面。子页面的下拉选项是定义该页面的字典的第二个部分。在上面的示例中，`User Guide`字典包含三个键值对，因为它定义了该页面及其子页面。在此示例中，每个页面定义为一个Markdown文件的路径。

每个页面都可以有可选的元数据。支持的元数据字段是：

* `title`: 页面的标题，如果未定义则使用页面的文件名。
* `description`: 页面的描述，如果未定义则使用在页面中找到的文本的一部分。
* `keywords`: 页面的关键字。
* `hide`: 将页面从导航栏中隐藏。

以下是一个完整的具有元数据的示例：

```yaml
nav:
  - Home: index.md
  - About: about.md
    title: About us
    description: Learn more about who we are and what we do.
    keywords: [about, us]
    hide: true
```

如果你没有提供导航结构，则MkDocs将使用查找指定文件夹中的所有Markdown文件并在导航中包含每个文件的标题。有关自动生成的导航结构的更多信息，请参见[构建页面](building-the-site.md#building-your-pages)。

### `exclude`

用于指定应从生成的站点中排除的文件和文件夹。例如：

```yaml
exclude:
  - SECRET_NOTE.txt
  - secret_folder
```

在上面的例子中，`SECRET_NOTE.txt`文件和`secret_folder`文件夹都将在构建站点时排除。

请注意，在默认情况下，与构建需要的文件数量相比，对于不属于站点内容的文件，排除不提高构建性能。如果在设置中指定了除了Markdown之外的其他文件类型，则必须将它们包含在内。

默认情况下，README和index文件什么时候将被忽略。如果您想要包含一个README文件或文件名为’index’的Markdown文件，您可以使用此选项防止该文件被排除。

例如，如果不想要您的README文件被排除，则可以：

```yaml
exclude: ['!README.md']
```

### `include`

和排除选项的作用相反，允许您只包含明确指定要生成的文件和文件夹。在大型文档库中使用时，它可能会加速生成`.md`文件到`.html`文件形式的转换。其中一种情况是，当只有一个列表标准时，选项的排除部分可能更容易维护，而选项的包含部分则更难维护。例如：

```yaml
include:
  - api
  - api/my_module.md
```

在上面的示例中，`api`文件夹和`api/my_module.md`文件将在构建站点时包含。

### `extra`

用于添加自定义键值。这对于存储MkDocs无法或不提供的其他元数据或元数据非常有用。这可以是一个字符串或一个包含键值对的字典。例如：

```yaml
extra:
  website: https://example.com
  owner: John Doe
```

在上面的例子中，`website`和`owner`是任意的自定义键。

### `markdown_css`

用于指定用于Markdown渲染的CSS文件。默认情况下，这个选项是`markdown.css`并且是在主题目录中定义的。如果你想使用不同的CSS文件，则需要使用这个选项来指定另一个文件。例如：

```yaml
markdown_css: css/my_custom_markdown.css
```

### `strict`

用于停止在发现错误时生成站点。例如：

```yaml
strict: true
```

### `use_directory_urls`

将这个选项设置为`true`，将使用MkDocs的高级路由功能将文件URL更改为不带.htm的目录样式。例如：

```yaml
use_directory_urls: true
```

如果选择此选项，则将不再通过`.htm`文件扩展来访问任何文件。而是，像这样访问它们：

```
http://localhost:8000/about/
```

在上面的示例中，您可以通过路径`/about/`访问`about.md`文件的内容。

### `use_directory_index`

请开启这个选项以在使用目录URL时自动包含名为`index`的Markdown文件。例如：

```yaml
use_directory_urls: true
use_directory_index: true
```

在上面的示例中，`about/index.md`可以通过路径`/about/`来访问。

### `markdown`

用于配置Python Markdown的选项。此选项使用一个字典来传递配置。下面是一些示例：

```yaml
markdown:
  extension_configs:
    pymdownx.magiclink:
      repo_url_shortener: true
```

在上面的示例中，`pymdownx.magiclink`是Markdown扩展之一，`repo_url_shortener: true`是将在扩展上使用的配置。

### `extra_files`

指定一个不属于您文档和主题的目录（此选项用于记录`.nojekyll`文件或其他文件）或文件图标。例如，在设置IGG披露徽标：

```yaml
extra_files:
  - igg-badge.png
```

`.nojekyll`文件将防止在您的GitHub Pages上运行站点时从另一个文件夹开头忽略文件夹或文件。

```yaml
extra_files:
  - .nojekyll
```

注：如果你想隐藏`.nojekyll`文件，可以设置`.githubfile`并使用`.gitignore`来隐藏目录或文件。

更多有关`.nojekyll`文件相关信息：

- [GitHub pages下的`.nojekyll`](https://blog.csdn.net/Roteleader/article/details/105191101)
- [让 GitHub Pages 保留文件和目录名中的下划线](https://segmentfault.com/a/1190000016684221)

### `toc`

如果禁用章节标题链接中的锚定，则使用该选项。通常，单击标题后将链接移到文档的特定部分。例如：

```yaml
toc:
  toc_depth: 2
  permalink: true
```

在上面的示例中，`toc_depth`控制到目录的级别。使用这个选项可以控制web页面上呈现的Markdown到C目录的深度。默认值为`2`。

当`permalink`为`true`时，这个选项添加了一个蓝色的链接，用户可以点击它，使一个永久链接到当前标题在目录中生成。

### `markdown_engine`

设置使用的Markdown处理器。默认情况下，MkDocs使用Python Markdown：`pymd`。您可以设置为其他处理程序，例如CommonMark：`commonmark`或Python Markdown的扩展版：`misaka`。例如：

```yaml
markdown_engine: commonmark
```

### `markdown_extensions`

你可以自定义要为站点构建的Markdown扩展。默认情况下，MkDocs已经包括了[pymdownx扩展](https://facelessuser.github.io/pymdown-extensions/)。您可以指定包含哪些扩展及其参数。以下是一个完整的示例：

```yaml
markdown_extensions:
  - pymdownx.emoji:
      emoji_generator: !!python/name:pymdownx.emoji.to_svg
  - pymdownx.inlinehilite
  - pymdownx.superfences:
      custom_fences:
        - {
            name: "console",
            class: "console",
            format: "!!python/name:pymdownx.superfences.fence_div_format"
          }
```

### `markdown_extensions_configs`

如果您有多个选项可以为一个Markdown扩展进行配置，则可以使用此设置为它们分别配置参数。以下是一个示例：

```yaml
markdown_extensions:
  - pymdownx.details

markdown_extension_configs:
  pymdownx.details:
    block_expander: ">"
```

在上面的示例中，只传递`pymdownx.details`扩展名，默认情况下没有参数。但是，通过使用`markdown_extensions_configs`，将设置该扩展内部的子选项之一：`block_expander`。

### `exclude_file`

用于指定yaml文件，其中包含应该在构建站点时排除的文件和文件夹。

```yaml
exclude_file: exclude.yaml
```

在上面的示例中，`exclude.yaml`文件包含排除的文件和文件夹清单。

### `language`

用于指定语言设置。此选项表示由[iso 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)定义的语言代码字符串或语言文件。这将更改日期和时间的格式，生成正确的元HTML Lang标记，生成日期的合适格式等。例如：

```yaml
language: zh
```

或：

```yaml
language: !lang es
```

在上面的第二个例子中，使用`!lang`的例子是一个文件名为`lang/es.yaml`的文件，其中包含日历、日期等的语言设置。

### `metadata`

此选项可用于设置页面相关的如发布日期、修改日期、作者等元数据。数据添加到页面的元数据：`<meta>`标签和HTML注释中。通常在主题中修改和使用这些值，以及将它们添加到feed.xml中。

以下是一个完整的示例，说明如何在一个页面上使用元数据：

```yaml
pages:
- Some Section:
  - index.md:
      title: Some Section
  - page.md:
      title: A Subpage
      published: 2014-03-17
      modified: 2015-08-11T13:32:37+00:00
      author: John Smith <john@example.com>
      description: A short description of the content on the page.
```

默认情况下，元数据转换为HTML注释并放在页面的顶部。如果你想将它们作为`<meta>`标签添加到`<head>`中，你的主题应该告诉你如何这样做。例如，在使用`mkdocs-moonstone`主题时，可以在`extra.javascript`中指定名为`window.MKDOCS_METADATA`的元对象：

```yaml
extra_javascript:
  - !javascript |
      window.MKDOCS_METADATA = {{ metadata|tojson|safe }};
      console.log("Metadata", window.MKDOCS_METADATA);
```

在上面的示例中，使用`!javascript`是为了防止单引号的使用。如果没有使用`!javascript`，则需要转义引号。

它还被交付到一个指定的feed.xml文件中，如果存在。

### `search`

用于启用搜索。此选项指定了许多选项，这些选项由[Lunr.js搜索库](https://lunrjs.com/)使用。以下是一个完整的示例：

```yaml
search:
  lang: zh
  # The minimum length of a search query.
  min_search_length: 1
  # A list of modes to search on (leave blank for all).
  search_modes:
    - Loose
  # A list of characters that split the search query into tokens.
  separator: '[\s\-\.]+'
  prebuild_index: False
  indexing: 'full'
```

此外还有一些其他可用选项。

### `min_search_length`

用于定义搜索查询的最小长度的整数值。默认情况下，忽略搜索长度小于3个字符的搜索结果。但是，对于一些使用情况（例如，关于消息队列的文档可能会生成对“MQ”的搜索），希望设置一个比较短的限制。例如：

```yaml