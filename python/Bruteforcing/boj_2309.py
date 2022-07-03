###일곱 난쟁이
def ps_2309():
    dwarf = []
    finding = False
    for i in range(9):
        dwarf.append(int(input()))

    height_diff = sum(dwarf) - 100
    for i in range(9):
        for j in range(i+1, 9):
            if dwarf[i]+dwarf[j] == height_diff:
                del dwarf[i]
                del dwarf[j-1]
                finding = True
                break

        if finding:
            break

    for n in sorted(dwarf):
        print(n)
