import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import statsmodels.api as sm

n = 100
beta_0 = 5
beta_1 = 2

np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale = 1, size = n)


rss = []
slopes = np.arange(-10, 15, 0.01)
for slope in slopes:
    rss.append(np.sum((y - beta_0 - slope * x)**2))


ind_min = np.argmin(rss)
print(slopes[ind_min])

plt.figure()
plt.plot(slopes, rss)
plt.xlabel("slope")
plt.ylabel("rss")
plt.show()

#with no intercept
mod = sm.OLS(y, x) #ordinary least squares
est = mod.fit()
print(est.summary())

#with intercept
print(x)
X = sm.add_constant(x)
print(X)
mod = sm.OLS(y, X) #ordinary least squares
est = mod.fit()
print(est.summary())
