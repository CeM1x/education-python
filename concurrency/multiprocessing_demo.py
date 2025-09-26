import multiprocessing
import time


def count_time(sec):
    time.sleep(sec)
    print(f"Task {sec} done after {sec} seconds")


def multiprocessing_demo():
    start = time.time()
    processes = []
    for i in range(1,16):
        p = multiprocessing.Process(target=count_time, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(f"Multiprocessing total time: {time.time() - start} сек\n")


def sync_demo():
    start = time.time()
    for i in range(1,16):
        count_time(i)

    print(f"Synchronous total time: {time.time() - start} sec\n")

def main():
    print("--SYNCHRONOUS VERSION--")
    sync_demo()
    print("--MULTIPROCESSING VERSION--")
    multiprocessing_demo()

if __name__ == "__main__":
    main()