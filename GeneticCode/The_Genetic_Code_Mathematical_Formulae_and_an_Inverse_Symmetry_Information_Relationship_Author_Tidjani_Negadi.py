## Calculate a combinatorial from article Levinthals Paradox of The Interactome

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from scipy.special import factorial


## SECTION 3: THE GENETIC CODES VIA Q-DEFORMATIONS

t = np.linspace(0,4,200)

fN = 1/2
for N in [1,2,3,4]:
    fN = fN - (-1)**N * np.sin(2*N*np.pi*t)/(N*np.pi)
    plt.subplot(2,2,N)
    plt.plot(t,fN)
    plt.title('N = {}'.format(N))

plt.tight_layout()
plt.show()


# EQ 21
#
# q = [0.9959,1,1.0040,1.0079, 1.0116]
#
# nq_e21a = (pow(q,n)-1)/(q-1)
#
# for i in range(n,1,-1):
# #     f=f*i
# nq_e21b = (1+q+pow(q,2)+pow(q,2))
#
#
# n = 7
