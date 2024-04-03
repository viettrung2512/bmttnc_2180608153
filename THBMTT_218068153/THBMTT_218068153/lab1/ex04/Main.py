from QuanLySinhVien import QuanLySinhVien

qlsv=QuanLySinhVien()
while(1==1):
    print("\n CHUONG TRINH QLSV")
    print("********************************MENU************************************************")
    print("1. Them Sinh Vien")
    print("2. Cap nhat thong tin sinh vien boi ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    key=int(input("Nhap tuy chon: "))
    if(key==1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSV()
        print("\n Them sinh vien thanh cong!")
    elif (key==2):
        if(qlsv.soLuongSV()>0):
            print("\n2. Cap Nhat Thong Tinh Sinh Vien.")
            print("\nNhap ID: ")
            ID=int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\n Ko tim thay hoac danh sach rong!")

    elif(key==3):
        if(qlsv.soLuongSV()>0):
            print("\n3. Xoa Sinh Vien.")
            print("\nNhap ID: ")
            ID= int(input())
            if(qlsv.deleteById(ID)):
                print("\n Sinh vien co Id=",ID," da bi xoa")
            else:
                print("\nSinh Vien co id=",ID," ko ton tai")  
        else:
            print("\nSanh sach sinh vien trong!")
    elif(key==4):
        if(qlsv.soLuongSV()>0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name=input()
            kq=qlsv.findByName(name)
            qlsv.ShowSinhVien(kq)
        else:
            print("\n Danh Sach sinh vien trong!")
    elif(key==5):
        if(qlsv.soLuongSV()>0):
            print("\n5. Sap Xep sinh vien theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.ShowSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh Sach sinh vien trong!")
    elif(key==6):
        if(qlsv.soLuongSV()>0):
              print("\n5. Sap Xep sinh vien theo ten.")
              qlsv.sortByName()
              qlsv.ShowSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh Sach sinh vien trong!")
    elif(key==7):
        if(qlsv.soLuongSV()>0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.ShowSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach Sinh Vien trong!")
    elif(key==0):
        print("\n Ban da chon thoat chuong trinh!")
        break
    else:
        print("\nKo co chuc nang nay!")
        print("\nHay chon chuc nang trong menu")
            
              