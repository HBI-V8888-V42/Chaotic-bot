import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import gitty
import botclass

load_dotenv()
tken = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='&', intents =intents)
client.remove_command('help')
client.load_extension('botclass')
@client.event
async def on_ready():
    print(f'{gitty.colors.BLUE}OK{gitty.colors.ENDC}')
    #print('Messages')
    #client.loop.create_task(botclass.fetchenable())
    pass


#print('\n'+tken+'\n')


client.run(tken)
os.system('clear')

