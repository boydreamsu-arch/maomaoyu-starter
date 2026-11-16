"""命令行入口：安装后用 ``maomaoyu`` 命令调用，也可 ``python -m maomaoyu_starter``。"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from . import __version__, greet


def build_parser() -> argparse.ArgumentParser:
    """构造命令行参数解析器。"""
    parser = argparse.ArgumentParser(
        prog="maomaoyu",
        description="maomaoyu-starter 的示例命令行工具。",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="要问候的对象（默认：World）",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """程序主入口，返回退出码。"""
    parser = build_parser()
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
