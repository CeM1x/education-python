import asyncio
import time


async def count_time(sec):
    await asyncio.sleep(sec)
    print(f"Task {sec} done after {sec} seconds")


async def async_demo():
    start = time.time()
    async with asyncio.TaskGroup() as tg:
        for i in range(1,16):
            tg.create_task(count_time(i))
    print(f"Async total execute time: {time.time() - start}")


def waiting(sec):
    time.sleep(sec)
    print(f"Task {sec} done after {sec} seconds")


def sync_demo():
    start = time.time()
    for i in range(1,16):
        waiting(i)
    print(f"Sync total execute time: {time.time() - start}\n")


async def main():
    print("--SYNCHRONOUS VERSION--")
    sync_demo()

    print("--ASYNCHRONOUS VERSION--")
    await async_demo()



if __name__ == "__main__":
    asyncio.run(main())