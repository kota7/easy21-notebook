# coding: utf-8

import matplotlib.pyplot as plt
import seaborn as sns

def draw_heatmap(array, title="", ax=None,
                 cmap="coolwarm", alpha=0.8, annot=True, fmt=".2f", cbar=False):
    if ax is None:
        fig, ax = plt.subplot()
    sns.heatmap(array, ax=ax, cmap=cmap, alpha=alpha, annot=annot, fmt=fmt, cbar=cbar)
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.set_xticklabels(range(1, 11))
    ax.set_yticklabels(range(1, 22))
    ax.set_xlabel("Dealer's sum")
    ax.set_ylabel("Player's sum")
    ax.set_title(title)
    return ax