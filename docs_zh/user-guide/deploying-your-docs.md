# 部署你的文档

一份关于部署到不同托管提供者的基础指南

---

## GitHub Pages

如果你将一个项目的源代码托管在 [GitHub] 上，你可以使用 [GitHub Pages] 轻松地为你的项目提供文档托管。GitHub Pages 网站分为两种基本类型：[项目页面] 和 [用户和组织页面]。它们几乎相同，但有一些重要的区别，因此在部署时需要不同的工作流程。

### 项目页面

项目页面较为简单，因为站点文件被部署到项目存储库内的分支 (`gh-pages` 是默认值)。在你检出你维护源代码文档的 git 存储库主工作分支（通常为 `master`）之后，运行以下命令：

```sh
mkdocs gh-deploy
```

这就是全部！在幕后，MkDocs 将构建你的文档，并使用 [ghp-import] 工具将其提交到 `gh-pages` 分支并将 `gh-pages` 分支推送到 GitHub。

使用 `mkdocs gh-deploy --help` 来获取 `gh-deploy` 命令的所有可用选项的完整列表。

请注意，在将站点推送到 GitHub 之前，你将无法审核生成的站点。因此，你可能需要通过使用 `build` 或 `serve` 命令来验证所做的任何更改，并在本地审查生成的文件。

警告：
如果你使用 `gh-deploy` 命令，你不应手动编辑页面存储库中的文件，因为下一次运行该命令时会丢失你的工作。

警告：
如果在运行 `mkdocs gh-deploy` 的本地存储库中存在未跟踪的文件或未提交的工作，则这些文件将包含在所部署的页面中。

### 用户和组织页面

用户和组织网站并不绑定到特定的项目，站点文件将部署到名为 GitHub 帐户名称的专用存储库中的 `master` 分支。因此，你需要在本地系统上拥有两个存储库的工作副本。例如，考虑以下文件结构：

```text
my-project/
    mkdocs.yml
    docs/
orgname.github.io/
```

在更新项目并验证之后，你需要更改目录到 `orgname.github.io` 存储库，并从 there 调用 `mkdocs gh-deploy` 命令：

```sh
cd ../orgname.github.io/
mkdocs gh-deploy --config-file ../my-project/mkdocs.yml --remote-branch master
```

请注意，你需要显式指向 `mkdocs.yml` 配置文件的位置，因为它不再位于当前工作目录中。你还需要告知部署脚本提交到 `master` 分支。你可以使用 [remote_branch] 配置设置覆盖默认配置，但是如果在运行部署脚本之前忘记更改目录，则会将其提交到项目的 `master` 分支，你可能不希望这样。

### 自定义域

GitHub Pages 包括支持使用 [自定义域] 的站点。除了 GitHub 提供的步骤之外，你还需要执行一个附加步骤以使 MkDocs 在自定义域上运行。你需要在 [docs_dir] 的根目录下添加一个 `CNAME` 文件。该文件必须包含单个裸域名或子域名（请参阅 MkDocs 的 [CNAME 文件] 作为示例）。你可以手动创建该文件，也可以使用 GitHub 的 Web 界面设置自定义域（在“Settings / Custom Domain”下）。如果使用 Web 界面，则 GitHub 将为您创建 `CNAME` 文件并将其保存到“pages”分支的根目录中。为了避免下次部署时删除该文件，你需要将文件复制到你的 `docs_dir`。正确包含在 `docs_dir` 中的文件，MkDocs 将在每次运行 `gh-deploy` 命令时将该文件包含在生成的站点中，并将其推送到你的“pages”分支。

如果你在使用自定义域时遇到问题，请参阅 GitHub 关于[自定义域故障排除]的文档。

[GitHub]: https://github.com/
[GitHub Pages]: https://pages.github.com/
[项目页面]: https://help.github.com/articles/user-organization-and-project-pages/#project-pages-sites
[用户和组织页面]: https://help.github.com/articles/user-organization-and-project-pages/#user-and-organization-pages-sites
[ghp-import]: https://github.com/davisp/ghp-import
[remote_branch]: ./configuration.md#remote_branch
[自定义域]: https://help.github.com/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site
[docs_dir]: ./configuration.md#docs_dir
[CNAME 文件]: https://github.com/mkdocs/mkdocs/blob/master/docs/CNAME
[自定义域故障排除]: https://help.github.com/articles/troubleshooting-custom-domains/

## Read the Docs

[Read the Docs][rtd] 提供免费的文档托管。您可以使用任何主要版本控制系统导入文档，包括 Mercurial、Git、Subversion 和 Bazaar。Read the Docs 对 MkDocs 支持的非常好。请按照他们网站上的[说明]适当地排列仓库中的文件，创建一个帐户并指向你的公共托管存储库。如果配置正确，每次将提交推送到公共存储库时，你的文档将更新。

注意：
为了从 [Read the Docs] [提供的所有功能]中受益，你需要使用 [Read the Docs 主题]，这是 MkDocs 自带的。可以在 Read the Docs 文档中引用的各种主题是 Sphinx 专用的主题，无法与 MkDocs 一起使用。

[rtd]: https://readthedocs.org/
[说明]: https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html
[提供的所有功能]: https://docs.readthedocs.io/en/latest/features.html
[Read the Docs 主题]: ./choosing-your-theme.md#readthedocs

## 其他提供者

使用 MkDocs 生成的文档可以部署到任何可以提供静态文件的托管提供商上。虽然不可能记录如何上传文档到每个托管提供商，但以下准则应该提供一些一般性的帮助。

当你构建你的站点（使用 `mkdocs build` 命令）时，所有的文件都会被写入到 [site_dir] 配置选项所分配的目录中（默认值为 `"site"`）的 `mkdocs.yaml` 配置文件中。通常，你只需要将该目录的内容复制到托管提供商服务器的根目录。根据你的托管提供者的设置，你可能需要使用图形化或命令行 [ftp]、[ssh] 或 [scp] 客户端传输文件。

例如，从命令行的典型命令可能如下所示：

```sh
mkdocs build
scp -r ./site user@host:/path/to/server/root
```

当然，你需要使用你的托管提供者的用户名替换 `user`，并使用适当的域名替换 `host`。此外，你需要调整 `/path/to/server/root`，以使其与你主机的文件系统配置相匹配。

参见你的主机文档以获取具体信息。你可能需要搜索他们的文档以获取“FTP”或“上传站点”的信息。

## 本地文件

与其在服务器上托管文档，你可以直接分发文件，用户可以使用 `file://` 方案在浏览器中查看文件。

请注意，由于所有现代浏览器的安全设置，某些事情的功能与常规情况下不同，有些功能可能根本不工作。事实上，一些设置需要以非常特定的方式进行自定义。

- [site_url]：

​     `site_url` 必须设置为空字符串，这指示 MkDocs 建立您的网站，以便它可以与 `file://` 方案一起使用。

```yaml
    site_url: ""
```

-   [use_directory_urls]:

​		设置 `use_directory_urls` 为 `false`。否则，页面之间的内部链接将无法正常工作。

```yaml
    use_directory_urls: false
```

-   [search]:

​		你将需要禁用搜索插件，或使用专门设计为与 `file://` 方案一起使用的第三方搜索插件。要禁用所有插件，请将 `plugins` 设置为空列表。

```yaml
    plugins: []
```

​		如果启用了其他插件，请确保不包含“search”。

在编写文档时，使用相对 URL 来引用所有内部链接是至关重要的，如 [文档] [内部链接] 所述。请记住，每个读者的文档将使用不同的设备，并且文档文件很可能位于该设备上的不同位置。

如果你希望你的文档在离线情况下查看，则还需要谨慎选择主题。许多主题使用 CDNs 作为各种支持文件，这需要使用现场互联网连接。你需要选择一个主题，其中所有支持文件都直接包含在主题中。

当你构建你的路线（使用 `mkdocs build` 命令）时，所有的文件都会被写入到 [site_dir] 配置选项所分配的目录中（默认值为 `"site"`）的 `mkdocs.yaml` 配置文件中。通常，你只需要将该目录的内容复制并分发到你的读者。或者，你可以选择使用第三方工具将 HTML 文件转换为其他文档格式。

## 404 页面

当 MkDocs 构建文档时，它将在 [build directory][site_dir] 中包括一个 404.html 文件。在 [GitHub]（#github-pages）上部署时，将自动使用此文件，但仅在自定义域上。其他 Web 服务器则可以配置使用它，但不一定每个服务器都支持该功能。有关详细信息，请参阅你选择的服务器的文档。

[site_dir]: ./configuration.md#site_dir
[site_url]: ./configuration.md#site_url
[use_directory_urls]: ./configuration.md#use_directory_urls
[search]: ./configuration.md#search
[文档]: ./writing-your-docs.md#internal-links
[内部链接]: ./writing-your-docs.md#internal-links
