import os

def scan_junk_files(folder_path):
    junk_files = []

    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print("找不到这个文件夹，请检查路径是否正确。")
        return

    # 遍历文件夹里的所有文件和子文件夹
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 只处理文件，跳过文件夹
        if os.path.isfile(file_path):
            # 检查文件大小
            file_size = os.path.getsize(file_path)

            # 判断：如果是空文件(0字节)，或者是特定的垃圾后缀
            if file_size == 0:
                junk_files.append((filename, "空文件"))
            elif filename.endswith('.tmp') or filename.endswith('.log'):
                junk_files.append((filename, "临时/日志文件"))

    # 输出结果
    if junk_files:
        print(f"在 '{folder_path}' 中发现了以下疑似垃圾文件：")
        for name, reason in junk_files:
            print(f"- {name} ({reason})")
    else:
        print("文件夹很干净，没有发现垃圾文件！")

# 主程序：扫描当前目录
current_dir = os.getcwd()
print(f"正在扫描文件夹: {current_dir}\n")
scan_junk_files(current_dir)
current_dir = os.getcwd()
print(f"正在扫描文件夹: {current_dir}\n")
scan_junk_files(current_dir)