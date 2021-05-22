import math
import os
import csv
from matplotlib import pyplot
import matplotlib


def interpolation_function(points):
    def f(x):
        res = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            mult = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    xj, yj = points[j]
                    mult *= (float(x) - float(xj))/(float(xi) - float(xj))
            res += float(yi) * mult
        return res
    return f

def interpolate_lagrange(k):
    for file in os.listdir("./data"):
        f = open("./data/" + file, 'r')
        data = list(csv.reader(f))

        interpolation_data = data[1::k]
        F = interpolation_function(interpolation_data)

        distance = []
        h = []
        interpolated_h = []
        for point in data[1::]:
            x, y = point
            distance.append(float(x))
            h.append(float(y))
            interpolated_h.append(F(float))

        train_distance = []
        train_h = []
        for point in interpolation_data:
            x, y = point
            train_distance.append(x)
            train_h.append(y)
        
        # komentarz - aproksymacja bez oscylacji
        # n = math.floor(len(distance)/3)
        # pyplot.plot(distance[n::2*n], h[n::2*n], 'r.', label="pelne dane")
        # pyplot.plot(distance[n::2*n], interpolated_h[n::2*n], color="blue", label="funkcja interpolujaca")
        # pyplot.plot(train_distance[n::2*n], train_h[n::2*n], 'g.', label="dane do interpolacji")

        pyplot.semilogy(distance, h, 'r.', label="pelne dane")
        pyplot.semilogy(distance, interpolated_h, color="blue", label="funkcja interpolujaca")
        pyplot.semilogy(train_distance, train_h, 'g.', label="dane do interpolacji")

        pyplot.legend()
        pyplot.ylabel("Wysokosc")
        pyplot.xlabel("Odleglosc")
        pyplot.title("Przyblizenie interpolacja Lagranga \'a, " + str(len(interpolation_data)) + ' punktow')
        pyplot.suptitle(file)
        pyplot.grid()
        pyplot.show()
