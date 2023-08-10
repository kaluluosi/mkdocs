# MkDocs插件

安装、使用和创建MkDocs插件的指南。

---

## 安装插件

在使用插件之前，必须先在系统上安装插件。如果您使用的是MkDocs带有的插件，则在安装MkDocs时已安装该插件。但是，要安装第三方插件，需要确定适当的包名称并使用`pip`进行安装：

```bash
pip install mkdocs-foo-plugin
```

插件成功安装后，它就可以使用了。只需要在配置文件中[启用](#使用插件)即可。[Catalog]存储库中有一个大型的插件排名列表，您可以安装并使用。## 使用插件

[`plugins`] [config]配置选项应该包含一个要在构建网站时使用的插件列表。每个“插件”都必须是分配给插件的字符串名称（请参阅给定插件的文档以确定其“名称”）。列出的插件必须已经[安装](#安装插件)。```yaml
plugins:
  - search
```

某些插件可能提供自己的配置选项。如果要设置任何配置选项，则可以嵌套一个键/值映射(`option_name: option value`)，其中包含给定插件支持的任何选项。请注意，冒号(`:`)必须跟随插件名称，然后在新行上缩进并用冒号分隔选项名称和值。如果要为单个插件定义多个选项，则每个选项都必须在单独的行上定义。```yaml
plugins:
  - search:
      lang: en
      foo: bar
```

有关给定插件可用的配置选项的信息，请参阅该插件的文档。有关默认插件的列表以及如何覆盖它们，请参阅[配置][config]文档。## 开发插件

与MkDocs一样，插件必须用Python编写。通常期望每个插件都作为单独的Python模块分发，尽管可以在同一模块中定义多个插件。至少，MkDocs插件必须包括[BasePlugin]子类和指向它的[入口点]。### BasePlugin

`mkdocs.plugins.BasePlugin`的子类应该定义插件的行为。该类通常由构建过程中特定事件的操作以及插件的配置方案组成。所有`BasePlugin`子类都包含以下属性：

#### config_scheme

配置验证实例的元组。每个项目必须由一个元组组成，其中第一个项目是配置选项的字符串名称，第二个项目是`mkdocs.config.config_options.BaseConfigOption`或其任何子类的实例。例如，以下`config_scheme`定义了三个配置选项：`foo`，它接受字符串;“bar”，它接受整数;和“baz”，它接受布尔值。```python
class MyPlugin(mkdocs.plugins.BasePlugin):
    config_scheme = (
        ('foo', mkdocs.config.config_options.Type(str, default='a default value')),
        ('bar', mkdocs.config.config_options.Type(int, default=0)),
        ('baz', mkdocs.config.config_options.Type(bool, default=True))
    )
```

> NEW：**版本1.4中新增：**
>
> ##### 子类Config以指定配置模式
>
> 为了获得类型安全性的益处，如果您只针对MkDocs 1.4+，则应将配置模式定义为类：
>
> ```python
> class MyPluginConfig(mkdocs.config.base.Config):
>     foo = mkdocs.config.config_options.Type(str, default='a default value')
>     bar = mkdocs.config.config_options.Type(int, default=0)
>     baz = mkdocs.config.config_options.Type(bool, default=True)
>
> class MyPlugin(mkdocs.plugins.BasePlugin[MyPluginConfig]):
>     ...
> ```

##### 配置定义示例

>！例子：
>
> ```python
> from mkdocs.config import base, config_options as c
>
> class _ValidationOptions(base.Config):
>     enabled = c.Type(bool, default=True)
>     verbose = c.Type(bool, default=False)
>     skip_checks = c.ListOfItems(c.Choice(('foo', 'bar', 'baz')), default=[])
>
> class MyPluginConfig(base.Config):
>     definition_file = c.File(exists=True)  # required
>     checksum_file = c.Optional(c.File(exists=True))  # can be None but must exist if specified
>     validation = c.SubConfig(_ValidationOptions)
> ```
>
> 从用户的角度来看，`SubConfig`类似于`Type(dict)`，只是它还保留了完整的验证能力：您定义了所有有效的键以及每个值应遵循的约束。>
> 而`ListOfItems`类似于`Type(list)`，但我们再次定义了每个值必须遵循的约束。>
> 这将接受以下配置：
>
> ```yaml
> my_plugin:
>   definition_file: configs/test.ini  # 相对于mkdocs.yml
>   validation:
>     enabled: !ENV [CI, false]
>     verbose: true
>     skip_checks:
>       - foo
>       - baz
> ```
<!--  -->
>？例子：
>
> ```python
> import numbers
> from mkdocs.config import base, config_options as c
>
> class _Rectangle(base.Config):
>     width = c.Type(numbers.Real)  # 必须
>     height = c.Type(numbers.Real)   # 必须
>
> class MyPluginConfig(base.Config):
>     add_rectangles = c.ListOfItems(c.SubConfig(_Rectangle))  # 必须
> ```
>
> 在此示例中，我们定义了一个复杂项列表，方法是通过将具体的`SubConfig`传递给`ListOfItems`来实现的。>
> 这将接受以下配置：
>
> ```yaml
> my_plugin:
>   add_rectangles:
>     - width: 5
>       height: 7
>     - width: 12
>       height: 2
> ```

加载用户配置时，上述方案将用于验证配置并为未提供用户的设置填充任何默认值。验证类可以是`mkdocs.config.config_options`中提供的任何类或插件中定义的第三方子类。由用户提供的任何设置都将在验证失败或未在`config_scheme`中定义的情况下引发`mkdocs.config.base.ValidationError`。#### 配置

一个字典，包含插件的配置选项，在`load_config`方法完成配置验证后会填充该属性。使用此属性访问用户提供的选项。```python
def on_pre_build(self, config, **kwargs):
    if self.config['baz']:
        # 在此实现“baz”功能...
```

> NEW：**版本1.4中新增：**
>
> ##### 安全属性访问
>
> 为了获得类型安全性的益处，如果您只针对MkDocs 1.4+，请使用属性访问访问配置选项：
>
> ```python
> def on_pre_build(self, config: MkDocsConfig, **kwargs):
>     if self.config.baz:
>         print(self.config.bar ** 2)  # OK，“int**2”有效。
> ```

所有`BasePlugin`子类都包含以下方法：

#### load_config(options)

从选项字典中加载配置。返回一个元组`(errors，warnings)`。MkDocs在配置验证期间调用此方法，插件不应需要调用它。#### on_&lt;event_name&gt;()

定义特定[事件]的行为的可选方法。插件应在这些方法中定义其行为。使用实际事件名称替换`<event_name>`。例如，`pre_build`事件将在`on_pre_build`方法中定义。大多数事件接受一个位置参数和各种关键字参数。通常，位置参数将被修改（或替换）by插件并返回。如果不返回任何内容（方法返回`None`），则使用原始的未修改对象。关键字参数仅用于提供上下文和/或提供可能用于确定应如何修改位置参数的数据。接受关键字参数作为`**kwargs`通常是良好的做法。如果在将来版本的MkDocs中向事件提供其他关键字，则无需更改插件。例如，以下事件将向主题配置中添加其他的static_template：

```python
class MyPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        config['theme'].static_templates.add('my_template.html')
        return config
```

> NEW：**版本1.4中新增：**
>
> 为了获得类型安全性的好处，如果您只针对MkDocs 1.4+，请将配置选项作为属性而不是字典中的键访问：
>
> ```python
> def on_config(self, config: MkDocsConfig, **kwargs):
>     config.theme.static_templates.add('my_template.html')
>     return config
> ```

### 事件

有三种类型的事件：[全局事件]，[页面事件]和[模板事件]。<details class ="card">
<summary>
    查看一个事件与所有插件事件之间的关系的图表
</summary>
<div class ="card-body">
    <ul>
        <li>事件本身显示为黄色，带有其参数。箭头显示每个事件的参数和输出的流。也有时省略。</li>
        <li>事件在时间轴上从上到下按时间顺序排序。</li>
        <li>虚线出现在全局事件到每个页面事件的拆分处。</li>
        <li>单击事件的标题以跳转到其描述。</li>
    </ul>
    <!-- -->
！--图：插件事件-->
</div>
</详情>
<br>

#### 一次性事件

一次性事件每次mkdocs调用时只运行一次。它们与[全局事件]的区别仅适用于`mkdocs serve`：与这些事件不同，全局事件将多次运行-每次*build*一次。##### on_startup

::: mkdocs.plugins.BasePlugin.on_startup
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_shutdown

::: mkdocs.plugins.BasePlugin.on_shutdown
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_serve

::: mkdocs.plugins.BasePlugin.on_serve
    options:
        show_root_heading: false
        show_root_toc_entry: false

#### 全局事件

全局事件在构建过程的开始或结束时每个构建仅调用一次。在这些事件中所做的任何更改都将对整个站点产生全局影响。##### on_config

::: mkdocs.plugins.BasePlugin.on_config
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_pre_build

::: mkdocs.plugins.BasePlugin.on_pre_build
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_files

::: mkdocs.plugins.BasePlugin.on_files
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_nav

::: mkdocs.plugins.BasePlugin.on_nav
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_env

::: mkdocs.plugins.BasePlugin.on_env
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_post_build

::: mkdocs.plugins.BasePlugin.on_post_build
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_build_error

::: mkdocs.plugins.BasePlugin.on_build_error
    options:
        show_root_heading: false
        show_root_toc_entry: false

#### 模板事件

模板事件为每个非页面模板调用一次。每个模板事件将为[extra_templates]配置设置中定义的每个模板以及主题中定义的任何[static_templates]都调用。所有模板事件都是在[env]事件之后和任何[页面事件]之前调用的。##### on_pre_template

::: mkdocs.plugins.BasePlugin.on_pre_template
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_template_context

::: mkdocs.plugins.BasePlugin.on_template_context
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_post_template

::: mkdocs.plugins.BasePlugin.on_post_template
    options:
        show_root_heading: false
        show_root_toc_entry: false

#### 页面事件

页面事件为包括在站点中的每个Markdown页面每次调用一次。所有页面事件都是在[post_template]事件之后和[post_build]事件之前调用的。##### on_pre_page

::: mkdocs.plugins.BasePlugin.on_pre_page
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_read_source

::: mkdocs.plugins.BasePlugin.on_page_read_source
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_markdown

::: mkdocs.plugins.BasePlugin.on_page_markdown
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_content

::: mkdocs.plugins.BasePlugin.on_page_content
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_context

::: mkdocs.plugins.BasePlugin.on_page_context
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_post_page

::: mkdocs.plugins.BasePlugin.on_post_page
    options:
        show_root_heading: false
        show_root_toc_entry: false

### 事件优先级

对于每种事件类型，插件的相应方法按照插件出现在`plugins`[config][]中的顺序进行调用。自MkDocs 1.4以来，插件可以选择为其事件设置优先值。具有更高优先级的事件将首先被调用。没有选择优先级的事件会得到默认值0。优先级相同的事件按它们在配置中出现的顺序排序。

#### ::: mkdocs.plugins.event_priority

### 处理错误

MkDocs定义了四个错误类型：

#### ::: mkdocs.exceptions.MkDocsException

#### ::: mkdocs.exceptions.ConfigurationError

#### ::: mkdocs.exceptions.BuildError

#### ::: mkdocs.exceptions.PluginError

意外和未捕获的异常将中断构建过程并生成典型的Python回溯，这对于调试代码很有用。但是，用户通常发现回溯令人不知所措，并且经常错过有用的错误消息。因此，MkDocs将捕获上述任何错误，检索错误消息并立即退出，只显示有用的消息。因此，您可能希望在插件中捕获任何异常并提出一个`PluginError`，传递自己的自定义消息，以使构建过程中断并显示有用的消息。对于任何异常，[on_build_error]事件都将被触发。例如：

```python
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin


class MyPlugin(BasePlugin):
    def on_post_page(self, output, page, config, **kwargs):
        try:
            # 抛出一个KeyError的一些代码
            ...
        except KeyError as error:
            raise PluginError(str(error))

    def on_build_error(self, error, **kwargs):
        # 一些代码清理
        ...
```

### 插件日志记录

MkDocs提供了一个`get_plugin_logger`函数，用于返回可以用于记录消息的记录器。#### ::: mkdocs.plugins.get_plugin_logger

### 入口点

插件需要打包为Python库（与MkDocs分开在PyPI上分布），并且每个插件都必须通过setuptools的`entry_points`注册为插件。将以下内容添加到您的`setup.py`脚本中：

```python
entry_points={
    'mkdocs.plugins': [
        'pluginname = path.to.some_plugin:SomePluginClass',
    ]
}
```

-“pluginname”将是用户使用的名称（在配置文件中），而“path.to.some_plugin：SomePluginClass”将是可导入的插件本身（`from path.to.some_plugin import SomePluginClass`），其中`SomePluginClass`是[BasePlugin]的子类，定义了插件行为。自然，多个Plugin类可能存在于同一模块中。只需将每个定义为单独的入口点。```python
entry_points={
    'mkdocs.plugins': [
        'featureA = path.to.my_plugins:PluginA',
        'featureB = path.to.my_plugins:PluginB'
    ]
}
```

请注意，注册插件不会激活它。用户仍然需要告诉MkDocs使用它通过配置。### 发布插件

您应该在[PyPI]上发布一个软件包，然后将其添加到[Catalog]以进行发现。强烈建议插件具有唯一的插件名称（入口点名称），以符合目录的要求。[Base