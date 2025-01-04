import tkinter as tk

# 样式配置
def apply_style(widget):
    widget.configure(
        bg="#f9f9f9",
        fg="#333",
        highlightbackground="#ddd",
        highlightcolor="#ddd",
        relief="flat",
        bd=0
    )

def style_button(button):
    button.configure(
        bg="#4CAF50",
        fg="#fff",
        activebackground="#45a049",
        bd=0,
        padx=10,
        pady=5,
        font=("Arial", 10, "bold"),
        highlightthickness=1,
        highlightbackground="#4CAF50",
        relief="flat",
        borderwidth=0
    )

def style_entry(entry):
    entry.configure(
        bg="#fff",
        fg="#333",
        highlightthickness=1,
        highlightbackground="#ccc",
        relief="solid",
        font=("Arial", 10),
        borderwidth=0
    )
    entry.configure(
        highlightthickness=1,
        highlightbackground="#ccc",
        highlightcolor="#4CAF50"
    )

def style_checkbox(checkbox):
    checkbox.configure(
        bg="#f9f9f9",
        activebackground="#f9f9f9",
        selectcolor="#4CAF50",
        font=("Arial", 10),
        borderwidth=0
    )
    checkbox.configure(
        highlightthickness=1,
        highlightbackground="#4CAF50",
        relief="flat"
    )

def style_radiobutton(radiobutton):
    radiobutton.configure(
        bg="#f9f9f9",
        activebackground="#f9f9f9",
        selectcolor="#4CAF50",
        font=("Arial", 10),
        borderwidth=0
    )
    radiobutton.configure(
        highlightthickness=1,
        highlightbackground="#4CAF50",
        relief="flat"
    )

def style_frame(frame):
    frame.configure(
        bg="#f9f9f9",
        relief="flat",
        bd=0,
        highlightthickness=0
    )
