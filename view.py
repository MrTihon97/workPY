
def typeofoperation():
    a = (input("Введите тип арифметики 0(комплекс) 1(целые): "))
    while a not in "01":
        print("неверный ввод")
        a = (input("Введите тип арифметики 0(комплекс) 1(целые): "))
    return a

def getop():
    op = input("Введите операцию: ")
    while op not in ['*', '/', '%', '//', '-', '+']:
        print("неверный ввод")
        op = input("Введите операцию: ")
    return op

def getincomplex():
    a = complex(input("Введите комплексное число а: "))
    b = complex(input("Введите комплексное число b: "))
    op = getop()
    return a, b, op

def getininteger():
    a = int(input("Введите целое число а: "))
    b = int(input("Введите целое число b: "))
    op = getop()
    return a, b, op

def printdata(data):
    print(data)
