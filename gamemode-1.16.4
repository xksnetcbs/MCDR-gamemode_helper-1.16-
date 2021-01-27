# -*- coding: utf-8 -*-
import json
import re
global x
global y
global z
PLUGIN_METADATA = {
	'id': 'gmode',
	'version': '1.3.2',
	'name': 'Change Your Gamemode Like Tweakeroo!',
	'author': [
		'DC_Provide'
   ],
	'link': 'Nope...[doge]'
}

# set it to 0 to disable hightlight
# 将其设为0以禁用高亮
HIGHLIGHT_TIME = 15
playerList = ''
playerX = 0
playerY = 0
playerZ = 0
here_user = 0
def on_info(server, info):
        global position, demen
        global playerX, playerY, playerZ
        PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
        i = 0
        if info.content == '!c':
                position = PlayerInfoAPI.getPlayerInfo(server, info.player, path='Pos')
                server.execute("gamemode spectator " + info.player)
                playerX, playerY, playerZ = position
                f = open("./plugins/gm/" + info.player,'r')
                if f.read() != '':
                        server.say("装你妈的B！")
                        return 0
                f.close()
                f = open("./plugins/gm/" + info.player,'w')
                f.write(str(playerX) + ' ' + str(playerY) + ' ' + str(playerZ))
                f.close()
                f = open("./plugins/gm/" + info.player + ".dat", 'w')
                f.write(str(PlayerInfoAPI.getPlayerInfo(server, info.player, path='Dimension')))
                f.close()
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
