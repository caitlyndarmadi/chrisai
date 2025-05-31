import discord
from discord.ext import commands
import uuid
import os
from ai import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name='upload_image')
async def upload_image(ctx):
    attachments = ctx.message.attachments
    
    if not attachments:
        await ctx.send("❌ Tidak ada gambar yang dilampirkan. Silakan unggah gambar bersamaan dengan perintah ini.")
        return

    for attachment in attachments:
        if attachment.content_type and attachment.content_type.startswith('image'):
            # Buat nama file unik menggunakan UUID
            ext = os.path.splitext(attachment.filename)[1]  # ambil ekstensi (misal .png)
            unique_name = f"{uuid.uuid4()}{ext}"
            save_path = os.path.join("images", unique_name)
            await attachment.save(save_path)

            result = get_class(save_path)
            if result == "Chris Pratt":
                await ctx.send(f"""Ini adalah gambar dari aktor Chris Pratt
        Nama: Chris Pratt
        Tanggal lahir: 21 Juni 1979
        Asal: Amerika Serikat
        Film yang dibintangi: Guardians of the Galaxy Trilogy, Jurassic World, The Electric State""")
            elif result == "Chris Evans":
                await ctx.send(f"""Ini adalah gambar dari aktor Chris Evans
        Nama: Chris Evans
        Tanggal lahir: 13 Juni 1981
        Asal: Amerika Serikat
        Film yang dibintangi: The Avengers, Fantastic Four, Gifted""")
            elif result == "Chris Hemsworth":
                await ctx.send(f"""Ini adalah gambar dari aktor Chris Hemsworth
        Nama: Chris Hemsworth
        Tanggal lahir: 11 Agustus 1983
        Asal: Australia
        Film yang dibintangi: Thor, Extraction, Furiosa: A Mad Max Saga""")


bot.run("help")