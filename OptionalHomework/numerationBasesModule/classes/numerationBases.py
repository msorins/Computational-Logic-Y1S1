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

        precision = 4
        i = 0
        while fractional != 0.0 and i < precision:
            fractional = fractional * 10
            convertedFractionalNumber.append(self.getInteger(fractional))
            fractional = round(fractional - self.getInteger(fractional), 4)
            i = i + 1

        return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}

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

    def getInteger(self, nr):
        return int(nr)

    def getFractional(self, nr):
        return round(nr - self.getInteger(nr), 4)

    def convertFromBase10(self, nr, baseDst):
        '''
        :param nr: number to be converted
        :param base:  destionation base
        :return: a dictionary containing two list (one with fractional and one with integer part)
        '''
        convertedIntegerNumber = []
        convertedFractionalNumber = []

        integer = self.getInteger(nr)
        fractional = self.getFractional(nr)

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
            fractional = self.getFractional(newRes)
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
                convertedIntegerNumber.append(binaryDigits[j])

        #Converting the fractional part
        for i in range(len(a["fractional"])):
            binaryDigits = self.convertFromBase10(a["fractional"][i], baseDst)
            binaryDigits = binaryDigits["integer"]
            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)

            for j in range(nrOfRepeats):
                convertedFractionalNumber.append(binaryDigits[j])


        return {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}

    def rapidConversionToHigherBase(self, a, baseSrc, baseDst):
        '''
        :param a: vector
        :param baseSrc: the source base
        :param baseDst: the destination base
        :return: a dictionary containing two list (one with fractional and one with integer part)
        '''
        pass

    def conversionToLowerBase(self, a, baseSrc, baseDst):
        pass

    def conversionToHigherBase(self, a, baseSrc, baseDst):
        pass