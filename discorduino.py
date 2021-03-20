import discord
from discord.ext import commands
import pyfirmata
import sdisplay

client = commands.Bot(command_prefix='!')
board = pyfirmata.Arduino('COM5')

in2 = board.get_pin('d:7:o')
in1 = board.get_pin('d:8:o')
ledg = board.get_pin('d:6:o')
ledr = board.get_pin('d:5:o')
ledr2 = board.get_pin('d:3:o')
ledg2 = board.get_pin('d:4:o')
state = False
state2 = False
in2.write(1)
in1.write(1)
ledr.write(1)
ledr2.write(1)


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def display(ctx, n):
    try:
        n = int(n)
        if n > 9999:
            await ctx.send('Number too big :/')
        else:
            sdisplay.sevDisplay(board, n, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)
            await ctx.send(str(n) + ' Sent!')
    except:
        await ctx.send('That\'s not a valid number :/')


@client.command()
async def fan(ctx):
    global state
    if state is False:
        in1.write(0)
        ledg.write(1)
        ledr.write(0)
        state = True
        await ctx.send('Turned On')
    else:
        in1.write(1)
        ledg.write(0)
        ledr.write(1)
        state = False
        await ctx.send('Turned Off')


@client.command()
async def thi(ctx):
    global state2
    if state2 is False:
        in2.write(0)
        ledg2.write(1)
        ledr2.write(0)
        state2 = True
        await ctx.send('Turned On')
    else:
        in2.write(1)
        ledg2.write(0)
        ledr2.write(1)
        state2 = False
        await ctx.send('Turned Off')


client.run('NzM1NTg1MTc2NTg3MDc1NTk0.Xxiaow.wJIMW8bVSEFgHQFBcCUSLc9Cfd8')
