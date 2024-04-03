def chia_het_cho_5(bin):
    demicial=int(bin,2)
    if demicial%5==0: 
        return True
    else:
        return False
    
chuoi_so_nhi_phan=input("Nhap so chuoi nhi phan (Phan tach boi dau phay): ")

# print(chuoi_so_nhi_phan)

so_nhi_phan_list=chuoi_so_nhi_phan.split(',')

# print(so_nhi_phan_list)

so_chia_het_cho_5=[so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5)>0:
    kq=','.join(so_chia_het_cho_5)
    print("Cac so chia het cho 5 la: ",kq)
else:
    print("Ko co so nhin phan nao chia het cho 5 trong chuoi da nhap.")