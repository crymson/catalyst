subarch: amd64
version_stamp: 20040223
target: grp
rel_type: default
rel_version: 2004.0
snapshot: 20040223
source_subpath: default-amd64-2004.0/stage3-amd64-20040223
grp: cd1 cd2 src

grp/use: 
	gtk2 
	gnome 
	kde 
	qt 
	bonobo 
	cdr 
	directfb
	esd 
	gtkhtml 
	mozilla
	mysql
	perl
	postgres
	ruby
	tcltk
	acl
	cups
	ldap
	ssl
	tcpd

grp/cd1/type: pkgset
grp/cd1/packages:
	iptables
	gpm
	rp-pppoe
	ppp
#	wvdial (not building correctly)
	speedtouch
	pciutils
	hdparm
	hotplug
	aumix
	xfree
	iputils
	vixie-cron
	sysklogd
	metalog
	syslog-ng
	raidtools
	jfsutils
	xfsprogs
	reiserfsprogs
	lvm2
	dosfstools
	grub-static
	gentoo-dev-sources
	superadduser
	gentoolkit
#USE effects for these?:
	dante
	tsocks
	chkrootkit
	minicom
	lynx
	rpm2targz
	parted
	rdate
	whois
	tcpdump
	cvs
	unzip
	zip
	netcat
#	partimage
#	lukemftp
#	lcrzoex
	genkernel
	genflags
	screen
#	joe
#	vile
	nfs-utils
	mirrorselect
	ufed
	dev-lang/tcl
	dev-lang/tk
	
grp/cd2/type: pkgset
grp/cd2/packages:
#	DirectFB
	apache
	app-cdr/cdrtools
	gnome
	evolution
	cups
	dev-db/mysql
	dev-db/postgresql
	dev-lang/ruby
	emacs
#enlightenment has a build problem if USER!=root
#	enlightenment
	fluxbox
	kde
	libsdl
	links
	mozilla
##	xfce4
#	openbox
#	openoffice is breaking during build (see bug 33168)
#	openoffice
	sylpheed
	vim
	xemacs
	xmms
#use interactions?
	mozilla-firefox
#	abiword
	gaim
	tetex
	xcdroast
	kdrive
	samba
	nmap
	gradm
##	gradm2
##	ettercap
	xchat

grp/src/type: srcset
grp/src/packages:
#isdn4k-utils was a binary pkg in 1.4, so we will need to get docs updated
#since it's kernel-dependent? maybe?
	isdn4k-utils
#	nforce-net
#	nforce-audio
	iproute
#nvidia-glx requires nvidia-kernel
	nvidia-kernel
	nvidia-glx
#	ati-drivers
#	e100
#	e1000
	wireless-tools
	pcmcia-cs
#	emu10k1
	evms2
#	linux-wlan-ng
