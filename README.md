# 20210625 Update (by EsonJohn)：




# Foreword

Python script to parse raw Channel State Information (CSI) data collected from Intel 5300 NIC.

For the matlab version provided by 5300 CSI Tool, please refer to: https://github.com/dhalperi/linux-80211n-csitool-supplementary

  

# Usage


 demo.py：  

```python
from wifilib import *
import matplotlib.pyplot as plt

# Interface
csi_np, timestamp = csi_get_all("./data_sample_1.dat")

# Visualization
print("csi shape: ",csi_np.shape)
fig = plt.figure()
plt.plot(np.abs(csi_np)[:,0,0,0])
plt.show()

```
**Shape:**

csi_np:[time, Ntx, NRx, 30]

timestamp:[1, time]

NTx: number of transmitter; NRx: number of receiver; 30: number of subcarriers;


# Bug Fix
Function *get_scale_csi* will have NaN value, induced by zero elements in *csi_pwr* variable, fixed by substituting:
```
csi_pwr = np.sum(csi_sq, axis=-1)
```
with
```
csi_pwr = np.sum(csi_sq)
```