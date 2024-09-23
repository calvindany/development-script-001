from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

def leadership_graph_bar(labels, values):
    # Creating the bar chart
    fig, ax = plt.subplots()
    # Adding rounded bars using FancyBboxPatch
    for i, value in enumerate(values):
        if value == 0:
            continue  # Skip drawing bars with 0 value
        bar_height = value - 0.05 if value > 0.1 else value
        bar = FancyBboxPatch((i - 0.6 / 2, 0), 0.6, bar_height, 
                             boxstyle="round,pad=0.05", 
                             linewidth=0, edgecolor=None, facecolor='#00626C', zorder=3)
        ax.add_patch(bar)
     
    # Setting the x-axis limits and ticks
    ax.set_xlim(-0.5, len(labels) - 0.5)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
    
    # Adding labels inside the bars (centered and white-colored)
    for i, value in enumerate(values):
        ax.annotate(f'{value}', xy=(i, value / 2),
                    xytext=(0, 0), textcoords="offset points", ha='center', va='center', color='white', fontsize=12)

    # Title and removing y-axis labels
    # ax.set_title('Skor Gaya Kepemimpinan', fontsize=14)
    ax.set_yticks([])  # Remove Y-axis ticks (values)
    ax.set_ylabel('')   # Remove Y-axis label
    
    # Check if all values are 0 to apply custom y-ticks
    if all(v == 0 for v in values):
        yticks = np.linspace(0, 1, 6)  # 5 horizontal lines (6 ticks including 0)
    else:
        max_value = max(values)  # Maximum value for grid scale
        yticks = np.arange(0, max_value + 2, max(max_value // 5, 1))  # Setting y-ticks at regular intervals
    ax.set_yticks(yticks)  # Apply custom y-ticks

    # Adding horizontal lines (grid) on the y-axis behind bars
    ax.grid(True, axis='y', color='grey', linestyle='--', linewidth=0.7, zorder=0)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    # Remove the y-axis labels but keep the grid
    ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
    
    # Add padding to graph
    fig.tight_layout(pad=0.5)
    
    
    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    image = Image.open(buf)
    plt.close(fig)
    return image

# Create Leadership Graph (Bar)
values = [
    0,
    0,
    0,
    0,
    0,
]
labels = [
    "Consultative",
    "Delegative",
    "Directive",
    "Participative",
    "Persuasive"
]

image = leadership_graph_bar(labels, values)

image.show()