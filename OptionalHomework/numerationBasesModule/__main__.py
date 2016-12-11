__author__ = 'sorynsoo'

from numerationBasesModule.classes.numerationBases import *

numerationBasesObj = NumerationBases()


menu = [
    "",
    "---  MENU  ---",
    "1. Add two numbers",
    "2. Substract two numbers",
    "3. Multiply two numbers",
    "4. Divide two numbers",
    "5. Get reminder from the division of two numbers",
    "6. Rapid conversion (bases 2 - 4 - 16 or 4 - 16) - rational numbers: ",
    "7. Convert to base 10 (successive divisions/multiplications) - rational numbers:",
    "8. Convert from base 10 (successive divisions/multiplications) - rational numbers:",
    "9. Convert directly from any base to any base (successive divisions/multiplications) - rational numbers:",
    ""
]


numerationBasesObj.conversionToHigherBase(10111.1011, 2, 8)


while True:
    for crt in menu:
        print(crt)

    try:
        cmd = input("Command: ")
        if cmd == "1":
            #ADDITION
            a = numerationBasesObj.numberToVector(int(input("First number: ")))
            b = numerationBasesObj.numberToVector(int(input("Second number: ")))
            a = a["integer"]
            b = b["integer"]
            base = int(input("Base: "))
            print(numerationBasesObj.vectorToNumber(numerationBasesObj.sum(a, b, base)))

        if cmd == "2":
            #SUBSTRACTION
            a = numerationBasesObj.numberToVector(int(input("First number: ")))
            b = numerationBasesObj.numberToVector(int(input("Second number: ")))
            a = a["integer"]
            b = b["integer"]
            base = int(input("Base: "))
            print(numerationBasesObj.vectorToNumber(numerationBasesObj.sub(a, b, base)))

        if cmd == "3":
            #MULTIPLICATION
            a = numerationBasesObj.numberToVector(int(input("First number: ")))
            b = int(input("Second number: "))
            a = a["integer"]

            base = int(input("Base: "))
            print(numerationBasesObj.vectorToNumber(numerationBasesObj.prod(a, b, base)))

        if cmd == "4":
            #DIVISION
            a = numerationBasesObj.numberToVector(int(input("First number: ")))
            b = int(input("Second number: "))
            a = a["integer"]

            base = int(input("Base: "))
            print(numerationBasesObj.vectorToNumber(numerationBasesObj.div(a, b, base)))

        if cmd == "5":
            #REMAINDER OF THE DIVISION
            a = numerationBasesObj.numberToVector(int(input("First number: ")))
            b = int(input("Second number: "))
            a = a["integer"]

            base = int(input("Base: "))
            print(numerationBasesObj.divR(a, b, base))

        if cmd == "6":
            #RAPID CONVERSION
            a = numerationBasesObj.numberToVector(float(input("Number: ")))

            baseSrc = int(input("Source base: "))
            baseDst = int(input("Destination base: "))

            if(baseSrc < baseDst):
                res = numerationBasesObj.rapidConversionToHigherBase(a, baseSrc, baseDst)
            else:
                res = numerationBasesObj.rapidConversionToLowerBase(a, baseSrc, baseDst)

            print(str(numerationBasesObj.vectorToNumber(res["integer"])) + "." + str(numerationBasesObj.vectorToNumber(res["fractional"])))

        if cmd == "7":
            # CONVERT TO BASE 10
            a = float(input("Number: "))
            baseSrc = int(input("Source base: "))

            res = numerationBasesObj.convertToBase10(a, baseSrc)

            print(str(numerationBasesObj.vectorToNumber(res["integer"])) + "." + str(numerationBasesObj.vectorToNumber(res["fractional"])))

        if cmd == "8":
            # CONVERT FROM BASE 10
            a = float(input("Number: "))
            baseDst = int(input("Destination base: "))

            res = numerationBasesObj.convertFromBase10(a, baseDst)

            print(str(numerationBasesObj.vectorToNumber(res["integer"])) + "." + str(numerationBasesObj.vectorToNumber(res["fractional"])))

        if cmd == "9":
            # CONVERT FROM ANY BASE TO BASE
            a = float(input("Number: "))
            baseSrc = int(input("Source base: "))
            baseDst = int(input("Destination base: "))

            if baseSrc < baseDst:
                res = numerationBasesObj.conversionToHigherBase(a, baseSrc, baseDst)
            else:
                res = numerationBasesObj.conversionToLowerBase(a, baseSrc, baseDst)


            print(str(numerationBasesObj.vectorToNumber(res["integer"])) + "." + str(numerationBasesObj.vectorToNumber(res["fractional"])))
    except ValueError as e:
        print("Invalid value !")