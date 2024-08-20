from concurrent import futures
import math


import requests

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    paginas = [
        r"https://www.digitalocean.com/community/tutorials/how-to-use-threadpoolexecutor-in-python-3",
        r"https://stackoverflow.com/questions/51828790/what-is-the-difference-between-processpoolexecutor-and-threadpoolexecutor",
        r"https://www.digitalocean.com/community/tutorials/how-to-use-threadpoolexecutor-in-python-3",
    ] * 50

    PRIMES = [
        112272535095293,112582705942171,112272535095293,115280095190773,115797848077099,
        112272535095293,112582705942171,112272535095293,112272535095293,112582705942171,
        112272535095293,112272535095293,112582705942171,112272535095293,112272535095293
    ] * 10

    #executor = futures.ThreadPoolExecutor(max_workers=4)
    #executor = futures.ProcessPoolExecutor()
    #for pagina in paginas:
    #    executor.submit(get_wiki_page_existence, pagina, timeout=10)
    #    get_wiki_page_existence(pagina, timeout=10)
    #print("Esperando por que finalicen los Threads...")
    #executor.shutdown(wait=True)

    #executor = futures.ThreadPoolExecutor(max_workers=4)
    executor = futures.ProcessPoolExecutor()
    for number in PRIMES:
        executor.submit(is_prime, n=number)
    #    print("{} is prime: {}".format(number, is_prime(number)))
    #print("Esperando por que finalicen los Threads...")
    executor.shutdown(wait=True)

    #with futures.ProcessPoolExecutor() as executor:
    #    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
    #        print('{} is prime: {}'.format(number, prime))

if __name__ == '__main__':
    main()
