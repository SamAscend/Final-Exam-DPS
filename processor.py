import time
import threading
import multiprocessing
from my_utils import sort_and_filter


# Sequential
def process_sequential(data):
    start = time.perf_counter()
    _ = sort_and_filter(data)
    end = time.perf_counter()
    return end - start

# Threading
def process_thread(data):
    start = time.perf_counter()
    result = []

    def task():
        result.append(sort_and_filter(data))

    thread = threading.Thread(target=task)
    thread.start()
    thread.join()

    end = time.perf_counter()
    return end - start

# Multiprocessing
def task(data, queue):
    result = sort_and_filter(data)
    queue.put(result)

def process_multiprocessing(data):
    start = time.perf_counter()
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=task, args=(data, queue))
    process.start()
    process.join()
    _ = queue.get()
    end = time.perf_counter()
    return end - start
