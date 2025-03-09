import asyncio
import os
import shutil
import socket
from datetime import datetime
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters

import config
from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import get_active_chats, remove_active_chat, remove_active_video_chat
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.pastebin import AnonyBin


async def is_heroku():
    return "heroku" in socket.getfqdn()


# Get Bot Logs
@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & SUDOERS)
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text("Error: Log file not found.")


# Update Bot
@app.on_message(filters.command(["update", "gitpull"]) & SUDOERS)
@language
async def update_(client, message, _):
    response = await message.reply_text("Checking for updates...")

    try:
        repo = Repo()  # Load the Git repository
    except InvalidGitRepositoryError:
        return await response.edit("Error: This directory is not a valid Git repository.")
    except GitCommandError as e:
        return await response.edit(f"Git error: {str(e)}")

    # Fetch updates from GitHub
    os.system(f"git fetch origin {config.UPSTREAM_BRANCH}")
    await asyncio.sleep(5)

    # Count new commits
    new_commits = list(repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"))
    if not new_commits:
        return await response.edit("No new updates available.")

    # Generate update summary
    updates = ""
    repo_url = repo.remotes.origin.url.split(".git")[0]

    for commit in new_commits:
        commit_date = datetime.fromtimestamp(commit.committed_date).strftime("%d %b %Y")
        updates += f"<b>➣ Commit: <a href='{repo_url}/commit/{commit.hexsha}'>{commit.summary}</a> by {commit.author}</b>\n"
        updates += f"  ➥ Date: {commit_date}\n\n"

    # If updates are too long, upload to Pastebin
    if len(updates) > 4000:
        paste_url = await AnonyBin(updates)
        updates = f"New updates available! Check here: <a href='{paste_url}'>View Changes</a>"

    # Apply updates
    await response.edit(f"<b>New updates found!</b>\n\n{updates}\n\nApplying updates...")
    
    # Stash uncommitted changes and pull latest code
    os.system("git reset --hard")
    os.system("git stash")
    os.system(f"git pull origin {config.UPSTREAM_BRANCH}")

    # Notify active chats about restart
    try:
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            try:
                await app.send_message(chat_id=int(chat_id), text="The bot is updating and will restart soon.")
                await remove_active_chat(chat_id)
                await remove_active_video_chat(chat_id)
            except:
                pass
    except:
        pass

    # Restart the bot
    await response.edit("Update applied! Restarting bot...")
    os.system("pip3 install -r requirements.txt")
    os.system(f"kill -9 {os.getpid()} && bash start")
    exit()


# Restart Bot
@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(client, message):
    response = await message.reply_text("Restarting bot...")

    # Notify active chats
    active_chats = await get_active_chats()
    for chat_id in active_chats:
        try:
            await app.send_message(
                chat_id=int(chat_id),
                text="The bot is restarting...\nIt will be back online in 15-20 seconds.",
            )
            await remove_active_chat(chat_id)
            await remove_active_video_chat(chat_id)
        except:
            pass

    # Clean up temporary files
    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass

    # Restart the bot
    await response.edit("Restarting now...")
    os.system(f"kill -9 {os.getpid()} && bash start")
    exit()
