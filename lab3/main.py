import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Считывание данных с файла
data = pd.read_csv('file.csv')
time = data['time']
heading = data['head']
pitch = data['pitch']


# Графические зависимости для задания 1, 2
def figures():
    # Графики без шага
    print_figure(time, heading, 'Залежність кутів курсу від часу')
    print_figure(time, pitch, 'Залежність кутів крену від часу')

    # усреднённые графики с шагом 10 секунд
    step = 10
    averaged_time_10_step, averaged_heading_10_step, averaged_pitch_10_step = averaged_with_step(step)
    print_figure(averaged_time_10_step, averaged_heading_10_step,
                 f'Залежність усереднених кутів курсу від часу (шаг {step} секунд)')
    print_figure(averaged_time_10_step, averaged_pitch_10_step,
                 f'Залежність усереднених кутів крену від часу(шаг {step} секунд)')

    # усреднённые графики с шагом 20 секунд
    step = 20
    averaged_time_20_step, averaged_heading_20_step, averaged_pitch_20_step = averaged_with_step(step)
    print_figure(averaged_time_20_step, averaged_heading_20_step,
                 f'Залежність усереднених кутів курсу від часу (шаг {step} секунд)')
    print_figure(averaged_time_20_step, averaged_pitch_20_step,
                 f'Залежність усереднених кутів крену від часу(шаг {step} секунд)')

    # графики разницы
    print_triple_figure(time, heading, averaged_time_10_step, averaged_heading_10_step, averaged_time_20_step,
                        averaged_heading_20_step, "Різниця залежністей кутів курсу від часу")
    print_triple_figure(time, pitch, averaged_time_10_step, averaged_pitch_10_step, averaged_time_20_step,
                        averaged_pitch_20_step, "Різниця залежністей кутів крену від часу")


# Подсчёт статистических характеристик
def statistical_characteristics():
    # Средние значения
    mean_heading = np.mean(heading)
    mean_pitch = np.mean(pitch)

    # Подсчёт среднеквадратического отклонения
    std_heading = np.std(heading)
    std_pitch = np.std(pitch)

    # Подсчёт максимальных отклонений от среднего значения
    max_dev_heading = np.max(np.abs(heading - mean_heading))
    max_dev_pitch = np.max(np.abs(pitch - mean_pitch))

    # Вывод результата в терминал
    print(f'Середнє значення куту курсу: {mean_heading} градуси')
    print(f'Середнє значення куту крену: {mean_pitch} градуси')
    print(f'Середньоквадратичне відхилення куту курсу: {std_heading} градуси')
    print(f'Середньоквадратичне відхилення куту крену: {std_pitch} градуси')
    print(f'Максимальне відхилення куту курсу: {max_dev_heading} градуси')
    print(f'Максимальне відхилення куту крену: {max_dev_pitch} градуси')


# Подсчёт усреднённых данных для указаного шага
def averaged_with_step(step):
    averaged_time_step = np.arange(min(time), max(time), step)
    averaged_heading_step = [np.mean(heading[(time >= t) & (time < t + step)]) for t in averaged_time_step]
    averaged_pitch_step = [np.mean(pitch[(time >= t) & (time < t + step)]) for t in averaged_time_step]
    return averaged_time_step, averaged_heading_step, averaged_pitch_step


# Создание графических фигур, с указаными данными, и названием
def print_figure(data_1, data_2, string):
    plt.figure(figsize=(12, 6))
    plt.plot(data_1, data_2)
    plt.xlabel('Час (с)')
    plt.ylabel('Кут (градуси)')
    plt.title(string)
    plt.show()


# Созданий графических фигур разницы, с указанными данными и названием
def print_triple_figure(data_1_1, data_1_2, data_2_1, data_2_2, data_3_1, data_3_2, string):
    plt.figure(figsize=(12, 6))
    plt.plot(data_1_1, data_1_2, label="Не усереднені")
    plt.plot(data_2_1, data_2_2, label="Шаг 10 секунд")
    plt.plot(data_3_1, data_3_2, label="Шаг 20 секунд")
    plt.legend()
    plt.xlabel('Час (с)')
    plt.ylabel('Кут (градуси)')
    plt.title(string)
    plt.show()


if __name__ == '__main__':
    figures()
    statistical_characteristics()
