import tkinter as tk


def bam_nut(gia_tri):
    noi_dung_hien_tai = bien_hien_thi.get()
    bien_hien_thi.set(noi_dung_hien_tai + str(gia_tri))


def tinh_ket_qua():
    try:
        bieu_thuc = bien_hien_thi.get()
        ket_qua = eval(bieu_thuc)
        bien_hien_thi.set(str(ket_qua))
    except:
        bien_hien_thi.set("Loi")


def xoa_man_hinh():
    bien_hien_thi.set("")


cua_so = tk.Tk()
cua_so.title("May tinh bo tui")

# Tang chieu rong de hien thi du 4 cot nut
cua_so.geometry("420x380")
cua_so.resizable(False, False)

bien_hien_thi = tk.StringVar()

entry_hien_thi = tk.Entry(
    cua_so,
    textvariable=bien_hien_thi,
    font=("Arial", 18),
    justify="right",
    width=22
)

entry_hien_thi.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=15
)


# Hang 1
tk.Button(
    cua_so,
    text="7",
    width=7,
    height=2,
    command=lambda: bam_nut(7)
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="8",
    width=7,
    height=2,
    command=lambda: bam_nut(8)
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="9",
    width=7,
    height=2,
    command=lambda: bam_nut(9)
).grid(row=1, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="/",
    width=7,
    height=2,
    command=lambda: bam_nut("/")
).grid(row=1, column=3, padx=5, pady=5)


# Hang 2
tk.Button(
    cua_so,
    text="4",
    width=7,
    height=2,
    command=lambda: bam_nut(4)
).grid(row=2, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="5",
    width=7,
    height=2,
    command=lambda: bam_nut(5)
).grid(row=2, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="6",
    width=7,
    height=2,
    command=lambda: bam_nut(6)
).grid(row=2, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="*",
    width=7,
    height=2,
    command=lambda: bam_nut("*")
).grid(row=2, column=3, padx=5, pady=5)


# Hang 3
tk.Button(
    cua_so,
    text="1",
    width=7,
    height=2,
    command=lambda: bam_nut(1)
).grid(row=3, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="2",
    width=7,
    height=2,
    command=lambda: bam_nut(2)
).grid(row=3, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="3",
    width=7,
    height=2,
    command=lambda: bam_nut(3)
).grid(row=3, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="-",
    width=7,
    height=2,
    command=lambda: bam_nut("-")
).grid(row=3, column=3, padx=5, pady=5)


# Hang 4
tk.Button(
    cua_so,
    text="0",
    width=7,
    height=2,
    command=lambda: bam_nut(0)
).grid(row=4, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="C",
    width=7,
    height=2,
    command=xoa_man_hinh
).grid(row=4, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="=",
    width=7,
    height=2,
    command=tinh_ket_qua
).grid(row=4, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="+",
    width=7,
    height=2,
    command=lambda: bam_nut("+")
    ).grid(row=4, column=3, padx=5, pady=5)


cua_so.mainloop()