import threading
import time


def count_time(sec):
    time.sleep(sec)
    print(f"Task {sec} done after {sec} seconds")


def threading_demo():
    start = time.time()
    threads = []

    for i in range(1,16):
        t = threading.Thread(target=count_time, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Threading total time: {time.time() - start} sec\n")

def sync_demo():
    start = time.time()
    for i in range(1,16):
        count_time(i)

    print(f"Synchronous total time: {time.time() - start} sec\n")


def main():
    print("--SYNCHRONOUS VERSION--")
    sync_demo()
    print("--THREADING VERSION--")
    threading_demo()


if __name__ == "__main__":
    main()