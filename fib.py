from functools import lru_cache
import time
import matplotlib.pyplot as plt
import numpy as np

xpoints = []
ypoints = []

def timer(func):
	def wrapper(*args, **kwargs):
		t1 = time.time()
		res = func(*args, **kwargs)
		timeTaken = time.time() - t1
		xpoints.append(args[0])
		ypoints.append(timeTaken)
		print(f"Finished in {timeTaken:.8f}s: f({args[0]}) -> {res}")
		return res
	return wrapper

@lru_cache
@timer
def fib(n: int):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fib(n-1) + fib(n-2)

fib(100)
xpoints = np.array(xpoints)
ypoints = np.array(ypoints)

plt.plot(xpoints, ypoints)
plt.show()