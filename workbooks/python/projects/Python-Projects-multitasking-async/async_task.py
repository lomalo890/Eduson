"""
Модифицируйте код так, чтобы добиться параллельного выполениня вместо последовательного.
"""

import asyncio
from time import monotonic
import random


async def parse_request(request):
    await asyncio.sleep(random.random())
    data = random.randint(1, 100)
    print(f'{request} done')
    return data


async def process_data(data):
    await asyncio.sleep(random.random())
    return data * 2

'''
async def main():
    requests = [f'Request {i}' for i in range(1000)]
    
    for request in requests:
        data = await parse_request(request)
        await process_data(data)
'''

# Моё решение
async def main():
    tasks = [parse_request(f'Request {i}') for i in range(1000)]
    results = await asyncio.gather(*tasks)
    process_tasks = [process_data(data) for data in results]
    await asyncio.gather(*process_tasks) # 2.5


#solution proffi
async def main():
    tasks = [asyncio.create_task(parse_request(f'Request {i}')) for i in range(1000)]
    processing_tasks = []

    for task in asyncio.as_completed(tasks):
        data = await task
        processing_task = asyncio.create_task(process_data(data))
        processing_tasks.append(processing_task)

    await asyncio.gather(*processing_tasks) #1.96



if __name__ == '__main__':
    start = monotonic()

    asyncio.run(main())

    duration = monotonic() - start
    print(f'It took {duration:0.2f} secs')
