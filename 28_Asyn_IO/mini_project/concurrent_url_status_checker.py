import asyncio
import aiohttp

urls = [
    "https://www.google.com",
    "https://github.com",
    "https://python.org",
    "https://nonexistent.url.xyz"
]

async def fetch_status(session, url):
    try:
        async with session.get(url) as response:
            print(f"{url}: {response.status}")
    except Exception as e:
        print(f"{url}: Error - {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
