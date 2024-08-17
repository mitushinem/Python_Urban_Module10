from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name) as f:
        lines = f.readlines()
        all_data.append(lines)


if __name__ == '__main__':

    start_dt = datetime.now()

    path_list = [f'./files/file {i}.txt' for i in range(1, 5)]
    for path in path_list:
        read_info(path)
    print(datetime.now() - start_dt)

    start_dt = datetime.now()

    with Pool(processes=4) as pool:
        pool.map(read_info, path_list)

    print(datetime.now() - start_dt)
