import numpy as np
from astropy.table import Table
from ctapipe.utils import datasets
from ctapipe.visualization import ArrayDisplay
from matplotlib import pyplot as plt


if __name__ == '__main__':

    plt.style.use("ggplot")
    arrayfile = datasets.get_path("PROD2_telconfig.fits.gz")
    tels = Table.read(arrayfile, hdu="TELESCOPE_LEVEL0")

    plt.figure(figsize=(10, 8))
    adisp = ArrayDisplay(tels['TelX'], tels['TelY'], tels['MirrorArea'] * 2,
                         title='PROD2 all telescopes', autoupdate=False)
    plt.tight_layout()

    intensities = np.zeros(len(tels))

    # do a small animation to show various trigger patterns:
    
    for ii in range(20):
        # generate a random trigger pattern and integrated intensity:
        ntrig = np.random.poisson(10)
        trigmask = np.random.random_integers(len(tels) - 1, size=ntrig)
        intensities[:] = 0
        intensities[trigmask] = np.random.uniform(0, 100, size=ntrig)
        # update the display:
        adisp.intensities = intensities
        plt.pause(0.5)
