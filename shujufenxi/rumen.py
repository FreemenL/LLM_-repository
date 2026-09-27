import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

data = np.random.randn(100,3)


df  = pd.DataFrame(data,columns=['A','B','C'])
print(df.head())

#
df.plot(kind='line',alpha=0.5)
#
plt.show()

