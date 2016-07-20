class ShapeError(Exception):
    pass

def shape(vector):
    return (len(vector),)

def check_shape(*vectors):
    if len(set([shape(vector) for vector in vectors])) != 1:
        raise ShapeError

def vector_add(vector1, vector2):
    check_shape(vector1, vector2)
    return [item1 + item2 for item1, item2 in zip(vector1, vector2)]

def vector_sub(vector1, vector2):
    check_shape(vector1, vector2)
    return [item1 - item2 for item1, item2 in zip(vector1, vector2)]

def vector_sum(*vectors):
    check_shape(*vectors)
    return [sum(vector) for vector in zip(*vectors)]

def dot(vector1, vector2):
    check_shape(vector1, vector2)
    return sum([item1 * item2 for item1, item2 in zip(vector1, vector2)])

def vector_multiply(vector, scalar):
    return [item1 * scalar for item1 in vector]

def vector_mean(*vectors):
    return [sum(vector) / len(vector) for vector in zip(*vectors)]

def magnitude(vector):
        return (sum([(item)**2 for item in vector]))**.5
