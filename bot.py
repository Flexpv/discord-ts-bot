import discord
from discord.ext import commands
import os
import asyncio

# Bot Setup
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Channel der ignoriert werden soll
IGNORED_CHANNEL = "24/7 🔉"

# Pfade zu den Sound-Dateien
SOUND_ENTER = "sounds/user_joined.wav"
SOUND_LEAVE = "sounds/user_left.wav"

# Dictionary um zu tracken in welchem Channel der Bot gerade ist
bot_voice_clients = {}


@bot.event
async def on_ready():
    print(f'✅ Bot ist online als {bot.user}')
    print(f'🎵 TeamSpeak Sounds aktiviert!')
    print(f'🚫 Ignorierter Channel: {IGNORED_CHANNEL}')


@bot.event
async def on_voice_state_update(member, before, after):
    # Ignoriere Bots
    if member.bot:
        return
    
    # Ignoriere wenn der Member stumm geschalten wird oder ähnliches (kein Channel-Wechsel)
    if before.channel == after.channel:
        return
    
    # User hat einen Channel betreten
    if after.channel is not None:
        # Prüfe ob es der ignorierte Channel ist
        if after.channel.name == IGNORED_CHANNEL:
            return
        
        await play_sound(after.channel, SOUND_ENTER)
    
    # User hat einen Channel verlassen
    if before.channel is not None:
        # Prüfe ob es der ignorierte Channel ist
        if before.channel.name == IGNORED_CHANNEL:
            return
        
        # Nur Sound abspielen wenn noch andere User im Channel sind
        # (sonst würde der Bot den Sound spielen nachdem alle weg sind)
        remaining_members = [m for m in before.channel.members if not m.bot]
        if len(remaining_members) > 0:
            await play_sound(before.channel, SOUND_LEAVE)


async def play_sound(channel, sound_file):
    """Spielt einen Sound in einem Voice Channel ab"""
    
    # Prüfe ob Sound-Datei existiert
    if not os.path.exists(sound_file):
        print(f'⚠️ Sound-Datei nicht gefunden: {sound_file}')
        return
    
    try:
        # Verbinde zum Voice Channel wenn nicht schon verbunden
        voice_client = discord.utils.get(bot.voice_clients, guild=channel.guild)
        
        if voice_client is None:
            voice_client = await channel.connect()
        elif voice_client.channel != channel:
            await voice_client.move_to(channel)
        
        # Warte kurz falls der Bot gerade einen anderen Sound spielt
        while voice_client.is_playing():
            await asyncio.sleep(0.1)
        
        # Spiele den Sound ab
        voice_client.play(discord.FFmpegPCMAudio(sound_file))
        
        # Warte bis der Sound fertig ist
        while voice_client.is_playing():
            await asyncio.sleep(0.1)
        
        # Verlasse den Channel wenn niemand mehr drin ist (außer Bots)
        await asyncio.sleep(1)  # Kurze Pause
        remaining_members = [m for m in channel.members if not m.bot]
        if len(remaining_members) == 0:
            await voice_client.disconnect()
    
    except Exception as e:
        print(f'❌ Fehler beim Abspielen: {e}')


# Bot starten
if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    if TOKEN is None:
        print("❌ FEHLER: DISCORD_TOKEN nicht gefunden!")
        print("Bitte setze die Umgebungsvariable DISCORD_TOKEN in Railway.app")
    else:
        bot.run(TOKEN)
