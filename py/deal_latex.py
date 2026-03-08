"""
read target dir from config.py as workspace
you provide two commands: deploy and clean. you read the command from args
if deploy:
you should recursively scan _posts and its sub directories:
for any {path}/{name}.tex file, you should:
1. move {path}/latexbuild/{name}.pdf to workspace/pdf/{path}/{name}.pdf. replace if existed.
2. read {name}.tex, get the following attribute:
    - {tags}:read the comment by search "% tags:(.*)". use the first matching result.
    - {title}: search "\\title{.*}"
    - {date}: search "\\date{.*}". and if the date is \\today, set it to the current time with format like "2025-09-02 13:01:00".
3. create {path}/{name}.md with the content:
    {{yaml}}

    # {title}
    [spirit of fire,please show me a pdf {the path of the pdf}]

4. output what you had done
5. remove folder {path}/latexbuild

if clean:
you should recursively scan _posts and its sub directories:
for any {path}/{name}.tex file, you should:
remove {path}/{name}.md
remove {path}/latexbuild
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from datetime import datetime
from typing import Iterable

from config import target_directory


def _posts_root() -> str:
    return os.path.join(target_directory, "_posts")


def _iter_tex_files(root: str) -> Iterable[str]:
    for current_root, _, files in os.walk(root):
        for filename in files:
            if filename.lower().endswith(".tex"):
                yield os.path.join(current_root, filename)


def _parse_tex_metadata(tex_content: str, fallback_title: str) -> tuple[str, str, str]:
    tags_match = re.search(r"%\s*tags:(.*)", tex_content)
    title_match = re.search(r"\\title\{(.*?)\}", tex_content)
    date_match = re.search(r"\\date\{(.*?)\}", tex_content)

    tags = tags_match.group(1).strip() if tags_match else ""
    title = title_match.group(1).strip() if title_match else fallback_title
    date_raw = date_match.group(1).strip() if date_match else ""

    if date_raw == r"\today":
        date_value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        date_value = date_raw

    return title, tags, date_value


def _make_pdf_web_path(rel_dir: str, name: str) -> str:
    rel_dir = rel_dir.replace("\\", "/")
    if rel_dir in (".", ""):
        return f"/pdf/{name}.pdf"
    return f"/pdf/{rel_dir}/{name}.pdf"


def _deploy_tex(tex_path: str) -> None:
    posts_root = _posts_root()
    tex_dir = os.path.dirname(tex_path)
    name = os.path.splitext(os.path.basename(tex_path))[0]
    rel_dir = os.path.relpath(tex_dir, posts_root)

    pdf_source = os.path.join(tex_dir, "latexbuild", f"{name}.pdf")
    pdf_dest = os.path.join(target_directory, "pdf", rel_dir, f"{name}.pdf")
    os.makedirs(os.path.dirname(pdf_dest), exist_ok=True)

    if os.path.exists(pdf_source):
        if os.path.exists(pdf_dest):
            os.remove(pdf_dest)
        shutil.move(pdf_source, pdf_dest)
        print(f"[deal_latex] moved {pdf_source} -> {pdf_dest}")
    else:
        print(f"[deal_latex] missing pdf: {pdf_source}")

    with open(tex_path, "r", encoding="utf-8") as handle:
        tex_content = handle.read()

    title, tags, date_value = _parse_tex_metadata(tex_content, name)
    yaml_block = f"title: {title}\ntags: {tags}\ndate: {date_value}"
    pdf_web_path = _make_pdf_web_path(rel_dir, name)

    md_content = (
        f"---\n{yaml_block}\n---\n\n"
        f"# {title}\n"
        f"[spirit of fire,please show me a pdf {pdf_web_path}]\n"
    )
    md_path = os.path.join(tex_dir, f"{name}.md")
    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write(md_content)
    print(f"[deal_latex] wrote {md_path}")

    build_dir = os.path.join(tex_dir, "latexbuild")
    shutil.rmtree(build_dir, ignore_errors=True)
    print(f"[deal_latex] cleaned {build_dir}")


def deploy() -> None:
    posts_root = _posts_root()
    if not os.path.isdir(posts_root):
        print(f"[deal_latex] _posts not found: {posts_root}")
        return

    for tex_path in _iter_tex_files(posts_root):
        _deploy_tex(tex_path)


def clean() -> None:
    posts_root = _posts_root()
    if not os.path.isdir(posts_root):
        print(f"[deal_latex] _posts not found: {posts_root}")
        return

    for tex_path in _iter_tex_files(posts_root):
        tex_dir = os.path.dirname(tex_path)
        name = os.path.splitext(os.path.basename(tex_path))[0]
        md_path = os.path.join(tex_dir, f"{name}.md")
        if os.path.exists(md_path):
            os.remove(md_path)
            print(f"[deal_latex] removed {md_path}")
        build_dir = os.path.join(tex_dir, "latexbuild")
        if os.path.isdir(build_dir):
            shutil.rmtree(build_dir, ignore_errors=True)
            print(f"[deal_latex] removed {build_dir}")


def main() -> None:
    if len(sys.argv) < 2:
        print("[deal_latex] missing command: deploy | clean")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "deploy":
        deploy()
        return
    if command == "clean":
        clean()
        return

    print(f"[deal_latex] unknown command: {command}. Use deploy | clean")
    sys.exit(1)


if __name__ == "__main__":
    main()