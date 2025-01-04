## Author 👤

- **姓名**: sinvon
- **邮箱**: 2021469084@qq.com

## 项目描述 📝

一个用于在 PPT 文件中搜索指定字符串的工具。支持文件夹和单个 PPT 文件的搜索，并提供全字匹配和不区分大小写的选项。

## 创作目的 🔍

期末复习的时候,发现老师发的很多ppt,每一份ppt都很长,然后一张一张的翻页,或者通过打开每一个ppt去全文搜索这样很慢,所以就创建了这个仓库,用于快速查询一个文件夹下所有pptx文件或者一个pptx中的内容来查找,并且能够提示匹配项附近的关键字.

## 界面展示 🖼️

🔗<a href="https://github.com/isinvon/ppt-search-str/releases">
点击跳转下载 GUI</a>

<img src="./image/image.png" alt="gui界面">

## 安装指南 🛠️

1. 确保已安装 Python 3.x。
2. 克隆项目仓库：

   ```bash
   git clone https://github.com/isinvon/ppt-search-str.git
   cd ppt-search-str
   ```

3. 安装依赖包：

   ```bash
   pip install -r requirements.txt
   ```

## 打包exe程序 📦

确保你安装了python环境并且安装依赖, 然后直接运行

```bash
python build.py
```

会在项目根目录`dist`文件夹中生成一个exe文件

## 使用说明 📖

1. 运行程序：

   ```bash
   python main.py
   ```

2. 选择搜索类型（文件夹或单个 PPT 文件）。
3. 浏览并选择要搜索的路径。
4. 输入搜索字符。
5. 点击“搜索”按钮，查看结果。

## 许可证 📜

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
