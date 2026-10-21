

def gop(ds1, ds2):
    """Gộp 2 danh sách (có thể trùng)"""
    ket_qua = []
    for x in ds1:
        ket_qua.append(x)
    for x in ds2:
        ket_qua.append(x)
    return ket_qua

def giao(ds1, ds2):
    """Giao của 2 danh sách - chỉ lấy phần tử chung, không trùng"""
    ket_qua = []
    for x in ds1:
        if x in ds2 and x not in ket_qua:
            ket_qua.append(x)
    return ket_qua

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print(gop(a, b))      # [1, 2, 3, 4, 3, 4, 5, 6]
    print(giao(a, b))     # [3, 4]
