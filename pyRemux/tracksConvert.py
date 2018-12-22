import os
from pyRemux import ResetStyle

class tracksConvert:
	def __init__(self, tInfo, vidPath):
		if type(tInfo) != type([]):
			print("- Error: tracksConvert constructor received non-list type variable.")
			exit(1)

		self.trackInfo = tInfo
		self.vidPath = vidPath

		# Audio & Video were already converted before DeMuxing
		self.convertSubtitles()

	def convertSubtitles(self):
		for key in self.trackInfo[4]:
			if self.getSub(self.trackInfo[4][key]) == 'SRT':
				command = 'ffmpeg -i "{0}\\_pyremuxTmp\\{1}SUB.SRT" -scodec ass "{0}\\_pyremuxTmp\\{1}SUB.ASS"'.format(self.vidPath, key)
				os.system("call {0}>nul".format(command))

			ResetStyle.ResetStyle('{0}\\_pyremuxTmp\\{1}SUB.ASS'.format(self.vidPath, key))
	
	def getSub(self, type):
		if type == 'SubStationAlpha' or type == 'SubStation Alpha' or type == 'ASS' or type == 'SSA':
			return 'ASS'
		else:
			return 'SRT'