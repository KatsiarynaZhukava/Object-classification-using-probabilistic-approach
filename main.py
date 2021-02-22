import math

import matplotlib.pyplot as plt
import numpy as np

class Object:
    value = 0
    object_class = 0

    def __init__(self, value, object_class):
        self.value = value
        self.object_class = object_class


CLASS_DELIMITER_VALUE = 1 # Величины, большие 1, относим к 1му классу, меньшие 1 - к 0му
CENTRE = 2       # Mean (“centre”) of the distribution
DEVIATION = 0.4     # Standard deviation (spread or “width”) of the distribution. Must be non-negative
SIZE = 1000     # Output shape. A single value is returned if loc and scale are both scalars
P_class1_value1 = 0.4
P_class1_value2 = 0.7

s = np.random.normal(CENTRE, DEVIATION, SIZE)

expected_value = 0  # Математическое ожидание
for element in s:
    expected_value += element
expected_value /= s.size

print(expected_value)

standard_deviation = 0      # Среднеквадратичное отклонение
for element in s:
    standard_deviation += (element - expected_value) ** 2
standard_deviation /= s.size
standard_deviation = math.sqrt(standard_deviation)

print(standard_deviation)

x = np.linspace(0, 20, 100)
fn = (1/(standard_deviation * math.sqrt(2 * math.pi))) * math.exp((-1/2) * ((x - expected_value)/standard_deviation) ** 2)
#fn = x ** 2

fig = plt.figure()
plt.plot(x, fn * P_class1_value1, 'r')
plt.plot(x, fn * P_class1_value2, 'r')
plt.show()