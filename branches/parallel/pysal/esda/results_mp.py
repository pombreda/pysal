
import numpy as np
import matplotlib.pyplot as plt

t = np.loadtxt("mp_results.txt")
s = np.loadtxt("seq_results.txt")

sp = s/t

ns = [ 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
leg = ["k=5","k=7", "k=9"]
#plt.plot(ns, sequential)
plt.plot(ns, sp)
plt.xlabel("n")
plt.ylabel("Ts/Tp")
plt.legend(leg,loc="lower right")
plt.title("MultiProcessing Speedup")



plt.show()
