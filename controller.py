import view
import operation

def calculator():
    optype = view.typeofoperation()
    if optype == "0":
        data = view.getincomplex()
    else:
        data = view.getininteger()
    if data[2] == "+":
        ab = (data[0],data[1])
        res = operation.summ((ab))
    if data[2] == "*":
        res = operation.mult((data[0], data[1]))
    if data[2] == "-":
        res = operation.sub((data[0], data[1]))
    if data[2] == "/":
        res = operation.div((data[0], data[1]))
    if data[2] == "//":
        if optype == "1":
            res = operation.divinteger((data[0], data[1]))
        else:
            print("Такая операция запрещена для комплексных чисел")
            return
    if data[2] == "%":
        if optype == "1":
            res = operation.modinteger((data[0], data[1]))
        else:
            print("Такая операция запрещена для комплексных чисел")
            return
    view.printdata(res)
