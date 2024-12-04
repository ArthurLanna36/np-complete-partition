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

def plot_means(filename, color):
    # Parse file
    df = parse_file(filename)

    # Get collumns
    df = df[["Array size", "Execution time (s)"]]

    # Group by Array Size and calc means
    df = df.groupby("Array size")['Execution time (s)'].mean().reset_index()

    # Divide arrays
    array_size = df["Array size"]
    exec_time = df["Execution time (s)"]

    plt.figure(figsize=(12, 8))

    # Plot datas
    plt.plot(array_size, exec_time, label=filename, color=color)

    # Plot points
    for i in df.index:
        if (array_size[i] % 50.0 == 0.0):
            plt.scatter(array_size[i],
                        exec_time[i],
                        color=color,
                        marker='o')
            plt.text(array_size[i],
                    exec_time[i] + 0.005,
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

    max = exec_time[len(exec_time) - 1] * 1.5

    plt.ylim(0, max)

    path =  "Tests/" + filename
    plt.savefig(path, dpi=300)
    plt.close()

color_list = ['g', 'r', 'c', 'm', 'y', 'k']


for filename in files:
    color = color_list.pop()
    plot_means(filename, color)
