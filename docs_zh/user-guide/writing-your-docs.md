# 编写你的文档

如何布局和编写你的Markdown源文件。

---

## 文件布局

你的文档源应编写为常规Markdown文件（参见 [使用Markdown编写](#使用Markdown编写)），并放置在[文档目录](configuration.md#docs_dir)中。默认情况下，该目录将被命名为 `docs`，并将位于项目的顶级目录，与配置文件 `mkdocs.yml` 并列。

你可以创建一个最简单的项目如下：

```text
mkdocs.yml
docs/
    index.md
```

按照惯例，项目主页应命名为 `index.md`（有关详细信息，请参见下面的 [索引页面](#index-pages)）。Markdown源文件可以使用以下任何文件扩展名：`markdown`、`mdown`、`mkdn`、`mkd`、`md`。文档目录中包括的所有Markdown文件都将在构建站点时呈现，而不考虑任何设置。 

注意：
以点开始命名的文件和目录（例如：`.foo.md` 或 `.bar/baz.md`）将被MkDocs忽略。这可以使用[`exclude_docs`配置项](configuration.md#exclude_docs)覆盖。

您还可以创建多页文档，通过创建多个Markdown文件：

```text
mkdocs.yml
docs/
    index.md
    about.md
    license.md
```

您使用的文件布局决定了用于生成页面的URL。考虑上述布局，将为以下URL生成页面：

```text
/
/about/
/license/
```

如果更适合您的文档布局，您也可以在嵌套目录中包含您的Markdown文件。

```text
docs/
    index.md
    user-guide/getting-started.md
    user-guide/configuration-options.md
    license.md
```

内部嵌套目录中的Markdown文件将导致生成带有嵌套URL的页面，如下所示：

```text
/
/user-guide/getting-started/
/user-guide/configuration-options/
/license/
```

在[文档目录](configuration.md#docs_dir)中未标识为Markdown文件（通过其文件扩展名）的任何文件都将由MkDocs不加修改地复制到已构建的站点中。有关详细信息，请参见[链接到图像和媒体](#链接到图像和媒体)。

### 索引页面

默认情况下，当请求目录时，大多数Web服务器会返回该目录内包含的索引文件（通常命名为 `index.html`）（如果存在的话）。出于这个原因，以上所有示例中的主页都被命名为 `index.md`，当构建站点时，MkDocs将其呈现为 `index.html`。

许多存储库托管网站通过在浏览目录内容时显示README文件的内容来提供特殊处理。因此，MkDocs允许您将索引页面命名为`README.md`而不是 `index.md`。因此，当用户浏览源代码时，存储库主机可以将该目录的索引页面显示为README文件。但是，当MkDocs呈现您的站点时，该文件将被重命名为`index.html`，以便服务器将其作为正确的索引文件提供。

如果在同一目录中找到一个 `index.md` 文件和一个 `README.md` 文件，那么将使用 `index.md` 文件，而将忽略 `README.md` 文件。

### 配置页面和导航

您的 `mkdocs.yml` 文件中的 [nav](configuration.md#nav) 配置设置定义了包括全局站点导航菜单以及该菜单的结构在内的哪些页面。如果未提供，则将通过在[文档目录](configuration.md#docs_dir)中发现所有Markdown文件来自动创建导航。自动创建的导航配置始终按文件名按字母数字顺序排序（子节中的索引文件始终排在第一位）。如果你想以不同的方式排序你的导航菜单，你需要手动定义你的导航配置。

最简单的导航配置可能如下：

```yaml
nav:
  - 'index.md'
  - 'about.md'
```

导航配置中的所有路径都必须相对于`docs_dir`配置选项。如果该选项设置为默认值 `docs`，那么上述配置的源文件将位于 `docs/index.md` 和 `docs/about.md`。

上述示例将生成两个顶级导航项，并以Markdown文件或（如果文件中未定义标题）文件名为标题推断导航项的标题。要在 `nav` 设置中覆盖标题，请在文件名之前加上标题。

```yaml
nav:
  - Home: 'index.md'
  - About: 'about.md'
```

请注意，如果在导航中为页面定义了标题，则在整个站点中使用该标题，并覆盖页面自身定义的标题。

可以通过将相关页面列在具有标题的分组下来创建导航子项。例如：

```yaml
nav:
  - Home: 'index.md'
  - 'User Guide':
    - 'Writing your docs': 'writing-your-docs.md'
    - 'Styling your docs': 'styling-your-docs.md'
  - About:
    - 'License': 'license.md'
    - 'Release Notes': 'release-notes.md'
```

用上述设置，我们有三个一级项：“Home”，“User Guide”和“About”。Home是站点主页的链接。在“User Guide”下列出了两页：“编写文档”和“样式化文档”。在“About”下列出了两个页面：“License”和“Release Notes”。

请注意，一个部分不能有一个页面分配给它。部分仅是子页面和子部分的容器。您可以尽可能深地嵌套部分。但要小心，不要通过过度复杂的嵌套使用户在站点导航中难以导航。虽然部分可以镜像您的目录结构，但不必如此。

未在您的导航配置中列出的任何页面仍将呈现并包含在已构建的站点中，但它们不会链接到全局导航并且不会包含在`previous`和`next`链中。除非直接链接到，否则这样的页面将被“隐藏”。

## 使用Markdown编写

MkDocs页面必须用[Markdown][md]撰写，这是一种轻量级标记语言，可以生成易于阅读、易于编写的纯文本文档，并以可预测的方式转换为有效的HTML文档。

MkDocs使用[Python-Markdown]库将Markdown文档呈现为HTML。Python-Markdown在几乎所有方面都与[参考实现][md]兼容，尽管存在一些微小的[differences]。

除了在所有Markdown实现中共同存在的[基本语法][syntax]之外，MkDocs还支持通过Python-Markdown [extensions]扩展Markdown语法。有关启用扩展的详细信息，请参见MkDocs的[markdown_extensions]配置设置。

MkDocs默认包含一些扩展，如下所示。

[Python-Markdown]: https://python-markdown.github.io/
[md]: https://daringfireball.net/projects/markdown/
[differences]: https://python-markdown.github.io/#differences
[syntax]: https://daringfireball.net/projects/markdown/syntax
[extensions]: https://python-markdown.github.io/extensions/
[markdown_extensions]: configuration.md#markdown_extensions

### 内部链接

MkDocs允许您使用常规Markdown[links]链接进行文档间的交互。但是，按照以下方式为MkDocs格式化这些链接将添加一些额外的优点。

[links]: https://daringfireball.net/projects/markdown/syntax#link

#### 链接到页面

在文档之间链接时，您可以简单地使用常规Markdown[linking][links]语法，包括您希望链接到的Markdown文档的*相对路径*。

```markdown
请查看 [project license](license.md) 以获取更多详情。
```

当MkDocs构建运行时，这些Markdown链接将自动转换为指向适当HTML页面的HTML超链接。

警告：
使用带有链接的绝对路径不受官方支持。相对路径由MkDocs调整，以确保它们始终相对于该页面。绝对路径根本不被修改。这意味着在本地环境中，使用绝对路径的链接可能工作得很好，但是一旦将它们部署到生产服务器上，它们可能会出现问题。

如果目标文档在另一个目录中，则需要确保在链接中包含任何相对目录路径。

```markdown
请查看 [project license](../about/license.md) 以获取更多详情。
```

[toc]扩展由MkDocs用于为Markdown文档中的每个标题生成ID。可以使用该ID通过锚链接链接到目标文档中的部分。生成的HTML将正确地转换链接路径部分，而保留锚部分不变。

```markdown
请参阅 [project license](about.md#license) 以获取更多详情。
```

请注意，ID是从标题的文本创建的。所有文本都转换为小写字母，并将任何不允许的字符（包括空格）转换为破折号。连续的破折号将然后减少为一个破折号。

toc扩展提供了一些配置设置，您可以在 `mkdocs.yml` 配置文件中设置它们以更改默认行为：

*   **`permalink`**

    在每个标题的末尾生成永久链接。默认：`False`。

    当设置为True时，使用段落符号（&para;或`&para;`）作为链接文本。当设置为字符串时，提供的字符串将用作链接文本。例如，要使用井号符号（`#`），请执行：

    ```yaml
    markdown_extensions:
      - toc:
          permalink: "#"
    ```

*   **`baselevel`**

    标题的基本级别。默认值：`1`。

    此设置允许自动调整标题级别以适应HTML模板的层次结构。例如，如果Markdown文本的页面不应包含比二级标题（`<h2>` ）更高级别的标题，那么请执行：

    ```yaml
    markdown_extensions:
      - toc:
          baselevel: 2
    ```

    然后，文档中的任何标题都将增加1。例如，标题 `# Header` 将以HTML输出中的二级标题 (`<h2>`) 渲染。

*   **`separator`**

    字词分隔符。默认值：`-`。

    生成的ID中替换空格的字符。如果您喜欢下划线，则执行：

    ```yaml
    markdown_extensions:
      - toc:
          separator: "_"
    ```

请注意，如果要定义多个以上设置，则必须将其在 `markdown_extensions` 配置选项的单个 `toc` 条目下定义。

```yml
markdown_extensions:
  - toc:
      permalink: "#"
      baselevel: 2
      separator: "_"
```

[toc]: https://python-markdown.github.io/extensions/toc/

#### 链接到图像和媒体

除了Markdown源文件之外，您还可以在文档中包含其他文件类型，这些文件在生成文档站点时会被复制。这可能包括图像和其他媒体。

例如，如果您的项目文档需要包括 [GitHub Pages CNAME file] 和PNG格式的屏幕截图，则您的文件布局可能如下所示：

```text
mkdocs.yml
docs/
    CNAME
    index.md
    about.md
    license.md
    img/
        screenshot.png
```

要在文档源文件中包含图像，请使用任何常规的Markdown图像语法：

```Markdown
Cupcake indexer是一个炫酷的用于索引小蛋糕的新项目。

![Screenshot](img/screenshot.png)

*上图：Cupcake indexer 进展中*
```

现在，当你构建文档时，你的图像将被嵌入，如果你使用Markdown编辑器来编写文档，它也会有预览效果。

[GitHub Pages CNAME file]: https://help.github.com/articles/using-a-custom-domain-with-github-pages/

#### 从原始HTML中链接

当Markdown syntax不满足作者的需求时，Markdown允许文档作者回退到原始的HTML。MkDocs在这方面不限制Markdown。但是，由于所有原始HTML都被Markdown解析器忽略，因此MkDocs无法验证或转换原始HTML中包含的链接。在原始HTML中包含内部链接时，您需要根据呈现的文档手动格式化链接。

### 元数据

MkDocs包括对YAML和MultiMarkdown样式元数据（通常称为前置元数据）的支持。元数据由在Markdown文档开头定义的一系列关键字和值组成，这些关键字和值在传递给Python-Markdown处理之前在文档中被删除。MkDocs将关键/值对传递到页面模板。因此，如果主题包括支持，则任何键的值可以在页面上显示或用于控制页面呈现。有关哪些键可能被支持（如果有）的信息，请参见主题的文档。

除了在模板中显示信息外，MkDocs还支持一些预定义的元数据键，其可以更改MkDocs的行为以支持特定页面。支持以下键：

* **`template`**

    用于当前页面的模板。

    默认情况下，MkDocs使用主题的`main.html`模板来呈现Markdown页面。您可以使用 `template` 元数据键为该特定页面定义不同的模板文件。模板文件必须在主题环境的路径中可用。

* **`title`**

    文档的“标题”。

    MkDocs会尝试以下方式确定文档的标题：

    1. 在[nav]配置设置中对于文档定义的标题。
    2. 在文档的 `title` 元数据关键字中定义的标题。
   