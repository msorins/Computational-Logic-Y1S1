__author__ = 'sorynsoo'

from numerationBasesModule.classes.numerationBases import *

numerationBasesObj = NumerationBases()

v1 = numerationBasesObj.numberToVector(125.16)
v3 = numerationBasesObj.rapidConversionToLowerBase(v1,16,4)

print(v3["integer"])
print(v3["fractional"])


print(numerationBasesObj.vectorToNumber(v1["fractional"]))