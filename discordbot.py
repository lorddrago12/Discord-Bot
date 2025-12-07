import discord
from discord.ext import commands
from discord import Interaction, app_commands

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


class View(discord.ui.View):
    @discord.ui.button(label='click me', style=discord.ButtonStyle.green, emoji='☕')
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'{interaction.user.mention}, you clicked the button!')

    @discord.ui.button(label='click me', style=discord.ButtonStyle.red, emoji='🔥')
    async def second_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'{interaction.user.mention}, you clicked the second button!')

    @discord.ui.button(label='click me', style=discord.ButtonStyle.blurple, emoji='👻')
    async def third_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'{interaction.user.mention}, you clicked the third button!')


@client.tree.command(name='button', description='Displaying a button.', guild=GUILD_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())

class Menu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Option 1", description="This is the first option", emoji="🔥", value="option1"),
            discord.SelectOption(label="Option 2", description="This is the second option", emoji="👻", value="option2"),
            discord.SelectOption(label="Option 3", description="This is the third option", emoji="☕", value="option3")
        ]

        super().__init__(placeholder="Select an option", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction): 
        await interaction.response.send_message(f'You selected {self.values[0]}')   


class menuview(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menu())



@client.tree.command(name='menu', description='Displaying a dropdown menu.', guild=GUILD_ID)
async def mymenu(interaction: discord.Interaction):
    await interaction.response.send_message(view=menuview())


client.run('YOUR_BOT_TOKEN')
