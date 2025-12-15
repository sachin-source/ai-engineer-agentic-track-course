import asyncio
async def do_some_processing() -> str:
    return "done!"

my_coroutine = do_some_processing()
my_result = asyncio.run(my_coroutine)
print(my_result)

results = asyncio.gather(
    do_some_processing(),
    do_some_processing(),
    do_some_processing()
)
all_results = asyncio.run(results)
print(all_results)