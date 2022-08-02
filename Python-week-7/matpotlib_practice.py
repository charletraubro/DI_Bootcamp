import matplotlib.pyplot as plt

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

x = [1, 2, 3, 4]
y = [2, 20, 35, 6]
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('first graph')
plt.show()