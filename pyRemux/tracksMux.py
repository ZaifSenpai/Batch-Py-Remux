import os

class tracksMux:
	
	def __init__(self, tInfo, vidPath):
		if type(tInfo) != type([]):
			print("- Error: tracksMux constructor received non-list type variable.")
			exit(1)

		self.trackInfo = tInfo
		self.vidPath = vidPath

		self.MuxCommand = ''

		self.generateCommand()
		self.executeMuxCommand()

	def generateCommand(self):
		self.MuxCommand = 'mkvmerge.exe --ui-language en --output ^"{0}\\RemuxOut\\{1}^"'.format(self.vidPath, self.trackInfo[0])
		trackOrder = ' --track-order '
		extension = ''

		for key in self.trackInfo[1]:
			if self.trackInfo[1][key] == 'video':
				extension = 'RM'
			elif self.trackInfo[1][key] == 'audio':
				extension = 'AAC'
			elif self.trackInfo[1][key] == 'subtitles':
				extension = 'ASS'

			self.MuxCommand = self.MuxCommand + ' --language "0:{4}" --track-name "0:{5}" ^"^(^" ^"{0}\\_pyremuxTmp\\{1}{2}.{3}^" ^"^)^"'.format(self.vidPath, key, self.trackInfo[1][key][0:3].upper(), extension, self.trackInfo[5][key], self.trackInfo[6][key])

			trackOrder = trackOrder + "{0}:0,".format(key)

		trackOrder = trackOrder[0:len(trackOrder)-1]

		self.MuxCommand = self.MuxCommand + ' --title ^"{0}^"'.format(self.trackInfo[0]) + trackOrder

	def executeMuxCommand(self):
		print("Muxing", self.trackInfo[0])
		os.system("call {0}".format(self.MuxCommand))
