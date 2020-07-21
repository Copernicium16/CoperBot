#CoperBot Project
import discord
import random
from discord.ext import commands
coper = commands.Bot(command_prefix = 'c.')

#bot on
@coper.event
async def on_ready():
    print('Bot is ready.')

#c.ping
@coper.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(coper.latency*1000)}ms')

#c.sneeze
@coper.command()
async def sneeze(ctx):
    await ctx.send('God Bless You...')

#c.hi
@coper.command()
async def hi(ctx):
    await ctx.send(f'Hello fellow {format(ctx.author.mention)}.')

#c.8ball or c.8ball (question)
@coper.command(aliases=['8ball'])
async def _8ball(ctx, question = 'No question?'):
    if question == 'No question?':
       await ctx.send('I can predict your future, maybe...')
       await ctx.send('command : ```c.8ball (question)```')
    else:
       responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
       await ctx.send(f'{random.choice(responses)}')
       
#c.trump
@coper.command()
async def trump(ctx):
    trump_says = ['North Korea. :love_letter:', ':exploding_head: Nuke Kim!', 'Release the COVID19! (conspiracy intensifies)', 'Does black live matter?', ':oil: Keep the oil! :oil:', "Why don't we do it with Rusian?"]
    await ctx.send(f'{random.choice(trump_says)}')

#c.clean and c.clean(amount)
@coper.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, amount = 3):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Clean succeed. :)')
    await ctx.channel.purge(limit=1)

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that...")
        await ctx.channel.purge(limit=1)

#TOKEN
coper.run('')
