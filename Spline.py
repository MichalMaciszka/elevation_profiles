import os
import csv
import matrix, vector, solving
from matplotlib import pyplot
import random


def interpolation_function(points):
    def calculate_params():
        n = len(points)

        A = matrix.matrix_zeros(4 * (n - 1), 4 * (n - 1))
        b = vector.vector_zeros(4 * (n - 1))

        # Si(xj) = f(xj)
        for i in range(n - 1):
            x, y = points[i]
            row = vector.vector_zeros(4 * (n - 1))
            row[4 * i + 3] = 1
            A[4 * i + 3] = vector.copy_vector(row)
            b[4 * i + 3] = float(y)
        
        # Sj(xj+1) = f(xj+1)
        for i in range(n - 1):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = vector.vector_zeros(4 * (n - 1))
            row[4 * i] = h ** 3
            row[4 * i + 1] = h ** 2
            row[4 * i + 2] = h
            row[4 * i + 3] = 1

            A[4 * i + 2] = row.copy()
            b[4 * i + 2] = float(y1)

        # Sj-1'(xj) = Sj'(xj)
        for i in range(n - 2):
            x1, y1 = points[i+1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = vector.vector_zeros(4 * (n - 1))
            row[4 * i] = 3 * (h ** 2)
            row[4 * i + 1] = 2 * h
            row[4 * i + 2] = 1
            row[4 * (i + 1) + 2] = -1

            A[4 * i] = row.copy()
            b[4 * i] = float(0)

        # Sj-1''(xj) = Sj''(xj)
        for i in range(n - 2):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = vector.vector_zeros(4 * (n - 1))
            row[4 * i] = 6 * h
            row[4 * i + 1] = 2
            row[4 * (i + 1) + 1] = -2

            A[4 * (i + 1) + 1] = vector.copy_vector(row)
            b[4 * (i + 1) + 1] = float(0)

        # S0''(x0) = 0, Sn-1''(xn-1) = 0
        row = vector.vector_zeros(4 * (n - 1))
        row[1] = 2
        A[1] = row.copy()
        b[1] = 0.0

        row = vector.vector_zeros(4 * (n - 1))
        x1, y1 = points[-1]
        x0, y0 = points[-2]
        h = float(x1) - float(x0)
        row[1] = 2
        row[-4] = 6 * h
        A[-4] = vector.copy_vector(row)
        b[-4] = 0.0

        result = solving.lu_factor(A, b)
        return result
    
    params = calculate_params()

    def f(x):
        array = []
        row = []
        for param in params:
            row.append(param)
            if len(row) == 4:
                array.append(row.copy())
                row.clear()
        
        for i in range(1, len(points)):
            xi, yi = points[i-1]
            xj, yj = points[i]
            if float(xi) <= x <= float(xj):
                a, b, c, d = array[i - 1]
                h = x - float(xi)
                val = a * (h**3) + b * (h**2) + c * h + d
                # print(val)
                return val
        return -999
    return f


def interpolate_spline(k, rand=False):
    for file in os.listdir("./data"):
        if file.find(".csv") == -1:
            continue
        f = open("./data/" + file, 'r')
        data = list(csv.reader(f))
        data.pop(0)

        shift = (-1) * (len(data) % k)
        if shift != 0:
            interpolation_data = data[:shift:k]
        else:
            interpolation_data = data[::k]

        if rand:
            for i in range(len(interpolation_data)):
                interpolation_data[i] = random.choice(data)
            if shift != 0:
                interpolation_data[0] = data[:shift:k][0]
                interpolation_data[-1] = data[:shift:k][-1]
            else:
                interpolation_data[0] = data[::k][0]
                interpolation_data[-1] = data[::k][-1]
        
        F = interpolation_function(interpolation_data)
        
        distance = []
        h = []
        interpolated_h = []
        for point in data:
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

        shift = (-1) * interpolated_h.count(-999)

        if shift != 0:
            pyplot.plot(distance[:shift], h[:shift], 'r.', label="pelne dane")
            pyplot.plot(distance[:shift], interpolated_h[:shift], color="blue", label="funkcja interpolujaca")
            pyplot.plot(train_distance, train_h, 'g.', label="dane do interpolacji")
        else:
            pyplot.plot(distance, h, 'r.', label="pelne dane")
            pyplot.plot(distance, interpolated_h, color="blue", label="funkcja interpolujaca")
            pyplot.plot(train_distance, train_h, 'g.', label="dane do interpolacji")
        pyplot.legend()
        pyplot.ylabel("Wysokosc")
        pyplot.xlabel("Odleglosc")
        pyplot.title("Przyblizenie interpolacja Spline, " + str(len(interpolation_data)) + " punkt??w")
        pyplot.suptitle(file)
        pyplot.grid()
        pyplot.show()
