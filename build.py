import os
import subprocess
import shutil

def build_executable():
    # 定义 PyInstaller 命令
    command = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--name', 'ppt-search-str',
        # '--icon', 'icon.ico',  # 指定图标文件路径
        'main.py'
    ]

    # 运行 PyInstaller 命令
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"PyInstaller 打包失败: {e}")
        return

    # 清理临时文件
    clean_up()

def clean_up():
    # 删除 build 文件夹
    build_folder = 'build'
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)

    # 删除 .spec 文件
    spec_file = 'ppt-search-str.spec'
    if os.path.exists(spec_file):
        os.unlink(spec_file)

if __name__ == "__main__":
    build_executable()