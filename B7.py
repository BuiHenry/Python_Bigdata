t = int(input("Nhập số lượng các dòng: "))
for i in range(1, t+1):
    words = [x for x in input("Nhập chuỗi: ").split()]
    m = set()
    print(f"Test {i}: ")
    for i in words :
        if i not in m:
            print(f'{i} ', end='')
            m.add(i)
    print()