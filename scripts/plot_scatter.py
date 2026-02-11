import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import numpy as np

# Read scatter plot data
sp = pd.read_csv("data\\10_project_data_scatter.csv")

# Create the figure with a custom gridspec layout
fig = plt.figure(figsize=(16, 14))  # Create a new figure with a size of 16x14 inches
gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1])  # Add a gridspec layout with 3 rows and 2 columns

# Scatter plot
ax1 = fig.add_subplot(gs[0, 0])
ax1.scatter(x='x1', y='x2', data=sp, marker='o', color='none', s=40, edgecolors='black')
ax1.set_xlim(6, 14)  # Set x-axis limits from 6 to 14
xticks = np.arange(8, 14, 2)  # Start from 8 to exclude 6
ax1.set_xticks(xticks)  # Set the x-axis ticks
ax1.set_xticklabels(xticks)  # Set x-axis tick labels to match the ticks
ax1.grid(True, linestyle='dotted', color='lightgrey', linewidth=1)
#set the axis labels
ax1.set_xlabel('X1')
ax1.set_ylabel('X2')


plt.show()  # Display the figure