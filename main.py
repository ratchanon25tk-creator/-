import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

KEYWORDS = ["แจกรหัส", "แจกไอดี", "แจกรหัสฟรี", "รหัสฟีฟาย", "รหัส roblox", "รหัสบล็อกฟุต"]

@bot.event
async def on_ready():
    print(f'✅ บอท {bot.user} ออนไลน์เรียบร้อยแล้ว!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg_content = message.content.lower()
    found_keyword = any(keyword in msg_content for keyword in KEYWORDS)
    pattern_account = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[^\s]+'
    found_credentials = re.search(pattern_account, message.content)

    if found_keyword or found_credentials:
        embed = discord.Embed(
            title="🚨 ตรวจพบการแจกรหัส / ข้อมูลบัญชี!",
            description=f"แจ้งเตือนคุณ {message.author.mention} ห้ามโพสต์หรือแจกรหัสในช่องนี้นะครับ",
            color=discord.Color.red()
        )
        embed.add_field(name="ข้อความที่พบ", value=message.content, inline=False)
        await message.channel.send(embed=embed)

    await bot.process_commands(message)

# ดึง Token จากระบบคลาวด์
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
              
