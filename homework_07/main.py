from jsonplaceholder_requests import async_get_users, async_get_posts
import asyncio
from models import User, Post, init_db, async_session, close_db
from typing import List, Dict
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from views import router
import uvicorn
import logging

app = FastAPI()


app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")

logger = logging.getLogger(__name__)


__all__ = [
    "app",
]

def get_users(db: async_session):
    return db.query(User).all


def get_post(db: async_session):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: async_session, post: PostCreate, author_id: User.id):
    db_post = Post(**post.dict(), author_id=author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post




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
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    uvicorn.run("app:app", host='0.0.0.0', port=8000)
    logger.info('Finished')

if __name__ == "__main__":
    main()