from bs4 import BeautifulSoup
import csv
import os

#input_file has XML data
#output_file gets raw text data from the
#metadata is the *actual file object* (actually a csv writer)
#that can be written to with metadata.writerow(list)
def parse_file(input_file, output_file, metadata, clean_file_name):
    soup = BeautifulSoup(open(input_file), "lxml")
    output = open(output_file, "w")
    pages = soup.find_all("pagetext")
    for page in pages:
        output.write(str(page.contents[0]))
        
    title = soup.title.contents[0]
    description = soup.description.contents[0]
    publishers = soup.find_all("publisher")
    publisher = publishers[1].contents[0]
    date = soup.date.contents[0]
    metadata.writerow([clean_file_name, title, description, publisher, date])

metadata = csv.writer(open("metadata.csv", "w"))
metadata.writerow(['Filename','Title','Description','Publisher','Date'])
parse_file("42202.cpd.xml", "testout.txt", metadata, "42202.txt")

inputdirectory = "Denison University"
for filename in os.listdirectory(inputdirectory):
    
