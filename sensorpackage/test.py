import matplotlib.pyplot as plt

x = [1,2,3]
for i in x:
    plt.plot(i, i, marker=(3, 0, 5), markersize=20, linestyle='None')

plt.xlim([0,4])
plt.ylim([0,4])

plt.show()
