import tkinter as tk
from tkinter import filedialog, messagebox
from service.search_logic import search_in_ppt
from style.style import apply_style, style_button, style_entry, style_checkbox, style_radiobutton, style_frame

def browse_file_or_folder():
    if select_type_var.get() == "folder":
        path = filedialog.askdirectory()
    else:
        path = filedialog.askopenfilename(filetypes=[("PPTX 文件", "*.pptx")])
    path_var.set(path)

def search():
    global FULL_MATCH, IGNORE_CASE

    path = path_var.get()
    term = search_term_var.get()
    is_folder = select_type_var.get() == "folder"

    FULL_MATCH = full_match_var.get()
    IGNORE_CASE = ignore_case_var.get()

    if not path or not term:
        messagebox.showwarning("警告", "请填写完整的路径和搜索字符！")
        return

    matches = search_in_ppt(path, term, is_folder)

    if matches:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "\n".join(matches))
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "未找到匹配项。")

# 创建主窗口
def create_gui():
    global path_var, search_term_var, result_text, full_match_var, ignore_case_var, select_type_var

    root = tk.Tk()
    root.title("PPT 搜索工具")
    root.geometry("600x550")
    root.configure(bg="#f9f9f9")

    path_var = tk.StringVar()
    search_term_var = tk.StringVar()
    full_match_var = tk.BooleanVar(value=False)
    ignore_case_var = tk.BooleanVar(value=True)
    select_type_var = tk.StringVar(value="folder")

    frame = tk.Frame(root, bg="#f9f9f9")
    style_frame(frame)
    frame.pack(pady=10, padx=10, fill=tk.X)

    type_frame = tk.Frame(root, bg="#f9f9f9")
    style_frame(type_frame)
    type_frame.pack(pady=5)

    folder_radio = tk.Radiobutton(type_frame, text="文件夹", variable=select_type_var, value="folder")
    style_radiobutton(folder_radio)
    folder_radio.pack(side=tk.LEFT, padx=5)

    file_radio = tk.Radiobutton(type_frame, text="PPTX 文件", variable=select_type_var, value="file")
    style_radiobutton(file_radio)
    file_radio.pack(side=tk.LEFT, padx=5)

    folder_label = tk.Label(frame, text="路径:", bg="#f9f9f9", font=("Arial", 10))
    folder_label.pack(side=tk.LEFT)

    folder_entry = tk.Entry(frame, textvariable=path_var, width=50)
    style_entry(folder_entry)
    folder_entry.pack(side=tk.LEFT, padx=5)

    browse_button = tk.Button(frame, text="浏览", command=browse_file_or_folder)
    style_button(browse_button)
    browse_button.pack(side=tk.LEFT)

    term_label = tk.Label(root, text="搜索字符:", bg="#f9f9f9", font=("Arial", 10))
    term_label.pack()

    term_entry = tk.Entry(root, textvariable=search_term_var, width=50)
    style_entry(term_entry)
    term_entry.pack(pady=5)

    options_frame = tk.Frame(root, bg="#f9f9f9")
    style_frame(options_frame)
    options_frame.pack(pady=5)

    full_match_check = tk.Checkbutton(options_frame, text="全字匹配", variable=full_match_var)
    style_checkbox(full_match_check)
    full_match_check.pack(side=tk.LEFT, padx=5)

    ignore_case_check = tk.Checkbutton(options_frame, text="不区分大小写", variable=ignore_case_var)
    style_checkbox(ignore_case_check)
    ignore_case_check.pack(side=tk.LEFT, padx=5)

    search_button = tk.Button(root, text="搜索", command=search)
    style_button(search_button)
    search_button.pack(pady=5)

    result_text = tk.Text(root, height=15, wrap=tk.WORD, bg="#fff", fg="#333", font=("Arial", 10))
    result_text.configure(
        highlightthickness=1,
        highlightbackground="#ccc",
        relief="solid",
        borderwidth=0
    )
    result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()