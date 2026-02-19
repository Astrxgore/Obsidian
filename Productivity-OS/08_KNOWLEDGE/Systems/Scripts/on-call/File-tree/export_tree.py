#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_IGNORE_DIRS = {".git", ".idea", ".vscode", "__pycache__", ".pytest_cache", "node_modules", ""}
DEFAULT_IGNORE_FILES = {".DS_Store", "Thumbs.db"}


def should_skip(path: Path, ignore_dirs: set[str], ignore_files: set[str]) -> bool:
    """
    Решает, пропускать ли этот путь.

    - Игнорируем некоторые системные файлы.
    - Игнорируем директории по имени.
    """
    name = path.name

    if path.is_dir() and name in ignore_dirs:
        return True

    if path.is_file() and name in ignore_files:
        return True

    return False


def build_tree_lines(
    root: Path,
    *,
    max_depth: int | None,
    ignore_dirs: set[str],
    ignore_files: set[str],
) -> list[str]:
    """
    Строит список строк дерева для папки root.

    Формат примерно как tree:
    root/
    ├── a.txt
    ├── src/
    │   └── main.py
    └── docs/
    """
    root = root.resolve()
    lines: list[str] = [f"{root.name}/"]

    def walk(dir_path: Path, prefix: str, depth: int) -> None:
        # depth = 0 для root, 1 для его детей и т.д.
        if max_depth is not None and depth >= max_depth:
            return

        # Собираем детей, фильтруем, сортируем:
        children = []
        for p in dir_path.iterdir():
            if should_skip(p, ignore_dirs, ignore_files):
                continue
            children.append(p)

        # Сортировка: сначала папки, потом файлы; внутри — по имени
        children.sort(key=lambda p: (p.is_file(), p.name.lower()))

        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            connector = "└── " if is_last else "├── "
            line = f"{prefix}{connector}{child.name}{'/' if child.is_dir() else ''}"
            lines.append(line)

            if child.is_dir():
                # Для следующего уровня меняется "префикс"
                next_prefix = prefix + ("    " if is_last else "│   ")
                walk(child, next_prefix, depth + 1)

    walk(root, "", 0)
    return lines


def write_markdown(output_path: Path, title: str, tree_lines: list[str]) -> None:
    """
    Пишем Markdown:
    - Заголовок
    - Кодовый блок с деревом
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    md = []
    md.append(f"# {title}\n")
    md.append("```text")
    md.extend(tree_lines)
    md.append("```")
    md.append("")  # финальный перевод строки

    output_path.write_text("\n".join(md), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export folder tree to a Markdown file."
    )
    parser.add_argument("folder", help="Path to folder to scan")
    parser.add_argument(
        "-o", "--out",
        default="tree.md",
        help="Output markdown file path (default: tree.md)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Limit recursion depth (e.g. 2). Default: unlimited",
    )
    parser.add_argument(
        "--ignore-dir",
        action="append",
        default=[],
        help="Directory name to ignore (can be repeated)",
    )
    parser.add_argument(
        "--ignore-file",
        action="append",
        default=[],
        help="File name to ignore (can be repeated)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    root = Path(args.folder)
    if not root.exists():
        raise SystemExit(f"Folder does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    ignore_dirs = set(DEFAULT_IGNORE_DIRS) | set(args.ignore_dir)
    ignore_files = set(DEFAULT_IGNORE_FILES) | set(args.ignore_file)

    tree_lines = build_tree_lines(
        root,
        max_depth=args.max_depth,
        ignore_dirs=ignore_dirs,
        ignore_files=ignore_files,
    )

    out_path = Path(args.out)
    title = f"File tree for: {root.resolve()}"
    write_markdown(out_path, title, tree_lines)

    print(f"Saved: {out_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
