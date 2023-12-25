# The Vector class represents a vector in a multidimensional space.
class Vector(object):
    # This is the constructor method, which initializes a Vector object with a set of coordinates.
    # It checks that the coordinates are nonempty and form a valid iterable.
    # It stores the coordinates as a tuple and determines the dimension of the vector.
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError("The coordinates must be nonempty")
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    # This method provides a human-readable string representation of the vector when you try to print it using print().
    # It returns a string in the format "Vector: (coordinate1, coordinate2, ...)".
    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    # This method is used to compare two vectors for equality.
    # It returns True if the coordinates of the two vectors are equal, and False otherwise.
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    # a method to the Vector class that performs vector addition
    # The add method checks whether the two vectors have the same dimension before performing the addition.
    # If they have different dimensions, it raises a ValueError. If the dimensions match,
    # it creates a new vector with coordinates equal to the sum of corresponding coordinates of the two vectors.
    def add(self, v):
        if self.dimension != v.dimension:
            raise ValueError("Vectors must have the same dimension for addition")

        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # a method to the Vector class for vector subtraction
    # the subtract method checks whether the two vectors have the same dimension before performing the subtraction.
    # If they have different dimensions, it raises a ValueError. If the dimensions match,
    # it creates a new vector with coordinates equal to the difference of corresponding coordinates of the two vectors.
    def subtract(self, v):
        if self.dimension != v.dimension:
            raise ValueError("Vectors must have the same dimension for subtraction")

        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # a method to the Vector class To scalar multiply vectors (multiply a vector by a scalar)
    # The scalar_multiply method creates a new vector with coordinates equal to the product of the scalar and the coordinates of the original vector.
    # The scalar is a number that is multiplied by each coordinate of the vector.
    # The scalar is passed as a parameter to the method.
    # The method returns the new vector.
    def scalar_multiply(self, scalar):
        new_coordinates = [scalar * x for x in self.coordinates]
        return Vector(new_coordinates)

    # a method to the Vector class To calculate the magnitude of a vector
    # The magnitude method calculates the magnitude of a vector by squaring each coordinate and summing the results.
    # The square root of the sum is the magnitude of the vector.
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sum(coordinates_squared) ** 0.5


# Example usage for the add method
v1 = Vector([7.119, 8.215])
v2 = Vector([-8.223, 0.878])

v_sum = v1.add(v2)
print("Add method output-->", v_sum)

# Example usage for the subtract method
v_diff = v1.subtract(v2)
print("Subtract method output-->", v_diff)

# Example usage for scalar
v1 = Vector([1.671, -1.012, -0.318])
scalar = 7.41

v_scaled = v1.scalar_multiply(scalar)
print("Scalar method ouput-->", v_scaled)

# Example usage for magnitude
v1 = Vector([1, 2, 3])

magnitude_v1 = v1.magnitude()
print("Magnitude method ouput-->", magnitude_v1)