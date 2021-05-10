def decimalParaHexadecimal( V ):
    hex = str()
    v = []
    while V >= 16:
        v.append(int(V%16))
        V = int(V/16)
    else:
        v.append(int(V))
        v.reverse()
        for i in range(len(v)):
            if v[i] == 0:
                hex += "0"
            elif v[i] == 1:
                hex += "1"
            elif v[i] == 2:
                hex += "2"
            elif v[i] == 3:
                hex += "3"
            elif v[i] == 4:
                hex += "4"
            elif v[i] == 5:
                hex += "5"
            elif v[i] == 6:
                hex += "6"
            elif v[i] == 7:
                hex += "7"
            elif v[i] == 8:
                hex += "8"
            elif v[i] == 9:
                hex += "9"
            elif v[i] == 10:
                hex += "A"
            elif v[i] == 11:
                hex += "B"
            elif v[i] == 12:
                hex += "C"
            elif v[i] == 13:
                hex += "D"
            elif v[i] == 14:
                hex += "E"
            elif v[i] == 15:
                hex += "F"
    return hex

if __name__ == '__main__':
    V = input()
    hex = decimalParaHexadecimal(int(V))
    print(hex)
