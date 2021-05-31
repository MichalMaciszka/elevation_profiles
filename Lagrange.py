import os
import csv
from matplotlib import pyplot
import random


def interpolation_function(points):
    def f(x):
        res = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            mult = 1.0
            for j in range(n):
                if i != j:
                    xj, yj = points[j]
                    mult *= (float(x) - float(xj))/(float(xi) - float(xj))
            res += float(yi) * mult
        return res
    return f


def interpolate_lagrange(k, rand=False):
    for file in os.listdir("./data"):
        f = open("./data/" + file, 'r')
        if file.find(".csv") == -1:
            continue
        data = list(csv.reader(f))

        interpolation_data = data[1::k]

        if rand:
            for i in range(len(interpolation_data)):
                x = random.choice(data[1::])
                if x not in interpolation_data:
                    interpolation_data[i] = x
            interpolation_data[0] = data[1]
            interpolation_data[-1] = data[-1]
            interpolation_data = interpolation_data[1::]

        F = interpolation_function(interpolation_data)

        distance = []
        h = []
        interpolated_h = []
        for point in data[1::]:
            x, y = point
            distance.append(float(x))
            h.append(float(y))
            interpolated_h.append(F(float(x)))

        train_distance = []
        train_h = []
        for point in interpolation_data:
            x, y = point
            train_distance.append(float(x))
            train_h.append(float(y))

        pyplot.plot(distance, h, 'r.', label="pelne dane")
        pyplot.plot(distance, interpolated_h, color="blue", label="funkcja interpolujaca")
        pyplot.plot(train_distance, train_h, 'g.', label="dane do interpolacji")

        pyplot.legend()
        pyplot.ylabel("Wysokosc")
        pyplot.xlabel("Odleglosc")
        pyplot.title("Przyblizenie interpolacja Lagranga, " + str(len(interpolation_data)) + ' punktow')
        pyplot.suptitle(file)
        pyplot.grid()
        pyplot.show()
