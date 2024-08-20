import time
import asyncio
#from concurrent import futures

#def func(x):
async def func(x):
    print("Waiting from func - " + str(x))
    #time.sleep(x)
    await asyncio.sleep(x)
    print("Getting out from func")

def func_final():
    print("Entra a ejecutar func_final...")
    for i in range(2):
        time.sleep(2)
    print("Termina de ejecutar func_final!")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [asyncio.ensure_future(func(5)), asyncio.ensure_future(func(8)), asyncio.ensure_future(func(9))]
    loop.run_until_complete(asyncio.gather(*tasks))

    #NUMEROS = [5, 8, 9]
    #executor = futures.ProcessPoolExecutor()
    #for number in NUMEROS:
    #    executor.submit(func, x=number)
    #executor.shutdown(wait=True)

    #func(5)
    #func(8)
    #func(9)

    func_final()
