#OCR_cleaner
#Isabel T
#Takes an input path, output path, and dictionary name 
#checks of each word in the file is in dictionary - if it is, add it to a new output file (based o the Id of the original file)
#and have that file in the designated output file




import os
#keep track of how many words we loose


#change for directory with files
inputPath = "./files/"
outputPath = "./outputFiles/"
dictName = "./testdict.txt"
missingWord = 0

dictFile = open(dictName, 'r')
dictionary = set()

for word in dictFile:
	word = word.strip('\n')
	dictionary.add(word)



def loopFiles():
	for filename in os.listdir(inputPath):
		cleanFile(filename, missingWord)

def cleanFile(fileName, missingWord):
	inputFile = open(inputPath+fileName, 'r')
	Newfile = fileName.split("_")[0] + ".txt"
	file = open(outputPath+Newfile,"w+")
	for line in inputFile:
		for word in line.split():
			if word in dictionary:
				file.write(word+" ")
			else:
				missingWord = missingWord + 1
		file.write("\n")
	file.close()


loopFiles()

