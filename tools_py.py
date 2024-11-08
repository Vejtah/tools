import random
import math
import pygame

class Tools:
    # math
    def ran_pos_circle(self, radius=1, x=0, y=0, precision=1):

        radius = round(radius * precision)  # convert radius to integer

        rand_x = random.randint(radius * -1, radius)
        rand_y = random.randint(radius * -1, radius)

        while ((rand_x * rand_x) + (rand_y * rand_y)) ** 0.5 >= radius:
            rand_x = random.randint(radius * -1, radius)
            rand_y = random.randint(radius * -1, radius)

        rand_x /= precision
        rand_y /= precision

        x_pos = rand_x + x
        y_pos = rand_y + y

        return x_pos, y_pos


    def pytagoras(self, x_lengh, y_lengh):
        hyp = round(math.sqrt(pow(x_lengh, 2) + pow(y_lengh, 2)))
        return hyp
    

    # pygame
    def pixel(self, pos_x, pos_y):
        global screen
        pygame.draw.circle(screen, (0, 255, 0), (pos_x, pos_y), 1)


    # lists
    def most_frequent(self, list):
        counter = 0
        num = list[0]
        for i in list:
            curr_frequency = list.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i
        return num





