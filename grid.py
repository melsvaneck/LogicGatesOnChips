import matplotlib.pyplot as plt

netlist_1 = [(23, 4), (5, 7), (1, 0), (15, 21), (3, 5), (7, 13), (3, 23), (23, 8), (22, 13), (15, 17), (20, 10), (15, 8), (13, 18), (19, 2), (22, 11), (10, 4), (11, 24), (3, 15), (2, 20), (3, 4), (20, 19), (16, 9), (19, 5), (3, 0), (15, 5), (6, 14), (7, 9), (9, 13), (22, 16), (10, 7)]

def make_grid(netlist):
    plt.figure(figsize=(16,16))
    x,y = zip(*netlist_1)
    plt.scatter(x, y)
    plt.xticks(range(25))
    plt.yticks(range(25))
    plt.xlim([0,25])
    plt.ylim([0,25])
    plt.grid(True)
    plt.show()
