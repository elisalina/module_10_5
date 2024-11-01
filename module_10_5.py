import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data[0:-1])

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
# Линейный вызов
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])

end = datetime.datetime.now()
print(f'{end - start} (линейный)')
# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)

    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')