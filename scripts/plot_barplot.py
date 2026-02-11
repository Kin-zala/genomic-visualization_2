import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import numpy as np

# Custom labels for bar plot x-axis
custom_labels = ['x->y', 'x->z', 'y->x', 'y->z']
# Read bar plot data
bp = pd.read_csv("data\\10_project_data_barplot.csv")

# Extract data for bar plot

# Extract the labels for the x-axis from the DataFrame 'bp'
labels = bp['Unnamed: 0']

# Extract data for the first sample of condition A from the DataFrame 'bp'
condition_a_sample_1 = bp['condition_a_sample_1']

# Extract data for the second sample of condition A from the DataFrame 'bp'
condition_a_sample_2 = bp['condition_a_sample_2']

# Extract data for the control group from the DataFrame 'bp'
control = bp['control']

# Create the figure with a custom gridspec layout
fig = plt.figure(figsize=(16, 14))  # Create a new figure with a size of 16x14 inches
gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1])  # Add a gridspec layout with 3 rows and 2 columns

# Bar plot
ax2 = fig.add_subplot(gs[0, 1])  # Add a subplot in the first row, second column
x = np.arange(len(labels))  # Define the x-axis locations for the bars
width = 0.2  # Set the width of each bar
spacing = 0.02  # Define spacing between groups of bars

# Plot bars for Condition A Sample 1
rects1 = ax2.bar(x - (width + spacing / 2), condition_a_sample_1, width,
                 label='Condition A Sample 1', color='black', zorder=3)
# Plot bars for Condition A Sample 2
rects2 = ax2.bar(x, condition_a_sample_2, width, label='Condition A Sample 2',
                 color='black', zorder=3)
# Plot bars for Control
rects3 = ax2.bar(x + (width + spacing / 2), control, width, label='Control',
                 color='red', zorder=3)

ax2.set_yticks(np.arange(0, 2725, 500))  # Set y-axis major ticks
ax2.set_yticks(np.arange(0, 2725, 250), minor=True)  # Set y-axis minor ticks
ax2.yaxis.grid(True, which='major', zorder=0, linestyle='dotted')  # Add grid lines for major y-axis ticks
ax2.yaxis.grid(True, which='minor', linestyle='dotted')  # Add grid lines for minor y-axis ticks
ax2.set_ylabel('Number of events')  # Label y-axis as 'Number of events'
ax2.set_xticks(x)  # Set x-axis ticks
ax2.set_xticklabels(custom_labels)  # Set x-axis tick labels to 'custom_labels'

# Add legend for bar plot
condition_patch = plt.Line2D([0], [0], color='black', lw=4, label='Condition')  # Create a legend patch for Condition
control_patch = plt.Line2D([0], [0], color='red', lw=4, label='Control')  # Create a legend patch for Control
ax2.legend(handles=[condition_patch, control_patch])  # Add the legend to the bar plot
plt.show()  # Display the figure