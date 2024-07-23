import os
from PIL import Image
import pillow_avif  # 导入pillow-avif-plugin以启用AVIF支持

# 打印pillow_avif插件版本
print(f'当前pillow_avif版本：{pillow_avif.__version__}')

# 获取当前目录下的所有文件
current_directory = os.getcwd()
files = os.listdir(current_directory)

# 遍历所有文件，找到AVIF格式的文件并转换为PNG格式
for file in files:
    if file.endswith('.avif'):
        # 读取AVIF格式图片
        image = Image.open(file)

        # 获取文件名（不带扩展名）
        file_name = os.path.splitext(file)[0]

        # 将图片保存为PNG格式
        image.save(f'{file_name}.png', format='PNG')

        print(f"{file} 已成功转换为 {file_name}.png")
