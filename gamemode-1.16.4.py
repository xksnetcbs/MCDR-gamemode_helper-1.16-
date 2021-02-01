# -*- coding: utf-8 -*-
import json
import time
from mcdreforged.api.all import *
import re
import os

PLUGIN_METADATA = {
	'id': 'gmode',
	'version': '1.3.7',
	'name': 'Change Your Gamemode Like Tweakeroo!',
	'author': [
		'DC_Provide'
   ],
	'link': 'Nope...[doge]'
}

@new_thread(PLUGIN_METADATA['name'])
def show_me(source: CommandSource):
        if isinstance(source, PlayerCommandSource):
                api = source.get_server().get_plugin_instance('minecraft_data_api')
                coord = api.get_player_coordinate(source.player)
                
                dim = api.get_player_dimension(source.player)
                dim_text = api.get_dimension_translation_text(dim)
                f = open("./plugins/gm/" + source.player, 'r')
                if f.read() != '':
                        return 2
                f.close()
                f = open("./plugins/gm/" + source.player, 'w')
                f.write(str(coord.x) + ' ' + str(coord.y) + ' ' + str(coord.z))
                f.close()
                f = open("./plugins/gm/" + source.player + '.dat', 'w')
                if dim == 0:
                        f.write("minecraft:overworld")
                elif dim == 1:
                        f.write("minecraft:the_end")
                else:
                        f.write("minecraft:the_nether")
                f.close()
                source.get_server().execute("gamemode spectator " + source.player)

def on_load(server: ServerInterface, prev):
        #server.register_help_message('!!s-here', '广播坐标并高亮玩家')
        server.register_command(Literal('!c').runs(show_me))
def on_player_join(server, info):
        #server.reply("你现在可以使用GM插件了")
        server.execute("gamemode survival " + str(info.player))
        f = open("./plugins/gm/" + str(info.player), 'w')
        f.write('')
        f.close()
def on_player_joined(server, player, info):
        if os.path.exists("./plugins/gm/" + str(info.player)) == False:
                server.say("歪！你还没有注册Gamemode插件呢！不注册你用不了的啊！")
                server.say("还不快输入!Clear注册一下！")
def on_info(server, info):
        global position, demen
        global playerX, playerY, playerZ
        #PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
        i = 0
        if info.content == '!s':
                f = open("./plugins/gm/" + info.player, 'r')
                pos = f.read()
                f.close()
                f = open("./plugins/gm/" + info.player, 'w')
                f.write('')
                f.close()
                f = open("./plugins/gm/" + info.player + '.dat', 'r')
                dem = f.read()
                server.execute("execute at " + info.player + " in " + dem + " run tp " + info.player + " " + pos)
                f.close()
                server.execute("gamemode survival " + info.player)
        if info.content == '!Clear':
                on_player_join(server, info)
