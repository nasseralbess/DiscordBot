# pip install -U discord.py
# Import the required modules
import discord
import subprocess
import os
from discord.ext import commands 
from dotenv import load_dotenv
import random

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='%', intents=intents)

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def clear():
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def greet(ctx):
    response = 'Hello, I am your discord bot'
    await ctx.send(response)

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions'
    await ctx.send(response)

@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord chatbot! I will reply to your command!'
    await ctx.send(response)

@bot.command()
async def weather(ctx):
    # Run the Python script
    subprocess.run(["python", 'weather.py'])
    with open('weather.png', 'rb') as f:
        image = discord.File(f)
    # Send the image
    await ctx.send(file=image)
@bot.command()
async def tic_tac_toe(ctx,next_move = None):
    if next_move is not None:
        if next_move[0] == 'x':
            board[int(next_move[1])][int(next_move[2])] = 'x'
            #bot's response
            x,y = random.randint(0,2),random.randint(0,2)
            while board[x][y] != ' ':
                x,y = random.randint(0,2),random.randint(0,2)
            board[x][y] = 'o'

        elif next_move[0] == 'o':
            board[int(next_move[1])][int(next_move[2])] = 'o'
            #bot's response
            x,y = random.randint(0,2),random.randint(0,2)
            while board[x][y] != ' ':
                x,y = random.randint(0,2),random.randint(0,2)
            board[x][y] = 'x'
        #check for winner
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
                response = 'Current board: \n'
                for i in range(3):
                    response += ' | '.join(board[i]) + '\n'
                await ctx.send(f'{response}\n\n{board[i][0]} wins!')
                clear()
                return
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
                response = 'Current board: \n'
                for i in range(3):
                    response += ' | '.join(board[i]) + '\n'
                await ctx.send(f'{response}\n\n{board[i][0]} wins!')
                clear()
                return
            if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
                response = 'Current board: \n'
                for i in range(3):
                    response += ' | '.join(board[i]) + '\n'
                await ctx.send(f'{response}\n\n{board[i][0]} wins!')
                clear()
                return
        
    response = 'Current board: \n```'
    for i in range(3):
        response += ' | '.join(board[i]) + '\n'
    response+='```'
    await ctx.send(response)
# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))