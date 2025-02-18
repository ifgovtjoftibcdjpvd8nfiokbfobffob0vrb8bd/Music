import time
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from AnonXMusic import app
from AnonXMusic.misc import _boot_
from AnonXMusic.plugins.sudo.sudoers import sudoers_list
from AnonXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AnonXMusic.utils.decorators.language import LanguageStart
from AnonXMusic.utils.formatters import get_readable_time
from AnonXMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string


# Function to send the start video separately
async def send_start_video(chat_id):
    """Send the start video separately with a slight delay."""
    try:
        sent_video = await app.send_video(
            chat_id=chat_id, 
            video=config.START_VIDEO_URL, 
            supports_streaming=True
        )
        return sent_video
    except Exception as e:
        print(f"Error sending start video: {e}")
        return None


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.react("❤️")

    out = private_panel(_)

    # Animated Loading Text
    baby = await message.reply_text("**▒▒▒▒▒▒▒▒▒▒ 0%**")
    for i in range(10, 110, 10):
        await baby.edit_text(f"**{'█' * (i // 10)}{'▒' * (10 - i // 10)} {i}%**")
        await asyncio.sleep(0.2)  # Smooth delay

    await baby.delete()

    # Send sticker first
    await message.reply_sticker("CAACAgUAAxkBAAEN1VxntHV8PA9Cl2EHOH852LXr8EnS4AAC7RsAAlTjqFWxscXm9hJhvDYE")
    await asyncio.sleep(1)  # Short delay before sending video

    # Send the start video separately
    await send_start_video(message.chat.id)

    # Send the text message with buttons
    await message.reply_text(
        text=_["start_2"].format(message.from_user.mention, app.mention),
        reply_markup=InlineKeyboardMarkup(out),
    )

    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOGGER_ID,
            text=(
                f"{message.from_user.mention} started the bot.\n\n"
                f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
                f"<b>Username:</b> @{message.from_user.username}"
            ),
        )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)

    # Send the start video first
    await send_start_video(message.chat.id)

    # Send the text message with buttons
    await message.reply_text(
        text=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    
    await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass

            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)

                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)

                # Send the start video first
                await send_start_video(message.chat.id)

                # Send the welcome text message
                await message.reply_text(
                    text=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )

                await add_served_chat(message.chat.id)
                await message.stop_propagation()

        except Exception as ex:
            print(f"Error in welcome handler: {ex}")
