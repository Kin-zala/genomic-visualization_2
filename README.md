# Genomic Visualization Exercise 2

This repository contains **Exercise 2** (from 'genomic-visualization-rna-binding-protein' repository) for visualizing genomic and RNA binding protein data with **multi-panel figures**. This exercise builds upon Exercise 1 by adding scatter and bar plots to the top of the figure, while keeping RNA binding protein heatmaps and annotations at the bottom.

## Repository Structure

- `data/` – Contains CSV files:
  - `10_project_data_scatter.csv`: Data for the scatter plot.
  - `10_project_data_barplot.csv`: Data for the bar plot.
  - `10_project_data_annotations.csv`: Gene/transcript annotations.
  - `10_project_data_signals.csv`: RNA binding protein signals.

- `images/` – Optional folder for saved output plots:
  - `full_figure_example.png`

- `notebooks/` – Jupyter notebook:
  - `Visualization_Exercise_2.ipynb`: Complete multi-panel figure creation with explanations and code.

- `scripts/` – Optional standalone Python scripts for each plot or full figure:
  - `plot_scatter.py` – Generates scatter plot panel.
  - `plot_barplot.py` – Generates bar plot panel.
  - `plot_heatmap_annotations.py` – Generates RNA binding protein heatmap + annotation panels.
  

- `.gitignore` – To ignore Python cache files and Jupyter checkpoints.
- `LICENSE` – Recommended license (MIT).  

## Exercises Overview

**Exercise 2**:

1. **Scatter Plot**: Visualizes relationships between two variables from `10_project_data_scatter.csv`.  
2. **Bar Plot**: Compares multiple conditions using `10_project_data_barplot.csv`.  
3. **Heatmap + Annotations**: Reuse of Exercise 1's(from different repository) RNA binding protein heatmap and genomic annotations panels.  

The figure is arranged in a **multi-panel layout** using Matplotlib gridspec, combining scatter, bar, heatmap, and annotations in a single figure.

## Libraries Used

- Python 3.x  
- `pandas`, `numpy`, `matplotlib`, `seaborn`

## How to Use

1. Clone the repository:
```bash
git clone https://github.com/Kin-zala/genomic-visualization_2.git
```

## output

![Multi-panel genomic visualization displaying scatter plot and bar plot in upper panels with RNA binding protein heatmap and gene annotations in lower panels](https://github.com/Kin-zala/genomic-visualization_2/blob/913decdf4e67c64a4e94a45e51530b5268e52989/Images/full_figure_example.png)
