import os
import shutil


def list_and_copy_files_recursive(src_directory, dst_directory):
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    for root, dirs, files in os.walk(src_directory):
        for file in files:
            src_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, src_directory)
            dst_file_path = os.path.join(dst_directory, relative_path, file)

            dst_file_dir = os.path.dirname(dst_file_path)
            if not os.path.exists(dst_file_dir):
                os.makedirs(dst_file_dir)

            shutil.copy2(src_file_path, dst_file_path)
            print(f"Copied {src_file_path} to {dst_file_path}")


src_directory = 'E://'  # 替换为源目录路径
dst_directory = 'D://U//'  # 替换为目标目录路径

list_and_copy_files_recursive(src_directory, dst_directory)
