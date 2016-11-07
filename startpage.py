import curses
import webbrowser
import subprocess

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)

run=True

while run==True:	
	stdscr.addstr(1,1,"Willkommen")
	stdscr.addstr(3,1,"1.Reddit",curses.A_UNDERLINE)
	stdscr.addstr(4,1,"2.Unixporn")
	stdscr.addstr(5,1,"3.Battlestations")
	stdscr.addstr(6,1,"4.Pink Floyd")
	stdscr.addstr(7,1,"5.Cyberpunk")

	stdscr.addstr(2,35," ____          _     _ _ _ ")
	stdscr.addstr(3,35,"|  _ \ ___  __| | __| (_) |_")
	stdscr.addstr(4,35,"| |_) / _ \/ _` |/ _` | | __|")
	stdscr.addstr(5,35,"|  _ <  __/ (_| | (_| | | |_")
	stdscr.addstr(6,35,"|_| \_\___|\__,_|\__,_|_|\__|")

	stdscr.addstr(9,1,"6.Browser",curses.A_UNDERLINE)
	stdscr.addstr(10,1,"7.Deskthority")
	stdscr.addstr(11,1,"8.Golem")
	stdscr.addstr(12,1,"9.Ricardo")
	stdscr.addstr(13,1,"a.Arch Wiki")
	stdscr.addstr(14,1,"w.WhatsApp Web")

	stdscr.addstr(8,35," ____")                                
	stdscr.addstr(9,35,"| __ ) _ __ _____      _____  ___ _ __") 
	stdscr.addstr(10,35,"|  _ \| '__/ _ \ \ /\ / / __|/ _ \ '__|")
	stdscr.addstr(11,35,"| |_) | | | (_) \ V  V /\__ \  __/ |")   
	stdscr.addstr(12,35,"|____/|_|  \___/ \_/\_/ |___/\___|_| ")

	stdscr.addstr(16,1,"t.Terminal")
	stdscr.addstr(17,1,"x.Xresources")
	stdscr.addstr(18,1,"s.Startpage")

	stdscr.addstr(15,35," ____            _")            
	stdscr.addstr(16,35,"/ ___| _   _ ___| |_ ___ _ __ ___")
	stdscr.addstr(17,35,"\___ \| | | / __| __/ _ \ '_ ` _ \\")
	stdscr.addstr(18,35," ___) | |_| \__ \ ||  __/ | | | | |")
	stdscr.addstr(19,35,"|____/ \__, |___/\__\___|_| |_| |_|")
	stdscr.addstr(20,35,"       |___/")                       

	stdscr.refresh()
	c = stdscr.getch()

	if c == ord('1'):
		webbrowser.open_new_tab('https://reddit.com')
	elif c == ord('2'):
		webbrowser.open_new_tab('https://reddit.com/r/unixporn')
	elif c == ord('3'):
		webbrowser.open_new_tab('https://reddit.com/r/battlestations')
	elif c == ord('4'):
		webbrowser.open_new_tab('https://reddit.com/r/pinkfloyd')
	elif c == ord('5'):
		webbrowser.open_new_tab('https://reddit.com/r/cyberpunk')
	elif c == ord('6'):
		webbrowser.open_new_tab('https://duckduckgo.com')
	elif c == ord('7'):
		webbrowser.open_new_tab('https://deskthority.net')
	elif c == ord('8'):
		webbrowser.open_new_tab('http://golem.de')
	elif c == ord('9'):
		webbrowser.open_new_tab('https://ricardo.ch')
	elif c == ord('a'):
		webbrowser.open_new_tab('https://wiki.archlinux.org')
	elif c == ord('w'):
		webbrowser.open_new_tab('https://web.whatsapp.com')
	elif c == ord('t'):
		subprocess.Popen(["urxvt"])	
	elif c == ord('x'):
		subprocess.Popen(["urxvt","-e","vim","/home/noah/.Xresources"])
	elif c == ord('s'):
		subprocess.Popen(["urxvt","-e","vim","/home/noah/startpage/startpage.py"])


curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()


