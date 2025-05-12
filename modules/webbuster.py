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


def load_wordlist(wordlist_path):
    try:
        with open(wordlist_path, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Error: Wordlist '{wordlist_path}' not found!")
        exit(1)


async def bustit(words):
    print("enter URL to scan:")
    print()
    target = input("> ")
    print("enter path to wordlist: (custom is wl.txt)")
    print()
    wl_path = input("> ")
    words = load_wordlist(wl_path)
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, f"{target}/{word.strip()}")
                 for word in words]
        await asyncio.gather(*tasks)
        input("press enter to return to menu")
