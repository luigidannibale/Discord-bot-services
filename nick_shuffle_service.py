"""
This is a portion of code to insert in a given bot. First to import this code in your bot study a bit the official docs.
I am using a global variable "Nick_shuffle service" declared as True, and a global variable Name_change_role_id = "id=931218456951601685",
moreover im using a file named "nomi.txt" in wich i store all the names the service can assign to the users.
"""

"""
Add this as command in a cog or as bot command
"""
@commands.command(name='nick_shuffle',pass_context=True)
    async def _nick_shuffle(self, ctx: commands.Context, options = ""):
        """
        Nick_shuffle service :
            There's a secret file fulfilled with strange names on each line somewhere in this shitty world,
            while the service is active anytime a stupid dumbass joins a channel, his nickname will be renewed with a random one from the file.
            This service is provided by Shuffle, Nick Shuffle.
        
        Commands:
            >nick_shuffle -s : shows the current status of the service, it can be either running or disabled
            >nick_suhffle : toggles the service, admins only
        """
        try:
            global Nick_shuffle_service
            
            if options == "-s": #option "-s" stands for status, if so it only sends a message containings the actual status of the service that can be either Running or Disabled
                await ctx.send(embed = (discord.Embed(title="Hey dumbass", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                      description="", 
                                                      color=discord.Color.blue())
                                    .add_field(name = "Nick shuffle service - {}".format(status[int(Nick_shuffle_service)]), value = " io te posso canta na canzone")))
            else: #without an option this is the actual command
            #the following if/else is a control over the permissions,for the moment only administrators can use the command
                if ctx.author.guild_permissions.administrator: 
                    Nick_shuffle_service = not Nick_shuffle_service
                    await ctx.send(embed = (discord.Embed(title="Hey dumbass", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                          description="", 
                                                          color=discord.Color.green())
                                            .add_field(name = "Nick shuffle service - {}".format(status[int(Nick_shuffle_service)]), value = " io te posso canta na canzone")))
        
                else:
                    await ctx.send(embed = (discord.Embed(title="Hey dumbass", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                          description="X", 
                                                          color=discord.Color.red())
                                            .add_field(name = "Nick shuffle service - {}".format(status[int(Nick_shuffle_service)]), value = "Non hai il permesso per cambiarlo")))
        except Exception as e:
            print(e)

"""
Add this code in the on_voice_state_update() method in the bot event
"""
@bot.event
async def on_voice_state_update(member, before, after):
    #when a member joins a channel 
    if before.channel is None and after.channel is not None:
        nickname = member.nick
        if Nick_shuffle_service:
            try:
                with open("nomi.txt","r",encoding="utf-8") as file:
                    lista_di_nomi = [riga for riga in file]
                    import random
                    r_number = random.randint(0, len(lista_di_nomi)-1)
                    nickname = lista_di_nomi[r_number]
            except Exception as e:
                print(e)
        
            except Exception as e:
                print(e)
        
        #Nick is only changed if the users has the role
        if Name_change_role_id in str(member.roles):    
            await member.edit(nick=nickname[0:32])      

    #when a member lefts a channel the name is reset
    if before.channel is not None and after.channel is None:
        await member.edit(nick = member.name)
