import asyncio


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [
        task for aw in awaitables
        if (task := asyncio.ensure_future(aw)) is not aw
    ]
    # for aw_obj in awaitables:
    #     task = asyncio.ensure_future(aw_obj)
    #     if task != aw_obj:
    #         tasks.append(task)
    return await asyncio.gather(*tasks)