import numpy as np
import matplotlib.pyplot as plt

dA2 = np.array([[1,-2,3],
      [4,-5,6]
      ])



dA3 = np.multiply(dA2, np.int64(dA2 > 0))



print(dA3)