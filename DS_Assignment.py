#Disclaimer: This code does NOT work in JDoodle as the module required(matplotlib) doesn't exist in it

import matplotlib.pyplot as plt

#Function that returns probability of n people having the same birthday in 365 days
def prob(n):
    if n >= 365:
        return 1
    c = 1
    for i in range(0, n):
        a = (365 - i) / 365
        c *= a
    return 1 - c

n = []
p = []

for i in range(1, 400):
    n.append(i)
    p.append(prob(i))

#Plotting the graph
plt.plot(n, p)
plt.xlabel("Number of People")
plt.ylabel("Probability")
plt.show()