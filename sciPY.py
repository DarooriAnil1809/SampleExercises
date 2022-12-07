from scipy.special import comb
import math
import numpy as np
from scipy.special import cbrt

# METHOD 1 - CUBE ROOT
# Cube root of 64 - syntax - cbrt(num)
print("Cube Root of 64")
print(cbrt(64))

print("Cube Root of 128")
print(cbrt(128))


# Cube Root of Given Elements
print("Cube Root of Given Elements")
arr = [64, 164, 564, 4, 640]
arr = list(map(cbrt, arr))
print(arr)


# METHOD 2 - comb() - combination of given value
#syntax - scipy.special.comb(N,k)

# Combinations of 4
print("NO of Combinations")
print(comb(4, 1))

# Combinations of 6
print([comb(6, 1), comb(6, 2), comb(6, 3), comb(6, 4), comb(6, 5)])


