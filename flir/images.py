#%%
import numpy as np
import matplotlib.pyplot as plt

from skimage import measure

#%%
x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
r = np.sin(np.exp((np.sin(x)**3 + np.cos(y)**2)))

fig, ax = plt.subplots()
ax.imshow(r, cmap=plt.cm.gray)
# %%
contours = measure.find_contours(r, 0.9)
# %%
for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
# %%
ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
# %%
