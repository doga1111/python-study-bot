from tkinter import E
from turtle import title
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("봇 구동 중")
    bar = discord.Game("퀴즈 만들기")
    await client.change_presence(status=discord.Status.online, activity=bar)

science = {"표준화석이란?" : "지층의 생성시대를 알려주는 화석"}
check = False
b = ""

@client.event
async def on_message(message):
    global science, b, check

    if message.content.startswith("!퀴즈"):
        if check == False:
            subject = message.content[4:]
            if subject =="과학":
                a = random.choice(list(science.keys()))
                b = science[a]
                check = True
                await message.channel.send("'" + a + "'")

        elif check == True:
            await message.channel.send("'이미 퀴즈를 푸시는 중 입니다. 모르겟다면 !패스를 쳐주세요.'") 
   
    if message.content.startswith("!정답"):
        if check == True:
            answer = message.content[4:]
            if answer == b:
                check = False
                embed = discord.Embed(title = "!정답!", color = 0x00aaaa)
                await message.channel.send(embed = embed)
            elif answer != b:
                embed = discord.Embed(title = "오답...", color = 0x00aaaa)
                await message.channel.send(embed = embed)

        elif check == False:
            await message.channel.send("'풀고 있는 퀴즈가 없습니다.'")

    if message.content.startswith("!패스"):
        if check == True:
            embed = discord.Embed(title = "#패스#", color = 0x00aaaa)
            await message.channel.send(embed = embed)
            await message.channel.send("'정답은 '" + b + "' 이었습니다.\n문제를 패스하셧습니다.'")
        elif check == False:
            await message.channel.send("'풀고 있는 퀴즈가 없습니다.'")



client.run("OTY2NjI2NjA0ODUzODg2OTc4.YmEfLQ.bp8el4C8lvgI-ab1vHOL8LVxeBc")