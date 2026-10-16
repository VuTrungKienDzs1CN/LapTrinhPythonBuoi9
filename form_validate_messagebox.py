import tkinter as tk
from tkinter import messagebox  # Bắt buộc import thêm messagebox để hiện hộp thoại thông báo

def xu_ly_submit():
    # .strip() giúp cắt bỏ các khoảng trắng thừa ở 2 đầu chuỗi do người dùng vô tình gõ
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    # 1. Kiểm tra họ tên rỗng
    if ho_ten == "":
        messagebox.showerror("Loi", "Ho ten khong duoc de trong.")
        return  # Dừng hàm ngay lập tức, không chạy các lệnh bên dưới nữa

    # 2. Kiểm tra tuổi có phải là số nguyên hợp lệ không
    try:
        tuoi = int(tuoi_nhap)
    except ValueError:
        messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.")
        return

    # 3. Kiểm tra email có chứa ký tự @ không
    if "@" not in email:
        messagebox.showerror("Loi", "Email khong hop le (thieu ky tu @).")
        return

    # Nếu vượt qua hết các bước kiểm tra trên thì báo thành công
    messagebox.showinfo("Thanh cong", f"Da nhan thong tin: {ho_ten} - {tuoi} tuoi - {email}")

# Phần khởi tạo giao diện (nằm sát lề trái, ngoài hàm xu_ly_submit)
cua_so = tk.Tk()
cua_so.title("Form co validate")
cua_so.geometry("380x220")

# Dòng 0: Họ tên
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

# Dòng 1: Tuổi
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

# Dòng 2: Email
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Dòng 3: Nút Submit
tk.Button(cua_so, text="Submit", command=xu_ly_submit).grid(
    row=3, column=0, columnspan=2, pady=15
)

cua_so.mainloop()