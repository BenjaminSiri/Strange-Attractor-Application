# Ben Siri 4-12-23
import random
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot
import math
from time import time

def search_attractors(n = 1):

    found = 0

    while (found < n):
        # initialize convergence and lyapunov
        converging = False
        lyapunov = 0

        # random starting point
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        # random alternative point nearby
        xe = x + random.uniform(-0.5, 0.5) / 1000
        ye = y + random.uniform(-0.5, 0.5) / 1000

        # distance between the points
        dx = xe - x
        dy = ye - y
        d0 = math.sqrt(dx*dx + dy*dy)

        # random parapeter vector
        a = [random.uniform(-2,2) for i in range(12)]

        # lists to hold paths
        x_list = [x]
        y_list = [y]

        # iteratively pass (x,y) into the quadratic map
        for i in range(10000):

            # compute next point
            x_next = a[0] + a[1]*x + a[2]*x*x + a[3]*y + a[4]*y*y + a[5]*x*y
            y_next = a[6] + a[7]*x + a[8]*x*x + a[9]*y + a[10]*y*y + a[11]*x*y

            # check if it converges to infinity
            if (x_next > 1e10 or y_next > 1e10 or x_next < -1e10 or y_next < -1e10):
                converging = True
                break

            # check if it converging to a single point
            if (abs(x-x_next) < 1e-10 and abs(y-y_next) < 1e-10):
                converging = True
                break

            # check for chaotic behavior
            if (i > 1000):

                # compute next alternative point
                xe_next = a[0] + a[1]*xe + a[2]*xe*xe + a[3]*ye + a[4]*ye*ye + a[5]*xe*ye
                ye_next = a[6] + a[7]*xe + a[8]*xe*xe + a[9]*ye + a[10]*ye*ye + a[11]*xe*ye

                # compute distance between new point and alternative point
                dx = xe_next - x_next
                dy = ye_next - y_next
                d = math.sqrt(dx*dx + dy*dy)

                # lyapunov exponent
                lyapunov += math.log(abs(d/d0))

                # rescale the alternatve point
                xe = x_next + d0*dx/d
                ye = y_next + d0*dy/d

            # update (x,y)
            x = x_next
            y = y_next

            # store (x,y) om the path lists
            x_list.append(x)
            y_list.append(y)

        if (not converging and lyapunov >= 10):
            found += 1
            #print("Strange attractor with L = " + str(lyapunov))

            pyplot.clf()

            # plot design
            pyplot.style.use("dark_background")
            pyplot.axis("off")

            # create the plot
            pyplot.scatter(x_list[100:], y_list[100:], s=0.1, c="white", linewidth=0)
            
            # save the plot
            #name = str(time())
            #pyplot.savefig("store/" + name + ".png", dpi=200)

            # save the parameters
            parameters = (x_list[0], y_list[0], a)
            #file = open("store/" + name + ".txt", "w+")
            #file.write(str(parameters))

            return parameters