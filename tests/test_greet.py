"""单元测试：只用标准库 unittest，无第三方依赖，任何环境都能跑。

运行::

    python -m unittest discover -s tests -v
"""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from maomaoyu_starter import __version__, greet
from maomaoyu_starter.cli import main


class TestGreet(unittest.TestCase):
    def test_default(self) -> None:
        self.assertEqual(greet(), "Hello, World!")

    def test_custom_name(self) -> None:
        self.assertEqual(greet("maomaoyu"), "Hello, maomaoyu!")

    def test_strips_whitespace(self) -> None:
        self.assertEqual(greet("  fish  "), "Hello, fish!")

    def test_blank_falls_back_to_world(self) -> None:
        self.assertEqual(greet("   "), "Hello, World!")

    def test_rejects_non_str(self) -> None:
        with self.assertRaises(TypeError):
            greet(123)  # type: ignore[arg-type]


class TestCli(unittest.TestCase):
    def test_main_prints_greeting(self) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main([])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, World!")

    def test_main_accepts_name(self) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["fish"])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, fish!")


class TestVersion(unittest.TestCase):
    def test_version_is_semver_like(self) -> None:
        parts = __version__.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(p.isdigit() for p in parts))


if __name__ == "__main__":
    unittest.main()
