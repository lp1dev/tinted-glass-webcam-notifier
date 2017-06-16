PYEXE=tinted-glass.py
EXE=tinted-glass

all:
	$(info use make install to install tinted-glass)

clean:
	rm -fr tinted-glass

build:
	echo "#!"`which python3` > tinted-glass
	cat tinted-glass.py >> tinted-glass
	chmod +x tinted-glass

install: build
	cp notify-all /usr/bin/notify-all
	cp tinted-glass /usr/bin/tinted-glass
	chmod +x /usr/bin/tinted-glass
	cp tinted-glass.service /etc/systemd/system/
	mkdir /etc/tinted-glass/
	cp config.json /etc/tinted-glass/

.PHONY: all install
