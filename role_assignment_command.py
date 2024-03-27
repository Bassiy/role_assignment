import discord
from discord import app_commands


TOKEN = "Your_Bot_TOKEN"


intents = discord.Intents.all()
intents.messages = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# グローバル変数の初期化
global channel_ID
channel_ID = None
global role_ID
role_ID = None

@client.event
async def on_guild_join(guild):
    # ギルド（サーバー）に参加した際に最初のテキストチャンネルを見つける
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("ありがとうございます！")
            await channel.send("私は指定のチャンネルで発言があった場合、指定のロールを付与するBotです！")
            await channel.send("/channelと/roleで、それぞれを指定してください！")
            break  # 最初の送信可能なチャンネルにメッセージを送ったらループを抜ける

@client.event
async def on_ready():
    print('ログインしました')
    await tree.sync()
      

@client.event
async def on_message(message):
    global channel_ID
    global role_ID

    if message.author.bot:#Botのには反応しない
        return

    if message.channel.id != channel_ID:#指定のチャンネルのみに反応
        return    
    
    # 指定されたチャンネルでメッセージが投稿された場合
    if message.channel.id == int(channel_ID):
        role = message.guild.get_role(int(role_ID))
        #print(role)
        await message.author.add_roles(role)
        await message.add_reaction("🎉")
        print(f'ロール：{role.name} をユーザー：{message.author} に付与しました。')

@tree.command(name="channel",description="チャンネルを指定してください")
async def test_command(interaction: discord.Interaction,channel:discord.TextChannel):
    global channel_ID
    channel_ID = channel.id
    await interaction.response.send_message(channel,ephemeral=True)

@tree.command(name="role",description="付与するロールを指定してください")
async def test_command(interaction: discord.Interaction,role:discord.Role):
    global role_ID
    role_ID = role.id
    await interaction.response.send_message(role,ephemeral=True)

client.run(TOKEN)  
