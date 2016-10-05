""" 
Created 9/28/2016
Parses  10Q,10K,8K,and 13F and prints out to data.txt
written for: satvikakumar@gmail.com
"""
import sys
import os
import re

def parseInformation(file):
	"""parses keywodrds in file and returns as ordered dictionary"""
	key_words = []
	key_words.append("FILED AS OF DATE:")
	key_words.append("COMPANY CONFORMED NAME:")
	key_words.append("FORM TYPE:")
	key_words.append("SEC FILE NUMBER:")

	data = [] #array of tuples

	for key_word in key_words:
		for line in file:	
			if key_word in line:
				value = parse_value(line,key_word)
				data.append([key_word,value])				
				break

	return data

def parse_value(line,key_word):
	"""finds value in line by parsing keyword"""
	value = re.sub(key_word,'',line,1)
	return value.strip()
		

def fileSize(file_name):
	"""returns size of file in bytes as string """
	return str(os.path.getsize(file_name)) + " bytes"

def wordCount(file):
	"""returns word count as int """
	return len(file.read().split())

if __name__ == "__main__": #run from console
	if(len(sys.argv) != 2):
		print "Syntax: python [filename.txt]"
	else:
		file = open(sys.argv[1])
		filename = sys.argv[1]
		wordCount = wordCount(file)
		size = fileSize(filename)
		data = parseInformation(open(filename,"r"))

		#todo print to data.txt



		
