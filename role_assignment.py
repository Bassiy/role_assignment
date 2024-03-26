#Bot自身のロールを上位に設定する必要がある

import discord

TOKEN = "token"
channel_ID = "channel_ID"
role_ID = "role_ID"

intents = discord.Intents.all()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')
      

@client.event
async def on_message(message):

    if message.author.bot:#Botのには反応しない
        return

    if message.channel.id != channel_ID:#指定のチャンネルのみに反応
        return    
    
    # 指定されたチャンネルでメッセージが投稿された場合
    if message.channel.id == int(channel_ID):
        role = message.guild.get_role(int(role_ID))
        #print(role)
        await message.author.add_roles(role)
        print(f'ロール：{role.name} をユーザー：{message.author} に付与しました。')

client.run(TOKEN)  