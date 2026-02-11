import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import numpy as np

# Load the dataframes
df1 = pd.read_csv("data\\10_project_data_annotation.csv")
df2 = pd.read_csv("data\\10_project_data_signals.csv")


# Create the figure with a custom gridspec layout
fig = plt.figure(figsize=(16, 14))  # Create a new figure with a size of 16x14 inches
gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1])  # Add a gridspec layout with 3 rows and 2 columns

# Heatmap
ax3 = fig.add_subplot(gs[1, :])  # Add a subplot in the second row, spanning both columns
data = np.vstack([df2['P1'], df2['P2'], df2['P3'], df2['P4']])  # Stack data arrays vertically for the heatmap
sns.heatmap(data, cmap='Greys', cbar=False, yticklabels=['P1', 'P2', 'P3', 'P4'], ax=ax3)  # Create a heatmap with specified properties
ax3.xaxis.grid(True)  # Add grid lines to the x-axis
ax3.set_xticks([])  # Hide x-axis ticks
ax3.set_xlim([0, 20000])  # Set x-axis limits
# Add solid outline for heatmap
ax3.spines['top'].set_visible(True)
ax3.spines['right'].set_visible(True)
ax3.spines['left'].set_visible(True)
ax3.spines['bottom'].set_visible(True)



# Annotations
ax4 = fig.add_subplot(gs[2, :])  # Add a subplot in the third row, spanning both columns
ax4.set_xlim([0, 20000])  # Set x-axis limits
ax4.set_xlabel('Genomic position', fontsize=10)  # Label x-axis as 'Genomic position'
ax4.set_ylabel('Annotations', fontsize=10)  # Label y-axis as 'Annotations'
ax4.set_ylim(-0.5, 1.5)  # Set y-axis limits
ax4.set_yticks([0, 1])  # Set y-axis ticks
ax4.set_yticklabels(['−', '+'])  # Label y-axis ticks
ax4.xaxis.grid(True, linestyle='dotted', linewidth = 2)  # Add dotted grid lines to the x-axis

# Plot annotations
for _, r in df1.iterrows():  # Iterate over rows of DataFrame 'df1'
    marker = '|'
    markersize = 10  # Marker size
    lw = 2
    if r['type'] == 'exon':  # If type is 'exon'
        marker = None
        lw = 15
    y = 1 if r['strand'] == '+' else 0  # Set y-coordinate based on strand
    ax4.plot((r['start'], r['stop']), (y, y),  # Plot line for the annotation
             marker=marker, lw=lw,  # Set marker and line width
             solid_capstyle='butt',  # Set line cap style
             color='#505050')  # Set line color
    
plt.show()  # Display the figure