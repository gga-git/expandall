# -*- coding: utf-8 -*-
#

###

# Changelog
# 0.1
# First version

import weechat
import re

SCRIPT_NAME    = "expandall"
SCRIPT_AUTHOR  = "Georges"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "Expand /all to all nicks in channel (TODO -> make blacklist for bot and stuff by channel)"

settings = {}



if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
			SCRIPT_DESC, "", ""):
	for option, default_value in settings.iteritems():
		if not weechat.config_is_set_plugin(option):
			weechat.config_set_plugin(option, default_value)

	weechat.hook_command("all",
			 SCRIPT_DESC,
			 "[text]",
			 "text: text to be inserted after <all>:\n"
			 "",
			 "", "all_cmd_cb", "")


def all_cmd_cb(data, buffer, args):
	''' Command /all '''
	translate_input = args
	if not translate_input:
	   translate_input = weechat.buffer_get_string(buffer, "input")

	channel = weechat.buffer_get_string(buffer, 'localvar_channel')
	server = weechat.buffer_get_string(buffer, 'localvar_server')

	joined_nick=""
	infolist = weechat.infolist_get("irc_nick", "", server+","+channel)
	if infolist:
		while weechat.infolist_next(infolist):
			name = weechat.infolist_string(infolist, "name")
			weechat.prnt("", "buffer: %s" % name)
			joined_nick += name+" "

		weechat.infolist_free(infolist)

	translate_input=joined_nick +": "+ translate_input
	
	#outstring = translate_input.encode('UTF-8')
	outstring = translate_input
	weechat.buffer_set(buffer, 'input', outstring)
	weechat.buffer_set(buffer, 'input_pos', '%d' % len(outstring))
	return weechat.WEECHAT_RC_OK
