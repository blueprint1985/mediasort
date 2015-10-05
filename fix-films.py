import os, sys, shutil

fileexts = ["mp4", "avi", "srt"]

for film in os.listdir(os.getcwd()):

	if os.path.isdir(film):

		newname = film.split(' (')[0]
		os.rename(film, newname)
		film = newname

		for filename in os.listdir(os.path.abspath(film)):

			if not os.path.isdir(filename):

				fileext = filename.split('.')[-1]
				oldfile = os.path.abspath(film) + "/" + filename

				if fileext in fileexts:
					
					newfile = os.path.abspath(film) + "/" + newname + "." + fileext
					os.rename(oldfile, newfile)

				else:

					os.remove(oldfile)

			else:

				shutil.rmtree(filename)

		checksequel = film.split(' - ')

		if len(checksequel) > 1:

			abbreviations = [["MCU", "Marvel Cinematic Universe"]]

			for abbrev in abbreviations:
				if checksequel[0] in abbrev:
					checksequel[0] = abbrev[1]
					break

			os.rename(film, checksequel[0])

		print(newname + ": Done")
