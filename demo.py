from wifilib import *
import matplotlib.pyplot as plt

# Interface
csi_np, timestamp = csi_get_all("./data_sample.dat")

# Visualization
print("csi shape: ",csi_np.shape)
fig = plt.figure()
plt.plot(np.abs(csi_np)[:,0,0,0])
plt.show()
