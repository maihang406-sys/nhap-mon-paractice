try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    # Kiểm tra có phải tam giác hợp lệ không
    if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
        # Tam giác đều
        if a == b == c:
            print("Tam giác đều")
        # Tam giác vuông (kiểm tra định lý Pythagore)
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            if a == b or a == c or b == c:
                print("Tam giác vuông cân")
            else:
                print("Tam giác vuông")
        # Tam giác cân
        elif a == b or a == c or b == c:
            print("Tam giác cân")
        # Tam giác thường
        else:
            print("Tam giác thường")
    else:
        print("Ba cạnh không tạo thành một tam giác hợp lệ.")
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")