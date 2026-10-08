# ==========================================
# Author: Your Name (ඔයාගේ නම මෙතනට දාන්න)
# Project: Modern Python Calculator
# Copyright (c) 2026. All Rights Reserved.
# ==========================================

import customtkinter as ctk

# Appearance setup
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Electric Green & Dark Charcoal theme vibes

app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("320x490")
app.resizable(False, False)

expression = ""

# Screen එක update කරන්න
def click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Clear (C) - මුළු එකම මකන්න
def clear():
    global expression
    expression = ""
    input_text.set("")

# Delete (DEL) - අන්තිමට ගැහූ අංකය හෝ ලකුණ පමණක් මකන්න (Backspace)
def delete_one():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# සමානයි (=) - ගණන් හැදෙන තැන
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

input_text = ctk.StringVar()

# Display Screen එක
input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=15)

input_field = ctk.CTkEntry(
    input_frame, 
    font=('Arial', 24, 'bold'), 
    textvariable=input_text, 
    width=280, 
    height=60, 
    corner_radius=10,
    justify="right"
)
input_field.pack()

# Buttons Frame එක
btns_frame = ctk.CTkFrame(app, fg_color="transparent")
btns_frame.pack(pady=5)

# Button Design Parameters
btn_w = 65
btn_h = 50
corner = 10

# Row 1: C, DEL, %, /
btn_c = ctk.CTkButton(btns_frame, text="C", width=btn_w, height=btn_h, corner_radius=corner, fg_color="#d9534f", hover_color="#c9302c", font=('Arial', 16, 'bold'), command=clear)
btn_c.grid(row=0, column=0, padx=5, pady=5)

btn_del = ctk.CTkButton(btns_frame, text="DEL", width=btn_w, height=btn_h, corner_radius=corner, fg_color="#f0ad4e", hover_color="#ec971f", font=('Arial', 14, 'bold'), command=delete_one)
btn_del.grid(row=0, column=1, padx=5, pady=5)

btn_mod = ctk.CTkButton(btns_frame, text="%", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click("%"))
btn_mod.grid(row=0, column=2, padx=5, pady=5)

btn_div = ctk.CTkButton(btns_frame, text="/", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click("/"))
btn_div.grid(row=0, column=3, padx=5, pady=5)

# Row 2: 7, 8, 9, *
btn_7 = ctk.CTkButton(btns_frame, text="7", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(7))
btn_7.grid(row=1, column=0, padx=5, pady=5)

btn_8 = ctk.CTkButton(btns_frame, text="8", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(8))
btn_8.grid(row=1, column=1, padx=5, pady=5)

btn_9 = ctk.CTkButton(btns_frame, text="9", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(9))
btn_9.grid(row=1, column=2, padx=5, pady=5)

btn_mul = ctk.CTkButton(btns_frame, text="*", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click("*"))
btn_mul.grid(row=1, column=3, padx=5, pady=5)

# Row 3: 4, 5, 6, -
btn_4 = ctk.CTkButton(btns_frame, text="4", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(4))
btn_4.grid(row=2, column=0, padx=5, pady=5)

btn_5 = ctk.CTkButton(btns_frame, text="5", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(5))
btn_5.grid(row=2, column=1, padx=5, pady=5)

btn_6 = ctk.CTkButton(btns_frame, text="6", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(6))
btn_6.grid(row=2, column=2, padx=5, pady=5)

btn_min = ctk.CTkButton(btns_frame, text="-", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click("-"))
btn_min.grid(row=2, column=3, padx=5, pady=5)

# Row 4: 1, 2, 3, +
btn_1 = ctk.CTkButton(btns_frame, text="1", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(1))
btn_1.grid(row=3, column=0, padx=5, pady=5)

btn_2 = ctk.CTkButton(btns_frame, text="2", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(2))
btn_2.grid(row=3, column=1, padx=5, pady=5)

btn_3 = ctk.CTkButton(btns_frame, text="3", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(3))
btn_3.grid(row=3, column=2, padx=5, pady=5)

btn_plus = ctk.CTkButton(btns_frame, text="+", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click("+"))
btn_plus.grid(row=3, column=3, padx=5, pady=5)

# Row 5: 0, ., =
btn_0 = ctk.CTkButton(btns_frame, text="0", width=142, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click(0))
btn_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btn_dot = ctk.CTkButton(btns_frame, text=".", width=btn_w, height=btn_h, corner_radius=corner, font=('Arial', 16, 'bold'), command=lambda: click("."))
btn_dot.grid(row=4, column=2, padx=5, pady=5)

btn_eq = ctk.CTkButton(btns_frame, text="=", width=btn_w, height=btn_h, corner_radius=corner, fg_color="#28a745", hover_color="#218838", font=('Arial', 16, 'bold'), command=evaluate)
btn_eq.grid(row=4, column=3, padx=5, pady=5)

# Signature Footer Label
signature_label = ctk.CTkLabel(
    app, 
    text="Created with 💻 by Your Name", 
    font=('Arial', 11), 
    text_color="gray"
)
signature_label.pack(side="bottom", pady=8)

app.mainloop()