# 开始使用 MkDocs

一个入门级教程！

## 安装

在命令行中运行以下命令安装 MkDocs：

```bash
pip install mkdocs
```

更多详情请参考[安装指南](user-guide/installation.md)。

## 创建一个新项目

创建一个新项目超级简单。可以在命令行中运行以下命令：

```bash
mkdocs new my-project
cd my-project
```

浏览你所创建的初始项目。![初始 MkDocs 布局](img/initial-layout.png)

有一个名为`mkdocs.yml`的配置文件以及一个名为`docs`的文件夹，该文件夹将包含文档源文件(`docs`是 [docs_dir] 配置设置的默认值)。现在，`docs`文件夹只包含一个名为 `index.md` 的文档页面。MkDocs 附带了一个内置的 dev-server，让您在工作时预览文档。确保在与 `mkdocs.yml` 配置文件相同的目录中，并运行 `mkdocs serve` 命令来启动服务器：

```console
$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.22 seconds
INFO    -  [15:50:43] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [15:50:43] Serving on http://127.0.0.1:8000/
```

在浏览器中打开<http://127.0.0.1:8000/>，您将看到默认的主页面显示：

![MkDocs live 服务器](img/screenshot.png)

dev-server 还支持自动重载，并将在配置文件、文档目录或主题目录中发生任何更改时重建文档。在您选择的文本编辑器中打开 `docs/index.md` 文档，将初始标题更改为“MkLorum”并保存更改。浏览器将自动重新加载，您应该立即看到已更新的文档。现在尝试编辑配置文件：`mkdocs.yml` 将 [`site_name`][site_name] 设置更改为 `MkLorum` 并保存文件。

```yaml
site_name: MkLorum
site_url: https://example.com/
```

你的浏览器应该会立即重新加载，你会看到你的新的网站名起作用。![site_name 设置](img/site-name.png)

提示：

[`site_name`][site_name] 和 [`site_url`][site_url] 配置选项是配置文件中唯一必需的选项。 当您创建新项目时，`site_url` 选项被分配为占位符值：`https://example.com`。 如果已知最终位置，则现在可以更改设置以指向它。或者您可以选择暂时不要更改它。只需确保在将您的站点部署到生产服务器之前编辑它。

## 添加页面

现在将第二个页面添加到您的文档：

```bash
curl 'https://jaspervdj.be/lorem-markdownum/markdown.txt' > docs/about.md
```

由于我们的文档站点将包括一些导航标题，因此您可能希望编辑配置文件并添加有关导航标头中每个页面的顺序、标题和嵌套的一些信息。例如，添加一个 [`nav`][nav] 设置：

```yaml
site_name: MkLorum
site_url: https://example.com/
nav:
  - Home: index.md
  - About: about.md
```

保存更改，您现在将在左侧看到具有 “主页” 和 “关于”的导航栏项以及右侧的“搜索”、“上一篇”和“下一篇”。![屏幕截图](img/multipage.png)

尝试菜单项并在页面之间来回导航。然后点击“搜索”。一个搜索对话框将出现，允许您搜索任何页面上的任何文本。请注意，搜索结果包括站点上搜索词的每个出现并直接链接到搜索词出现的页面部分。您可以在不花费任何精力或配置的情况下获得所有这些功能。![屏幕截图](img/search.png)

## 主题化我们的文档

现在，通过更改主题，更改配置文件以更改文档的显示方式。编辑 `mkdocs.yml` 文件并添加一个 [`theme`][theme] 设置：

```yaml
site_name: MkLorum
site_url: https://example.com/
nav:
  - Home: index.md
  - About: about.md
theme: readthedocs
```

保存更改，您将看到使用 ReadTheDocs 主题。![屏幕截图](img/readthedocs.png)

## 更改 Favicon 图标

默认情况下，MkDocs 使用 [MkDocs Favicon] 图标。要使用不同的图标，请在 `docs` 目录中创建一个 `img` 子目录，并将自定义的 `favicon.ico` 文件复制到该目录中。MkDocs 将自动检测并使用该文件作为您的 Favicon 图标。[MkDocs Favicon]: img/favicon.ico

## 构建站点

现在看起来很好。你可以部署 `MkLorum` 文档的第一遍了。首先构建文档：

```bash
mkdocs build
```

这将创建一个名为 `site` 的新目录。查看目录：

```console
$ ls site
about  fonts  index.html  license  search.html
css    img    js          mkdocs   sitemap.xml
```

请注意，您的源文档已输出为两个名为 `index.html` 和 `about/index.html` 的 HTML 文件。您还有各种其他媒体作为文档主题的一部分复制到了 `site` 目录。您甚至有一个 `sitemap.xml` 文件和 `mkdocs/search_index.json`。如果使用源代码控制，如 `git`，则可能不希望将文档构建检入存储库。向您的 `.gitignore` 文件添加包含 `site/` 的行。

```bash
echo "site/" >> .gitignore
```

如果您使用另一个源代码控制工具，您将需要检查其文档，以了解如何忽略特定目录。

## 其他命令和选项

有各种其他命令和选项可用。要查看完整的命令列表，请使用 `--help` 标志：

```bash
mkdocs --help
```

要查看给定命令上可用的选项列表，请使用该命令的 `--help` 标志。例如，要获取在我们运行以下命令列出的“build”命令上可用的所有选项的列表：

```bash
mkdocs build --help
```

## 部署

你刚刚构建的文档网站只使用静态文件，所以你可以在几乎任何地方托管它。只需上传整个 `site` 目录的内容到您托管网站的任何位置，完成。有关一些常见主机的具体说明，请参阅 [部署您的文档][deploy] 页面。

## 获取帮助

请参考[用户指南][User Guide]以获取MkDocs所有功能的更完整的文档。如果需要MkDocs的帮助，请使用 [GitHub讨论][GitHub Discussions] 或[GitHub问题][GitHub Issues]。

[docs_dir]: user-guide/configuration.md#docs_dir
[nav]: user-guide/configuration.md#nav
[site_name]: user-guide/configuration.md#site_name
[site_url]: user-guide/configuration.md#site_url
[theme]: user-guide/configuration.md#theme
[deploy]: user-guide/deploying-your-docs.md
[MkDocs Favicon]: img/favicon.ico
[User Guide]: user-guide/README.md
[GitHub Discussions]: https://github.com/mkdocs/mkdocs/discussions
[GitHub Issues]: https://github.com/mkdocs/mkdocs/issues