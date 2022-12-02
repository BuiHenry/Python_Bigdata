def thayTu(str1, str2, str3):
    print(str1.replace(str2, str3))


t = int(input("Nhập số lượng các dòng: "))
if 0 < t <= 100:
    for i in range(t):
        str1 = input("Nhập chuỗi: ")
        str2 = input("Nhập chuỗi cần thay thế: ")
        str3 = input("Nhập chuỗi từ thay thế: ")
        print(f"test {i + 1}:", end="\n")
        thayTu(s1, s2, s3)