#!/usr/bin/python3

#from itertools import takewhile
#from pprint import pprint

import i3ipc # https://github.com/acrisci/i3ipc-python
i3 = i3ipc.Connection()
print("starting")

#################### -- window management -- ####################
def left_gap():
    i3.command('gaps left current set 640')
    i3.command('gaps right current set 0')
    
def right_gap():    
    i3.command('gaps right current set 640')
    i3.command('gaps left current set 0')


def remove_gaps():
    i3.command('gaps left current set 0')
    i3.command('gaps right current set 0')    
   
def make_window_normal(workspace):
    i3.command('fullscreen disable')
    
def make_window_fullscreen(workspace):
    i3.command('fullscreen enable')
    
def manage_new_close_window(self, e):
    focused = i3.get_tree().find_focused()
    workspace = focused.workspace()
    monitor = workspace.ipc_data['output']
    y = len(workspace.nodes)
    
    if workspace.name.startswith('trading'):
        if y > 1:
            make_window_normal(workspace)
            return
        if y == 1:
            make_window_fullscreen(workspace)
            return
        return

    if y > 1:
        remove_gaps()
        return
    
    if (monitor == 'DP-1'):
        left_gap()
        return
    if (monitor == 'DP-2'):
        right_gap()
        return
########################### -- end -- ###########################


i3.on('window::new', manage_new_close_window)
i3.on('window::close', manage_new_close_window)
i3.on('window::move', manage_new_close_window)
i3.on('window::focus', manage_new_close_window)
i3.on('workspace::empty', manage_new_close_window)
i3.on('workspace::init', manage_new_close_window)
i3.on('binding', dispatch_binding)

i3.main()
