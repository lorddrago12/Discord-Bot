import discord
from discord.ext import commands
from discord import app_commands

class client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

        try:
             guild = discord.Object(id=1445753336249716881)
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

@client.tree.command(name='coffebreak', description='embed demo!', guild=GUILD_ID)
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Have a coffe", url="https://www.youtube.com/@LordDrago12", description="coffe increases focus.", color=0x00ff12)
    embed.set_thumbnail(url="https://i.pinimg.com/736x/21/a6/72/21a672ca5abaaed41a285edb34252e00.jpg")
    embed.add_field(name="You can also listen to music while drinking coffe", value="music improves mood", inline=True)
    embed.set_footer(text="Have a nice day!")
    embed.set_author(name="LordDrago", url="https://www.youtube.com/@LordDrago12", icon_url="https://i.pinimg.com/736x/ef/ad/8c/efad8ca3a538cd6172c96987d71bac56.jpg")
    await interaction.response.send_message(embed=embed)


client.run('YOUR_BOT_TOKEN')

