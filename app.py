from discord.ext import commands
import discord
from locate import TOKEN, ID_CHANNEL, WELCOME_REGISTER_CHANNEL, HEI, JOIN_FAILED, JOIN_OFF_PERFECT, JOIN_OFF_TEXT, ERROR_CHANNEL
from urllib import parse, request
import re

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='j>', description='you are starting joji bot', intents=intents) # el bot se usa con j>

@client.event
async def on_member_join(member):
    channel = client.get_channel(ID_CHANNEL)
    await channel.send(WELCOME_REGISTER_CHANNEL)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='NECTAR | j>joji', artist='Joji', album_cover_url='Joji_Smithereens.png')) # actividad
    print('{} is open for the user!'.format(client.user))


@client.command()
async def joji(ctx):
    await ctx.send(HEI)

@client.command()
async def embed(ctx):
    embed = discord.Embed(title='Joji bot', description="""is a bot that allows you to listen to the albums of the singer-songwriter joji, in order to promote the user to continue listening to their favorite artist is a voice chat!

commands: is used with 'j>'""", color=0x0000ff)
    embed.set_author(name='Follow me on GitHub! @fcoagz', icon_url='https://avatars.githubusercontent.com/u/103836660?v=4', url='https://github.com/fcoagz')
    embed.set_thumbnail(url='https://preview.redd.it/n7ff6z0xvkk91.jpg?auto=webp&s=50a2edb84f8d1ce64bab2785d6bdebb2db43bace')
    embed.add_field(name='joji', value='It is the main command of the bot that allows you to welcome and send you to this section.', inline=False)
    embed.add_field(name='join', value='With join you will make joji bot join in a voice chat to be able to play one of your albums.', inline=False)
    embed.add_field(name='share', value='The best command that you should use, it will help us a lot that you share the server and that more people know about this incredible bot.', inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send(JOIN_FAILED)

@client.command()
async def youtube(ctx, search): # ERROR: []
    url = parse.urlencode({'search_query': search})
    content = request.urlopen('https://www.youtube.com/results?' + url)
    results = re.findall('href=\"\\/watch\\?v=(.{11})', content.read()
    .decode())
    await ctx.send(results)
    pass


@client.command(pass_context = True)
async def join_off(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(JOIN_OFF_PERFECT)
    else:
        await ctx.send(JOIN_OFF_TEXT)
client.run(TOKEN)
