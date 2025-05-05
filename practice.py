import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,5)
y= x**3
# plt.plot([1,2,3,4],[5,6,7,8],"--",x,y,'r^')
# plt.hist([1,2,3,4],[5,6,7,8])
plt.title("Title")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()