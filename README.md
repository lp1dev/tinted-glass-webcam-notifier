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

 