
print("Solution No.1")

import numpy as np
x = np.arange(20)
print("\nOriginal array:")
print(x)
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print("\nMean: ", r1)
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2))
assert np.allclose(r1, r2)
print("\nstd: ", 1)
r1 = np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2)
assert np.allclose(r1, r2)
print("\nvariance: ", r1)

print("--------------------------------------------------")
print("--------------------------------------------------")

print("Solution No.2")

# Original array
array = np.arange(20)
print(array)

r1 = np.mean(array)
print("\nMean: ", r1)

r2 = np.std(array)
print("\nstd: ", r2)

r3 = np.var(array)
print("\nvariance: ", r3)
