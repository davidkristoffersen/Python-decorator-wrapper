#!/usr/bin/telegram-cli

import tgl
from pprint import pprint as p

def on_loop():
    # do_something()
    peer.send_msg("Yo")

tgl.set_on_loop(on_loop)
# p(dir(tgl))
# p(type(tgl))
