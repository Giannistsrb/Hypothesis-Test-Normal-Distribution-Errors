import math as m
from scipy.stats import norm

# H0 and H1 means for normal distribution N(μ,σ), 
# critical mean, random samples and sigma value of normal 
# distribution:
μ_H0, μ_H1, critical_mean, N, σ    = 20, 22, 21, 9, 1

#Type I error (a value):
a   = 1 - norm.cdf((critical_mean - μ_H0) / (σ / m.sqrt(N)))

#Type II error (b value):
b   =     norm.cdf((critical_mean - μ_H1) / (σ / m.sqrt(N)))

#Power of the test:
powooftest = 1 - b 

print(f"Value a = {a}, value b = {b} and the power of the test is {1-b}")














