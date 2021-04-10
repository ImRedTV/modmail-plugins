importez la  discorde
de la  discorde . commandes d' importation ext  

à partir  des contrôles d' importation de base  
du  noyau . modèle d'  importation  PermissionLevel

class  Publish ( commandes . Cog ):
    "" "Publier les messages envoyés dans les canaux d'annonces" ""
    
    def  __init__ ( self , bot ):
        soi . bot  =  bot

    @ commandes . commande ()
    @ chèques . has_permissions ( PermissionLevel . MODERATOR )
    async  def  publish ( self , ctx , message_id : discord . Message ):
        "" "Publiez le message envoyé dans le canal d'annonce. \ N [Reportez-vous ici] (https://github.com/codeinteger6/modmail-plugins/blob/master/publish/README.md) pour des conseils détaillés." ""
        attendre  message_id . publier ()
        attendez  ctx . send ( "Message publié avec succès." )
                                        
 configuration def ( bot ):
    bot . add_cog ( Publier ( bot ))
