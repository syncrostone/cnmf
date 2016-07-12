
## fit a model
import thunder as td
from regional import one, many
import numpy as np
import matplotlib.pyplot as plot
from showit import image

from cnmf import CNMF

path = '/Users/user/Desktop/NeuroFinder/data/neurofinder.00.00/'

images = td.images.fromtif(path + 'images',stop=10, ext='tiff')
data=images.toarray()
base = images.mean().toarray()
image(base, size=10);
plot.show()

algorithm = CNMF( k=60, gSig=[4,4], merge_thresh=0.8)

model,temporaldata = algorithm.fit(data)

def convert(array):
    r,c = np.where(array > 0.0)
    return one(zip(r,c))

regions = many([convert(model[:,:,i]) for i in range(model.shape[2])])

masks = regions.mask(cmap_stroke='rainbow', fill=None, base=base.clip(0,4000) / 4000)
image(masks, size=14);
plot.show()
