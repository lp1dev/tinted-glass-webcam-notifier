from subprocess import run, PIPE
from os.path import isfile
from sys import argv
from time import sleep
import json

CONFIG_FILE="/etc/tinted-glass/config.json"
CONFIGURATION={}

def     get_config(config_file=CONFIG_FILE):
  global CONFIGURATION
  try:
    with open(CONFIG_FILE) as f:
      CONFIGURATION = json.loads(f.read())
  except Exception as e:
    print(e)
    exit(-1)

def     parse_output(stdout, filename):
  lines = stdout.decode(CONFIGURATION['encoding']).split('\n')[:-1]
  print(lines)
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
  run(["/usr/bin/notify-all" ,text])

def     lsof(filename):
  completed_process = run(["lsof", filename], stdout=PIPE)
  return parse_output(completed_process.stdout, filename)

def     get_devices(prefix=None):
  if prefix is None:
    prefix = CONFIGURATION['prefix']
  i = 0
  devices = []
  while i < CONFIGURATION['output_limit']:
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
    CONFIGURATION['daemonize'] = True
  go_on = True
  get_config()
  if not CONFIGURATION['daemonize']:
    return refresh()
  while go_on:
    refresh()
    sleep(CONFIGURATION['refresh_rate'])
  return 0

if __name__ == '__main__':
  exit(main())
