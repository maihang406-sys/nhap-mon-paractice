
from itertools import permutations, product

def chinh_hop(*so):
    ds = list(so)
    for p in permutations(ds):
        print(list(p), end=", ")
    print()


def chinh_hop_trung(*so):
    ds = list(so)
    for p in product(ds, repeat=len(ds)):
        print(list(p), end=", ")
    print()

def chinh_hop_input_trung(*so):
    ds = list(so)
    for p in product(ds, repeat=len(ds)):
        if len(set(p)) == len(ds):  # chỉ lấy những tổ hợp có đủ các giá trị gốc (không thiếu)
            print(list(p), end=", ")
    print()


if __name__ == "__main__":
    print("Chỉnh hợp không lặp:")
    chinh_hop(2, 3, 4)
    
    print("\nChỉnh hợp có lặp:")
    chinh_hop_trung(2, 3, 4)
    
    print("\nChỉnh hợp input có trùng:")
    chinh_hop_input_trung(2, 2, 3)



