import re
import sys

"""
Set all styles to:
Style: Default,Open Sans Semibold,50,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,0,0,28,1
"""

def ResetStyle(inPath):
	pos = 'Start'
	styleDone = False
	StylePos = 0

	with open(inPath, encoding="utf8") as f:
		contents = f.readlines()
	f.close()
	
	with open(inPath, 'w', encoding="utf8") as f:
		for line in contents:
			if 'Styles]' in line:
				pos = 'Styles'
				f.write(line)
			elif '[Events]' in line:
				pos = 'Events'
				f.write(line)

			if pos == 'Start':
				f.write(line)

			elif pos == 'Styles' and styleDone == False:
				f.write('Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n')
				f.write('Style: Default,Open Sans Semibold,50,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,0,0,28,1\n\n')
				styleDone = True

			elif pos == 'Events':
				if 'Dialogue:' in line:

					newLine = getB4Str(line, StylePos) + ' Default' + getAfterStr(line, StylePos)
					
					newLine = newLine.replace(r'\b', r'\+').replace(r'\shad', r'\+').replace(r'\u', r'\+').replace(r'\i', r'\+').replace(r'\s', r'\+').replace(r'\fn', r'\+').replace(r'\fe', r'\+').replace(r'\c&H', r'\+').replace(r'\1c&H', r'\+').replace(r'\2c&H', r'\+').replace(r'\3c&H', r'\+').replace(r'\4c&H', r'\+')
					newLine = re.sub(r'\\fs\d', r'\+', newLine)

					f.write(newLine)

				elif 'Format:' in line:
					StylePos = line.count(',', 0, line.find('Style') + 1)
					f.write(line)

	f.close()

def getB4Str(line, StylePos):
	pos=0
	splitList = line.split(',')

	for i in range(len(splitList)):
		if i == StylePos:
			break

		pos = pos + len(splitList[i])+1

	return line[0:pos]

def getAfterStr(line, StylePos):
	pos=0
	splitList = line.split(',')

	for i in range(len(splitList)):
		pos = pos + len(splitList[i]) + 1

		if i == StylePos:
			break

	return ',' + line[pos:]

if __name__ == '__main__':
	if len(sys.argv) > 1:
		for file in sys.argv[1:]:
			ResetStyle(file)