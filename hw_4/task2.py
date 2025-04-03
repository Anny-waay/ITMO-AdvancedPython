import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count


def integrate(f, a, start, end, step):
    acc = sum(f(a + i * step) * step for i in range(start, end))
    return acc


def execute(f, a, b, executor, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter
    job_iters = n_iter // n_jobs

    with executor(max_workers=n_jobs) as ex:
        futures = []
        start = 0
        for i in range(n_jobs):
            if i == n_jobs - 1:
                end = n_iter
            else:
                end = start + job_iters
            futures.append(ex.submit(integrate, f, a, start, end, step))
            start = end
        result = sum(f.result() for f in as_completed(futures))

    return result


def get_execution_time(f, a, b, jobs_list, n_iter=10000000):
    threads_time = []
    processes_time = []
    for i in range(len(jobs_list)):
        start = time.time()
        execute(f, a, b, ThreadPoolExecutor, jobs_list[i], n_iter)
        threads_time.append(time.time() - start)
        start = time.time()
        execute(f, a, b, ProcessPoolExecutor, jobs_list[i], n_iter)
        processes_time.append(time.time() - start)
    return threads_time, processes_time


if __name__ == "__main__":
    jobs_list = [i for i in range(1, cpu_count() * 2 + 1)]
    threads_time, processes_time = get_execution_time(math.cos, 0, math.pi/2, jobs_list)
    with open("artifacts/task2.txt", "w") as file:
        file.write(f"n_jobs\t|\tthreads\t|\tprocesses\n")
        for i in range(len(jobs_list)):
            file.write(f"{jobs_list[i]}\t\t|\t{threads_time[i]:.4f}\t|\t{processes_time[i]:.4f}\n")
