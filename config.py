import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Function to clean and convert environment variables to integers safely
def clean_int(value, default=0):
    try:
        return int(str(value).strip().replace("\u200e", ""))
    except ValueError:
        return default

# Get values from environment variables
API_ID = "23568641"
API_HASH = "a39098e8752a45c2d6d1889941547bbc"
BOT_TOKEN = "7836466334:AAEXG1Ifz-KHhQvmabE3s8wUN9hKDbJ981Q"
MONGO_DB_URI = "mongodb+srv://Lord_ichigo:Roshni@cluster0.ytuss.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = clean_int(os.getenv("DURATION_LIMIT", 60000))
ADS_MODE = os.getenv("ADS_MODE", None)
LOGGER_ID = clean_int(os.getenv("LOGGER_ID", "-1002323856532"))
OWNER_ID = clean_int(os.getenv("OWNER_ID", "8177810307"))

# Heroku Configs
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# Repository Information
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/DEV-ZTX/Music")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# Telegram Support & Channels
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Beast_Tuhin")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/Riya_Support_Chat")

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", None))

# Spotify API Credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist Limits
PLAYLIST_FETCH_LIMIT = clean_int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram File Size Limits (in bytes)
TG_AUDIO_FILESIZE_LIMIT = clean_int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = clean_int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Pyrogram Session Strings
STRING1 = "BQGyhVAAsac1l44Zxwnh29UGP-PW3-fqkS4w8oOeWE1aNYWx1bHGbDZlYQq-T7cDbS07jFDhyjuWqqnAIVB_yx1mGp_1QCcWlzc65S07eriebbXi_O3Wz0sE5tfIh7cdmlY7Y9rMKPQogfq3prmHvdKGxQTAHZR9S68huurNSIC7-lWjPAMg60W1x-GPCNFsU2I1FrvZHO32VF5HrLPMrF5VCmbM0a-lG25i4myJRIlq3McPyWeyzcapWrkPATVXqEUjdmcqy9gc98Su90aXaXjvpU1DvrJqc9mrW1vjX-hpJ5tMGK97WGGX5b987LgVgOjY04GfqUVyi_Snoc37DtrV5hQUtgAAAAHQ9QGyAA"
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# Banned Users & Other Variables
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image & Video URLs
START_VIDEO_URL = os.getenv("START_VIDEO_URL", "https://files.catbox.moe/akyeq2.mp4")
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/8rg2ht.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/8rg2ht.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
STATS_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/8rg2ht.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/8rg2ht.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"

# Convert time format (hh:mm:ss) to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Validate URLs
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is incorrect. It must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is incorrect. It must start with https://")
