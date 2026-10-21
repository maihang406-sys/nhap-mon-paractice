
def nguyen_am(s):
    nguyen_am_set = set()
    for c in s.lower():
        if c in 'aiueo':
            nguyen_am_set.add(c)
    return list(nguyen_am_set)

def phu_am(s):
    phu_am_set = set()
    for c in s.lower():
        if c.isalpha() and c not in 'aiueo':
            phu_am_set.add(c)
    return list(phu_am_set)

def nguyen_am_tieng_viet(s):
    bang_nguyen_am = "aáàảãạăắằẳẵặâấầẩẫậeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵ"
    ket_qua = set()
    for c in s:
        if c.lower() in bang_nguyen_am:
            ket_qua.add(c)
    return list(ket_qua)

if __name__ == "__main__":
    print(nguyen_am("python"))                    
    print(phu_am("python"))                       
    print(nguyen_am_tieng_viet("ngôn ngữ python"))
