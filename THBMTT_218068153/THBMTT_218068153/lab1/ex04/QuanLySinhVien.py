from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien=[]
    
    def generateID(self):
        maxId = 1
        if(self.soLuongSV()>0):
            maxId=self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId<sv._id):
                    maxId=sv._id
            maxId=maxId+1
        return  maxId
    
    def soLuongSV(self):
        return self.listSinhVien.__len__()
    
    def nhapSV(self):
        svId=self.generateID()
        name=input("Nhap ten sinh vien: ")
        sex=input("Nhap gioi tinh sinh vien: ")
        major= input("Nhap chuyen nganh cua sinh vien: ")
        diemTB=float(input("Nhap diem cua sinh vien: "))
        sv=SinhVien(svId,name,sex,major,diemTB)
        self.XepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self,ID):
        sv=self.findByID(ID)
        if(sv!=None):
            name=input("Nhap ten sinh vien: ")
            sex=input("Nhap gioi tinh sinh vien: ")
            major= input("Nhap chuyen nganh cua sinh vien: ")
            diemTB=float(input("Nhap diem cua sinh vien: "))
            sv._name=name
            sv._sex=sex
            sv._major=major
            sv._demTB=diemTB
            self.XepLoaiHocLuc(sv)
        else:
            print("Sinh vien co  ID={} ko ton tai.".format(ID))
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x:x._id,reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name,reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._demTB,reverse=False)
    
    def findByID(self,ID):
        searchResult = None
        if (self.soLuongSV()>0):
            for sv in self.listSinhVien:
                if(sv._id==ID):
                    searchResult=sv
        return searchResult
    
    def findByName(self,keyword):
        listSV=[]
        if(self.soLuongSV()>0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self,ID):
        isDeleted=False
        sv=self.findByID(ID)
        if(sv!=None):
            self.listSinhVien.remove(sv)
            isDeleted=True
        return isDeleted
    
    def XepLoaiHocLuc(self,sv:SinhVien):
        if (sv._demTB>=8):
            sv._hocLuc="Gioi"
        elif (sv._demTB>=6.5):
            sv._hocLuc="Kha"
        elif (sv._demTB>=5):
            sv._hocLuc="Trung binh"
        else:
            sv._hocLuc="Yeu"
    
    def ShowSinhVien(self,listSV):
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("ID","Name","Sex","Major","DiemTB","Hoc Luc"))
        if(listSV.__len__()>0):
            for sv in listSV:
                print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name , sv._sex , sv._major , sv._demTB ,sv._hocLuc))
                print("\n")
                
    def getListSinhVien(self):
        return self.listSinhVien
        
            