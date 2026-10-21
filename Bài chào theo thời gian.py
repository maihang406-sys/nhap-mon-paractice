try:
    gio = int(input("Nhập giờ trong ngày (0 - 23): "))

    # Kiểm tra và in lời chào phù hợp
    if 0 <= gio <= 12:
        print("Chào buổi sáng")
    elif 12 < gio < 17:
        print("Chào buổi chiều")
    elif 17 < gio <= 23:
        print("Chào buổi tối")
    else:
        print("Lỗi: Giờ không hợp lệ. Vui lòng nhập giá trị từ 0 đến 23.")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên.")