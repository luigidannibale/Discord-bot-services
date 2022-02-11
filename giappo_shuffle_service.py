@commands.command(name='giappo_shuffle',pass_context=True)
    async def _giappo_shuffle(self, ctx: commands.Context, options = ""):
        """
        Giappo suffixo shuffle service:
            while the service is active anytime a stupid dumbass joins a channel, his nickname will be modified appendiang a japanese suffix 
            to its original nickname, if the nick originally contains another suffix it will be changed.
            This service is provided by Shuffle, Giappo Shuffle. Nick Shuffle's brothero. 
            (Can work alongside Nick_shuffle or not, he's got his own legs)            
        
        Commands:
            >giappo_shuffle -s : shows the current status of the service, it can be either running or disabled
            >giappo_shuffle : toggles the service, admins only
        """
        try:
            global Giappo_shuffle_service
            
            if options == "-s": #option "-s" stands for status, if so it only sends a message containings the actual status of the service that can be either Running or Disabled
                await ctx.send(embed = (discord.Embed(title="Hey dumbass", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                      description="", 
                                                      color=discord.Color.blue())
                                    .add_field(name = "Giappo suffixo shuffle service - {}".format(status[int(Giappo_shuffle_service)]), value = " io te posso canta na canzone")))
            else: #without an option this is the actual command
            #the following if/else is a control over the permissions,for the moment only administrators can use the command  
                if ctx.author.guild_permissions.administrator: 
                    Giappo_shuffle_service = not Giappo_shuffle_service
                    await ctx.send(embed = (discord.Embed(title="Hey dumbass", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                          description="", 
                                                          color=discord.Color.green())
                                            .add_field(name = "Giappo suffixo shuffle service - {}".format(status[int(Giappo_shuffle_service)]), value = " io te posso canta na canzone")))
        
                else:
                    await ctx.send(embed = (discord.Embed(title="Hey dumbass", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                          description="X", 
                                                          color=discord.Color.red())
                                            .add_field(name = "Giappo suffixo shuffle service - {}".format(status[int(Giappo_shuffle_service)]), value = "Non hai il permesso per cambiarlo")))
        except Exception as e:
            print(e)
            
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
        
        if Giappo_shuffle_service:
            try:
                with open("suffissi-giapponesi.txt","r",encoding="utf-8") as file:
                    lista_di_suffissi = [riga for riga in file]
                    dizionario_suffissi = {indice:str(suffisso).replace("-","") for indice,suffisso in enumerate(lista_di_suffissi)}
                    import random
                    r_number = random.randint(0, len(lista_di_suffissi)-1)
                    # controllo se ha già suffisso
                    controllo = nickname.split("-")
                    for indice,elemento in enumerate(controllo):
                        if not indice: 
                            continue
                        if elemento in dizionario_suffissi.values():
                            nickname.remove("-{}".format(elemento))
                    if len(nickname +  lista_di_suffissi[r_number]) <= 32:    
                        nickname = nickname +  lista_di_suffissi[r_number]
            except Exception as e:
                print(e)
        
        #Il nick viene cambiato solamente se si possiede il ruolo che permette la modifica sul nome
        if Name_change_role_id in str(member.roles):    
            await member.edit(nick=nickname[0:32])      

    #when a member lefts a channel
    if before.channel is not None and after.channel is None:
        await member.edit(nick = member.name)        
