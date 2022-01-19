# as clause used to bind the name plot, with pyplot module from matplotlib

import numpy as np
from matplotlib import pyplot as plot

sampleSequence = np.arange(0, 400, 10)
magnitudeSequence = np.sin(2 * np.pi * sampleSequence * 1 / 400)

plot.plot(sampleSequence, magnitudeSequence)
plot.title('Sinusoid')
plot.xlabel('Sample')
plot.ylabel('Amplitude')
plot.show()