# 2019 Emir Erbasan (humanova)

import asyncio
import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot

import checker
import env_set
env_set._set()

msg_list = ['213262071050141696',
            '608001852700622855']

c_count = 0
################################

Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Logged in as %s." % (client.user.name))
    await check_website()


async def check_website():
    global c_count

    while not client.is_closed:
        is_changed, change = checker.check_cw_website()

        if is_changed and not c_count == 0:
            for user in msg_list:

                usr = await client.get_user_info(user)
                await client.start_private_message(usr)
                await client.send_message(usr, change)

        c_count+=1
        print(f"check {c_count}")
        # sleep for 10 mins
        await asyncio.sleep(600)

@client.event
async def on_message(message):

    if message.author.id in msg_list:
        if message.content == "!check":
            await client.start_private_message(message.author)
            await client.send_message(message.author, checker.check_cw_website()[1])

token = os.environ['BOT_TOKEN']
client.run(token)
