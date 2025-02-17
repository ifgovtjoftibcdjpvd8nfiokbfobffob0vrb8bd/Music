import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "27934563"
API_HASH = "50516d67db72b07709904734c69a658b"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8004440473:AAG5BESHY2eHonzjfxnhMC5g4r5DeufEOO8"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://jazibot02:jazibot02@cluster0.s7fhq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60000))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002266615669"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7057381827))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Block2002/Samrio",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Jazi_sam")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Jazi_sam")

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
STRING1 = "BQC86fAAgi2DrWAiXvjz2Fmjmgy85V64RCf78AsKF2hXumREWkyv-E_rxUFmtTguGnX67caTTnvreX4AG7JVzVV0E0gr_esaMQ4PG-d5CBOgRHfCqEwWNAuE9LXxari-fL4OM2hm_DGTcHPGBm5HfImDq6w1yiLMN1gh7N51VCJSoxlqvauLzj9kWnvVQ4gvxDBGPIjD8-KngBZNRce9wMhupQG7WrdkamRh_qTO99x2Czo3cAq3G13jKgKTnbCK_4lW2_Subt56vUEnuHZzRjLADc4PwWoEbkwzlbBWYGc9Qcx0N_HwqHik-JFOXoSqCZ9F6BIZwL-FhiqWbYuLnuUOpZVTQAAAAAHWSSZLAA"
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
