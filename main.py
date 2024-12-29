from discord import Intents
from discord.ext.commands import Bot

from dotenv import load_dotenv
from os import getenv, listdir
from asyncio import run

load_dotenv()

client = Bot('-', intents = Intents.all())


async def cogs(path = 'cogs'):
    for file in listdir(path):
        if file != '__pycache__':
            if file.endswith('.py'):
                file = f'{path}.{file}'.replace('.py', '')
                await client.load_extension(file.replace('/', '.'))

            else:
                await cogs(path + '/' + file)
 

if __name__ == '__main__':
    run(cogs())
    client.run(getenv('BOT_TOKEN'))
