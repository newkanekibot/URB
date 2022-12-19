# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "29913092"))
    API_HASH = os.environ.get("API_HASH", "21ad78b36fcdb7f48c1d01858d7fbfab")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5926536733:AAFhHrOn3KBtPNiHRsVxw4sU8KZopIOuwm8")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 800954971))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://moviestrooper:hn5zyiPPhfgrROG2@cluster0.u7nh3fx.mongodb.net/?retryWrites=true&w=majority")
    FORCE_SUB = os.environ.get("FORCE_SUB", "mtmovies002")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001810941379"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
