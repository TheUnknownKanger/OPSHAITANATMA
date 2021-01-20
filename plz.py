from telethon import events
import asyncio
@borg.on(events.NewMessage(pattern=r"^.plzzz", outgoing=True))
async def _(event):
     a="plz 🥺🙏🥺🙏🥺🙏🥺🙏🥺🙏🥺"
     await event.edit(a)
     await asyncio.sleep(1)
     b="plz 🙏🥺🙏🥺🙏🥺🙏🥺🙏🥺🙏"
     await event.edit(b)
     await asyncio.sleep(1)
     c="🥺🙏🥺🙏🥺🙏🥺🙏🥺🙏🥺🙏"
     await event.edit(c)
     await asyncio.sleep(1)
     d="plz 🥺🥺🥺bhaiya🥺🥺🥺"
     await event.edit(d)
     await asyncio.sleep(1)
     e="plz didi,bhaiya sabko bol raha plz🙏🥺🙏🥺🙏🥺🙏🥺🙏🥺🙏🥺🙏🥺"
     await event.edit (e)
     await asyncio.sleep(1)
     f="🥺🥺🥺           🥺            🥺🥺 🥺\
        \n🥺       🥺         🥺                    🥺\
        \n🥺 🥺🥺          🥺                  🥺\
        \n🥺                    🥺               🥺🥺🥺\
        \n🥺                    🥺\
        \n🥺                    🥺🥺🥺🥺🥺"
     await event.edit(f)
