from bs4 import BeautifulSoup
import csv
import sys
import os

#the directory which contains all the files
inputdirectory = "./all_newspapers/"
outputdirectory = "./all_out/"
metadata_filename = 'test_metadata.csv'
display_every = 100

#input_file has XML data
#output_file gets raw text data from the
#metadata is the *actual file object* (actually a csv writer)
#that can be written to with metadata.writerow(list)
def parse_file(input_file, output_file, metadata, clean_file_name):
    soup = BeautifulSoup(open(inputdirectory+input_file), "lxml")
    output = open(outputdirectory+output_file, "w")
    pages = soup.find_all("pagetext")
    for page in pages:
        output.write(str(page.contents[0]))
        
    title = soup.title.contents[0]
    description = soup.description.contents[0]
    publishers = soup.find_all("publisher")
    publisher = publishers[1].contents[0]
    date = soup.date.contents[0]
    metadata.writerow([clean_file_name, title, description, publisher, date])

    
#parse_file("42202.cpd.xml", "testout.txt", metadata, "42202.txt")

metadata = csv.writer(open(metadata_filename, "w"))
metadata.writerow(['Filename','Title','Description','Publisher','Date'])

counter = 0

print("There are", len(os.listdir(inputdirectory)), "files")
for filename in os.listdir(inputdirectory):
    if(counter % display_every == 0):
        print("Processed", counter, "files")
    id = filename.split('.')[0]
    parse_file(filename, id + "_raw.txt", metadata, id+".txt")    

    counter += 1
