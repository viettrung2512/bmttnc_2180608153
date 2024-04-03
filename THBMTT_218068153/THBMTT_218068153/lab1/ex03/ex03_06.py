def xoa_phan_tu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    return False

my_dict={'a':1,'b':2,'c':3,'d':4}

key_to_delete ='b'

kq= xoa_phan_tu(my_dict,key_to_delete)
if kq:
    print("Phan tu da duoc xoa tu Dictionary:",my_dict)
else:
    print("Ko tim thay phan tu can xoa trong Dictionary.")