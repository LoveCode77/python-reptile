# python 提取文件 不包括文件夹
import os
import shutil


def list_and_copy_files_flat(src_directory, dst_directory):
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    for root, dirs, files in os.walk(src_directory):
        for file in files:
            src_file_path = os.path.join(root, file)
            dst_file_path = os.path.join(dst_directory, file)

            # 如果目标目录中已经存在同名文件，可以选择重命名或覆盖
            if os.path.exists(dst_file_path):
                base, extension = os.path.splitext(file)
                counter = 1
                new_dst_file_path = os.path.join(dst_directory, f"{base}_{counter}{extension}")
                while os.path.exists(new_dst_file_path):
                    counter += 1
                    new_dst_file_path = os.path.join(dst_directory, f"{base}_{counter}{extension}")
                dst_file_path = new_dst_file_path

            shutil.copy2(src_file_path, dst_file_path)
            print(f"Copied {src_file_path} to {dst_file_path}")


src_directory = 'E://'  # 替换为源目录路径
dst_directory = 'D://U//'  # 替换为目标目录路径

list_and_copy_files_flat(src_directory, dst_directory)
