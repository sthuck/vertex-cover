import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_hist(x, title, num_bins=50, plot_guiding_line=True):
    mu = 0  # mean of distribution
    sigma = 1  # standard deviation of distribution

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=1)

    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))

    if plot_guiding_line:
        ax.plot(bins, y, '--')

    ax.set_xlabel('')
    ax.set_ylabel('Probability density')
    ax.set_title(title)

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()


def plot_density(x):
    ax = pd.DataFrame(x).plot(kind='density', grid=True, xlim=(-3, 3))
    ax.plot()
    plt.show()


if __name__ == '__main__':
    x = np.load('./theorem2_c_10_c1.npy')
    plot_hist(x, r'Theorem 2c', 50)

# plot_density()
# plot_hist(x, 100)
# plot_hist(x, 150)