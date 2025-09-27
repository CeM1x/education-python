import threading
import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        print(f"Total execute time: {time.time() - start} sec\n")
    return wrapper


def count_time(sec):
    time.sleep(sec)
    print(f"Task {sec} done after {sec} seconds")


@timer
def threading_demo():
    threads = []
    for i in range(1,5):
        t = threading.Thread(target=count_time, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

@timer
def sync_demo():
    for i in range(1,5):
        count_time(i)



def main():
    print("--SYNCHRONOUS VERSION--")
    sync_demo()
    print("--THREADING VERSION--")
    threading_demo()


if __name__ == "__main__":
    main()
