## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BQBQeqhDKj0Afpt9cH4u_C48Ken7lfgi3HyJnszr-aASSkvEDXRWRIhO1FqKJhJb11B7kOykAJyIH7ghFbYIVP82He38DmgRu7qN-wUYexJ3p-HR62mT7DWGs_UfS1-lpPUjofRxQ3B5xwiqj9nNr5I_q_uB0vbPD5WuKbvt15TpvQzDrS0UdKEITphs_YDDI25T0gdS-TstZyBUPk7LlmVOjyjBx_VLO8cqfhif1P5oeSZnfpcir6Dd32x7boWGEZS5w9EKufqrJjoc2-2-9c2q0cU9cFPZaRGhn4bsy5qxtMl9_A1JKCSJpOh9mlo09sUb3LAFUngS1nxU3NX7wb6eAAAAAUAyzEEA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5718269633:AAFgbTa6uFuuxAr9Sc0gfF78R5lfU7HjvFc")
BOT_NAME = getenv("BOT_NAME", "Mr.Eric")

API_ID = int(getenv("API_ID", "17674920"))
API_HASH = getenv("API_HASH", "4c55df5c8d646c88aa4bbe177761117c")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Plexitics")
ALIVE_NAME = getenv("ALIVE_NAME", "Mr.Eric")
BOT_USERNAME = getenv("BOT_USERNAME", "Mr_Eric_Robot")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zaid2_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
