import discord

class delete():
    def __init__(self, bot):
        self.bot = bot
        
        async def on_message(self,message,ctx):
            if ctx.message.author.id == '436294612521582603':
               if ' ' in message.content:
                await self.bot.delete_message(ctx.message)
