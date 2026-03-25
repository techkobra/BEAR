"""
voice.py
Handles B.E.A.R.'s text-to-speech voice output using Edge-TTS (online, free).
Streams spoken audio into Discord voice channels.
"""

import asyncio
import discord
import edge_tts
import os
import uuid

# Voice settings
VOICE_NAME = "en-US-GuyNeural"  # Older American male voice
VOICE_RATE = "+0%"              # Speed (0% = normal)
VOICE_VOLUME = "+0%"            # Volume (0% = normal)


async def generate_tts_audio(text: str) -> str:
    """
    Generates a TTS audio file using Edge-TTS and returns the file path.
    """
    output_file = f"tts_{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE_NAME,
        rate=VOICE_RATE,
        volume=VOICE_VOLUME
    )

    await communicate.save(output_file)
    return output_file


async def speak_text(vc: discord.VoiceClient, text: str):
    """
    Converts text to speech and plays it in the connected voice channel.
    """
    if vc is None or not vc.is_connected():
        return

    # Generate TTS audio
    audio_file = await generate_tts_audio(text)

    # Play audio in Discord
    audio_source = discord.FFmpegPCMAudio(audio_file)
    vc.play(audio_source)

    # Wait until playback finishes
    while vc.is_playing():
        await asyncio.sleep(0.1)

    # Clean up temporary file
    try:
        os.remove(audio_file)
    except:
        pass
