from matplotlib import pyplot
from time import time
import imageio

def animate(parameters, t=0, t_step=.00001, frame_c=15):

    # unpack parameters
    x, y, a = parameters

    # list to hold all the frames
    frames = []
    iteration = 0


     # 15 frames a second for 1 second
    # iteravely pass t to get each frame
    while t < frame_c*t_step:

        # lists to hold paths
        x_list = [x]
        y_list = [y]

        # iteratively pass (x,y) into the quadratic map
        for i in range(10000):

            # compute next point
            x_next = a[0] + a[1]*x*t + a[2]*x*x + a[3]*y + a[4]*y*y + a[5]*x*y
            y_next = a[6] + a[7]*x + a[8]*x*x + a[9]*y + a[10]*y*y + a[11]*x*y*t

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
        pyplot.scatter(x_list, y_list, s=0.1, c="white", linewidth=0)
                        
        # save the plot
        name = str(iteration)
        pyplot.savefig("frames/" + name + ".png", transparent = False, dpi=100)

        # create the imageio image and add to frames
        image = imageio.v2.imread("frames/" + name + ".png")
        frames.append(image)

        # increase t by t_step
        t += t_step
        iteration += 1;


    name = str(time())
    imageio.mimsave("animations/" + name + ".gif", frames, fps=3)

parameters = (-0.21989189908893003, 0.03669586644649003, [-1.0865147769151133, 0.41448326459617446, 0.8193863496374583, 1.545404339136966, 1.318475100755344, 1.2541506090435166, -0.47940694878064427, -0.42683602894541517, -0.2682364583734369, 0.22890888203620507, 1.0981302448019536, 1.097397339718217])

animate(parameters)


