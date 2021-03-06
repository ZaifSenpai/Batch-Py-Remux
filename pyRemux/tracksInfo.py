import re
import sys

class tracksInfo:
	"""
	Simply used to extracts the information of video which is generated by mkvmerge.exe
	Constructor needs path to input txt file which contains information of the video.
	"""

	def __init__(self, infoFile=''):
		try:
			if infoFile == '':
				raise Exception("- Error: Input file is not given to tracksInfo class.")
		except Exception as e:
			print(e)
			exit(1)

		self.fileName = ''
		self.TrackIDs = {}
		self.Videos = {}
		self.Audios = {}
		self.Subtitles = {}
		self.Languages = {}
		self.TrackNames = {}
		self.allInfoList = []

		# enums
		self.TYPE_FILENAME = 0
		self.TYPE_TRACKINFO = 1

		# extract information from text file
		self.getInfo(infoFile)

	def getInfo(self, infoFile):
		file = open(infoFile, 'r')

		for line in file:
			dType = self.getdType(line)
			key = ''
			encType = ''

			if dType == self.TYPE_FILENAME:
				self.fileName = line[line.find("'")+1:line.find("'", line.find("'")+1)]
				key = ''
			elif dType == self.TYPE_TRACKINFO:
				key = self.getID(line)
				self.TrackIDs[key] = self.getType(line)
				encType = self.getEncType(line)

				self.Languages[key] = self.deEscapeChars(self.getLanguage(line))
				self.TrackNames[key] = self.deEscapeChars(self.getTrackName(line))

			if key != '':
				if self.TrackIDs[key] == 'video':
					self.Videos[key] = encType
				elif self.TrackIDs[key] == 'audio':
					self.Audios[key] = encType
				elif self.TrackIDs[key] == 'subtitles':
					self.Subtitles[key] = encType

		if self.isInfoEmpty() == True:
			print("- Error: Unable to extract any information.")
			exit(1)

		self.allInfoList = [self.fileName, self.TrackIDs, self.Videos, self.Audios, self.Subtitles, self.Languages, self.TrackNames]
		print("Tracks information has been extracted of video file:", self.fileName)

	def getdType(self, line):
		if line[0:4] == 'File':
			return self.TYPE_FILENAME
		elif line[0:8] == 'Track ID':
			return self.TYPE_TRACKINFO

	def getID(self, line):
		return line[9:line.find(':')]
	def getType(self, line):
		return line[line.find(':')+2:line.find('(')-1]
	def getEncType(self, line):
		return line[line.find('(')+1:line.find(')')]

	def getLanguage(self, line):
		language = 'und'

		languageList = re.compile(r'language:.*?\s').findall(line)
		
		if len(languageList) < 1:
			languageList = re.compile(r'language:.*?\]').findall(line)
		
		if len(languageList) > 0:
			language = languageList[0]
			language = language[language.find(':')+1:len(language)-1]

		return language

	def getTrackName(self, line):
		trackName = ''

		tracksList = re.compile(r'track_name:.*?\s').findall(line)

		if len(tracksList) < 1:
			tracksList = re.compile(r'track_name:.*?\]').findall(line)

		if len(tracksList) > 0:
			trackName = tracksList[0]
			trackName = trackName[trackName.find(':')+1:len(trackName)-1]

		return trackName

	def isInfoEmpty(self):
		if self.fileName == '':
			return True
		elif self.TrackIDs == {} and self.Videos == {} and self.Audios == {} and self.Subtitles == {} and self.Languages == {} and self.TrackNames == {}:
			return True
		else:
			return False

	def getAllInfoList(self):
		return self.allInfoList

	def deEscapeChars(self, text):
		return text.replace(r'\s', ' ').replace(r'\2', '"').replace(r'\c', ':').replace(r'\h', '#').replace(r'\b', '[').replace(r'\B', ']').replace('\\\\', '\\')

if __name__ == '__main__':
	if len(sys.argv) > 1:
		print(tracksInfo(sys.argv[1].replace('\\\\', '\\')).getAllInfoList())