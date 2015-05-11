# Elektrienergia mõõtmise lahendus

Tegemist on siis voolutarbimise jälgimise projektiga, mis baseerub vaarika riistvaral ja suurelt osalt openenergymonitor.org arendusele baseeruv.

Kasutatav riistvara:



vaarika seadistus

	sudo apt-get install git
	sudo git clone https://github.com/kieranc/power.git && cd power
	sudo cp power-monitor /etc/init.d/
	sudo chmod a+x /etc/init.d/power-monitor
	sudo update-rc.d power-monitor defaults
 
	sudo nano /etc/init.d/power-monitor 
	sudo /etc/init.d/power-monitor start