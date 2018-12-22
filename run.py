import os
import sys

from pyRemux.tracksInfo import tracksInfo
from pyRemux.tracksDeMux import tracksDeMux
from pyRemux.tracksConvert import tracksConvert
from pyRemux.tracksMux import tracksMux

if len(sys.argv) < 3:
	print("- Error: Command line arguments are missing")
	exit()

tracksInfoList = tracksInfo(sys.argv[1].replace('\\\\', '\\')).getAllInfoList()

tracksDeMux(tracksInfoList, sys.argv[2].replace('"', ''))
tracksConvert(tracksInfoList, sys.argv[2].replace('"', ''))
tracksMux(tracksInfoList, sys.argv[2].replace('"', ''))
