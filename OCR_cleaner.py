#OCR_cleaner
#Isabel T
#Takes an input path, output path, and dictionary name
#checks of each word in the file is in dictionary - if it is, add it to a new output file (based o the Id of the original file)
#and have that file in the designated output file




import os
import operator
#keep track of how many words we loose


#change for directory with files
#Examples:
#inputPath = "./files/"
#outputPath = "./outputFiles/"
#dictName = "./testdict.txt"

inputPath = "./denison_out/"
outputPath = "./denison_clean/"
dictName = "./words.txt"
missedDictName = "./denisonMissed.txt"

missedWords = {}
missingWord = 0
totalWord = 0



dictFile = open(dictName, 'r')
dictionary = set()

for word in dictFile:
	word = word.strip('\n')
	dictionary.add(word)



def loopFiles():
	fileCount = 0
	for filename in os.listdir(inputPath):
		fileCount += 1
		if fileCount % 100 == 0:
			print("Processed", fileCount, "files")
		cleanFile(filename)



	missedDict = open(missedDictName,"w+")
	d_view = [ (v,k) for k,v in missedWords.items() ]
	d_view.sort(reverse=True) # natively sort tuples by first element
	for v,k in d_view:
		missedDict.write("%s: %d\n" % (k,v))




	percentage = (missingWord/totalWord) * 100


	print("Program finished.\nTotal words:", totalWord, "\nMissing Words:", missingWord, "\nPercentage of data lost:", str(percentage)+"%")

def cleanFile(fileName):
	global missingWord
	global totalWord
	inputFile = open(inputPath+fileName, 'r')
	Newfile = fileName.split("_")[0] + ".txt"
	file = open(outputPath+Newfile,"w+")
	for line in inputFile:
		for word in line.split():
			word = word.lower()
			totalWord = totalWord + 1
			if word in dictionary:
				file.write(word+" ")
			else:
				if word in missedWords:
					missedWords[word] += 1
				else:
					missedWords[word] = 1
				missingWord = missingWord + 1
		file.write("\n")
	file.close()


loopFiles()
