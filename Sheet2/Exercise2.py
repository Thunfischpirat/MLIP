import numpy as np
import matplotlib.pyplot as plt


# Define operator A:
def A(f):
    def A_f(x):
        # Define the integral of f(x) from 0 to x smaller than 1:
        if not np.all((0 <= x) & (x <= 1)):
            raise ValueError("x must be between 0 and 1")
        t = np.linspace(np.zeros(x.shape), x, 100).T
        return np.trapz((x-t)*f(t), t)

    return A_f


def T_h(g, h):
    if h <= 0:
        raise ValueError("h must be greater than 0")

    # Define the approximation of the inverse operator:
    def T_g_h(x):
        return (g(x + h) - 2 * g(x) + g(x - h)) / (h**2)

    return T_g_h


def f(t):
    if not np.all((0 <= t) & (t <= 1)):
        raise ValueError("t must be between 0 and 1")
    return t * (1-t)


# %% b)
# Plot the function f(t) and the operator A(f)(t) and T_h(A(f), h)(t) for h = 0.1, 0.01, 0.001:
h = [0.1, 0.01, 0.001]
t = np.linspace(0.1, 0.9, 100)
plt.figure(dpi=300)
plt.plot(t, f(t), label="f(t)")
plt.plot(t, A(f)(t), label="A(f)(t)")
for i in range(len(h)):
    plt.plot(t, T_h(A(f), h[i])(t), label="T_h(A(f), h = {})(t)".format(h[i]))
plt.legend()
plt.show()

# %%
