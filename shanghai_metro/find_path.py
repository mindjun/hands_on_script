"""
find a path from start to end
"""
import queue
from shanghai_metro.fetch_data import DataFetch


def find_path(start, end):
    data_fetch = DataFetch()
    start_no, end_no = data_fetch.station_no_mapping.get(start), data_fetch.station_no_mapping.get(end)
    if not start_no:
        raise ValueError(f'start station: {start} is error, please check !')
    if not end_no:
        raise ValueError(f'start station: {end} is error, please check !')

    def get_neighbor(_node):
        station_name = data_fetch.stations_dict.get(_node)
        neighbors = list()
        for station_no in data_fetch.station_no_mapping.get(station_name):
            next_no = str(int(station_no) + 1).zfill(4)
            if next_no in data_fetch.stations_dict:
                neighbors.append(next_no)
            last_no = str(int(station_no) - 1).zfill(4)
            if last_no in data_fetch.stations_dict:
                neighbors.append(last_no)

        return neighbors

    # use bfs to find a path
    path_queue = queue.Queue()
    visited = list()

    for no in start_no:
        path_queue.put(no)
        visited.append(no)
    result_list = list()
    while path_queue:
        size = path_queue.qsize()
        for i in range(size):
            node = path_queue.get_nowait()
            if node in end_no:
                path = ''
                for no in result_list:
                    path += f'{data_fetch.stations_dict.get(no)} -> '
                return path
            for neighbor in get_neighbor(node):
                if neighbor not in visited:
                    visited.append(neighbor)
                    # todo 这里的 append 不对
                    result_list.append(neighbor)
                    path_queue.put(neighbor)


print(find_path('九亭', '徐家汇'))
