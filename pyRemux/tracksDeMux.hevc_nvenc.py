import os

class tracksDeMux:

	def __init__(self, tInfo, vidPath):
		if type(tInfo) != type([]):
			print("- Error: tracksDeMux constructor received non-list type variable.")
			exit(1)

		self.trackInfo = tInfo
		self.vidPath = vidPath

		self.extractVideos()
		self.extractAudios()
		self.extractSubtitles()

	def extractVideos(self):
		for key in self.trackInfo[2]:
			print("Converting video to h.265...")
			command = 'ffmpeg.exe -i "{0}\\{1}" -vcodec hevc_nvenc -acodec aac "{0}\\_pyremuxTmp\\{2}VID.MKV"'.format(self.vidPath, self.trackInfo[0], key)
			os.system("call {0}>nul".format(command))
			
			print("Extracting Video Track...")
			command = 'mkvextract.exe tracks "{0}\\_pyremuxTmp\\{1}VID.MKV" {1}:"{0}\\_pyremuxTmp\\{1}VID.RM"'.format(self.vidPath, key)
			os.system("call {0}>nul".format(command))
		print('')

	def extractAudios(self):
		print("Extracting Audio Tracks...")

		for key in self.trackInfo[3]:
			command = 'mkvextract.exe tracks "{0}\\{2}" {1}:"{0}\\_pyremuxTmp\\{1}AUD.AAC"'.format(self.vidPath, key, self.trackInfo[0])
			os.system("call {0}".format(command))

		print('')

	def extractSubtitles(self):
		print("Extracting Subtitle Tracks...")
		for key in self.trackInfo[4]:
			command = 'mkvextract.exe tracks "{0}\\{1}" {2}:"{0}\\_pyremuxTmp\\{2}SUB.{3}"'.format(self.vidPath, self.trackInfo[0], key, self.getSub(self.trackInfo[4][key]))
			os.system("call {0}>nul".format(command))
		print('')

	def getSub(self, type):
		if type == 'SubStationAlpha' or type == 'SubStation Alpha' or type == 'ASS' or type == 'SSA':
			return 'ASS'
		else:
			return 'SRT'