import tkinter as tk
from tkinter import filedialog, messagebox
from service.search_logic import search_in_ppt


def browse_folder():
    folder = filedialog.askdirectory()
    folder_path_var.set(folder)


def search():
    folder = folder_path_var.get()
    term = search_term_var.get()

    if not folder or not term:
        messagebox.showwarning("警告", "请填写完整的文件夹路径和搜索字符！")
        return

    matches = search_in_ppt(folder, term)

    if matches:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "\n".join(matches))
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "未找到匹配项。")


# 创建主窗口
def create_gui():
    global folder_path_var, search_term_var, result_text

    root = tk.Tk()
    root.title("PPT 搜索工具")
    root.geometry("600x400")

    # 文件夹选择
    folder_path_var = tk.StringVar()
    search_term_var = tk.StringVar()

    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10, fill=tk.X)

    folder_label = tk.Label(frame, text="文件夹路径:")
    folder_label.pack(side=tk.LEFT)

    folder_entry = tk.Entry(frame, textvariable=folder_path_var, width=50)
    folder_entry.pack(side=tk.LEFT, padx=5)

    browse_button = tk.Button(frame, text="浏览", command=browse_folder)
    browse_button.pack(side=tk.LEFT)

    # 搜索字符输入
    term_label = tk.Label(root, text="搜索字符:")
    term_label.pack()

    term_entry = tk.Entry(root, textvariable=search_term_var, width=50)
    term_entry.pack(pady=5)

    # 搜索按钮
    search_button = tk.Button(root, text="搜索", command=search)
    search_button.pack(pady=5)

    # 结果显示框
    result_text = tk.Text(root, height=15, wrap=tk.WORD)
    result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # 运行主循环
    root.mainloop()
