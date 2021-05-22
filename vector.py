def vector_zeros(length):
    vector = []
    for i in range(length):
        vector.append(0)
    return vector

def vector_ones(length):
    vector = []
    for i in range(length):
        vector.append(1)
    return vector

def diagonal(a):
    diagonal = []
    for i in range(len(a)):
        diagonal.append(a[i][i])
    return diagonal

def copy_vector(original):
    copy = []
    for element in original:
        copy.append(element)
    return copy

def vectors_sub(vector1, vector2):
    tmp = copy_vector(vector1)
    for i in range(len(tmp)):
        tmp[i] -= vector2[i]
    return tmp

def vectors_add(self, vector1, vector2):
    tmp = self.copy_vector(vector1)
    for i in range(len(tmp)):
        tmp[i] += vector2[i]
    return tmp

def norm(vector):
    result = 0
    for element in vector:
        result += element ** 2
    result **= 0.5
    return result