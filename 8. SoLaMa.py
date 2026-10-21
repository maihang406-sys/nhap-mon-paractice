
def so_la_ma(so):
    if so == 10: return "X"
    if so == 9:  return "IX"
    if so == 8:  return "VIII"
    if so == 7:  return "VII"
    if so == 6:  return "VI"
    if so == 5:  return "V"
    if so == 4:  return "IV"
    return "I" * so  # 1,2,3

def so_thap_phan(so_la_ma):
    tong = 0
    for c in so_la_ma:
        if c == "I": tong += 1
        if c == "V": tong += 5
        if c == "X": tong += 10
    if "IV" in so_la_ma or "IX" in so_la_ma: tong -= 2
    return tong
if __name__ == "__main__":
    for i in range(1, 11):
        print(i, "->", so_la_ma(i))
    print(so_thap_phan("IX"))  # 9
    print(so_thap_phan("VIII")) # 8