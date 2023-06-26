import pandas as pd
import matplotlib.pyplot as plt        
df = pd.read_csv("D:/raw/2022/insite/alr/M77 to M82/franatech_mets_time_corrected_20220923.csv") 
df["timestamp"] = pd.to_datetime(df["corrected_timestamp"], unit='s')
plt.plot(df["timestamp"], df["methane concentration(umol/l)"])
plt.show()
