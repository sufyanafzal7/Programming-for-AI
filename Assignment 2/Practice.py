# import pandas as pd
# from ydata_profiling import ProfileReport
# df = pd.read_csv("heart_2020_cleaned.csv",sep=',')
# print(df.head(15))
# prof = ProfileReport(df)
# prof.to_file(output_file='eda.html')
# print("work done")

# ---------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0,6])
# ypoints = np.array([0,250])

# plt.plot(xpoints,ypoints)
# plt.show()

# ----------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0,10])
# ypoints = np.array([0,256])

# plt.plot(xpoints,ypoints,'o')
# plt.show()

# -------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1,2,6,8])
# ypoints = np.array([3,8,1,10])

# plt.plot(xpoints,ypoints)
# plt.show()

# ----------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np


# ypoints = np.array([3,8,1,10,5,7])

# plt.plot(ypoints)
# plt.show()

# ------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np


# ypoints = np.array([3,8,1,10, 5,7])

# plt.plot(ypoints, marker = 's') # can use 'o' 'x' etc instead of 's'
# plt.show()

# ------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([1,10,4,8,1,7])

# plt.plot(ypoints, 'o:r')  # marker|line|color  called 'fmt' aka formar string
# plt.show()         # : dotted line, - solid line, etc   

# ------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np


# ypoints = np.array([3,8,1,10, 5,7])

# plt.plot(ypoints, marker = 'o', ms=20, mec = 'r', mfc = 'g', linestyle = 'dashed', color = 'y', lw = 10) # can use 'o' 'x' etc instead of 's'
# plt.show()

# ------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([1,10,2,9,3,8])
ypoint = np.array([2,9,1,10,4,6])

plt.plot(xpoint)
plt.plot(ypoint)

plt.show()


