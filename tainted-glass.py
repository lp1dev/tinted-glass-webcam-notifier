#!/bin/python

from subprocess import run, PIPE
from os.path import isfile
from sys import argv
from time import sleep
import config

ENCODING="UTF-8"
PREFIX="/dev/video"
OUTPUT_LIMIT=50

def     parse_output(stdout, filename):
  lines = stdout.decode(ENCODING).split('\n')[:-1]
  cut_lines = [line.split() for line in lines]
  output = []
  for line in cut_lines[1:]:
    output.append({})
    for index, item in enumerate(line):
      output[len(output) - 1][cut_lines[0][index]] = item
      output[len(output) - 1]['NODE'] = filename
  return output

def     notify(text):
  print(text)
  run(["notify-send", text])

def     lsof(filename):
  completed_process = run(["lsof", filename], stdout=PIPE)
  return parse_output(completed_process.stdout, filename)

def     get_devices(prefix=PREFIX):
  i = 0
  devices = []
  while i < OUTPUT_LIMIT:
    device = "%s%i" %(prefix, i)
    try:
      with open(device):
        devices.append(device)
    except FileNotFoundError:
      return devices
    i += 1
  return devices
  

def	refresh():
  data = {}
  for device in get_devices():
    data[device] = lsof(device)
    for line in data[device]:
      notify("%s(%s) is using %s" %(line['COMMAND'], line['PID'], line['NODE']))
  return 0

def     main():
  if "--daemon" in argv:
    config.daemonize = True
  go_on = True
  if not config.daemonize:
    return refresh()
  while go_on:
    refresh()
    sleep(config.refresh_rate)
  return 0

if __name__ == '__main__':
  exit(main())
