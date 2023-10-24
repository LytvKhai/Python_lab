import numpy as np
import matplotlib.pyplot as plt
import math

# Варіант 18
DATA = [
    "0GPGGA,060443.00,4950.4848,N,03638.5903,E,1,04,14.0,135.6,M,16.2,M,,*55",
    "0GPGGA,060444.00,4950.4849,N,03638.5903,E,1,04,14.0,135.4,M,16.2,M,,*51",
    "0GPGGA,060445.00,4950.4850,N,03638.5904,E,1,04,14.0,135.2,M,16.2,M,,*59",
    "0GPGGA,060446.00,4950.4851,N,03638.5903,E,1,04,14.0,135.1,M,16.2,M,,*5F",
    "0GPGGA,060447.00,4950.4852,N,03638.5904,E,1,04,14.0,134.9,M,16.2,M,,*53",
    "0GPGGA,060448.00,4950.4853,N,03638.5904,E,1,04,14.0,134.8,M,16.2,M,,*5C",
    "0GPGGA,060449.00,4950.4854,N,03638.5903,E,1,04,14.0,134.6,M,16.2,M,,*53",
    "0GPGGA,060450.00,4950.4856,N,03638.5903,E,1,04,13.9,134.5,M,16.2,M,,*54",
    "0GPGGA,060451.00,4950.4857,N,03638.5903,E,1,04,13.9,134.4,M,16.2,M,,*55",
    "0GPGGA,060452.00,4950.4858,N,03638.5903,E,1,04,13.9,134.3,M,16.2,M,,*5E",
    "0GPGGA,060453.00,4950.4859,N,03638.5903,E,1,04,13.9,134.1,M,16.2,M,,*5C",
    "0GPGGA,060454.00,4950.4860,N,03638.5903,E,1,04,13.9,133.9,M,16.2,M,,*5E",
    "0GPGGA,060455.00,4950.4863,N,03638.5903,E,1,04,13.9,133.7,M,16.2,M,,*52",
    "0GPGGA,060456.00,4950.4889,N,03638.5909,E,1,04,13.9,131.0,M,16.2,M,,*5A",
    "0GPGGA,060457.00,4950.4915,N,03638.5907,E,1,04,14.3,127.9,M,16.2,M,,*52",
    "0GPGGA,060458.00,4950.4937,N,03638.5897,E,1,04,14.3,124.1,M,16.2,M,,*5E",
    "0GPGGA,060459.00,4950.4954,N,03638.5884,E,1,04,14.3,119.3,M,16.2,M,,*54",
    "0GPGGA,060500.00,4950.4974,N,03638.5874,E,1,04,14.3,114.1,M,16.2,M,,*5B",
    "0GPGGA,060501.00,4950.4991,N,03638.5860,E,1,04,14.3,109.3,M,16.2,M,,*5A",
    "0GPGGA,060502.00,4950.5011,N,03638.5852,E,1,04,13.9,106.1,M,16.2,M,,*58",
    "0GPGGA,060503.00,4950.5031,N,03638.5843,E,1,04,13.9,104.4,M,16.2,M,,*5C"
]

R = 6371


def data_extraction():
    times = np.array([convert_to_seconds(line.split(",")[1]) for line in DATA])
    latitude = np.array([float(line.split(",")[2]) for line in DATA])
    longitude = np.array([float(line.split(",")[4]) for line in DATA])
    heights = np.array([float(line.split(",")[9]) for line in DATA])
    h_accuracy = np.array([float(line.split(",")[8]) for line in DATA])
    return times, latitude, longitude, heights, h_accuracy


def convert_to_seconds(time_str):
    hours = int(time_str[0:2])
    minutes = int(time_str[2:4])
    seconds = int(time_str[4:6])
    fractions = int(time_str[7:])
    return hours * 3600 + minutes * 60 + seconds + fractions / 100


def calculation_info(times_cv, heights_cv, h_accuracy_cv):
    print(times_cv)
    time_diff = np.diff(times_cv)

    # Сумарна довжина маршруту
    total_distance = np.sum(h_accuracy_cv[:-1] * time_diff)

    # Середня швидкість польоту
    average_speed = total_distance / (times_cv[-1] - times_cv[0])

    speed = np.array(h_accuracy_cv[:-1] / time_diff)

    # Мінімальна і максимальна швидкість польоту
    min_speed = np.min(speed)
    max_speed = np.max(speed)

    # Мінімальна і максимальна висота польоту
    min_height = np.min(heights_cv)
    max_height = np.max(heights_cv)

    # Загальний час польоту
    total_flight_time = times_cv[-1] - times_cv[0]

    print(f'Сумарна довжина маршруту польоту:{total_distance} метрів')
    print(f'Середня швидкість польоту: {average_speed} м/с')
    print(f'Мінімальна швидкість: {min_speed} м/с')
    print(f'Максимальна швидкість: {max_speed} м/с')
    print(f'Мінімальна висота: {min_height} м')
    print(f'Максимальна висота: {max_height} м')
    print(f'Загальний час польоту: {convert_seconds_to_time(total_flight_time)}')

    t_distance = np.cumsum(h_accuracy_cv[:-1] * time_diff)
    return speed, t_distance


def print_chart(times_cv, heights_cv, speed, t_distance, latitude, longitude):
    time = np.array([convert_seconds_to_time(t) for t in times_cv])

    latitude_s = np.array([line.split(",")[2] for line in DATA])
    longitude_s = np.array([line.split(",")[4] for line in DATA])

    #траєкторія руху літака в координатах (широта, довгота, висота)
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(latitude, longitude, heights_cv)
    ax.set_xticklabels(latitude_s)
    ax.set_yticklabels(longitude_s)
    ax.set_xlabel("широта")
    ax.set_ylabel("довгота")
    ax.set_zlabel("висота")

    # Швидкість польоту від часу
    plt.figure(figsize=(20, plt.gcf().get_figheight()))
    plt.plot(time[1:], speed)
    plt.title('Швидкість польоту')
    plt.xlabel('час')
    plt.ylabel('швидкість польоту (м/с)')
    plt.show()

    # Висота польоту від часу
    plt.figure(figsize=(20, plt.gcf().get_figheight()))
    plt.plot(time, heights_cv)
    plt.title('Висота польоту')
    plt.xlabel('час')
    plt.ylabel('висота польоту (м)')
    plt.show()

    # Пройдений час від шляху
    plt.figure(figsize=(20, plt.gcf().get_figheight()))
    plt.plot(time[1:], t_distance)
    plt.title('Пройдений шлях')
    plt.xlabel('час')
    plt.ylabel('пройдений шлях (м)')
    plt.show()


def convert_seconds_to_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def _main():
    times, latitude, longitude, heights, h_accuracy = data_extraction()
    speed, t_distance = calculation_info(times, heights, h_accuracy)
    print_chart(times, heights, speed, t_distance, latitude, longitude)


if __name__ == '__main__':
    _main()
