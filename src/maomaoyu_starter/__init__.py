"""maomaoyu_starter — 一个最小可用、结构规范的 Python 项目骨架。

用法::

    from maomaoyu_starter import greet

    greet()          # 'Hello, World!'
    greet("maomaoyu")  # 'Hello, maomaoyu!'
"""

from __future__ import annotations

__version__ = "0.1.0"

__all__ = ["__version__", "greet"]


def greet(name: str = "World") -> str:
    """返回一句问候语。

    Args:
        name: 被问候的对象，默认 ``"World"``。

    Returns:
        形如 ``Hello, <name>!`` 的字符串。

    Raises:
        TypeError: 当 ``name`` 不是字符串时。
    """
    if not isinstance(name, str):
        raise TypeError(f"name 必须是 str，收到 {type(name).__name__}")
    name = name.strip() or "World"
    return f"Hello, {name}!"
