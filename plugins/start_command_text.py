from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import time

''' def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result '''

bot_start_time = time.time()
bot_uptime = get_readable_time(time.time() - bot_start_time)

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    bot_start_time = time.time()
    bot_uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - bot_start_time)) 
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("JOIN", url="https://t.me/TGBotsCollection")],
        [InlineKeyboardButton(
            "Try", url="https://t.me/TGBotsCollectionbot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nThis is Multipurpose Bot that can perform many functions.\n\n/help for More info \n Bot Uptime : {bot_uptime}"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
