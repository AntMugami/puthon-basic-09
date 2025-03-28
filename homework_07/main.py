from jsonplaceholder_requests import async_get_users, async_get_posts
import asyncio
from models import User, Post, init_db, async_session, close_db
from typing import List, Dict

async def create_users_in_db(users_data: List[Dict]) -> None:
    async with async_session() as session:
        users = [User(**user_data) for user_data in users_data]
        session.add_all(users)
        await session.commit()

async def create_posts_in_db(posts_data: List[Dict]) -> None:
    async with async_session() as session:
        posts = [Post(**post_data) for post_data in posts_data]
        session.add_all(posts)
        await session.commit()

async def async_main():
    await init_db()
    users: List[Dict]
    posts: List[Dict]
    posts, users = await asyncio.gather(
        async_get_posts(),
        async_get_users(),
    )

    await asyncio.gather(
        create_users_in_db(users),
        create_posts_in_db(posts),
    )
    await close_db()

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()