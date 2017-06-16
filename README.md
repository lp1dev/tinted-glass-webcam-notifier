# Tinted Glass

Tinted glass is a daemon to notify the users whenever a program uses the webcam(s) on the machine.

## Compatibility

Tested on Ubuntu, ArchLinux, should work with most of the GNU/Linux distributions.
    
## Requirements

- Python 3.4
- notify-send
- lsof
- who

## Install

as root

```
    make install
```
    
## Usage

Edit the /etc/tinted-glass/config.json file according to your own needs

Then run the service :

as root
   
`sytemctl start tinted-glass`

To run at startup

`systemctl enable tinted-glass`

![screencapture](https://raw.githubusercontent.com/lp1dev/tinted-glass-webcam-notifier/master/demo/anim.gif)

## Todo

- Mac OS Compatibility
- Windows Version
- Android Version

 ```
Tinted Glass
Copyright (C) 2016 lp1.eu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
