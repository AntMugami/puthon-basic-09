import aiohttp

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def async_get_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            resp.raise_for_status()
            result = await resp.json()
            print(result) 
            return result

async def async_get_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            resp.raise_for_status()
            result = await resp.json()
            print(result) 
            return result
