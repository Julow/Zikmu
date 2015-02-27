#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# zikmu
#
# Set metadata to audio files
# Take one or more files as params and set metadatas
#
# File name: "Artist - Song name"
#
# Options:
#  -a album		Set album name for all songs
#  -d date		Set date for all songs
#  -g genre		Set genre for all songs
# Options can be placed after arguments, it take effect for following song only:
#  ./zikmu -g Dubstep -a Album1 -d 2013 song1 song2 -a Album2 -d 2015 song3 song4
#

#
# Use Mutagen lib
#

import mutagen
import sys
import os

def not_ascii(s):
	return "".join([i for i in s if i >= ' ' and i <= '~'])

class Zikmu():

	name = ""
	mfile = None
	meta = {}

	def __init__(self, name, meta={}):
		self.name = not_ascii(os.path.basename(name))
		try:
			self.mfile = mutagen.File(name, None, True)
		except:
			print("zikmu: \033[91m%s\033[39m: File not found or not audio" % self.name)
			raise
		self.meta = meta

	def set_meta(self):
		split = self.name.split(" - ", 2);
		if len(split) == 2:
			self.meta["Artist"] = split[0]
			self.meta["Title"] = os.path.splitext(split[1])[0]
		else:
			self.meta["Title"] = os.path.splitext(self.name)[0]
		sys.stdout.write("\033[90m%-64s\033[39m " % self.name)
		if self.mfile.tags == None:
			self.mfile.add_tags()
		s = ""
		for m in self.meta:
			s += m + ": \033[92m%-16s\033[39m " % self.meta[m]
			self.mfile.tags[m] = self.meta[m]
		print(s + "\033[39m")
		self.mfile.save()

# main

def main():
	i = 1
	meta = {}
	while i < len(sys.argv):
		if sys.argv[i] == "-g":
			i += 1
			meta["Genre"] = not_ascii(sys.argv[i])
		elif sys.argv[i] == "-d":
			i += 1
			meta["Date"] = not_ascii(sys.argv[i])
		elif sys.argv[i] == "-a":
			i += 1
			meta["Album"] = not_ascii(sys.argv[i])
		else:
			try:
				z = Zikmu(sys.argv[i], meta)
			except:
				z = None
				pass
			if not z == None:
				z.set_meta()
		i += 1
	if i <= 1:
		print("zikmu: Usage: %s [-g genre] [-d date] [-a album] [file1 ...]" % sys.argv[0])
	return 0

sys.exit(main())
