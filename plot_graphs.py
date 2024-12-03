import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

files = ["Multiple_Length_Tests/multiple_length_bottom_up_optimized",
         "Multiple_Length_Tests/multiple_length_equal_partition",
         "Multiple_Length_Tests/multiple_length_memorizes_top_down",
         "Multiple_Length_Tests/multiple_length_tabulation_bottom_up"]

def parse_file(filename):
    path =  "Tests/" + filename + ".csv"
    df = pd.read_csv(path, sep=',')
    return df

def plot_means(files):
    color_list = ['g', 'r', 'c', 'm', 'y', 'k']
    for filename in files:

        color = color_list.pop()

        # Parse file
        df = parse_file(filename)

        # Get collumns
        df = df[["Array size", "Execution time (s)"]]

        # Group by Array Size
        df = df.groupby("Array size")['Execution time (s)'].mean().reset_index()

        # Divide arrays
        array_size = df["Array size"]
        exec_time = df["Execution time (s)"]

        # Plot datas
        plt.plot(array_size, exec_time, label=filename, color=color)

        plt.scatter(array_size, exec_time, color=color, alpha=0.2, marker='o')  # Line plotj

        # Plot points
        if (filename == "Multiple_Length_Tests/multiple_length_bottom_up_optimized"): 
            for i in df.index:
                if (i%2 == 0):
                    plt.text(array_size[i],
                            exec_time[i] * 1.2,
                            f'{exec_time[i]:.5f}',
                            ha='center',
                            va='bottom',
                            color=color[0],
                            fontsize=10,
                            rotation=65)

        if (filename == "Multiple_Length_Tests/multiple_length_equal_partition"):
            for i in df.index:
                if (i%2 == 0):
                    plt.text(array_size[i],
                            exec_time[i] * 1.2,
                            f'{exec_time[i]:.5f}',
                            ha='center',
                            va='bottom',
                            color=color[0],
                            fontsize=10)

    plt.ylabel('Execution time (s)')
    plt.xlabel('Array size')
    plt.title('Execution time (s) x Array size')
    plt.legend()
    plt.grid(True)

    plt.yscale('log')

    path =  "Tests/" + filename
    plt.show()

plot_means(files)
