# maomaoyu-starter

一个最小可用、结构规范的 Python 项目骨架。开箱即用，无运行时第三方依赖。

## 特性

- **标准 src 布局**：源码放在 `src/` 下，避免导入路径踩坑
- **零依赖**：核心代码只用标准库，克隆下来就能跑
- **自带测试**：`unittest` 编写，无需安装 pytest 也能执行
- **类型标注**：全量 type hints，附 `py.typed` 标记（PEP 561）
- **开箱即用的工具配置**：`ruff`（格式化 + lint）、`mypy`（严格类型检查）、`pytest`
- **CI 就绪**：GitHub Actions 工作流已配好，push 即跑多版本测试

## 目录结构

```
maomaoyu-starter/
├── .github/workflows/ci.yml   # GitHub Actions 持续集成
├── src/
│   └── maomaoyu_starter/
│       ├── __init__.py        # 包入口，暴露 greet()
│       ├── __main__.py        # python -m maomaoyu_starter
│       ├── cli.py             # 命令行参数解析
│       └── py.typed           # PEP 561 类型标记
├── tests/
│   └── test_greet.py          # 单元测试
├── .editorconfig              # 跨编辑器风格统一
├── .gitignore                 # Python 项目标准忽略规则
├── LICENSE                    # MIT
├── README.md
└── pyproject.toml             # 打包与工具配置
```

## 快速开始

需要 **Python 3.10+**。

```bash
# 1. 创建虚拟环境
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# 2. 以可编辑模式安装（会生成 maomaoyu 命令）
pip install -e .

# 3. 跑起来
maomaoyu
# Hello, World!
maomaoyu maomaoyu
# Hello, maomaoyu!
```

不想安装也行，直接用源码路径运行：

```bash
set PYTHONPATH=src          # Windows
export PYTHONPATH=src       # macOS / Linux
python -m maomaoyu_starter 大鱼
```

## 运行测试

```bash
python -m unittest discover -s tests -v
```

装了 pytest 的话也可以：

```bash
pip install pytest
pytest
```

## 代码质量

```bash
pip install ruff mypy

ruff check .        # lint
ruff format .       # 格式化
mypy                # 严格类型检查
```

## 作为库使用

```python
from maomaoyu_starter import greet

greet()  # 'Hello, World!'
greet("大肥鱼")  # 'Hello, 大肥鱼!'
```

## 许可证

[MIT](LICENSE) © 2026 boydreamsu-arch
