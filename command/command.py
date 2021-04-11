from discord.ext import commands
const Discord = require('discord.js');
const client = new Discord.Client();
var prefix = "*";

client.on('message', message => {
  if (message.content === 'cc') {
    message.reply('Salut')
  }
})

client.on('message', message => {
  if (message.content === 'A+') {
    message.reply('A+')
  }
})

client.on('message', message => {
  if (message.content === 'ça vas ?') {
    message.reply('oui et toi ?')
  }
})

client.on('message', message => {
    if (message.content === 'MDR') {
      message.reply('Je suis mort de rire ! : https://tenor.com/M31E.gif')
    }
  })

client.on('message', message => {
  if (message.content === 'LOL') {
    message.reply('Alerte Raid !')
  }
})

client.on('message', message => {
  if (message.content === 'oui') {
    message.reply('Non !')
  }
})

client.on('message', message => {
  if (message.content === '*invite') {
    message.reply('https://discord.gg/ZaypxYV')
  }
})

client.on('message', message => {
  if (message.content === '*pay') {
    message.reply('Fait un dons sur paypal ! https://www.paypal.me/gael47 :wink: ')
  }
})

client.on('message', message => {
  if (message.content === '*site') {
    message.reply('https://animacraft.fr')
  }
})

client.on('message', message => {
  if (message.content === '*forum') {
    message.reply('Le forum : https://animacraft.fr/forums')
  }
})

client.on('message', message => {
  if (message.content === '*créateur') {
    message.reply('Le créateur de AnimaCraft est @AlexTheKing#0736')
  }
})

client.on('message', message => {
  if (message.content === '*boutique') {
    message.reply('https://animacraft.fr/boutique')
  }
})

client.on('message', message => {
  if (message.content === '*youtube') {
    message.reply('La chaîne youtube de notre serveur : https://www.youtube.com/channel/UCKniABB51Cr2T6NdL7oDy8g')
  }
})

client.on('guildMemberAdd', member => {

  const welcomechannel = member.guild.channels.find('id', '627418418764840989') // ID de notre channel
  var embed = new Discord.RichEmbed()
  .setColor('#76D880')
  .setDescription(`:inbox_tray: :tada: <@${member.user.id}> Bienvenue sur le AnimaCraft Serveur Gaming 2.0 !!`)
  return welcomechannel.send({embed})

  });

client.on('guildMemberRemove', member => {

    const welcomechannel = member.guild.channels.find('id', '627418418764840989')
    var embed = new Discord.RichEmbed()
    .setColor('#76D880')
    .setDescription(`:inbox_tray: :sob: <@${member.user.id}> nous a quitté !! `)
    return welcomechannel.send({embed})

  });

  client.on("ready", () => {
    client.user.setActivity("Pour voir les info *info. En Developpement par AlexTheKing");
  }); 

  client.on('message' , message => {
    if(message.content === "Bonjour"){

    if(message.author.id === "260039734678519808"){
      message.reply("Bonjour Dieu Eclipse") 
    } else {
      message.reply("Salut !");
      console.log("wsh");
     }
    }

    if(message.content === "ça va ?"){
      if(message.author.id === "260039734678519808"){
        message.reply("Oui Maître ! Et vous ?")
      }else{
      message.reply("Ouais et toi ?")
      };
    }

    if(message.content === "Ouais merci"){
      message.reply("De rien !")
    }

    if(message.content === prefix + "info"){
      var info_embed = new Discord.RichEmbed()
      .setColor("#DC143C")
      .setTitle("Les informations de mon Bot et du Serveur !")
      .addField(" :robot: Nom :", `${client.user.tag}`, true)
      .addField("Tag du bot :hash:", `#${client.user.discriminator}`)
      .addField(":id: ", `${client.user.id}`)
      .addField("Tu veux soutenir AlexTheKing ?", " https://www.paypal.me/gael47 :wink: ")
      .addField("Nombre de Membres", message.guild.memberCount)
      .addField("En développement par AlexTheKing", "AlexTheKing#0736")
      .setFooter("Info - Bot")
      message.channel.sendEmbed(info_embed);
      console.log("Info");
  }

});

client.on('ready', () => {
  console.log('I am ready!');
});

if(message.content === prefix + "messages"){
      var info_embed = new Discord.RichEmbed()
      .setColor("#DC143C")
      .setTitle("Les commandes du bot!")
      .addField("*invite", "Récuperer inviation du serveur")
      .addField("*forum", "Récuperer le lien du forum")
      .addField("*boutique", "Récuperer le lien de la boutique")
      .addField("*youtube", " Récuperer le lien de la chaîne YouTube")
      .addField("*créateur", "Savoir qui a crée AnimaCraft")
      .addField("*pay", "Faire un dons !")
      .addField("Les messages du bot", "")
      .addField("cc", "Réponse du bot : Salut")
      .addField("ça vas ?", "Réponse du bot : oui et toi ?")
      .addField("MDR", "Réponse du bot : Je suis mort de rire ! https://tenor.com/M31E.gif ")
      .addField("LOL", "Réponse du bot : Alerte Raid ! ")
      .addField("Oui", "Réponse du bot : Non ! ")
      .addField("A+", "Réponse du bot : A+ ")
      .setFooter("Commandes - Bot")
      message.channel.sendEmbed(info_embed);
      console.log("Commandes");
    }

client.on('message', message => {
  // Ignore messages that aren't from a guild
  if (!message.guild) return;

  // If the message content starts with "!kick"
  if (message.content.startsWith('*kick')) {
    // Assuming we mention someone in the message, this will return the user
    // Read more about mentions over at https://discord.js.org/#/docs/main/stable/class/MessageMentions
    const user = message.mentions.users.first();
    // If we have a user mentioned
    if (user) {
      // Now we get the member from the user
      const member = message.guild.member(user);
      // If the member is in the guild
      if (member) {
        /**
         * Kick the member
         * Make sure you run this on a member, not a user!
         * There are big differences between a user and a member
         */
        member.kick('Raison facultatif').then(() => {
          // We let the message author know we were able to kick the person
          message.reply(`L'utilisateur ${user.tag} à bien été kick`);
        }).catch(err => {
          // An error happened
          // This is generally due to the bot not being able to kick the member,
          // either due to missing permissions or role hierarchy
          message.reply('Tu n as pas la permission de kicker des membres');
          // Log the error
          console.error(err);
        });
      } else {
        // The mentioned user isn't in this guild
        message.reply('L utilistateur n est pas sur le serveur !');
      }
    // Otherwise, if no user was mentioned
    } else {
      message.reply('Tu as oublié de mentionner l utilisateur !');
    }
  }
});

client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', message => {
  // Ignore messages that aren't from a guild
  if (!message.guild) return;

  // if the message content starts with "!ban"
  if (message.content.startsWith('*ban')) {
    // Assuming we mention someone in the message, this will return the user
    // Read more about mentions over at https://discord.js.org/#/docs/main/stable/class/MessageMentions
    const user = message.mentions.users.first();
    // If we have a user mentioned
    if (user) {
      // Now we get the member from the user
      const member = message.guild.member(user);
      // If the member is in the guild
      if (member) {
        /**
         * Ban the member
         * Make sure you run this on a member, not a user!
         * There are big differences between a user and a member
         * Read more about what ban options there are over at
         * https://discord.js.org/#/docs/main/stable/class/GuildMember?scrollTo=ban
         */
        member.ban({
          reason: 'Raison Facultatif',
        }).then(() => {
          // We let the message author know we were able to ban the person
          message.reply(`L utilisateur ${user.tag} à bien été Banni !`);
        }).catch(err => {
          // An error happened
          // This is generally due to the bot not being able to ban the member,
          // either due to missing permissions or role hierarchy
          message.reply('Tu n as pas la permission de bannir un membre !');
          // Log the error
          console.error(err);
        });
      } else {
        // The mentioned user isn't in this guild
        message.reply('L uttilisateur mentionner n est pas sur le Serveur !');
      }
    } else {
    // Otherwise, if no user was mentioned
      message.reply('Tu n as pas mentionner l utilisateur !');
    }
  }
});

client.on('message', function(message) {
  if (message.content == "*clear") {
      if (message.member.hasPermission("MANAGE_MESSAGES")) {
          message.channel.fetchMessages()
             .then(function(list){
                  message.channel.bulkDelete(list);
              }, function(err){message.channel.send("Erreur")})                        
      }
  }

});

client.on('ready', () => {
console.log('I am ready!');
});

client.on('message', message => {
if (message.content === '*admin') {
  message.reply('Les commandes Administrateurs sont : *kick : pour expulser un utilisateur/*ban : pour bannir un utilisateur/*clear : Supprime 5 messages')
}
})
