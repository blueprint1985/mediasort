# mediasort
A couple of small media sort scripts I made to sort downloaded media

---------------------------

fix-films:

Renames films and sorts then into the following folder structure: Films/Name of Film/Name of Film.avi or other extension. 

Howto:

1. Make sure that each separate film is in a separate folder with the final name you want the film to have. The folder may not be named "Films".
2. Copy fix-films.py into the parent folder of all film folders.
3. Run fix-films.py

Notes:

* The name of each film folder is the name that the film will get. The name may have releas year in parentheses, which will be omitted (se example below).
* Sequels that you want numbered should be renamed as you want to have them numbered. Se example.
* Allowed extensions are avi or mp4, and srt for subtitles.
* Other files and/or folders will be removed

Example:

* Southpaw (2015)
	* Southpaw.2015.720p.BluRay.x264.YIFY.mp4
	* WWW.YTS.TO.jpg
* MCU – 11 – Avengers – Age of Ultron (2015)
	* Avengers.Age.of.Ultron.2015.720p.BluRay.x264.YIFY.mp4
	* Avengers.Age.of.Ultron.2015.1080p.BluRay.x264-SPARKS.srt
	* WWW.YTS.TO.jpg

Will be named:

* Films
	* Southpaw
		* Southpaw.mp4
	* Marvel Cinematic Universe
		* MCU – 11 – Avengers – Age of Ultron.mp4
		* MCU – 11 – Avengers – Age of Ultron.srt

The script does almost everything automatically. In the Avengers case you will see the that the downloaded folder is named "The Avengers Age of Ultron (2015)," which means that the folder must be renamed manually before you can run the script. I van't think of a good  way to do it automatically because the program doesn't know whether you want to have the film numbered as a sequel.

---------------------------

fix-shows:

Renames episodes of TV-shows and sorts then into the following folder structure: TV-shows/Name of Show/Season X/Episode.avi or other extension.

Howto:

1. Make sure that each separate show episode is in a separate folder with the final name you want the film to have. The folder may not be named "TV-shows".
2. Copy fix-shows.py into the parent folder of all film folders.
3. Run fix-shows.py

Notes:

* The name of each episode folder is the name that the film will get without anything after a left square bracket. 
* The name of the episode folder must be formatted as: "Name.of.tv.show.year.SxxExx.more.stuff". 
* "year" can be omitted. 
* "SxxExx" is season and episode number. 
* Dots in "Name.of.tv.show" can be switched to spaces.
* Allowed extensions are avi or mp4.
* Other files and/or folders will be removed

Example:

* Bones.S11E01.HDTV.x264-KILLERS[ettv]
	* Bones.S11E01.HDTV.x264-KILLERS.mp4
	* bones.s11e01.hdtv.x264-killers.nfo
	* Torrent-Downloaded-From-extratorrent.cc.txt
* Hawaii.Five-0.2010.S07E02.HDTV.x264-LOL[ettv]
	* Sample
		* hawaii.five-0.2010.702.hdtv-lol.sample.mp4
	* hawaii.five-0.2010.702.hdtv-lol.mp4
	* hawaii.five-0.2010.702.hdtv-lol.nfo
	* Torrent-Downloaded-From-extratorrent.cc.txt

Will be named:

* TV-shows
	* Bones
		* Season 11
			* Bones.S11E01.HDTV.x264-KILLERS.mp4
	* Hawaii Five-0
		* Season 7
			* Hawaii.Five-0.2010.S07E02.HDTV.x264-LOL.mp4
