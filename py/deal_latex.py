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
3. create {path}/{name}.html with the template "./template_for_pdf.html". replace {{path}} by workspace/pdf/{path}/{name}.pdf and replace {{yaml}} by "{{title:{title}\ntags:{tags}\ndate:{date}}}"

4. output what you had done
5. remove folder {path}/latexbuild

if clean:
you should recursively scan _posts and its sub directories:
for any {path}/{name}.tex file, you should:
remove {path}/{name}.html
remove {path}/latexbuild
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from datetime import datetime
from typing import Iterable, Optional

from config import target_directory


def _posts_root() -> str:
    return os.path.join(target_directory, "_posts")


def _template_path() -> Optional[str]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(base_dir, "template_for_pdf.html")
    if os.path.exists(candidate):
        return candidate
    fallback = os.path.join(base_dir, "pdftemplate.html")
    if os.path.exists(fallback):
        return fallback
    return None


def _load_template() -> str:
    template_path = _template_path()
    if not template_path:
        raise FileNotFoundError("template_for_pdf.html or pdftemplate.html not found")
    with open(template_path, "r", encoding="utf-8") as handle:
        return handle.read()


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


def _deploy_tex(tex_path: str, template: str) -> None:
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

    html_content = template.replace("{{path}}", pdf_web_path).replace("{{yaml}}", yaml_block)
    html_path = os.path.join(tex_dir, f"{name}.html")
    with open(html_path, "w", encoding="utf-8") as handle:
        handle.write(html_content)
    print(f"[deal_latex] wrote {html_path}")

    build_dir = os.path.join(tex_dir, "latexbuild")
    shutil.rmtree(build_dir, ignore_errors=True)
    print(f"[deal_latex] cleaned {build_dir}")


def deploy() -> None:
    posts_root = _posts_root()
    if not os.path.isdir(posts_root):
        print(f"[deal_latex] _posts not found: {posts_root}")
        return

    template = _load_template()
    for tex_path in _iter_tex_files(posts_root):
        _deploy_tex(tex_path, template)


def clean() -> None:
    posts_root = _posts_root()
    if not os.path.isdir(posts_root):
        print(f"[deal_latex] _posts not found: {posts_root}")
        return

    for tex_path in _iter_tex_files(posts_root):
        tex_dir = os.path.dirname(tex_path)
        name = os.path.splitext(os.path.basename(tex_path))[0]
        html_path = os.path.join(tex_dir, f"{name}.html")
        if os.path.exists(html_path):
            os.remove(html_path)
            print(f"[deal_latex] removed {html_path}")
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