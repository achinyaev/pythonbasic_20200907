import asyncio
import random

async def one(n):
    for num in range(n):
        print('start func', n)
        await asyncio.sleep(random.randint(1, 10))
        print(num, 'one', n)
        await asyncio.sleep(random.randint(1, 5))
        print('end func')

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    tasks = asyncio.wait([one(n) for n in range(1, 5)])
    print((tasks))
    asyncio.run(tasks)
    print('end')



