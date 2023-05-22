from matplotlib import pyplot
from time import time

def draw(parameters):

    # unpack parameters
    x, y, a = parameters

    # lists to hold paths
    x_list = [x]
    y_list = [y]

    # iteratively pass (x,y) into the quadratic map
    for i in range(10000):

        # compute next point
        x_next = a[0] + a[1]*x + a[2]*x*x + a[3]*y + a[4]*y*y + a[5]*x*y
        y_next = a[6] + a[7]*x + a[8]*x*x + a[9]*y + a[10]*y*y + a[11]*x*y


        # update (x,y)
        x = x_next
        y = y_next

        # store (x,y) om the path lists
        x_list.append(x)
        y_list.append(y)

    pyplot.clf()

    # plot design
    pyplot.style.use("dark_background")
    pyplot.axis("off")

    # create the plot
    pyplot.scatter(x_list[100:], y_list[100:], s=0.1, c="white", linewidth=0)

    # save the plot
    return pyplot.gcf()
