import tkinter as tk
from tkinter import messagebox

# Danh sách lưu các công việc. Mỗi công việc là 1 tuple: (noi_dung, da_hoan_thanh)
danh_sach_cong_viec = []


def lam_moi_listbox():
    # Xóa toàn bộ các dòng hiện tại trên Listbox (từ dòng 0 đến cuối) để vẽ lại từ đầu
    listbox_cong_viec.delete(0, tk.END)
    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        tien_to = "[Da xong] " if da_hoan_thanh else "[Chua xong] "
        listbox_cong_viec.insert(tk.END, tien_to + noi_dung)


def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()

    if noi_dung == "":
        messagebox.showerror("Loi", "Vui long nhap noi dung cong viec truoc khi them.")
        return

    # Lưu ý: Có 2 cặp ngoặc tròn vì ta truyền 1 tuple (noi_dung, False) vào hàm .append()
    danh_sach_cong_viec.append((noi_dung, False))
    bien_cong_viec_moi.set("")  # Xóa trắng ô nhập liệu sau khi thêm xong
    lam_moi_listbox()


def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showerror("Loi", "Vui long chon mot cong viec trong danh sach de xoa.")
        return

    vi_tri = lua_chon[0]
    danh_sach_cong_viec.pop(vi_tri)  # Xóa phần tử tại vị trí đang chọn
    lam_moi_listbox()


def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showerror("Loi", "Vui long chon mot cong viec de danh dau hoan thanh.")
        return

    vi_tri = lua_chon[0]
    # Dấu gạch dưới (_) dùng để bỏ qua giá trị trạng thái cũ vì ta sắp gán nó thành True
    noi_dung, _ = danh_sach_cong_viec[vi_tri]
    danh_sach_cong_viec[vi_tri] = (noi_dung, True)
    lam_moi_listbox()


# --- PHẦN KHỞI TẠO GIAO DIỆN (Sát lề trái) ---
cua_so = tk.Tk()
cua_so.title("Ung dung Ghi chu cong viec")
cua_so.geometry("420x400")
cua_so.resizable(False, False)  # Khóa kích thước cửa sổ, không cho kéo giãn

bien_cong_viec_moi = tk.StringVar()

# Dòng 0: Tiêu đề
tk.Label(cua_so, text="TO-DO LIST", font=("Arial", 16, "bold")).grid(
    row=0, column=0, columnspan=3, pady=15
)

# Dòng 1: Ô nhập công việc và nút Thêm
entry_cong_viec = tk.Entry(cua_so, textvariable=bien_cong_viec_moi, width=30)
entry_cong_viec.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Button(cua_so, text="Them", command=them_cong_viec).grid(
    row=1, column=2, padx=10, pady=5
)

# Dòng 2: Danh sách công việc (Listbox)
listbox_cong_viec = tk.Listbox(cua_so, width=45, height=12)
listbox_cong_viec.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Dòng 3: Nút Đánh dấu hoàn thành và Xóa
tk.Button(cua_so, text="Danh dau hoan thanh", command=danh_dau_hoan_thanh).grid(
    row=3, column=0, padx=10, pady=10
)
tk.Button(cua_so, text="Xoa cong viec", command=xoa_cong_viec).grid(
    row=3, column=1, padx=10, pady=10
)
# Lưu ý: Ở dòng cuối có 2 dấu gạch dưới (__) ở mỗi bên chữ name và main
if __name__ == "__main__":
    cua_so.mainloop()