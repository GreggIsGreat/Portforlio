import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

x = [1238,1320,1296,1210,1296,1765,1725,1794,1294,1372,1162,1996,1416,1730,1664]
y = [59900,66500,66500,66900,68000,68500,69000,70950,71000,72692,72801,75207,76000,77500,79900]

coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef)
plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')
plt.scatter(x,y)
plt.show()




