import matplotlib.pyplot as plt
import matplotlib.cm     as cm
import numpy             as np
import seaborn           as sns
import numpy.random      as rd

m = 10
s = 3

min_x = m - 4*s
max_x = m + 4*s

x = np.linspace(min_x, max_x, 201)
y = (1/np.sqrt(2*np.pi*s**2))*np.exp(-0.5*(x-m)**2/s**2)

plt.figure(figsize=(8, 5))
rd.seed(7)
data = rd.normal(10, 3, 10, )
plt.scatter(data, np.zeros_like(data), c="r", s=50)
