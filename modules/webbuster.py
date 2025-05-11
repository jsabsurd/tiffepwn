# from time import sleep
import aiohttp
import asyncio


async def check_url(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"[+] Found {url}")
    finally:
        pass


async def bustit(target, words):
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, f"{target}/{word.strip()}")
                 for word in words]
        await asyncio.gather(*tasks)
        input("press enter to return to menu")
