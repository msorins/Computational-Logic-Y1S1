import math

__author__ = 'sorynsoo'

class NumerationBases():
    def __init__(self):
        pass

    def sum(self, a, b, base):
        '''
        :param a: vector
        :param b: vector
        :param base: numeration base
        :return: a vector containing the sum of a and b
        '''
        result = []
        t = 0
        for i in range(len(a) - len(b)):
            b.append(0)

        for i in range(len(b) - len(a)):
            a.append(0)

        for i in range(max(len(a), len(b))):
            result.append((a[i] + b[i] + t)%base)
            t = (a[i] + b[i] + t) // base

        if t:
            result.append(t)

        return result

    def sub(self, a, b, base):
        '''
        :param a: vector (is greater than b)
        :param b: vector
        :param base: numeration base
        :return: a vector containing the substraction of a and b
        '''
        result = []
        t = 0

        for i in range(len(a) - len(b)):
            b.append(0)

        for i in range(max(len(a), len(b))):
            newRes = a[i] - b[i] - t

            if newRes < 0:
                t = 1
                newRes = newRes + base
            else:
                t = 0

            result.append(newRes)

        while result[len(result) -1] == 0:
            result.pop(len(result) - 1)

        return result

    def prod(self, a, nr, base):
        '''
        :param a: vector
        :param nr: a number with 1 digit in specified base
        :param base: numeration base
        :return: a vector containing the multiplication of a with base
        '''
        result = []
        t = 0

        for i in range(len(a)):
            newRes = a[i] * nr + t

            result.append(newRes % base)
            t = newRes // base

        while t:
            result.append(t % base)
            t = t // base

        return result

    def prodP(self, a, nr, base):
        '''
        :param a: vector
        :param nr: a number with 1 digit in specified base
        :param base: numeration base
        :return: return the extra digit
        '''
        result = []
        t = 0

        for i in range(len(a)):
            newRes = a[i] * nr + t
            t = newRes // base

        return t

    def div(self, a, nr, base):
        '''
        :param a: vector
        :param nr: a number with 1 digit in specified base
        :param base: numeration base
        :return: a vector containing the result of a / nr
        '''

        result = []
        t = 0

        for i in range(len(a)-1, -1, -1):
            t = t * base + a[i]
            newRes = t // nr
            result.append(newRes)
            t = t % nr

        while len(result) and result[0] == 0:
            result.pop(0)

        return result[::-1]

    def divR(self, a, nr, base):
        '''
        :param a: vector
        :param nr: a number with 1 digit in specified base
        :param base: numeration base
        :return: the rest of the division
        '''
        t = 0

        for i in range(len(a)-1, -1, -1):
            t = t * base + a[i]
            t = t % nr

        return t

    def numberToVector(self, nr):
        '''
        :param nr: a number in any base
        :return: a vector containing its digits in reverse order
        '''

        convertedIntegerNumber = []
        convertedFractionalNumber = []

        integer = self.getInteger(nr)
        fractional = self.getFractional(nr)

        while integer:
            convertedIntegerNumber.append(integer % 10)
            integer = integer // 10

        while fractional != 0:
            convertedFractionalNumber.append(fractional % 10)
            fractional = fractional // 10


        return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}

    def vectorToNumber(self, a):
        '''
        :param a: vector
        :return: a number contained by the vector
        '''
        nr = 0

        a = a[::-1]

        for i in range(len(a)):
            nr = nr * 10 + a[i]

        return nr

    def vectorToSubunitaryNumber(self, a):
        '''
        :param a: a vector containing a subunitary number
        :return: the subunitary number in float type
        '''
        p = 10
        res = 0
        counter = 0
        for crt in range(len(a) - 1, -1, -1):
            res = res + int(a[crt]) / p
            p *= 10
            counter += 1
            if counter >= 4:
                break

        return res

    def getInteger(self, nr):
        return int(nr)

    def getFractional(self, nr):
        if nr == int(nr):
            return 0

        splitNr = str(nr).split('.')
        fractional = int(splitNr[1])

        return fractional

    def getFractionalString(self, nr):
        if nr == int(nr):
            return 0

        splitNr = str(nr).split('.')
        fractional = splitNr[1]

        return fractional

    def removeInteger(self, nr):
        nr = str(nr).split('.')
        nr = nr[1]

        p = 10
        res = 0
        for crt in nr:
            res = res + int(crt) / p
            p *= 10

        return res

    def convertFromBase10(self, nr, baseDst):
        '''
        :param nr: number to be converted
        :param base:  destionation base
        :return: a dictionary containing two list (one with fractional and one with integer part)
        '''
        convertedIntegerNumber = []
        convertedFractionalNumber = []

        integer = self.getInteger(nr)
        fractional = self.removeInteger(nr)

        #Converting the integer part
        while integer != 0:
            convertedIntegerNumber.append(integer % baseDst)
            integer = integer // baseDst

        #Converting the fractional part
        maxDigits = 32
        crtDigits = 0
        while fractional != 0.0 and crtDigits < maxDigits:
            newRes = fractional * baseDst
            convertedFractionalNumber.append(self.getInteger(newRes))
            fractional = self.removeInteger(newRes)
            crtDigits = crtDigits + 1


        return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}

    def convertToBase10(self, nr, baseSrc):
         '''
         Substitution Method
         :param nr: number to be converted
         :param baseSrc: the destination base
         :return: a dictionary containing two list (one with fractional and one with integer part)
         '''

         convertedIntegerNumber = []
         convertedFractionalNumber = []

         integer = self.getInteger(nr)
         fractional = self.getFractional(nr)


         #Converting the integer part
         resInteger = 0
         power = 1
         while integer:
             resInteger = resInteger + (integer%10) * power
             power = baseSrc *  power
             integer = integer // 10

         convertedIntegerNumber = self.numberToVector(resInteger)
         convertedIntegerNumber = convertedIntegerNumber["integer"]


         #Converting the fractional part
         resFractional = 0
         power = 1 / baseSrc

         #Inverse the fractional part
         aux = self.numberToVector(fractional)
         aux = aux["fractional"]
         aux = aux[::-1]
         fractional = self.vectorToNumber(aux)

         while fractional:
             resFractional = resFractional + (fractional%10)*power
             power = power * 1 / baseSrc
             fractional = fractional // 10

         return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}

    def rapidConversionToLowerBase(self, a, baseSrc, baseDst):
        '''
        :param a: vector
        :param baseSrc: the source base
        :param baseDst: the destination base
        :return: a dictionary containing two list (one with fractional and one with integer part)
        '''

        if baseSrc == 16 and baseDst != 4 and baseDst != 2:
            raise RuntimeError("Combination of bases is not corect. Must be 16 -> 4 or 16 -> 2")

        if baseSrc == 8 and baseDst != 2:
            raise RuntimeError("Combination of bases is not corect. Must be 8 -> 2")

        if baseSrc == 4 and baseDst != 2:
            raise RuntimeError("Combination of bases is not corect. Must be 4 -> 2")

        convertedIntegerNumber = []
        convertedFractionalNumber = []

        nrOfRepeats = int(math.log(baseSrc, baseDst))

        #Converting the integer part
        for i in range(len(a["integer"])):
            binaryDigits = self.convertFromBase10(a["integer"][i], baseDst)
            binaryDigits = binaryDigits["integer"]
            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)

            for j in range(nrOfRepeats):
                convertedIntegerNumber.insert(0, binaryDigits[j])

        #Converting the fractional part
        for i in range(len(a["fractional"])-1, -1, -1):
            binaryDigits = self.convertFromBase10(a["fractional"][i], baseDst)
            binaryDigits = binaryDigits["integer"]
            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)
            binaryDigits = binaryDigits[::-1]
            for j in range(nrOfRepeats):
                convertedFractionalNumber.append(binaryDigits[j])


        return {"integer": convertedIntegerNumber[::-1], "fractional": convertedFractionalNumber[::-1]}

    def rapidConversionToHigherBase(self, a, baseSrc, baseDst):
        '''
        :param a: vector
        :param baseSrc: the source base
        :param baseDst: the destination base
        :return: a dictionary containing two list (one with fractional and one with integer part)
        '''

        if baseSrc == 2 and baseDst != 4 and  baseDst != 8 and baseDst != 16:
            raise RuntimeError("Combination of bases is not corect. Must be 2 -> 4 or 2 -> 8 or 2 -> 16")

        if baseSrc == 4 and baseDst != 16:
            raise RuntimeError("Combination of bases is not corect. Must be 4 -> 16")


        convertedIntegerNumber = []
        convertedFractionalNumber = []

        nrOfRepeats = int(math.log(baseDst, baseSrc))

        #Converting the integer part
        i = 0
        while i < len(a["integer"]):
            binaryDigits = a["integer"][i:i+nrOfRepeats]

            #binaryDigits = binaryDigits[::-1]
            nrBinaryDigits = self.vectorToNumber(binaryDigits) # Convert it to a vector
            nrBinaryDigits = self.convertToBase10(nrBinaryDigits, 2) # Convert the vector in base 10
            nrBinaryDigits = self.vectorToNumber(nrBinaryDigits["integer"]) # Convert the vector in base 10
            convertedIntegerNumber.append(nrBinaryDigits)

            i = i + nrOfRepeats


        i = 0
        while i < len(a["fractional"]):
            binaryDigits = a["fractional"][i:i+nrOfRepeats]

            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)

            binaryDigits = binaryDigits[::-1]
            nrBinaryDigits = self.vectorToNumber(binaryDigits) # Convert it to a vector
            nrBinaryDigits = self.convertToBase10(nrBinaryDigits, 2) # Convert the vector in base 10
            nrBinaryDigits = self.vectorToNumber(nrBinaryDigits["integer"]) # Convert the vector in base 10
            convertedFractionalNumber.append(nrBinaryDigits)

            i = i + nrOfRepeats

        return {"integer": convertedIntegerNumber[::-1], "fractional": convertedFractionalNumber[::-1]}

    def conversionToLowerBase(self, nr, baseSrc, baseDst):
        '''
        :param nr: number to be converted
        :param base:  destionation base
        :return: a dictionary containing two list (one with fractional and one with integer part)
        '''
        convertedIntegerNumber = []
        convertedFractionalNumber = []

        a = self.numberToVector(nr)
        integer = a["integer"]
        fractional = a["fractional"]

        #Converting the integer part
        while len(integer):
            rest = self.divR(integer, baseDst, baseSrc)
            quotent = self.div(integer, baseDst, baseSrc)

            convertedIntegerNumber.append(rest)
            integer = quotent

        #Converting the fractional part
        maxDigits = 4
        crtDigits = 0
        while len(fractional)  and crtDigits < maxDigits:
            integerDigit = self.prodP(fractional, baseDst, baseSrc)
            newFractional = self.prod(fractional, baseDst, baseSrc)

            convertedFractionalNumber.append(integerDigit)

            if(len(newFractional) > len(fractional)):
                newFractional.pop(len(newFractional)-1)

            fractional = newFractional
            crtDigits = crtDigits + 1


        return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}

    def conversionToHigherBase(self, nr, baseSrc, baseDst):
         '''
         Substitution Method
         :param nr: number to be converted
         :param baseSrc: the destination base
         :return: a dictionary containing two list (one with fractional and one with integer part)
         '''

         convertedIntegerNumber = []
         convertedFractionalNumber = []

         a = self.numberToVector(nr)
         integer = a["integer"]
         fractional = a["fractional"]

         #Converting the integer part
         power = 1

         for i in range(len(integer)):
             crtPower = self.numberToVector(power)
             crtPower = crtPower["integer"]
             crtProd = self.prod(crtPower, integer[i], baseDst)

             convertedIntegerNumber = self.sum(convertedIntegerNumber, crtProd, baseDst)

             power = self.prod(crtPower, baseSrc, baseDst)
             power = self.vectorToNumber(power)


         #Converting the fractional part
         powerHeins = 1 / baseSrc
         power = powerHeins
         power = self.convertFromBase10(power, baseDst)
         power = self.vectorToSubunitaryNumber(power["fractional"])

         for i in range(len(fractional)-1, -1, -1):
             crtFractional = self.numberToVector(fractional[i])
             crtFractional = crtFractional["integer"]


             if len(crtFractional) != 0:
                crtProd = self.prod(crtFractional, power, baseDst)
                crtProd = self.convertRationalToInteger(crtProd[0], 4)

                convertedFractionalNumber = self.sum(convertedFractionalNumber, crtProd, baseDst)



             powerHeins = powerHeins / baseSrc
             power = powerHeins
             power = self.convertFromBase10(power, baseDst)
             power = self.vectorToSubunitaryNumber(power["fractional"])




         return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}

    def convertRationalToInteger(self,a, precision):
        '''
        :param a: a rational number
        :return: the fractionary part as an integer
        '''

        res = []

        nr = self.getFractionalString(a)
        for crt in nr:
            res.append(int(crt))

        for i in range(precision-len(res)):
            res.append(0)

        return res[::-1]