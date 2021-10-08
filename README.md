# djangoshortcuts

提供一个全局命令，用于方便快捷生成模板等相关文件。  

## 安装
```
python setup.py install
```

## 使用方式

在安装成功之后，获得一个全局命令：dj，通过 dj -h 可以查看到该命令的使用方式  
```
$dj -h
usage: dj [-h] --app APP [-a ADD] [-t TEMPLATE] [-s STATIC]

Easily to create files when using django

optional arguments:
  -h, --help            show this help message and exit
  --app APP             input the app name which django created
  -a, --add ADD         add file automatically, the value must be one of
                        ['forms', 'urls']
  -t, --template TEMPLATE
                        add templates html files
  -s, --static STATIC   add static files

You must cd BASE_DIR to run this script
```

## 全局命令备忘查询

有时候忘记安装这些模块都提供了哪些全局命令，可以通过以下这种方式查询。  
```
$python -m djangoshortcuts -h
Please use command [dj -h] for the detail.
```

## 举例说明

下面简要举例说明这个命令的使用方式，其实看上面的 usage 就可以明白九成以上了。  

假设 django app 名称为 polls， 首先需要切换到网站的根目录下，就可以运行以下命令   

1.生成 forms.py 或者 urls.py 文件
```
dj --app polls -a forms
dj --app polls -a urls
```

2.生成 index.html 文件
```
dj --app polls -t index.html
```
该命令会自动创建 polls/templates/polls 相关的文件夹，并生成 polls/templates/polls/index.html 文件  

3.生成 style.css 文件  
```
dj --app polls -s style.css
```
该命令会自动创建 polls/static/polls 相关的文件夹，并生成 polls/static/polls/style.css 文件 

4.考虑到静态文件夹下常增加 css 和 js 文件夹来管理相关静态文件，所以在 -s 参数的行动逻辑多增加一个功能
4.1
```
dj --app polls -s css/style.css
```
该命令和 3 的区别在于，文件的路径为 polls/static/polls/css/style.css，相关的文件夹会自动创建  
4.2
```
dj --app polls -s js/login.js
```
和 4.1 类似，文件的路径为 polls/static/polls/js/login.js  

## 后记
以上参数中，--app 是必选参数，除此之外的参数都是可选参数并且不互斥。也就是说添加文件的时候，不同的参数可以同时进行。
