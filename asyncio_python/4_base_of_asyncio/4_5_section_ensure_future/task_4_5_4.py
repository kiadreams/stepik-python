async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [asyncio.ensure_future(aw) for aw in awaitables]
    return await asyncio.gather(*tasks)