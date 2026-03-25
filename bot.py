import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.voice_states = True

# Bot setup
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None  # We'll add custom help later
)

# -----------------------------
# Personality + Memory Hooks
# -----------------------------
# These will connect to bear_core.py later
def bear_reply(user_message: str) -> str:
    """
    Placeholder for B.E.A.R.'s personality engine.
    This will be replaced by bear_core.py logic.
    """
    return f"B.E.A.R. heard you say: {user_message}"


# -----------------------------
# Events
# -----------------------------
@bot.event
async def on_ready():
    print(f"B.E.A.R. is online as {bot.user}")


@bot.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return

    # Basic text response using personality hook
    response = bear_reply(message.content)
    await message.channel.send(response)

    # Allow commands to still work
    await bot.process_commands(message)


# -----------------------------
# Slash Commands
# -----------------------------
@bot.tree.command(name="bear", description="Talk to B.E.A.R.")
async def bear_command(interaction: discord.Interaction, message: str):
    response = bear_reply(message)
    await interaction.response.send_message(response)


# -----------------------------
# Voice Commands
# -----------------------------
@bot.command(name="join")
async def join(ctx):
    """Join the user's voice channel."""
    if ctx.author.voice is None:
        await ctx.send("You must be in a voice channel first.")
        return

    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("B.E.A.R. has joined the voice channel.")


@bot.command(name="leave")
async def leave(ctx):
    """Leave the voice channel."""
    if ctx.voice_client is None:
        await ctx.send("I'm not in a voice channel.")
        return

    await ctx.voice_client.disconnect()
    await ctx.send("B.E.A.R. has left the voice channel.")


# -----------------------------
# Run the bot
# -----------------------------
bot.run(TOKEN)
