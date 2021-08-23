import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager
import numpy as np

sns.set(style="ticks", palette="Set2")

colors = plt.cm.viridis(np.linspace(0.85, 0.0, 5))

CB91_Blue = colors[4]
CB91_Green = colors[1]

matplotlib.rcParams["axes.prop_cycle"] = plt.cycler(color=colors)
mpl.rcParams["axes.grid"] = True
mpl.rcParams["figure.facecolor"] = (1.0, 1.0, 1.0, 1.0)
mpl.rcParams["savefig.facecolor"] = (1.0, 1.0, 1.0, 1.0)

SMALL_SIZE = 7
MEDIUM_SIZE = 7
BIGGER_SIZE = 9

from os.path import expanduser
import matplotlib as mpl
import matplotlib.font_manager as font_manager

# mpl.use('Agg')
fontpath = expanduser("/usr/share/fonts/opentype/adobe/MyriadPro-Regular.otf")
prop = font_manager.FontProperties(fname=fontpath)
mpl.rcParams["font.family"] = prop.get_name()
mpl.rcParams["text.usetex"] = False

COLOR = "#6A6A6C"
COLOR = "black"
mpl.rcParams["text.color"] = COLOR
mpl.rcParams["axes.edgecolor"] = COLOR
mpl.rcParams["axes.labelcolor"] = COLOR
mpl.rcParams["xtick.color"] = COLOR
mpl.rcParams["ytick.color"] = COLOR

mpl.rc("font", size=SMALL_SIZE)  # controls default text sizes
mpl.rc("axes", titlesize=7)  # fontsize of the axes title
mpl.rc("axes", labelsize=7)  # fontsize of the x and y labels
mpl.rc("xtick", labelsize=6)  # fontsize of the tick labels
mpl.rc("ytick", labelsize=6)  # fontsize of the tick labels
mpl.rc("legend", fontsize=SMALL_SIZE)  # legend fontsize
mpl.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title

mpl.rcParams["grid.color"] = "#dddddd"
mpl.rcParams["grid.linewidth"] = 0.4
mpl.rcParams["axes.linewidth"] = 0.4
mpl.rcParams["axes.facecolor"] = "#fAfAfC"
mpl.rcParams["lines.linewidth"] = 1.0

mpl.rcParams["lines.markersize"] = 3.2

mpl.rcParams["xtick.major.size"] = 3
mpl.rcParams["xtick.major.width"] = 0.4
mpl.rcParams["xtick.minor.size"] = 3
mpl.rcParams["xtick.minor.width"] = 0.4

mpl.rcParams["ytick.major.size"] = 3
mpl.rcParams["ytick.major.width"] = 0.4
mpl.rcParams["ytick.minor.size"] = 3
mpl.rcParams["ytick.minor.width"] = 0.4
