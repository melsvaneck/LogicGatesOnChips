import matplotlib.pyplot as plt


def make_grid(netlist, size = 25):
    '''
    Visualize points on the grid
    '''
    # Convert data to useful data
    size += 1
    x,y = zip(*netlist)

    # scatter points
    plt.figure(figsize=(16,16))
    plt.scatter(x, y, linewidths=8, color='red')

    # Set range and differnce per line (one)
    plt.xticks(range(0,size,1))
    plt.yticks(range(0,size,1))

    # Set view limit
    plt.xlim([-1,size])
    plt.ylim([-1,size])

    # activate grid
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    netlist_1 = [(23, 4), (5, 7), (1, 0), (15, 21), (3, 5), (7, 13), (3, 23),
                 (23, 8), (22, 13), (15, 17), (20, 10), (15, 8), (13, 18),
                 (19, 2), (22, 11), (10, 4), (11, 24), (3, 15), (2, 20),
                 (3, 4), (20, 19), (16, 9), (19, 5), (3, 0), (15, 5),
                 (6, 14), (7, 9), (9, 13), (22, 16), (10, 7)]

    make_grid(netlist_1)
