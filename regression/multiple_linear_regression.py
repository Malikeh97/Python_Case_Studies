import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.api as sm
from sklearn  import linear_model
from sklearn.model_selection import train_test_split

n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1
np.random.seed(1)
x_1 = 10 * ss.uniform.rvs(size=n)
x_2 = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale = 1, size = n)
X = np.stack([x_1, x_2], axis=1) #axis = 1 to put x1 and x2 in columns

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$")
# plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)
lm = linear_model.LinearRegression(fit_intercept = True)
lm.fit(X_train, y_train)
print(lm.score(X_test, y_test))
