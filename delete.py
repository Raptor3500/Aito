import discord

class delete():
    def __init__(self, bot):
        self.bot = bot
        
        async def on_message(self,message,ctx,*args):
            mesg = ' '.join(args)
            if message.author.id == '436294612521582603':
                await self.bot.delete_message(mesg)
                
def setup(bot):
    bot.add_cog(delete(bot))
