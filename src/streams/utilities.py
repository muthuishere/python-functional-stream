import asyncio
import itertools
from itertools import islice

default_reduce_initializer = 0


def generator_from_list(data):
    for row in data:
        yield row


def generator_from_list_of_lists(toplist):
    for values in toplist:
        for value in values:
            yield value


async def executewith(currentdata, applicablepartials):
    result = currentdata



    for currentpartial in applicablepartials:
        chunks = chunk(1000, result)
        result = currentpartial(result)
    return result


def chunk(n, iterable):
    iterable = iter(iterable)
    while True:
        x = tuple(islice(iterable, n))
        if not x:
            return
        yield x


def executeasync(data, partials):
    #chunks = chunk(1000, data)
    return executewith(data, partials)
    #
    #
    # coroutines = (executewith(currentchunk, partials) for currentchunk in chunks)
    # results =  asyncio.gather(*coroutines)
    # print("type(results)", type(results))
    # for r in results:
    #     for k in r:
    #         for m in k:
    #             yield m



