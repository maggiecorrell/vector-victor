def shape(vector):
    return (len(vector),)

def vector_add(vector1, vector2):
    return [item1 + item2 for item1, item2 in zip(vector1, vector2)]
