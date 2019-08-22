# Python

## Tools

### [VScode](https://code.visualstudio.com/) for [python](https://code.visualstudio.com/docs/languages/python)

#### 安装`Python`插件

1. 打开`VScode`，`Ctrl+p`
2. 输入`ext install python`
3. 选择下载量最高的那个插件点击安装

默认按`F5`后需要再按一次F5程序才会运行，如果要按`F5`马上运行需要将`launch.json`文件的`"stopOnEntry": true`,改为`"stopOnEntry": false`。

插件`vscode-icons`可以使`VScode左侧`的资源管理器根据文件类型显示图标

#### 配置flake8

安装`flake8`之后写代码的时候编辑器就会提示哪里出错，代码格式不规范也会提示

1. 打开`命令行`
2. 输入 `"pip install flake8"`
3. 安装`flake8`成功后，打开`VScode`，`文件->首选项->用户设置`，在`settings.json`文件中输入`"python.linting.flake8Enabled": true`

#### 配置yapf

安装`yapf`之后在`VScode`中按`Alt+Shift+F`即可自动格式化代码

1. 打开`命令行`
2. 输入 `"pip install yapf"`
3. 安装`yapf`成功后，打开`VScode`，`文件->首选项->用户设置`，在`settings.json`文件中输入`"python.formatting.provider": "yapf"`
