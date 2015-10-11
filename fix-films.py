import os, sys, shutil, re

fileexts = ["mp4", "avi", "srt"]

for film in os.listdir(os.getcwd()):

	matchFilm = re.match('Filmer',film)	

	if os.path.isdir(film) and not matchFilm:

		newname = film.split(' (')[0]
		os.rename(film, newname)
		film = newname

		checksequel = film.split(' - ')

		if len(checksequel) > 1:

			abbreviations = [["MCU", "Marvel Cinematic Universe"]]

			for abbrev in abbreviations:
				if checksequel[0] in abbrev:
					checksequel[0] = abbrev[1]
					break

			newpath = os.getcwd() + "/Filmer/" + checksequel[0]

		else:

			newpath = os.getcwd() + "/Filmer/" + film			

		if not os.path.exists(newpath): 
			os.makedirs(newpath)		

		for filename in os.listdir(os.path.abspath(film)):
			
			if not os.path.isdir(os.path.abspath(film) + "/" + filename):

				fileext = filename.split('.')[-1]
				oldfile = os.path.abspath(film) + "/" + filename

				if fileext in fileexts:
					
					newfile = newpath + "/" + newname + "." + fileext
					os.rename(oldfile, newfile)

				else:

					os.remove(oldfile)

			else:

				shutil.rmtree(os.path.abspath(film) + "/" + filename)

		shutil.rmtree(film)

		print(newname + ": Klart")
