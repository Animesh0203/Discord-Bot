# Import Discord Bot
from re import search
import discord
from discord.channel import VoiceChannel
from discord.embeds import Embed
from discord.ext import commands
from discord.player import FFmpegAudio
import youtube_dl
import os
import traceback,json
import youtube_search
import nacl

client = commands.Bot(command_prefix="$")

@client.command()
async def join(ctx):
      if ctx.author.voice is None:
            await ctx.send("No one is there")
      voiceChannel = discord.utils.get(ctx.guild.voice_channels,id =924334945827168270)
      if ctx.voice_client is None:
            await voiceChannel.connect()
            

@client.command()
async def play(ctx,str):
      song_there = os.path.isfile("song.mp3")
      try:
        if song_there:
              os.remove("song.mp3")
      except PermissionError:
            await ctx.send("") 
      #voiceChannel = discord.utils.get(ctx.guild.voice_channels,id =922837520138510346)
      #await voiceChannel.connect()
      #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      ctx.voice_client.stop()
      ffmpeg_options = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
      ydl_options =  {'format': "bestaudio"}
      VC = ctx.voice_client 
      yt = youtube_search.YoutubeSearch(search, max_results=1).to_json()
      yt_id = str(json.loads(yt)['videos'][0]['id'])
      yt_url = 'https://www.youtube.com/watch?v='+yt_id
      print(yt_id)


      with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(yt_url,download=False)
            url2 = info['formats'][0]['yt_url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
            VC.play(source)
         
             

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
