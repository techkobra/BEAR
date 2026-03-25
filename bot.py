import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# B.E.A.R. modules
from bear_core import bear_reply
from voice import speak_text

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)


# -----------------------------
# Basic Events
# -----------------------------
@bot.event
async def on_ready():
    print(f"B.E.A.R. is online as {bot.user}")


# -----------------------------
# Voice Channel Commands
# -----------------------------
@bot.command(name="join")
async def join(ctx):
    """Join the user's current voice channel."""
    if ctx.author.voice is None:
        await ctx.send("You must be in a voice channel first.")
        return

    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("B.E.A.R. has joined the voice channel.")


@bot.command(name="leave")
async def leave(ctx):
    """Leave the current voice channel."""
    if ctx.voice_client is None:
        await ctx.send("B.E.A.R. is not in a voice channel.")
        return

    await ctx.voice_client.disconnect()
    await ctx.send("B.E.A.R. has left the voice channel.")


# -----------------------------
# Speak Command (TTS)
# -----------------------------
@bot.command(name="speak")
async def speak(ctx, *, message: str):
    """B.E.A.R. speaks the message in the voice channel."""
    vc = ctx.voice_client

    if vc is None:
        await ctx.send("B.E.A.R. must be in a voice channel to speak. Use !join first.")
        return

    # Generate personality-shaped response
    response = bear_reply(message)

    # Speak it
    await speak_text(vc, response)

    # Also show the text in chat
    await ctx.send(f"B.E.A.R. says: {response}")


# -----------------------------
# Text Response Command
# -----------------------------
@bot.command(name="bear")
async def bear(ctx, *, message: str):
    """B.E.A.R. replies in text using personality engine."""
    response = bear_reply(message)
    await ctx.send(response)


# -----------------------------
# Run the bot
# -----------------------------
bot.run(TOKEN)
