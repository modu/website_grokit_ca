QtNetworkMonitor
================

A free, open source, portable network monitor.

This is the home page for the Qt Network Monitor project. It is built in C++ and uses the underlying library libpcap / WinPcap to gather information about the network traffic. The GUI is built in QT and faily independent from the implementation of the device listener. You need to install WinPcap (download here) beforehand or else the program won't find any available device. Under Linux, you need to install libpcap (sudo apt-get install libpcap) and then run the program as root (sudo ./QtNetworkMon).

The project is a KISS network monitor (shows how much bandwidth you are taking on a daily basis) that I wrote after being frustrated to find no good open-source BM that works under both windows and linux. I built this since I am sometimes under strict restriction of bandwidth (university campus).


New functionnalities
--------------------

The application now keep tracks of the amount of data downloaded in a file so that when the computer is rebooted it keeps in memory how much data was transferred. It resets the data automatically at the beginning of a new day.

Downloads
---------

[Qt Network Monitor Windows Version 0.2 Beta (i386)](../../static/QtNetworkMon_Win32_i386_v0p2Beta.zip "")

[Qt Network Monitor Linux Version 0.2 Beta (i386)*](../../static/QtNetworkMon_Linux_i386_0p2Beta.tar.gz "")

** The Linux version need Qt4 and Libpcap installed in order to work **

Screenshots
-----------

Win32 screenshot

![](../../static/Screenshot_win_0p2_beta-full.jpg "Screenshot_win_0p2_beta-full")

Linux screenshot (Ubuntu)

![](../../static/QtNetworkMon_SC_nix_0p2-full.jpg "QtNetworkMon_SC_nix_0p2-full")

Source
------

The project is open source with a liberal license. You can download the source using:

  `svn checkout http://qtnetworkmonitor.googlecode.com/svn/trunk/ qtnetworkmonitor`


