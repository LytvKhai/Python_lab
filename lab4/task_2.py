import statistics


class Colors:
    DEFAULT = '\033[0m'
    CHANGED = '\033[95m'


def statistics_calc(data):
    print(f'{Colors.DEFAULT}Mean = {statistics.mean(data)}')
    print(f'Mode = {statistics.mode(data)}')
    print(f'Median = {statistics.median(data)}')
    print(f'St_deviation = {statistics.stdev(data)}')
    print(f'Variance = {statistics.variance(data)}')


print(f'{Colors.CHANGED}Degree:')
statistics_calc([59, 89, 46, 160, 10, 50, 45, 169, 128, 10])
print(f'{Colors.CHANGED}Velocity:')
statistics_calc([360, 25, 158, 200, 160, 63, 240, 58, 65, 50])
print(f'{Colors.CHANGED}Time:')
statistics_calc([5, 4, 18, 3, 6, 16, 18, 12, 6, 16])
