from time import sleep

from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(2000), desc='Мой первый прогресс-бар'):
        sleep(0.003)
    for i in tqdm(range(1000), desc='А вот и второй'):
        sleep(0.001)
    print('Ну наконец-то это случилось! ДОЖДАЛИСЬ!')
