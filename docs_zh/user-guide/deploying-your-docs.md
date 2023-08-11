# 部署文档

部署文档到各种托管提供商的基本指南

---

## GitHub Pages

如果你将项目的源代码托管在[GitHub]，你可以轻松利用[GitHub Pages]托管你项目的文档。GitHub Pages有两种基本的站点类型：[项目页面][Project Pages]站点和[用户和机构页面][User and Organization Pages]站点。它们几乎相同，但有一些重要的区别，需要在部署时采用不同的工作流程。

### 项目页面

项目页面站点更简单，因为站点文件部署到项目存储库的分支中（默认为“gh-pages”）。在你`checkout`该项目维护源文档的git存储库的主要工作分支（通常是`master`）之后，运行以下命令：

```sh
mkdocs gh-deploy
```

就这样！在幕后，MkDocs将构建你的文档并使用[ghp-import]工具将它们提交到`gh-pages`分支并将`gh-pages`分支推送到GitHub。

使用`mkdocs gh-deploy --help`获得`gh-deploy`命令可用选项的完整列表。

请注意，在将站点推送到GitHub之前，您将无法审核构建的站点。因此，在使用`build`或`serve`命令构建文件并在本地查看构建文件之前，您可能需要先验证对文档所做的任何更改。

警告：
如果使用`gh-deploy`命令，你不应该手动在你的页面存储库中编辑文件，否则下一次运行该命令时，你将丢失你的工作。

警告：
如果在运行`mkdocs gh-deploy`的本地存储库中有未跟踪的文件或未提交的工作，则这些文件将包括在部署的页面中。

### 机构和用户页面

用户和机构页面站点不与特定项目绑定，站点文件部署到名为GitHub帐户名的专用存储库的`master`分支中。因此，你需要在本地系统上有两个存储库副本。例如，考虑以下文件结构:

```text
my-project/
    mkdocs.yml
    docs/
orgname.github.io/
```

在对项目进行更新并验证后，你需要更改目录到`orgname.github.io`存储库并从那里调用`mkdocs gh-deploy`命令：

```sh
cd ../orgname.github.io/
mkdocs gh-deploy --config-file ../my-project/mkdocs.yml --remote-branch master
```

请注意，由于配置文件不再在当前工作目录中，因此需要显式指定`mkdocs.yml`配置文件的位置。你也需要通知部署脚本提交到`master`分支。你可以使用[remote_branch]配置设置覆盖默认设置，但是如果忘记在运行部署脚本之前更改目录，它将提交到您的项目的“master”分支，这可能不是你想要的。

### 自定义域名

GitHub Pages支持使用[Custom Domain]作为你的站点。除了GitHub记录的步骤外，你需要执行额外的一步，以使MkDocs可以与你的自定义域名一起使用。你需要在[docs_dir]的根目录下添加一个`CNAME`文件。该文件必须包含单个裸域或子域位于单个行上（以MkDocs自己的[CNAME file]为例）。你可以手动创建文件，也可以使用GitHub的Web接口设置自定义域名（在设置/自定义域中）。如果使用Web接口，GitHub将为你创建`CNAME`文件并将其保存到“pages”分支的根目录中。为了不在下一次部署时将文件删除，你需要将文件复制到你的`docs_dir`下。如果正确包含文件到你的`docs_dir`中，MkDocs将在每次运行`gh-deploy`命令时将文件包含在你的构建站点中并将其推送到你的“pages”分支。

如果你在使用自定义域名时遇到问题，请参阅GitHub的[自定义域名故障排除]文档。

[GitHub]：https://github.com/
[GitHub Pages]：https://pages.github.com/
[Project Pages]：https://help.github.com/articles/user-organization-and-project-pages/#project-pages-sites
[User and Organization Pages]：https://help.github.com/articles/user-organization-and-project-pages/#user-and-organization-pages-sites
[ghp-import]：https://github.com/davisp/ghp-import
[remote_branch]：./configuration.md#remote_branch
[Custom Domain]：https://help.github.com/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site
[docs_dir]：./configuration.md#docs_dir
[CNAME file]：https://github.com/mkdocs/mkdocs/blob/master/docs/CNAME
[自定义域名故障排除]：https://help.github.com/articles/troubleshooting-custom-domains/

## Read the Docs

[Read the Docs][rtd]提供免费的文档托管服务。你可以使用任何主流版本控制系统，包括Mercurial、Git、Subversion和Bazaar导入你的文档。Read the Docs支持MkDocs。按照他们网站上的[说明]正确安排您的文件，然后创建一个帐户并将其指向在公共存储库上托管的文件。如果正确配置，则每当您将提交推送到公共存储库时，您文档都会更新。

注意：
为了使Read the Docs提供的[功能]全部生效，你需要使用MkDocs附带的[Read the Docs主题][theme]。在Read the Docs文档中可能会引用到的各种主题都是Sphinx特定的主题，不能与MkDocs一起使用。

[rtd]：https://readthedocs.org/
[说明]：https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html
[功能]：https://docs.readthedocs.io/en/latest/features.html
[theme]：./choosing-your-theme.md#readthedocs

## 其他提供商

任何可以提供静态文件服务的托管提供商都可以用于托管由MkDocs生成的文档。虽然不可能记录如何将文档上传到每个托管提供商，但以下准则应该提供一些一般性援助。

当你构建站点（使用`mkdocs build`命令）时，所有文件都被写入了[site_dir]配置选项（默认为“site”）指定的目录中。通常，你只需要将该目录的内容复制到托管提供商服务器的根目录中。根据你的托管提供商设置，你可能需要使用图形化或命令行[ftp]、[ssh]或[scp]客户端传输文件。

例如，从命令行传输文件的典型命令可能如下所示：

```sh
mkdocs build
scp -r ./site user@host:/path/to/server/root
```

当然，你需要用你在托管提供商处使用的用户名替换`user`，并用相应的域名替换`host`。此外，你需要根据你的主机文件系统的配置调整`/path/to/server/root`。

具体规定请见你的主机供应商文档。你可能需要搜索它们的文档以获得“ftp”或“上传站点”的相关说明。

## 本地文件

你可以直接分发文件而不是将文档托管在服务器上，文件可以使用`file://`方案在浏览器中查看。

请注意，由于所有现代浏览器的安全设置，某些事物将不能正常工作，有些功能根本不能正常工作。实际上，一些设置需要以非常特定的方式进行自定义。

- [site_url]:

    `site_url`必须设置为空字符串，这将使MkDocs构建您的站点，以便可以使用`file://`方案。

    ```yaml
    site_url: ""
    ```

- [use_directory_urls]:

    将`use_directory_urls`设置为`false`。否则，页面之间的内部链接将无法正常工作。

    ```yaml
    use_directory_urls: false
    ```

- [search]:

    你需要禁用搜索插件或使用专为使用`file://`方案而设计的第三方搜索插件。要禁用所有插件，请将“插件”设置为空列表。

    ```yaml
    plugins: []
    ```

    如果你启用了其他插件，只需确保`search`未包含在列表中即可。

当编写文档时，所有内部链接必须使用相对URL，如[文档][internal links]所述。请记住，每个读者都会使用不同的设备，文件在该设备上的位置也可能不同。

如果预计你的文档将在离线环境下查看，则你还需要谨慎选择主题。许多主题使用CDN来获取各种支持文件，这需要一个活动的互联网连接。你需要选择一个主题，其中所有支持文件都直接包含在主题中。

当你构建站点（使用`mkdocs build`命令）时，所有文件都被写入了[site_dir]配置选项（默认为“site”）指定的目录中。通常，你只需要复制该目录的内容并将其分发给你的读者。或者，你可以选择使用第三方工具将HTML文件转换为其他文档格式。

## 404 页面

当MkDocs构建文档时，将在[build directory][site_dir]中包括一个404.html文件。这个文件将在[GitHub](#github-pages)上自动使用，但仅在自定义域名上使用。其他Web服务器可能配置了使用它，但不一定具有该功能。有关更多信息，请参见所选服务器的文档。

[site_dir]：./configuration.md#site_dir
[site_url]：./configuration.md#site_url
[use_directory_urls]：./configuration.md#use_directory_urls
[search]：./configuration.md#search
[internal links]：./writing-your-docs.md#internal-links