# common

```PowerShell
│  locale/                  # 语言本地化文件夹
│  management/              # 管理文件夹
│  middleware/              # 中间件
│  migrations/              # 数据迁移文件夹
│  templatetages/           # 配置Django前端模板的标签（？）
│  tests/                   # 测试文件夹
│  admin.py                 # django.contrib.admin.ModelAdmin，配置需要在django后台显示的model
│  api_views.py             # API
│  apps.py                  # 组合本目录下的所有类和代码
│  classes.py               # 基本类，主要有`class Collection`、`class Dashboard`
│  compat.py                # Python2/3兼容代码
│  compressed_files.py      # 压缩文件
│  dashboards.py            # 主页
│  exceptions.py            # 异常类
│  forms.py                 # 前端表单
│  generics.py              # 组合forms、mixins和settings，形成前端view（？）
│  handlers.py              # 处理函数
│  licenses.py              # 许可证
│  links.py                 # 前端链接
│  literals.py              # 存放不会变的字面量
│  managers.py              # django.db.models.Manager
│  menus.py                 # 前端菜单
│  mixins.py                # 混入类
│  models.py                # 数据模型
│  permissions_runtime.py
│  queues.py                # 有关Celery的任务队列
│  runtime.py
│  serializers.py           # model序列化为REST（？）
│  settings.py              # 配置
│  signals.py               # 信号
│  tasks.py                 # 有关Celery的任务
│  urls.py                  # 前端URL
│  utils.py                 # 辅助函数
│  validators.py            # 各种验证规则
│  views.py                 # 前端视图
│  widgets.py               # 前端页面的组件
└─ __init__.py
```
