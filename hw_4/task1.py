import time
import threading
import multiprocessing


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def run_sync(n):
    start = time.time()
    for _ in range(10):
        fib(n)
    return time.time() - start


def run_threads(n):
    start = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fib, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return time.time() - start


def run_processes(n):
    start = time.time()
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fib, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    return time.time() - start


if __name__ == "__main__":
    n = 35
    with open("artifacts/task1.txt", "w") as file:
        file.write(f"Sync: {run_sync(n):.4f}\n")
        file.write(f"Threads: {run_threads(n):.4f}\n")
        file.write(f"Processes: {run_processes(n):.4f}\n")
