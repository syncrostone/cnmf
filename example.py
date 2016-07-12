
## fit a model
import thunder as td
from cnmf import CNMF

data = td.images.fromtif('').toarray()

algorithm = CNMF(params)

model = algorithms.fit(data)