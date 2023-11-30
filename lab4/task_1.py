import statistics
import random
from fractions import Fraction as F
from decimal import Decimal as D

print("TASK 1")

print('statistics.mean([34, 12, 65, 15]) = '
      f'{statistics.mean([34, 12, 65, 15])}')
print('statistics.mean([F(10, 15), F(47, 93), F(5, 1)]) = '
      f'{statistics.mean([F(10, 15), F(47, 93), F(5, 1)])}')
print('statistics.mean([D("3.4"), D("1.2"), D("6.5"), D("1.5")]) = '
      f'{statistics.mean([D("3.4"), D("1.2"), D("6.5"), D("1.5")])}')

print(f'{"-" * 100}')
print('statistics.mean([random.randint(1, 100) for x in range(1, 1001)]) = '
      f'{statistics.mean([random.randint(1, 100) for x in range(1, 1001)])}')
print(
    'statistics.mean([random.triangular(1, 100, 70) for x in range(1, 1001)]) = '
    f'{statistics.mean([random.triangular(1, 100, 70) for x in range(1, 1001)])}'
)

print(f'{"-" * 100}')
print('statistics.mode([random.randint(1, 100) for x in range(1, 1001)]) = '
      f'{statistics.mode([random.randint(1, 100) for x in range(1, 1001)])}')
print('statistics.mode([random.randint(1, 100) for x in range(1, 1001)]) = '
      f'{statistics.mode([random.randint(1, 100) for x in range(1, 1001)])}')
print('statistics.mode([random.randint(1, 100) for x in range(1, 1001)]) = '
      f'{statistics.mode([random.randint(1, 100) for x in range(1, 1001)])}')
print('statistics.mode(["F-35", "F-16", "SU-27", "F-35", "Cessna 172"]) = '
      f'{statistics.mode(["F-35", "F-16", "SU-27", "F-35", "Cessna 172"])}')

print(f'{"-" * 100}')
print('statistics.median([random.randint(1, 100) for x in range(1, 50)]) = '
      f'{statistics.median([random.randint(1, 100) for x in range(1, 51)])}')
print(
    'statistics.median_grouped([random.randint(1, 100) for x in range(1, 50)]) = '
    f'{statistics.median_grouped([random.randint(1, 100) for x in range(1, 51)])}'
)
print(
    'statistics.median_high([random.randint(1, 100) for x in range(1, 50)]) = '
    f'{statistics.median_high([random.randint(1, 100) for x in range(1, 51)])}'
)
print(
    'statistics.median_low([random.randint(1, 100) for x in range(1, 50)]) = '
    f'{statistics.median_low([random.randint(1, 100) for x in range(1, 51)])}')

print(f'{"-" * 100}')
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'data = {data}')
print('statistics.pvariance(data) = '
      f'{statistics.pvariance(data)}')
print('statistics.pstdev(data) = '
      f'{statistics.pstdev(data)}')
print('statistics.variance(data) = '
      f'{statistics.variance(data)}')

more_data = [3, 4, 5, 5, 5, 5, 5, 6, 6]
print(f'more_data = {more_data}')
print('statistics.pvariance(more_data) = '
      f'{statistics.pvariance(more_data)}')
print('statistics.pstdev(more_data) = '
      f'{statistics.pstdev(more_data)}')
print('statistics.variance(more_data) = '
      f'{statistics.variance(more_data)}')

some_fractions = [F(5, 6), F(2, 7), F(11, 76)]
print(f'some_fractions = {some_fractions}')
print('statistics.pvariance(some_fractions) = '
      f'{statistics.pvariance(some_fractions)}')
print('statistics.pstdev(some_fractions) = '
      f'{statistics.pstdev(some_fractions)}')
print('statistics.variance(some_fractions) = '
      f'{statistics.variance(some_fractions)}')
