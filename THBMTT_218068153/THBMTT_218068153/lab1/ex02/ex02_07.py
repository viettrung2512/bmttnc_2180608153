print("Nhap cac dong van ban (Nhap 'done' de ket thuc): ")
lines=[]
while(True):
    line=input()
    if line.lower()=='done':
        break
    lines.append(line)

print("\nCac donng da nhap sau khi chuyen thanh chu hoa: ")
for line in lines:
    print(line.upper())