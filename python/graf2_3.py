import numpy as np
import matplotlib.pyplot as plt
import os

PATH = os.path.join(os.getcwd(), "Archivos")

plt.figure(figsize=(30, 18), dpi=80)
i = 311

for file in sorted(os.listdir(PATH)):                                        
    if file.endswith(".txt"):
        plt.subplot(i)
        file_dir = os.path.join(PATH, file)
        data = np.loadtxt(file_dir)
        plt.scatter(data[:,0], data[:,1], s=0.5, color = 'red')
        plt.xlabel(file[:-8])
        plt.grid()
        i += 1

plt.savefig("grafica.png") 
plt.show()