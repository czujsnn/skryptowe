def sum(arg1,arg2):

    if type(arg1) is complex and type(arg2) is complex:
        return complex(arg1.real + arg2.real, arg1.imag + arg2.imag)

    return float(arg1) + float(arg2)

if __name__ == "__main__":

    suma = sum(2,1)
    print(suma) 

