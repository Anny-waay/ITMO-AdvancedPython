import codecs
import time
from multiprocessing import Queue, Process
from datetime import  datetime
from queue import Empty


def process_a(in_queue, out_queue):
    while True:
        try:
            out_queue.put(in_queue.get(block=False).lower(), block=False)
            time.sleep(5)
        except Empty:
            pass


def process_b(out_queue, m_queue):
    while True:
        try:
            message = codecs.encode(out_queue.get(block=False), "rot_13")
            print(f"{datetime.now().strftime('%H:%M:%S')}\tB:\t{message}")
            m_queue.put(message, block=False)
        except Empty:
            pass


if __name__ == "__main__":
    stdin_queue = Queue()
    stdout_queue = Queue()
    main_queue = Queue()

    a = Process(target=process_a, args=(stdin_queue, stdout_queue))
    b = Process(target=process_b, args=(stdout_queue, main_queue))
    a.start()
    b.start()

    try:
        while True:
            msg = input()
            if msg != "exit":
                stdin_queue.put(msg, block=False)
            try:
                print(f"{datetime.now().strftime('%H:%M:%S')}\tMain:\t{main_queue.get(block=False)}")
            except Empty:
                pass
            if msg == "exit":
                break
    finally:
        a.terminate()
        b.terminate()



