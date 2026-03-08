"""
read target dir from config.py as workspace
you should recursively scan _posts and its sub directories:
if there is a folder contains a folder "image", you should:
1. read all the imgs below "image" like
/image/{passage_name}/{img_name.png}
2. move the content of "image" to workspace/imgs recursively
3. replace the path for all the markdown files in this "image" file,which means:
replace !\\[(.*?)\\]\\(image/{passage_name}/{img_name.png}\\) to the new path:
"/imgs/{passage_name}/{img_name.png}"
4. output what you had done and remove the folder "image"
"""

from __future__ import annotations

import os
import re
import shutil
from typing import Iterable

from config import target_directory


def _posts_root() -> str:
	return os.path.join(target_directory, "_posts")


def _iter_markdown_files(root: str) -> Iterable[str]:
	for current_root, _, files in os.walk(root):
		for filename in files:
			if filename.lower().endswith(".md"):
				yield os.path.join(current_root, filename)


def _replace_markdown_links(root: str) -> int:
	pattern = re.compile(r"!\[(.*?)\]\(image/([^\)]+)\)")
	replacements = 0

	for md_path in _iter_markdown_files(root):
		with open(md_path, "r", encoding="utf-8") as handle:
			content = handle.read()

		new_content, count = pattern.subn(r"![\1](/imgs/\2)", content)
		if count:
			with open(md_path, "w", encoding="utf-8") as handle:
				handle.write(new_content)
			replacements += count
			print(f"[deal_img] updated {md_path} ({count} replacements)")

	return replacements


def _move_images(image_dir: str) -> int:
	target_imgs_root = os.path.join(target_directory, "imgs")
	moved = 0

	for current_root, _, files in os.walk(image_dir):
		for filename in files:
			source_path = os.path.join(current_root, filename)
			rel_path = os.path.relpath(source_path, image_dir)
			dest_path = os.path.join(target_imgs_root, rel_path)
			os.makedirs(os.path.dirname(dest_path), exist_ok=True)
			if os.path.exists(dest_path):
				os.remove(dest_path)
			shutil.move(source_path, dest_path)
			moved += 1
			print(f"[deal_img] moved {source_path} -> {dest_path}")

	return moved


def process_images() -> None:
	posts_root = _posts_root()
	if not os.path.isdir(posts_root):
		print(f"[deal_img] _posts not found: {posts_root}")
		return

	for current_root, dirs, _ in os.walk(posts_root):
		if "image" not in dirs:
			continue

		image_dir = os.path.join(current_root, "image")
		print(f"[deal_img] processing {image_dir}")

		moved = _move_images(image_dir)
		replacements = _replace_markdown_links(current_root)

		shutil.rmtree(image_dir, ignore_errors=True)
		print(
			f"[deal_img] completed {image_dir}: moved {moved} files, "
			f"updated {replacements} links."
		)

		dirs[:] = [d for d in dirs if d != "image"]


if __name__ == "__main__":
	process_images()