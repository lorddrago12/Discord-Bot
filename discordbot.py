import discord

class client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')
    # This function is called when the bot is ready and connected to Discord.
    async def on_message(self, message):
        if message.author == self.user:
            return
        # If the message starts with 'hello', respond with a greeting.
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')
        # If the message starts with 'how are you', respond accordingly.
        if message.content.startswith('how are you'):
            await message.channel.send(f'I\'m fine how are you, {message.author}')
        # If a new me member joins, welcome them to the server.
    async def on_member_join(self, member):
        chanel = discord.utils.get(member.guild.text_channels, name='general')
        if chanel:
            await channel.send(f'Welcome to the server, {member.mention}!')


intents = discord.Intents.default()
intents.message_content = True


client = client(intents=intents)
client.run('YOUR_BOT_TOKEN')