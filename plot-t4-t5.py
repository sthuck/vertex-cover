import pandas as pd
import matplotlib.pyplot as plt
df5 = pd.read_csv('./theorem5_results-100-iteration-n-1000.csv', index_col=0)
df4 = pd.read_csv('./theorem4_results.csv', index_col=0)
plt.plot(df4.index, df4['t4']/1000, label='t4')
plt.plot(df5.index, df5['t5']/1000, label='t5')
plt.legend()
plt.show()