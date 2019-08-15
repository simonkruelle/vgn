from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


def plot_tsdf(tsdf):
    """Visualize multiple slices of a TSDF.
    
    Args:
        v: A 3-dimensional numpy array.    
    """
    res = tsdf.shape[0]
    fig, axs = plt.subplots(ncols=6)

    skip = res // 6

    for i in range(6):
        img = axs[i].imshow(tsdf[i * skip, :, :], vmin=0.0, vmax=1.0)
        axs[i].axis('off')

    plt.subplots_adjust(wspace=0.05, hspace=0.0)
    fig.colorbar(img, ax=axs[:])

    plt.show()