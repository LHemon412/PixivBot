import os
import random
import discord
from pixivpy3 import *
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
api = AppPixivAPI()
api.login("user_yaew2385", "Le168814")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = str(message.content)
    if msg.startswith("pixiv"):
        args = msg.split(" ")
        if args[1] == "help":
            await message.channel.send("LEMON IS HANDSOME")
        elif args[1] == "s":
            if len(args) <= 2:
                await message.channel.send("what you want dude")
                return
            json_result = api.search_illust(args[2], search_target='partial_match_for_tags', sort='date_desc', duration=None)
            gegs = random.choices(json_result.illusts, k=3)
            for ill in gegs:
                api.download(ill.image_urls.large)
                await message.channel.send(file=discord.File('%s_p0_master1200.jpg' % ill.id))
                os.remove('%s_p0_master1200.jpg' % ill.id)

client.run(token)
