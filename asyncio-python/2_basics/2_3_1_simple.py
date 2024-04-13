import asyncio


async def download_file(url):
    # Здесь могла бы быть асинхронная операция загрузки файла
    print(f"Downloading {url}...")
    await asyncio.sleep(1)  # Имитация асинхронной задержки
    print(f"Downloaded {url}!")


async def main():
    urls = ["http://example.com/file1", "http://example.com/file2"]
    await asyncio.gather(*[download_file(url) for url in urls])

asyncio.run(main())
