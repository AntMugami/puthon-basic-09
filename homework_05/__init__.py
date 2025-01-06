import app
import uvicorn
import logging


logger = logging.getLogger(__name__)


__all__ = [
    "app",
]

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    uvicorn.run("app:app", host='0.0.0.0', port=8000)
    logger.info('Finished')


if __name__ == '__main__':
    main()