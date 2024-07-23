# -*- coding: utf-8 -*-
# @Description:
import os


def rename_files_in_dir(directory, script_name):
    # 获取目录下的所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # 排除当前脚本或者打包后的可执行文件
    files = [f for f in files if f != script_name and not f.endswith('exe')]

    # 按文件名排序
    files.sort()

    # 重命名文件
    for index, filename in enumerate(files):
        # 提取文件的扩展名
        file_extension = os.path.splitext(filename)[1]

        # 构建新文件名（保留原有扩展名）
        new_filename = f"{index + 1}{file_extension}"

        # 构建原始和新的完整文件路径
        original_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)

        # 重命名文件
        os.rename(original_filepath, new_filepath)
        print(f"Renamed '{filename}' to '{new_filename}'")


if __name__ == "__main__":
    # 当前脚本的名称（包含扩展名）
    current_name = os.path.basename(__file__)
    # 当前脚本的路径
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # 调用函数
    rename_files_in_dir(current_directory, current_name)