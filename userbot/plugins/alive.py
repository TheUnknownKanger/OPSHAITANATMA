import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/968ce4f27a57e50a801f9.jpg"
pm_caption = "**🅻🅴🅶🅴🅽🅳 🅸🆂 🅾🅽🅻🅸🅽🅴**\n"

pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"

pm_caption += "Telethon Version         : 4.8\n"

pm_caption += "Python Version           : 3.8.5\n"

pm_caption += "Bot Version              : 7.0.9\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/legendsupportchannel)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ            : [ᴊᴏɪɴ](https://t.me/legendsupportgroup)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                  : AGPL-3.0  ʟɪᴄᴇɴꜱᴇ\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ             : LEGEND\n"

pm_caption += "╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X  X║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝"

@borg.on(admin_cmd(pattern=r"alive"))
async def legend(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()


@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def jarvis(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
