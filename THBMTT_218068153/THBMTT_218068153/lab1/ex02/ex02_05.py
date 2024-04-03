so_h_lam=float(input("Nhap so h lam moi tuan: "))
luong_h=float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
h_tieu_chuan=44
h_vuot_chuan=max(0,so_h_lam-h_tieu_chuan)
thuc_linh=h_tieu_chuan * luong_h + h_vuot_chuan * luong_h * 1.5
print(f"So tien thuc linh cua nhan vien: {thuc_linh}")
