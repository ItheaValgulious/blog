"""
read the first arg as command:

if command is deploy:
call the following commands:
python deal_img.py
python deal_latex.py deploy
hexo clean
hexo generate
hexo deploy
python deal_latex.py clean

if the command is server:
call the following commands:
python deal_img.py
python deal_latex.py deploy
hexo clean
hexo generate
hexo server

if the command is clean:
python deal_latex.py clean

"""

from __future__ import annotations

import os
import subprocess
import sys
from typing import Iterable, List


def _repo_root() -> str:
	return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _run(cmd: Iterable[str], cwd: str) -> None:
	cmd_list: List[str] = list(cmd)
	print(f"[manager] running: {' '.join(cmd_list)}")
	subprocess.run(cmd_list, cwd=cwd, check=True)


def _python_cmd(script_name: str, *args: str) -> List[str]:
	script_path = os.path.join(os.path.dirname(__file__), script_name)
	return [sys.executable, script_path, *args]


def _run_hexo(args: Iterable[str], cwd: str) -> None:
	cmd_list: List[str] = ["hexo", *list(args)]
	print(f"[manager] running: {' '.join(cmd_list)}")
	subprocess.run(' '.join(cmd_list),cwd=cwd,shell=True)


def main() -> None:
	if len(sys.argv) < 2:
		print("[manager] missing command. Use: deploy | server | clean")
		sys.exit(1)

	command = sys.argv[1].lower()
	cwd = _repo_root()
	hexo_cwd = os.path.dirname(os.path.dirname(__file__))

	if command == "deploy":
		_run(_python_cmd("deal_img.py"), cwd)
		_run(_python_cmd("deal_latex.py", "deploy"), cwd)
		_run_hexo(["clean"], hexo_cwd)
		_run_hexo(["generate"], hexo_cwd)
		_run_hexo(["deploy"], hexo_cwd)
		_run(_python_cmd("deal_latex.py", "clean"), cwd)
		return

	if command == "server":
		_run(_python_cmd("deal_img.py"), cwd)
		_run(_python_cmd("deal_latex.py", "deploy"), cwd)
		_run_hexo(["clean"], hexo_cwd)
		_run_hexo(["generate"], hexo_cwd)
		_run_hexo(["server"], hexo_cwd)
		return

	if command == "clean":
		_run(_python_cmd("deal_latex.py", "clean"), cwd)
		return

	print(f"[manager] unknown command: {command}. Use: deploy | server | clean")
	sys.exit(1)


if __name__ == "__main__":
	main()