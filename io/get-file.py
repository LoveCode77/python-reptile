# 获取文件列表
import os


def list_files_recursive(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list


directory = 'E://'
all_files = list_files_recursive(directory)

for file in all_files:
    print(file)
