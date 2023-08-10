# 部署你的文档

部署到各种托管提供商的基本指南

---

## GitHub Pages

如果您在 [GitHub] 上托管项目的源代码，您可以轻松使用 [GitHub Pages] 托管项目的文档。有两种基本类型的 GitHub Pages 网站：[项目 Pages] 网站和 [用户和组织 Pages] 网站。它们几乎相同但有一些重要的区别，因此在部署时需要不同的工作流。

### 项目 Pages

项目 Pages 网站比较简单，因为站点文件被部署到项目存储库中的一个分支 (`gh-pages`，默认为分支)。在您检出您维护项目源文档的 git 存储库的主要工作分支(通常是 `master`)之后，运行以下命令：

```sh
mkdocs gh-deploy
```

就这样！在幕后，MkDocs 会构建文档并使用 [ghp-import] 工具将它们提交到 `gh-pages` 分支并将 `gh-pages` 分支推送到 GitHub。使用 `mkdocs gh-deploy --help` 以获取 `gh-deploy` 命令可用选项的完整列表。请注意，您将无法在将站点推送到 GitHub 之前查看构建的站点。因此，您可能需要使用 `build` 或 `serve` 命令验证您对文档所做的任何更改，并在本地审查构建的文件。

警告：如果您使用 `gh-deploy` 命令，永远不要手动编辑页面仓库中的文件，因为下次运行命令时将丢失您的工作。

警告：如果本地存储库中有未跟踪的文件或未提交的工作正在运行 `mkdocs gh-deploy` 命令，这些文件将被包含在部署的页面中。

### 用户和组织 Pages

用户和组织 Pages 网站与特定项目无关，站点文件部署到以 GitHub 帐户名命名的专用存储库的 `master` 分支中。因此，您需要在本地系统上工作副本的两个存储库。例如，考虑以下文件结构：

```text
my-project/
    mkdocs.yml
    docs/
orgname.github.io/
```

在更新项目并验证其后，您需要更改目录到 `orgname.github.io` 存储库并从那里调用 `mkdocs gh-deploy` 命令：

```sh
cd ../orgname.github.io/
mkdocs gh-deploy --config-file ../my-project/mkdocs.yml --remote-branch master
```

请注意，由于 `config-file` 不再位于当前工作目录中，因此您需要显式指向 `mkdocs.yml` 配置文件。您还需要通知部署脚本提交到 `master` 分支。您可以使用 [remote_branch] 配置设置覆盖默认设置，但是如果在运行部署脚本之前忘记更改目录，则它将提交到您的项目的 `master` 分支，这可能不是您想要的。

### 自定义域

GitHub Pages 包括支持使用[自定义域名]的功能，您需要执行一个附加步骤，以便 MkDocs 能够与您的自定义域名一起使用。您需要将 `CNAME` 文件添加到您的[docs_dir]。该文件必须包含单独的域名或子域名（请参见 MkDocs 自己的 [CNAME 文件] 作为示例）。您可以手动创建该文件，也可以使用 GitHub 的 Web 界面设置自定义域名（在 Settings / Custom Domain 下）。如果使用 Web 界面，则 GitHub 将会为您创建 `CNAME` 文件，并将其保存到 "pages" 分支的根目录下。为了使该文件不会被下一次部署的时候删除，您需要将该文件复制到您的 `docs_dir`。将文件正确包含在 `docs_dir` 中后，MkDocs 会将该文件包括在构建的站点中，并在每次运行 `gh-deploy` 命令时将其推送到您的 "pages" 分支。如果在获取自定义域名的使用方面遇到问题，请参阅 GitHub 的文档，了解[自定义域名的故障排除]。

[GitHub]: https://github.com/
[GitHub Pages]: https://pages.github.com/
[Project Pages]: https://help.github.com/articles/user-organization-and-project-pages/#project-pages-sites
[User and Organization Pages]: https://help.github.com/articles/user-organization-and-project-pages/#user-and-organization-pages-sites
[ghp-import]: https://github.com/davisp/ghp-import
[remote_branch]:./configuration.md#remote_branch
[自定义域名]: https://help.github.com/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site
[docs_dir]:./configuration.md#docs_dir
[CNAME 文件]: https://github.com/mkdocs/mkdocs/blob/master/docs/CNAME
[自定义域名的故障排除]: https://help.github.com/articles/troubleshooting-custom-domains/

## Read the Docs

[Read the Docs][rtd] 提供免费的文档托管。您可以使用任何主要版本控制系统（包括 Mercurial、Git、Subversion 和 Bazaar）导入您的文档。Read the Docs 支持 MkDocs。按照其网站上的 [说明] 排列好存储库中的文件，创建一个帐户，并将其指向您的公共托管存储库。如果正确配置，每次您将提交推送到您的公共存储库时，您的文档都将更新。

注意: 要享受 Read the Docs 提供的所有 [功能]，您需要使用随 MkDocs 一起提供的 [Read the Docs 主题] 。在 Read the Docs 文档中提到的各种主题是 Sphinx 特定主题，无法与 MkDocs 兼容。

[rtd]: https://readthedocs.org/
[说明]: https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html
[功能]: https://docs.readthedocs.io/en/latest/features.html
[Read the Docs 主题]: ./choosing-your-theme.md#readthedocs

## 其他托管提供

任何能够提供静态文件的托管提供商都可以用于提供由 MkDocs 生成的文档。虽然不可能记录如何上传每个托管提供商的文档，但以下指南应提供一些一般性的协助。

当您构建站点时（使用 `mkdocs build` 命令），所有的文件都被写入分配给 [site_dir] 配置选项（默认为 `"site"`）的目录中。通常，您只需要将该目录的内容复制到您的托管提供程序服务器的根目录中。根据您的托管提供商的设置，您可能需要使用图形或命令行 [ftp]、[ssh] 或 [scp] 客户端来传输文件。

例如，从命令行运行的一组典型命令可能如下所示：

```sh
mkdocs build
scp -r ./site user@host:/path/to/server/root
```

当然，您需要用您与托管提供商的用户名替换 `user`, 使用相应的域名替换 `host`。此外，您需要将 `/path/to/server/root` 手动调整为您托管提供商文件系统的配置。

请参阅您托管提供商的文档以了解详细信息。您可能需要搜索其文档以查找 "ftp" 或 "上传站点" 等内容。

## 本地文件

与其在服务器上托管您的文档，您可能希望直接分发这些文件，然后可以使用 `file://` 分别在浏览器中查看这些文件。请注意，由于所有现代浏览器的安全设置，某些问题会导致功能无法正常工作以及未完全支持一些功能。实际上，需定制一些非常特定的设置。

- [site_url]：

   `site_url` 必须设置为空字符串，这将指示 MkDocs 构建您的站点，以便可以使用 `file://` 方案。```yaml
    site_url: ""
    ```

- [use_directory_urls]：

    设置 `use_directory_urls` 为`false`。否则，页面之间的内部链接将无法正常工作。```yaml
    use_directory_urls: false
    ```

- [search]：

    您将需要禁用搜索插件或使用专为 `file://` 方案设计的第三方搜索插件。要禁用所有插件，请将 `plugins` 设置为空列表。```yaml
    plugins: []
    ```
    如果您启用了其他插件，请确保不包含 `search`。在编写文档时，所有内部链接必须使用相对 URL（如[内部链接][internal links]中所述）。请记住，您的文档读者将使用不同的设备，文件可能位于该设备的不同位置。如果希望在离线情况下查看文档，则还需要注意选择哪些主题。许多主题使用 CDN 来支持各种支持文件，这需要一个实时的互联网连接。您需要选择包括所有支持文件在主题中的主题。


构建站点时（使用 `mkdocs build` 命令），所有的文件都被写入分配给 [site_dir] 配置选项（默认为 `"site"`）的目录中。通常，您只需要将该目录的内容复制并分发给读者。

另外，您还可以选择使用第三方工具将HTML文件转换为其他文档格式。

## 404 页面

当 MkDocs 构建文档时，它将在 [build 目录][site_dir] 中包括一个 404.html 文件。此文件将在部署到 [GitHub][#github-pages] 上自定义域名时自动使用。其他 Web 服务器可能已配置使用它，但该功能并不会总是可用。有关更多信息，请参阅您选择的服务器的文档。

[site_dir]:./configuration.md#site_dir
[site_url]:./configuration.md#site_url
[use_directory_urls]:./configuration.md#use_directory_urls
[search]:./configuration.md#search
[internal links]:./writing-your-docs.md#internal-links