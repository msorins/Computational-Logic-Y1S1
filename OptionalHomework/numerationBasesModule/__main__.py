__author__ = 'sorynsoo'

from numerationBasesModule.classes.numerationBases import *

numerationBasesObj = NumerationBases()


menu = [
    "",
    "---  MENU  ---",
    "1. Add two integer numbers",
    "2. Substract two integer numbers",
    "3. Multiply two integer numbers",
    "4. Divide two integer numbers",
    "5. Divide two integer numbers and get the remainder",
    "6. Rapid conversion (bases 2 - 4 - 16 or 4 - 16) of a rational numbers: ",
    "7. Convert to base 10 (successive divisions/multiplications) of a  rational number:",
    "8. Convert from base 10 (successive divisions/multiplications) of a  rational number:",
    "9. Convert directly from any base to any base (successive divisions/multiplications) of a rational number:",
    ""
]


while True:
    for crt in menu:
        print(crt)

    try:
        cmd = input("Command: ")
        if cmd == "1":
            #ADDITION
            a = numerationBasesObj.base16NumberToVector(input("First number: "))
            b = numerationBasesObj.base16NumberToVector(input("Second number: "))
            a = a["integer"]
            b = b["integer"]
            base = int(input("Base: "))
            print("Result: ", numerationBasesObj.vectorToBase16Number(numerationBasesObj.sum(a, b, base)))

        if cmd == "2":
            #SUBSTRACTION
            a = numerationBasesObj.base16NumberToVector(input("First number: "))
            b = numerationBasesObj.base16NumberToVector(input("Second number: "))
            a = a["integer"]
            b = b["integer"]
            base = int(input("Base: "))
            print("Result: ", numerationBasesObj.vectorToBase16Number(numerationBasesObj.sub(a, b, base)))

        if cmd == "3":
            #MULTIPLICATION
            a = numerationBasesObj.base16NumberToVector(input("First number: "))
            a = a["integer"]
            b = input("Second number: ")
            if b >= '0' and b <='9':
                b = int(b)
            else:
                if b >= 'A' and b <= 'F':
                    b = ord(b) - ord('A') + 10
                else:
                    raise RuntimeError("Invalid value, must be between 0 and F")

            base = int(input("Base: "))
            print("Result: ", numerationBasesObj.vectorToBase16Number(numerationBasesObj.prod(a, b, base)))

        if cmd == "4":
            #DIVISION
            a = numerationBasesObj.base16NumberToVector(input("First number: "))
            a = a["integer"]
            b = input("Second number: ")
            if b >= '0' and b <= '9':
                b = int(b)
            else:
                if b >= 'A' and b <= 'F':
                    b = ord(b) - ord('A') + 10
                else:
                    raise RuntimeError("Invalid value, must be between 0 and F")

            base = int(input("Base: "))
            print("Result: ", numerationBasesObj.vectorToBase16Number(numerationBasesObj.div(a, b, base)))

        if cmd == "5":
            #REMAINDER OF THE DIVISION
            a = numerationBasesObj.base16NumberToVector(input("First number: "))
            a = a["integer"]
            b = input("Second number: ")
            if b >= '0' and b <= '9':
                b = int(b)
            else:
                if b >= 'A' and b <= 'F':
                    b = ord(b) - ord('A') + 10
                else:
                    raise RuntimeError("Invalid value, must be between 0 and F")

            base = int(input("Base: "))
            res = numerationBasesObj.divR(a, b, base)
            if res < 10:
                print("Result: ", res)
            else:
                print("Result: ", chr(res+ord('A')-10))

        if cmd == "6":
            #RAPID CONVERSION
            a = numerationBasesObj.base16NumberToVector(input("Number: "))

            baseSrc = int(input("Source base: "))
            baseDst = int(input("Destination base: "))

            if(baseSrc < baseDst):
                res = numerationBasesObj.rapidConversionToHigherBase(a, baseSrc, baseDst)
            else:
                res = numerationBasesObj.rapidConversionToLowerBase(a, baseSrc, baseDst)

            print("Result: ", str(numerationBasesObj.vectorToBase16Number(res["integer"])) + "." + str(numerationBasesObj.vectorToBase16Number(res["fractional"])))

        if cmd == "7":
            # CONVERT TO BASE 10
            inputValue = input("Number: ",)
            try:
                a = float(inputValue)
            except Exception:
                a = numerationBasesObj.base16NumberToVector(inputValue)

            baseSrc = int(input("Source base: "))
            res = numerationBasesObj.convertToBase10(a, baseSrc)

            print("Result: ", str(numerationBasesObj.vectorToBase16Number(res["integer"])) + "." + str(numerationBasesObj.vectorToBase16Number(res["fractional"])))

        if cmd == "8":
            # CONVERT FROM BASE 10
            a = float(input("Number: "))
            baseDst = int(input("Destination base: "))

            res = numerationBasesObj.convertFromBase10(a, baseDst)

            print(str(numerationBasesObj.vectorToBase16Number(res["integer"])) + "." + str(numerationBasesObj.vectorToBase16Number(res["fractional"])))

        if cmd == "9":
            # CONVERT FROM ANY BASE TO BASE
            a = numerationBasesObj.base16NumberToVector(input("Number: "))
            baseSrc = int(input("Source base: "))
            baseDst = int(input("Destination base: "))

            if baseSrc < baseDst:
                res = numerationBasesObj.conversionToHigherBase(a, baseSrc, baseDst)
            else:
                res = numerationBasesObj.conversionToLowerBase(a, baseSrc, baseDst)


            print(str(numerationBasesObj.vectorToBase16Number(res["integer"])) + "." + str(numerationBasesObj.vectorToBase16Number(res["fractional"])))
    except ValueError as e:
        if e == "invalid literal for int() with base 10: 'e'":
            print("To many zecimals for this operation")
        else:
            print("Invalid value !")
    except Exception as e:
        print("There is something wrong with your value")