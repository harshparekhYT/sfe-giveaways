from disco.bot import Plugin, Config
import random


class ExtraPluginConfig(Config):

    cat_ids = [
        116757237262843906,  # Poptart
        137919409644765184,  # Jess
        150662786257518592,  # Zach
        210118905006522369,  # Ori
        249462738257051649,  # Lost
        303502679089348608,  # 1A3
        390906358259777536   # CustomName
    ]

    cat_should_ping = True

    cat_noun = "person"

    hug_phrases = [
        "<@{a}> gave <@{b}> a big big hug!"
    ]
    fight_phrases = [
        "<@{a}> fought with <@{b}> with a large fish.",
        "<@{a}> tried to fight <@{b}>, but it wasn't very effective!",
        "<@{a}> fought <@{b}>, but they missed.",
        "<@{a}> fought <@{b}> with a piece of toast!",
        "<@{a}> and <@{b}> are fighting with a pillow!"
    ]


@Plugin.with_config(ExtraPluginConfig)
class ExtraPlugin(Plugin):

    @Plugin.command("hug", "<person:user>", level=0)
    def hug_command(self, event, person):
        message = random.choice(self.config.hug_phrases)
        event.msg.reply(message.format(
            a=str(event.msg.author.id),
            b=str(person.id)
        ))

    @Plugin.command("fight", "<person:user>", level=0)
    def fight_command(self, event, person):
        message = random.choice(self.config.fight_phrases)
        event.msg.reply(message.format(
            a=str(event.msg.author.id),
            b=str(person.id)
        ))

    @Plugin.command("source", level=0)
    def open_source(self, event):
        event.msg.reply(
            "We are open-source! Go here to see the GitHub repo: https://github.com/brxxn/sfe-giveaways")

    @Plugin.command("help", level=0)
    def help(self, event):
        event.msg.reply(
            "List of Commands: https://github.com/brxxn/sfe-giveaways/wiki/Commands")

    @Plugin.command("poptart", "[ping:int]", "[noun:str...]", level=0, aliases=["cat"])
    def poptart(self, event, ping=None, noun=str):
        """This is the poptart command - Given to Poptart for most messages in a giveaway."""

        if ping and event.author.id == 116757237262843906:
            if ping == 1:
                event.msg.delete()
                self.config.cat_should_ping = False
                event.msg.reply(
                    ":ok_hand: Disabled pings. Enjoy your day, you fine cat.")
                return
            elif ping == 2:
                event.msg.delete()
                self.config.cat_should_ping = True
                event.msg.reply(
                    ":ok_hand: Enabled pings. Enjoy your day, you fine cat.")
                return
            elif ping == 3:
                event.msg.delete()
                if noun:
                    self.config.cat_noun = noun
                    event.msg.reply(":ok_hand: Noun set to {a}. Enjoy your day, you fine cat.".format(
                        a=str(self.config.cat_noun)))
                else:
                    event.msg.reply(
                        ":negative_squared_cross_mark: Expecting a string.")
            else:
                return event.msg.reply(":negative_squared_cross_mark: Expecting 1-3.")

        if event.author.id not in self.config.cat_ids:
            return

        event.msg.delete()

        if self.config.cat_should_ping:
            event.msg.reply(
                "**PSA: <@116757237262843906> is the coolest {a} here.**".format(a=str(self.config.cat_noun)))
        else:
            event.msg.reply(
                "**PSA: Cat is the coolest {a} here.**".format(a=str(self.config.cat_noun)))
