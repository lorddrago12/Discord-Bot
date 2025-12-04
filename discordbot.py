import discord
from discord.ext import commands
from discord import app_commands

class client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')
        
        if message.content.startswith('how are you'):
            await message.channel.send(f'I\'m fine how are you, {message.author}')
        
    async def on_member_join(self, member):
        chanel = discord.utils.get(member.guild.text_channels, name='general')
        if chanel:
            await channel.send(f'Welcome to the server, {member.mention}!')


intents = discord.Intents.default()
intents.message_content = True
client = client(command_prefix='!', intents=intents)


GUILD_ID = discord.Object(id=YOUR_SERVER_ID)

@client.tree.command(name='hello', description='Says hello to the user', guild=GUILD_ID)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.mention}!')

client.run('YOUR_BOT_TOKEN')
