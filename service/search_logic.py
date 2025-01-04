import os
from pptx import Presentation
import re

# 读取设置
try:
    from setting.setting import FULL_MATCH, IGNORE_CASE
except ImportError:
    print("未找到 setting.py 文件，将使用默认设置。")


def search_in_ppt(folder_path, search_term):
    """
    搜索指定文件夹下所有 PPT 文件中的指定字符，并返回匹配的文件名和定位页。

    :param folder_path: 文件夹路径
    :param search_term: 要搜索的字符
    :return: list，格式为 ["文件名 - 页码"]
    """
    result = []

    # 正则表达式设置
    flags = re.IGNORECASE if IGNORE_CASE else 0
    if FULL_MATCH:
        pattern = re.compile(rf"\\b{re.escape(search_term)}\\b", flags)
    else:
        pattern = re.compile(re.escape(search_term), flags)

    # 遍历文件夹中的 PPT 文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pptx"):
            file_path = os.path.join(folder_path, file_name)
            try:
                ppt = Presentation(file_path)
                for i, slide in enumerate(ppt.slides):
                    for shape in slide.shapes:
                        if shape.has_text_frame:
                            text = shape.text
                            if pattern.search(text):
                                result.append(f"{file_name} - 第{i + 1}页")
            except Exception as e:
                print(f"处理文件 {file_name} 时出错: {e}")

    return result