import discord

class delete():
    def __init__(self, bot):
        self.bot = bot
        
        async def on_message(self,message,ctx):
            if message.author.id == '436294612521582603' and ' ' in message.content:
                await self.bot.delete_message(message.content)
                
def setup(bot):
    bot.add_cog(delete(bot))
