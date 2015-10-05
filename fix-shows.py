import os, sys, shutil, re

for show in os.listdir(os.getcwd()):

	matchShow = re.match('Serier',show)	

	if os.path.isdir(show) and not matchShow:

		splitnewname = show.split('.')

		showName = "(active)"
		season = ""

		for textstr in splitnewname:
			matchSeason = re.match('S\d\dE\d\d',textstr)
			matchYear = re.match('\d\d\d\d',textstr)		

			if not matchSeason and not matchYear:
				showName += " " + textstr

			if matchSeason:
				season = textstr[1:-3]
				season = season.lstrip("0")
				season = "Season " + season
				break

		seasonpath = os.getcwd() + "/Serier/" + showName + "/" + season

		if not os.path.exists(seasonpath): 
			os.makedirs(seasonpath)

		oldfile = ""

		for filename in os.listdir(os.path.abspath(show)):

			if filename.split('.')[-1] == "mp4":

				oldfile = filename
				break

		oldfile = os.path.abspath(show) + "/" + oldfile
		newname = show.split('[')[0]
		newfile = seasonpath + "/" + newname + ".mp4"

		os.rename(oldfile, newfile)
		shutil.rmtree(show)

		print(newname + ": Done")
