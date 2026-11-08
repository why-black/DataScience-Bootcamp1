import sys
import os
import psutil

def file_read_generator(path):
    with open(path, 'r') as f:
        for line in f:
            yield line

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('must be 2 args')
    path = sys.argv[1]

    process = psutil.Process(os.getpid())
    start_times = process.cpu_times()

    for line in file_read_generator(path):
        pass

    end_times = process.cpu_times()
    total_time = (end_times.user - start_times.user) + (end_times.system - start_times.system)

    print(f"Peak Memory Usage = {(process.memory_info().rss / 1024 / 1024 / 1024):.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")