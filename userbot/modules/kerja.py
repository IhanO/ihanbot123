import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP
from userbot.events import register
	
@register(outgoing=True, pattern='^.wait(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("OK, tunggu bentar \n"
			 f"Aku akan menyiapkan semuanya untukmu")

@register(outgoing=True, pattern='^.subdo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Daftar harga **subdo**\n"
			 f"0X Garansi : 20.000\n"
			 f"1X Garansi : 30.000\n"
			 f"3X Garansi : 50.000\n")

@register(outgoing=True, pattern='^.tq(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Jangan lupa ganti datanya ya bos! \nKalau sudah aman jangan lupa ss lobby!\nTerima kasih #HanzBOT ")


# Create by myself @HundinTogam
@register(outgoing=True, pattern='^.sibuk(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Sebentar ya bos`")
	sleep(2)
	await typew.edit("`Masih Ngecek`")
	sleep(1)
	await typew.edit("`Ohh ternyata lagi sibuk bos`")
	
	
# Create by myself @HundinTogam
@register(outgoing=True, pattern='^.on(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Maaf baru online, ada apa bos?` \n#HanzBOT")
	

# Create by myself @HundinTogam
@register(outgoing=True, pattern='^.bri(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`BRI : `454901021040530 `A/N LINDA WATI` \nJangan lupa bukti transfernya bosku  \n#HanzBOT")

# Create by myself @HundinTogam
@register(outgoing=True, pattern='^.dana(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`DANA : `081572665200 `A/N MESSY HARIANI` \nJangan lupa bukti transfernya bosku \n#HanzBOT")


# Create by myself @HundinTogam
@register(outgoing=True, pattern='^.order(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Silahkan Isi! \nTampilan : \nEmail : \n Order  \n#HanzBOT")



