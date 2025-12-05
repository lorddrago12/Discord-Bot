import discord
from discord.ext import commands
from discord import app_commands

class client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

        try:
             guild = discord.Object(id=YOUR_BOT_ID)
             synced = await self.tree.sync(guild=guild)
             print(f'Synced {len(synced)} command(s) to the guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

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


GUILD_ID = discord.Object(id=YOUR_BOT_ID)

@client.tree.command(name='hello', description='Says hello to the user', guild=GUILD_ID)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.mention}!')

@client.tree.command(name='printer', description='Prints whatever the user input.', guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run('YOUR_API_KEY')
