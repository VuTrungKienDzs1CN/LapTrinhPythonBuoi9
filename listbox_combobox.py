import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Listbox")
cua_so.geometry("300x250")

# Tạo Listbox cho phép chọn 1 mục (selectmode="single")
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single")

# Vòng lặp thêm từng môn học vào cuối danh sách (tk.END)
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)  # Dòng này bắt buộc thụt lề vào trong vòng lặp for

listbox_mon_hoc.pack(pady=10)

def xem_mon_da_chon():
    # Lấy vị trí (index) của mục đang được chọn, trả về một tuple, ví dụ: (0,)
    lua_chon = listbox_mon_hoc.curselection()
    
    # Kiểm tra xem người dùng đã click chọn môn nào chưa (tránh lỗi khi bấm nút mà chưa chọn)
    if lua_chon:
        # lua_chon[0] là số thứ tự của dòng đang chọn (chú ý là số 0, không phải chữ O)
        nhan_ket_qua.config(text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}")

# Lưu ý: Từ dòng tk.Button trở xuống phải đưa ra sát lề trái (nằm ngoài hàm def)
tk.Button(cua_so, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=5)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()

import tkinter as tk
from tkinter import ttk  # Bắt buộc import thêm ttk vì Combobox nằm trong bộ công cụ mở rộng này

cua_so = tk.Tk()
cua_so.title("Vi du Combobox")
cua_so.geometry("300x180")

tk.Label(cua_so, text="Chon thanh pho:").pack(pady=10)

# Tạo danh sách thả xuống (Combobox)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0)  # Chọn giá trị đầu tiên ("Ha Noi" ở vị trí số 0) làm mặc định
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    # Với Combobox, chỉ cần dùng .get() là lấy được ngay chuỗi văn bản đang chọn
    nhan_ket_qua.config(text=f"Ban chon: {combobox_thanh_pho.get()}")

# Đưa các dòng tạo nút, nhãn và mainloop ra sát lề trái
tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()