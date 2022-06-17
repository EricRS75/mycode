#!/usr/bin/env python3
import time
import os
from subprocess import call
import yaml
import crayons
import sys
from datetime import datetime

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

def switchcount(switches):
  i = 0
  for switch in switches:
      i += 1
  return i

def connectthedots(dots):
    for dot in range(dots):
      sys.stdout.write(". ") 
      sys.stdout.flush()
      time.sleep(.3)
    print()  

def switchlog(switch,ipaddr,severity,command,subcommand):
    with open("switch.log", "a") as switchlog:
        print(f"{datetime.now()} {ipaddr} host:{switch} severity:{severity} command:{command} {subcommand}",file=switchlog)


def switchconfig():
    with open("switchdata.yaml", "r") as switches:
        myswitches = yaml.safe_load(switches)
    clear()
    #print title in bold green
    print(crayons.green(f"There are {switchcount(myswitches)} switches to configure, they are:", bold=True))
    # farm will be equal to one of the dict within the list "farms"
    for switch in myswitches:
        #print name of the farms in bold yellow
        print(crayons.white(f"connecting to {switch.get('switchname')} via {switch.get('sshtarget')}", bold=True), end="" )
        connectthedots(8)
        # from a single "farm" get the list from the key "agriculture"
        for command in switch.get('commands'):
            #print agriculture in bold blue
            print(crayons.blue(f"sending: " ), end="")
            print(crayons.yellow(f"{command.get('command')} {command.get('subcommand')} ", bold=True))
            switchlog(switch.get('switchname'),switch.get('sshtarget'),1,command.get('command'), command.get('subcommand'))
            time.sleep(1)
          #  sending: {command} + " " + {subcommand} (blue)\n

def main():
    switchconfig()


main()
