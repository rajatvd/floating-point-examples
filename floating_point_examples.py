# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Subtraction Is Bad

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
VALUE = 5


# %%
def identity(x):
    return x


# %%
def identity_sub(x):
    return (x + VALUE) - VALUE


# %%
def identity_mult(x):
    return (x * VALUE) / VALUE


# %% [markdown] jp-MarkdownHeadingCollapsed=true
# # Compare Relative Errors

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Using 32-bit floats

# %%
count = 100000
xs = np.logspace(-9, 9, count, dtype=np.float32)
ys = identity(xs)
ys_sub = identity_sub(xs)
ys_mult = identity_mult(xs)

sub_error = np.abs(ys - ys_sub) / np.abs(ys)
mult_error = np.abs(ys - ys_mult) / np.abs(ys)

# %%

plt.loglog()
plt.ylim(1e-9, 2)
plt.xlabel("x")
plt.title("Relative error between f(x) and x, 32-bit floating point")
plt.plot(xs, sub_error, label=f"f(x) = (x + {VALUE}) - {VALUE}")
plt.plot(xs, mult_error, label=f"f(x) = (x * {VALUE}) / {VALUE}")
plt.ylabel("|f(x) - x| / |x|")
plt.legend()
plt.show()

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Using 64-bit floats

# %%
xs = np.logspace(-17, 17, count, dtype=np.float64)
ys = identity(xs)
ys_sub = identity_sub(xs)
ys_mult = identity_mult(xs)

sub_error = np.abs(ys - ys_sub) / np.abs(ys)
mult_error = np.abs(ys - ys_mult) / np.abs(ys)

# %%

plt.loglog()
plt.ylim(1e-17, 2)
plt.xlabel("x")
plt.title("Relative error between f(x) and x, 64-bit floating point")
plt.plot(xs, sub_error, label=f"f(x) = (x + {VALUE}) - {VALUE}")
plt.plot(xs, mult_error, label=f"f(x) = (x * {VALUE}) / {VALUE}")
plt.ylabel("|f(x) - x| / |x|")
plt.legend()
plt.show()

# %%
plt.loglog()
plt.plot(xs, ys)
plt.plot(xs, ys_sub)
plt.plot(xs, ys_mult)

# %%
