import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm  # colour map
import csv


def make_colours(num_items):
    """Generates colours for num_item items"""
    # We'll generate enough numbers between 0 and 1 and choose their colours from colormap Set1.
    # The use of float() is only needed for Python 2 (because it would otherwise be integer division).
    colornums = []
    for n in range(num_items):
        colornums.append(n / float(num_items))
    cs = cm.Set1(colornums)
    return cs


def process_info(names, data):
    # What does this for-loop do?
    descriptions = []
    for i in range(0, len(data)):
        descriptions.append(names[i] + " (" + str(data[i]) + "%)")

    # We need as many colours as data items
    num_items = len(data)
    cs = make_colours(num_items)

    return (data, descriptions, cs)


def read_info(filename):
    z = 0
    types_of_energy = []
    percentages_of_energy = []
    lista = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        firstline = True
        for row in your_list:
            if firstline:  # skip first line
                firstline = False
                continue
            types_of_energy.append(row[0]);
            percentages_of_energy.append(row[1])

    print(types_of_energy)
    print(percentages_of_energy)
    return (types_of_energy, percentages_of_energy)


def make_pie_plot(values, labels, cols):
    # Draw the pie chart
    plt.pie(values, colors=cols)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    # Provide a legend whose 'centre left' is shifted outside the axes
    plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))

    # Add a title
    plt.title('Proportions of electricity sources')

    # Save the image and make sure the extent of the image includes the legend,
    # which was shifted outside.
    plt.savefig("pie.png", bbox_inches='tight')


def make_barh_plot(values, labels, cols):
    y_pos = np.arange(len(labels))
    val = [float(i) for i in values];
    performance = val

    plt.barh(y_pos, performance, align='center', alpha=0.4, color=cols)
    plt.yticks(y_pos, labels)
    plt.xlabel('percentages_of_energy')
    plt.title('Proportions of electricity sources')
    #plt.show()
    plt.savefig("bar.png", bbox_inches='tight')


def main():
    (types, percents) = read_info("energy.csv")
    (data, names, colours) = process_info(types, percents)

    #make_pie_plot(data, names, colours)
    make_barh_plot(data, names, colours)


if __name__ == "__main__":
    main()
