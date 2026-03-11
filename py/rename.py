import os
import re
import datetime

def _yy_mm_dd_prefix_from_date(date_obj: datetime.datetime) -> str:
    return date_obj.strftime('%y%m%d')


def _parse_md_date(content: str):
    """Extract YYYY-MM-DD from a markdown YAML front matter block.

    Accepts:
      - date: 2025-11-24
      - date: "2025-11-24 14:28:49"
    Returns a datetime on success, else None.
    """
    # 正则表达式：匹配 date 字段
    date_pattern = re.compile(r'^date:\s*["\']?(\d{4}-\d{2}-\d{2})', re.MULTILINE)

    if not content.startswith('---'):
        return None

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None

    yaml_block = parts[1]
    match = date_pattern.search(yaml_block)
    if not match:
        return None

    date_str = match.group(1)
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None


def _parse_tex_date(tex_content: str):
    """Extract date from a .tex file using deal_latex-style rule.

    Rule:
      - search \\date{...}
      - if it is \\today -> current time
      - parse first 10 chars as YYYY-MM-DD when possible
    Returns a datetime on success, else None.
    """
    date_match = re.search(r"\\date\{(.*?)\}", tex_content)
    if not date_match:
        return None

    date_raw = date_match.group(1).strip()
    if date_raw == r"\today":
        return datetime.datetime.now()

    # deal_latex writes date like: 2025-09-02 13:01:00
    # Some tex might store date as: 2025-09-02
    date_part = date_raw[:10]
    try:
        return datetime.datetime.strptime(date_part, '%Y-%m-%d')
    except ValueError:
        return None


def rename_files(folder_path, extensions=(".md", ".tex")):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"错误: 找不到文件夹 '{folder_path}'")
        return
    
    # 正则表达式：检查文件名是否已经以 6位数字+横杠 开头 (例如 251124-)
    prefix_pattern = re.compile(r'^\d{6}-')

    count_success = 0
    count_skip = 0

    print(f"正在处理文件夹: {folder_path} ...\n")

    for root, _, files in os.walk(folder_path):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in {e.lower() for e in extensions}:
                continue

            file_path = os.path.join(root, filename)

            # 尝试读取文件内容
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 读取前 5000 个字符通常足够包含头部信息，避免读取超大文件
                    content = f.read(5000) 
            except Exception as e:
                print(f"[读取失败] {filename}: {e}")
                continue

            if prefix_pattern.match(filename):
                print(f"[跳过] {filename}: 似乎已包含日期前缀")
                count_skip += 1
                continue

            date_obj = None
            if ext == ".md":
                date_obj = _parse_md_date(content)
                if date_obj is None:
                    if not content.startswith('---'):
                        print(f"[跳过] {filename}: 缺少 YAML 头部 (---)")
                    else:
                        print(f"[跳过] {filename}: 未找到或无法解析 date 属性")
                    continue
            elif ext == ".tex":
                date_obj = _parse_tex_date(content)
                if date_obj is None:
                    print(f"[跳过] {filename}: 未找到或无法解析 \\date{{...}}")
                    continue
            else:
                # Should never happen due to extension filter
                continue

            date_prefix = _yy_mm_dd_prefix_from_date(date_obj)

            new_filename = f"{date_prefix}-{filename}"
            new_file_path = os.path.join(root, new_filename)

            os.rename(file_path, new_file_path)
            print(f"[重命名成功] {filename} -> {new_filename}")
            count_success += 1

    print(f"\n处理完成: 成功 {count_success} 个, 跳过 {count_skip} 个。")

if __name__ == '__main__':
    from config import target_directory
    
    rename_files(os.path.join(target_directory,'_posts'))