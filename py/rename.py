import os
import re
import datetime

def rename_md_files(folder_path):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"错误: 找不到文件夹 '{folder_path}'")
        return

    # 正则表达式：匹配 date 字段
    # 逻辑：在 --- 包裹的区域内寻找 date: 20xx-xx-xx
    # 兼容写法：date: 2025-11-24 或 date: "2025-11-24 14:28:49"
    date_pattern = re.compile(r'^date:\s*["\']?(\d{4}-\d{2}-\d{2})', re.MULTILINE)
    
    # 正则表达式：检查文件名是否已经以 6位数字+横杠 开头 (例如 251124-)
    prefix_pattern = re.compile(r'^\d{6}-')

    count_success = 0
    count_skip = 0

    print(f"正在处理文件夹: {folder_path} ...\n")

    for root, _, files in os.walk(folder_path):
        for filename in files:
            # 只处理 markdown 文件
            if not filename.endswith(".md"):
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

            # 检查是否以 --- 开头（YAML Front Matter）
            if not content.startswith('---'):
                print(f"[跳过] {filename}: 缺少 YAML 头部 (---)")
                continue

            # 提取 YAML 块
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"[跳过] {filename}: YAML 格式不完整")
                continue
            
            yaml_block = parts[1]

            # 在 YAML 块中查找日期
            match = date_pattern.search(yaml_block)
            if match:
                date_str = match.group(1) # 提取 YYYY-MM-DD 部分
                
                try:
                    # 解析日期
                    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                    
                    # 生成 6 位数编码 (YYMMDD)
                    # %y = 两位数年份, %m = 月份, %d = 日期
                    date_prefix = date_obj.strftime('%y%m%d') 

                    # 检查文件名是否已经包含此前缀
                    # 如果当前文件已经以该日期开头，或者以任何6位数字开头，建议谨慎处理
                    # 这里逻辑是：如果已经有 6位数字- 开头，则认为已重命名过，跳过
                    if prefix_pattern.match(filename):
                        print(f"[跳过] {filename}: 似乎已包含日期前缀")
                        count_skip += 1
                        continue

                    # 构造新文件名
                    new_filename = f"{date_prefix}-{filename}"
                    new_file_path = os.path.join(root, new_filename)

                    # 执行重命名
                    os.rename(file_path, new_file_path)
                    print(f"[重命名成功] {filename} -> {new_filename}")
                    count_success += 1

                except ValueError:
                    print(f"[错误] {filename}: 日期格式解析失败 ({date_str})")
            else:
                print(f"[跳过] {filename}: 未找到 date 属性")

    print(f"\n处理完成: 成功 {count_success} 个, 跳过 {count_skip} 个。")

if __name__ == '__main__':
    from config import target_directory
    
    rename_md_files(os.path.join(target_directory,'_posts'))