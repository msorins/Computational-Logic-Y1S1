import math
import re
__author__ <- 'sorynsoo'
CLASS NumerationBases():
    FUNCTION __init__(self):
        pass
    ENDFUNCTION

    FUNCTION sum(self, a, b, base):
        '''
        :param a: vectOR
        :param b: vectOR
        :param base: numeration base
        :return: a vector containing the sum of a AND b
        '''
        result <- []
        t <- 0
        for i in range(len(a) - len(b)):
            b.append(0)
        ENDFOR
        for i in range(len(b) - len(a)):
            a.append(0)
        ENDFOR
        for i in range(max(len(a), len(b))):
            result.append((a[i] + b[i] + t)%base)
            t <- (a[i] + b[i] + t) // base
        ENDFOR
        IF t:
            result.append(t)
        ENDIF
        RETURN result
    ENDFUNCTION

    FUNCTION sub(self, a, b, base):
        '''
        :param a: vector (is greater than b)
        :param b: vectOR
        :param base: numeration base
        :return: a vector containing the substraction of a AND b
        '''
        result <- []
        t <- 0
        for i in range(len(a) - len(b)):
            b.append(0)
        ENDFOR
        for i in range(max(len(a), len(b))):
            newRes <- a[i] - b[i] - t
            IF newRes < 0:
                t <- 1
                newRes <- newRes + base
            ELSE:
                t <- 0
            ENDIF
            result.append(newRes)
        ENDFOR
        while result[len(result) -1] = 0:
            result.pop(len(result) - 1)
        ENDWHILE
        RETURN result
    ENDFUNCTION

    FUNCTION prod(self, a, nr, base):
        '''
        :param a: vectOR
        :param nr: a number with 1 digit in specified base
                                                ENDIF
        :param base: numeration base
        :return: a vector containing the multiplication of a with base
        '''
        result <- []
        t <- 0
        for i in range(len(a)):
            newRes <- a[i] * nr + t
            result.append(newRes % base)
            t <- newRes // base
        ENDFOR
        while t:
            result.append(t % base)
            t <- t // base
        ENDWHILE
        RETURN result
    ENDFUNCTION

    FUNCTION prodP(self, a, nr, base):
        '''
        :param a: vectOR
        :param nr: a number with 1 digit in specified base
                                                ENDIF
        :param base: numeration base
        :return: return the extra digit
        '''
        result <- []
        t <- 0
        for i in range(len(a)):
            newRes <- a[i] * nr + t
            t <- newRes // base
        ENDFOR
        RETURN t
    ENDFUNCTION

    FUNCTION div(self, a, nr, base):
        '''
        :param a: vectOR
        :param nr: a number with 1 digit in specified base
                                                ENDIF
        :param base: numeration base
        :return: a vector containing the result of a / nr
        '''
        result <- []
        t <- 0
        for i in range(len(a)-1, -1, -1):
            t <- t * base + a[i]
            newRes <- t // nr
            result.append(newRes)
            t <- t % nr
        ENDFOR
        while len(result) AND result[0] = 0:
            result.pop(0)
        ENDWHILE
        RETURN result[::-1]
    ENDFUNCTION

    FUNCTION divR(self, a, nr, base):
        '''
        :param a: vectOR
        :param nr: a number with 1 digit in specified base
                                                ENDIF
        :param base: numeration base
        :return: the rest of the division
        '''
        t <- 0
        for i in range(len(a)-1, -1, -1):
            t <- t * base + a[i]
            t <- t % nr
        ENDFOR
        RETURN t
    ENDFUNCTION

    FUNCTION base16NumberToVector(self, nr):
        '''
        :param nr: a string
        :return: a vector containing its digits in reverse order
        '''
        matcher <- re.compile(r"^[0-9A-F]+$")
        matcher2 <- re.compile(r"^[0-9A-F]+[.][0-9A-F]+$")
        convertedIntegerNumber <- []
        convertedFractionalNumber <- []
        IF matcher.match(nr):
            integerPart <- nr
            for i in range(len(integerPart) - 1, -1, -1):
                IF integerPart[i] >= '0' AND integerPart[i] <= '9':
                    convertedIntegerNumber.append(int(integerPart[i]))
                ELSE:
                    convertedIntegerNumber.append(ord(integerPart[i]) - ord('A') + 10)
                ENDIF
            ENDFOR
            RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}
        ENDIF
        IF matcher2.match(nr):
            nr <- nr.split('.')
            integerPart <- nr[0]
            fractionalPart <- nr[1]
            for i in range(len(integerPart) - 1, -1, -1):
                IF integerPart[i] >= '0' AND integerPart[i] <= '9':
                    convertedIntegerNumber.append(int(integerPart[i]))
                ELSE:
                    convertedIntegerNumber.append(ord(integerPart[i]) - ord('A') + 10)
                ENDIF
            ENDFOR
            for i in range(len(fractionalPart) - 1, -1, -1):
                IF fractionalPart[i] >= '0' AND fractionalPart[i] <= '9':
                    convertedFractionalNumber.append(int(fractionalPart[i]))
                ELSE:
                    convertedFractionalNumber.append(ord(fractionalPart[i]) - ord('A') + 10)
                ENDIF
            ENDFOR
            RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}
        ENDIF
        raise RuntimeError("Input is not valid")
    ENDFUNCTION

    FUNCTION numberToVector(self, nr):
        '''
        :param nr: a number in any base
        :return: a vector containing its digits in reverse order
        '''
        convertedIntegerNumber <- []
        convertedFractionalNumber <- []
        integer <-  getInteger(nr)
        fractional <-  getFractional(nr)
        while integer:
            convertedIntegerNumber.append(integer % 10)
            integer <- integer // 10
        ENDWHILE
        while fractional != 0:
            convertedFractionalNumber.append(fractional % 10)
            fractional <- fractional // 10
        ENDWHILE
        RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}
    ENDFUNCTION

    FUNCTION vectorToNumber(self, a):
        '''
        :param a: vectOR
        :return: a number contained by the vectOR
        '''
        nr <- 0
        a <- a[::-1]
        for i in range(len(a)):
            nr <- nr * 10 + a[i]
        ENDFOR
        RETURN nr
    ENDFUNCTION

    FUNCTION vectorToSubunitaryNumber(self, a):
        '''
        :param a: a vector containing a subunitary number
        :return: the subunitary number in float type
        '''
        p <- 10
        res <- 0
        counter <- 0
        for crt in range(len(a) - 1, -1, -1):
            res <- res + int(a[crt]) / p
            p *= 10
            counter += 1
            IF counter >= 4:
                break
            ENDIF
        ENDFOR
        RETURN res
    ENDFUNCTION

    FUNCTION vectorToBase16Number(self, a):
        '''
        :param a: a vectOR
        :return: a string containing the number in base 16
        '''
        res <- ''
        a <- a[::-1]
        for i in range(len(a)):
            IF a[i] < 10:
                res <- res + str(a[i])
            ELSE:
                res <- res + chr(a[i]+ord('A')-10)
            ENDIF
        ENDFOR
        RETURN res
    ENDFUNCTION

    FUNCTION getInteger(self, nr):
        RETURN int(nr)
    ENDFUNCTION

    FUNCTION getFractional(self, nr):
        IF nr = int(nr):
            RETURN 0
        ENDIF
        splitNr <- str(nr).split('.')
        fractional <- int(splitNr[1])
        RETURN fractional
    ENDFUNCTION

    FUNCTION getFractionalString(self, nr):
        IF nr = int(nr):
            RETURN 0
        ENDIF
        splitNr <- str(nr).split('.')
        fractional <- splitNr[1]
        RETURN fractional
    ENDFUNCTION

    FUNCTION removeInteger(self, nr):
        IF str(nr).find('.') = -1:
            RETURN 0
        ENDIF
        nr <- str(nr).split('.')
        nr <- nr[1]
        p <- 10
        res <- 0
        for crt in nr:
            res <- res + int(crt) / p
            p *= 10
        ENDFOR
        RETURN res
    ENDFUNCTION

    FUNCTION convertFromBase10(self, nr, baseDst):
        '''
        Successive divisions / multiplications8
        :param nr: number to be converted
        :param base:  destionation base
        :return: a dictionary containing two list (one with fractional AND one with integer part)
        '''
        convertedIntegerNumber <- []
        convertedFractionalNumber <- []
        integer <-  getInteger(nr)
        fractional <-  removeInteger(nr)
        #Converting the integer part
        while integer != 0:
            convertedIntegerNumber.append(integer % baseDst)
            integer <- integer // baseDst
        #Converting the fractional part
        ENDWHILE
        maxDigits <- 32
        crtDigits <- 0
        while fractional != 0.0 AND crtDigits < maxDigits:
            newRes <- fractional * baseDst
            convertedFractionalNumber.append( getInteger(newRes))
            fractional <-  removeInteger(newRes)
            crtDigits <- crtDigits + 1
        ENDWHILE
        RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}
    ENDFUNCTION

    FUNCTION convertToBase10(self, nr, baseSrc):
         '''
         Substitution Method
         :param nr: number to be converted
         :param baseSrc: the destination base
         :return: a dictionary containing two list (one with fractional AND one with integer part)
         '''
         #If the input number is in a base greater than 10 i can better use the convertToLower OR Higher Base (which basically does the same thing -> Substitution Method )
         IF(type(nr) is not int AND type(nr) is not float):
             IF baseSrc > 10:
                 RETURN  conversionToLowerBase(nr, baseSrc, 10)
             ELSE:
                 RETURN  conversionToHigherBase(nr, baseSrc, 10)
         ENDIF
             ENDIF
         convertedIntegerNumber <- []
         convertedFractionalNumber <- []
         integer <-  getInteger(nr)
         fractional <-  getFractional(nr)
         #Converting the integer part
         resInteger <- 0
         power <- 1
         while integer:
             resInteger <- resInteger + (integer%10) * power
             power <- baseSrc *  power
             integer <- integer // 10
         ENDWHILE
         convertedIntegerNumber <-  numberToVector(resInteger)
         convertedIntegerNumber <- convertedIntegerNumber["integer"]
         #Converting the fractional part
         resFractional <- 0
         power <- 1 / baseSrc
         #Inverse the fractional part
         aux <-  numberToVector(fractional)
         aux <- aux["integer"]
         aux <- aux[::-1]
         fractional <-  vectorToNumber(aux)
         while fractional:
             resFractional <- resFractional + (fractional%10)*power
             power <- power * (1 / baseSrc)
             fractional <- fractional // 10
         ENDWHILE
         convertedFractionalNumber <-  numberToVector(resFractional)
         convertedFractionalNumber <- convertedFractionalNumber["fractional"]
         RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}
    ENDFUNCTION

    FUNCTION rapidConversionToLowerBase(self, a, baseSrc, baseDst):
        '''
        :param a: vectOR
        :param baseSrc: the source base
        :param baseDst: the destination base
        :return: a dictionary containing two list (one with fractional AND one with integer part)
        '''
        IF baseSrc = 16 AND baseDst !=8 AND baseDst != 4 AND baseDst != 2:
            raise RuntimeError("Combination of bases is not corect. Must be 16 -> 4 or 16 -> 2")
        ENDIF
        IF baseSrc = 8 AND baseDst != 2:
            raise RuntimeError("Combination of bases is not corect. Must be 8 -> 2")
        ENDIF
        IF baseSrc = 4 AND baseDst != 2:
            raise RuntimeError("Combination of bases is not corect. Must be 4 -> 2")
        ENDIF
        convertedIntegerNumber <- []
        convertedFractionalNumber <- []
        nrOfRepeats <- int(math.log(baseSrc, baseDst))
        #Converting the integer part
        for i in range(len(a["integer"])):
            binaryDigits <-  convertFromBase10(a["integer"][i], baseDst)
            binaryDigits <- binaryDigits["integer"]
            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)
            ENDFOR
            for j in range(nrOfRepeats):
                convertedIntegerNumber.insert(0, binaryDigits[j])
            ENDFOR
        #Converting the fractional part
        ENDFOR
        for i in range(len(a["fractional"])-1, -1, -1):
            binaryDigits <-  convertFromBase10(a["fractional"][i], baseDst)
            binaryDigits <- binaryDigits["integer"]
            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)
            ENDFOR
            binaryDigits <- binaryDigits[::-1]
            for j in range(nrOfRepeats):
                convertedFractionalNumber.append(binaryDigits[j])
        ENDFOR
            ENDFOR
        RETURN {"integer": convertedIntegerNumber[::-1], "fractional": convertedFractionalNumber[::-1]}
    ENDFUNCTION

    FUNCTION rapidConversionToHigherBase(self, a, baseSrc, baseDst):
        '''
        :param a: vectOR
        :param baseSrc: the source base
        :param baseDst: the destination base
        :return: a dictionary containing two list (one with fractional AND one with integer part)
        '''
        IF baseSrc = 2 AND baseDst != 4 AND  baseDst != 8 AND baseDst != 16:
            raise RuntimeError("Combination of bases is not corect. Must be 2 -> 4 or 2 -> 8 or 2 -> 16")
        ENDIF
        IF baseSrc = 4 AND baseDst != 16:
            raise RuntimeError("Combination of bases is not corect. Must be 4 -> 16")
        ENDIF
        IF baseSrc != 2 AND baseSrc != 4:
            raise RuntimeError("Combination of bases is not corect")
        ENDIF
        convertedIntegerNumber <- []
        convertedFractionalNumber <- []
        nrOfRepeats <- int(math.log(baseDst, baseSrc))
        #Converting the integer part
        i <- 0
        while i < len(a["integer"]):
            binaryDigits <- a["integer"][i:i+nrOfRepeats]
            #binaryDigits <- binaryDigits[::-1]
            nrBinaryDigits <-  vectorToNumber(binaryDigits) # Convert it to a vector
            nrBinaryDigits <-  convertToBase10(nrBinaryDigits, baseSrc) # Convert the vector in base 10
            nrBinaryDigits <-  vectorToNumber(nrBinaryDigits["integer"]) # Convert the vector in base 10
            convertedIntegerNumber.append(nrBinaryDigits)
            i <- i + nrOfRepeats
        ENDWHILE
        a["fractional"] <- a["fractional"][::-1]
        i <- 0
        while i < len(a["fractional"]):
            binaryDigits <- a["fractional"][i:i+nrOfRepeats]
            for j in range(nrOfRepeats - len(binaryDigits)):
                binaryDigits.append(0)
            ENDFOR
            binaryDigits <- binaryDigits[::-1]
            nrBinaryDigits <-  vectorToNumber(binaryDigits) # Convert it to a vector
            nrBinaryDigits <-  convertToBase10(nrBinaryDigits, baseSrc) # Convert the vector in base 10
            nrBinaryDigits <-  vectorToNumber(nrBinaryDigits["integer"]) # Convert the vector in base 10
            convertedFractionalNumber.append(nrBinaryDigits)
            i <- i + nrOfRepeats
        ENDWHILE
        RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}
    ENDFUNCTION

    FUNCTION conversionToLowerBase(self, a, baseSrc, baseDst):
        '''
        :param nr: number to be converted
        :param base:  destionation base
        :return: a dictionary containing two list (one with fractional AND one with integer part)
        '''
        convertedIntegerNumber <- []
        convertedFractionalNumber <- []
        integer <- a["integer"]
        fractional <- a["fractional"]
        #Converting the integer part
        while len(integer):
            rest <-  divR(integer, baseDst, baseSrc)
            quotent <-  div(integer, baseDst, baseSrc)
            convertedIntegerNumber.append(rest)
            integer <- quotent
        #Converting the fractional part
        ENDWHILE
        maxDigits <- 4
        crtDigits <- 0
        while len(fractional)  AND crtDigits < maxDigits:
            integerDigit <-  prodP(fractional, baseDst, baseSrc)
            newFractional <-  prod(fractional, baseDst, baseSrc)
            convertedFractionalNumber.append(integerDigit)
            IF(len(newFractional) > len(fractional)):
                newFractional.pop(len(newFractional)-1)
            ENDIF
            fractional <- newFractional
            crtDigits <- crtDigits + 1
        ENDWHILE
        RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber[::-1]}
    ENDFUNCTION

    FUNCTION conversionToHigherBase(self, a, baseSrc, baseDst):
         '''
         Substitution Method
         :param nr: number to be converted
         :param baseSrc: the source base
         :param baseDst: the destination base
         :return: a dictionary containing two list (one with fractional AND one with integer part)
         '''
         convertedIntegerNumber <- []
         convertedFractionalNumber <- []
         integer <- a["integer"]
         fractional <- a["fractional"]
         #Converting the integer part
         power <- 1
         for i in range(len(integer)):
             IF baseSrc >= 10:
                 crtInteger <-  numberToVector(integer[i])
                 crtInteger <- crtInteger["integer"]
                 crtProd <-  prod(crtInteger, power, baseDst)
                 convertedIntegerNumber <-  sum(convertedIntegerNumber, crtProd, baseDst)
                 crtPower <-  numberToVector(power)
                 crtPower <- crtPower["integer"]
                 power <-  prod(crtPower, baseSrc, baseDst)
                 power <-  vectorToNumber(power)
             ELSE:
                 crtPower <-  numberToVector(power)
                 crtPower <- crtPower["integer"]
                 crtProd <-  prod(crtPower, integer[i], baseDst)
                 convertedIntegerNumber <-  sum(convertedIntegerNumber, crtProd, baseDst)
                 power <-  prod(crtPower, baseSrc, baseDst)
                 power <-  vectorToNumber(power)
             ENDIF
         #Converting the fractional part
         ENDFOR
         powerHeins <- 1 / baseSrc
         power <- powerHeins
         power <-  convertFromBase10(power, baseDst)
         power <-  vectorToSubunitaryNumber(power["fractional"])
         for i in range(len(fractional)-1, -1, -1):
             crtFractional <-  numberToVector(fractional[i])
             crtFractional <- crtFractional["integer"]
             IF len(crtFractional) != 0:
                crtProd <-  prod(crtFractional, power, baseDst)
                crtProd <-  convertRationalToInteger(crtProd[0], 4)
                convertedFractionalNumber <-  sum(convertedFractionalNumber, crtProd, baseDst)
             ENDIF
             powerHeins <- powerHeins / baseSrc
             power <- powerHeins
             power <-  convertFromBase10(power, baseDst)
             power <-  vectorToSubunitaryNumber(power["fractional"])
         ENDFOR
         RETURN {"integer": convertedIntegerNumber, "fractional": convertedFractionalNumber}
    ENDFUNCTION

    FUNCTION convertRationalToInteger(self,a, precision):
        '''
        :param a: a rational number
        :return: the fractionary part as an integer
        '''
        res <- []
        nr <-  getFractionalString(a)
        for crt in nr:
            res.append(int(crt))
        ENDFOR
        for i in range(precision-len(res)):
            res.append(0)
        ENDFOR
        RETURN res[::-1
