import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = ""
API_HASH = ""

# Get your token from @BotFather on Telegram.
BOT_TOKEN = ""

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = ""

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60000))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002323856532"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7678359785))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DEV-ZTX/Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/my_every_footstep")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Chat_Group_Weeb")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "OWNER_ID=7678359785
TOKEN=7595735004:AAEunj6vG4vqEOMbFpPugKvaxpw06e-65Rc
MONGO_DB_URL=mongodb+srv://vjimmy276:GL83MueHjvCT32m3@cluster0.pxamg.mongodb.net/?retryWrites=true&w=majority
LOGGER_ID=-1002323856532
API_ID=28928028
API_HASH=b097202e877124392f4851d215fa8f3a
STRING_SESSION="BQFfYv8AWK2heUFuFIqrHBK7AUWHpx2r1mvZTLPD9ES6w52EyMRDAbztsNBJJYI4u87ONFBuV4v4eHwksuc_MvlAOVTmjejCtXVyNvRmvUdyAT4Otcgc1K2H33G177XzdPCM7NGx7rc3-kGVsipjHGSEFnBlh69-NY72w97fg0G-c8jo4K7u-Rfw35HOpiVCi_jk6sS-pnDYRAScUkS14uHMNIiL7ORkunBkGxMRcCqzzxizE4QzcH3l0KUkjT9l-T48T4e-gsxqXzpu0OHWkcY_rYKkQtLf-UGnWniHAsAViusar1pH9EXGYfyRn_3T692IXos2smcmCBuQFLA1jg2zA243hwAAAAHH7QH1AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_VIDEO_URL = getenv(
    "START_VIDEO_URL", "https://envs.sh/hDP.mp4"
)
START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/hDu.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/hDu.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/hDu.jpg"
STATS_IMG_URL = "https://envs.sh/hDu.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/hDu.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/hDu.jpg"
STREAM_IMG_URL = "https://envs.sh/hDu.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/hDu.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/hDu.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/hDu.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/hDu.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/hDu.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
