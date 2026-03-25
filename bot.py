iimport os
import discord
from discord.ext import commands
from bear_core import bear_reply

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

WAKE_WORD = "bear,"

@bot.event
async def on_ready():
    print(f"B.E.A.R. is online as {bot.user}")

@bot.event
async def on_message(message):
    # ignore bot messages
    if message.author == bot.user:
        return

    # lowercase + strip for clean matching
    content = message.content.lower().strip()

    # only respond when message starts with wake word
    if content.startswith(WAKE_WORD):
        # remove wake word from the message
        user_text = content[len(WAKE_WORD):].strip()

        # generate personality reply
        reply = bear_reply(user_text)

        # send text reply
        await message.channel.send(reply)

    # allow commands to still work
    await bot.process_commands(message)

# optional commands (voice disabled)
@bot.command()
async def join(ctx):
    await ctx.send("Voice mode is disabled right now.")

@bot.command()
async def leave(ctx):
    await ctx.send("Voice mode is disabled right now.")

bot.run(os.getenv("DISCORD_TOKEN"))
