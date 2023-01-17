#!/usr/bin/env python3
import matplotlib.pyplot as plt


labels = ['correct', 'wrong']
sizes = [0.7836879432624113, 0.21631205673758866]
explode = (0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')

plt.show()
