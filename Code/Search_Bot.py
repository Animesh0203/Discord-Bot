# Import Discord Bot
import discord
from discord.channel import VoiceChannel
from discord.embeds import Embed
from discord.ext import commands
from discord.player import FFmpegAudio
import youtube_dl
import os
from youtubesearchpython import VideosSearch
import nacl

client = commands.Bot(command_prefix="$")

@client.command()
async def join(ctx):
      if ctx.author.voice is None:
            await ctx.send("No on is there")
      voiceChannel = discord.utils.get(ctx.guild.voice_channels,name = "General")
      if ctx.voice_client is None:
            await voiceChannel.connect()
            

@client.command()
async def play(ctx,url:str):
       song_there = os.path.isfile("song.mp3")
       try:
        if song_there:
              os.remove("song.mp3")
       except PermissionError:
            await ctx.send("") 
            
       ctx.voice_client.stop()
       ffmpeg_options = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
       ydl_options =  {'format': "bestaudio"}
       VC = ctx.voice_client


       with youtube_dl.YoutubeDL(ydl_options) as ydl:     
            info = ydl.extract_info("ytsearch:%s" % ctx, download = False)['entries'][0]
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
            print(url2)
            VC.play(source) 
       await ctx.send("Playing"+ctx)


@client.command()
async def dis(ctx):
       await ctx.voice_client.disconnect()
       await ctx.send("bye bye")


@client.command()
async def resume(ctx):
       ctx.voice_client.resume()

@client.command()
async def pause(ctx):
       ctx.voice_client.pause()

@client.command()
async def stop(ctx):
       ctx.voice_client.stop()
       


client.run('OTE1MTc3NDk4NzU5Nzk4ODI0.YaXzdg.o87acfvZVhZs5C-1Epn_dRk71-c')
