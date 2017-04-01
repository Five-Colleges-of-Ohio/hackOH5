from bs4 import BeautifulSoup
import csv
import sys
import os

#the directory which contains all the files
inputdirectory = "./all_newspapers/"
outputdirectory = "./debug_out/"
metadata_filename = 'all_metadata.csv'
display_every = 100

no_title_count = 0
no_description_count = 0
no_publisher_count = 0
no_date_count = 0

#input_file has XML data
#output_file gets raw text data from the
#metadata is the *actual file object* (actually a csv writer)
#that can be written to with metadata.writerow(list)
def parse_file(input_file, output_file, metadata, clean_file_name):
    global no_title_count
    global no_description_count
    global no_publisher_count
    global no_date_count
    soup = BeautifulSoup(open(inputdirectory+input_file), "lxml")
    output = open(outputdirectory+output_file, "w")
    pages = soup.find_all("pagetext")
    for page in pages:
        output.write(str(page.contents[0]))
    if(soup.title.contents):
        title = soup.title.contents[0]
    else:
        print("missing data: no title in file:", input_file)        
        title = "no-title"
        no_title_count += 1
    if(soup.description.contents):
        description = soup.description.contents[0]
    else:
        print("missing data: no description in file:", input_file)
        description = "no-description"
        no_description_count += 1
        
    publishers = soup.find_all("publisher")
    if(publishers[1].contents):
        publisher = publishers[1].contents[0]
    else:
        print("missing data: no publisher in file:", input_file)        
        publisher = "no-publisher"
        no_publisher_count += 1
    if(soup.date.contents):    
        date = soup.date.contents[0]
    else:
        print("missing data: no date in file:", input_file)        
        date = "no-date"
        no_date_count += 1
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
print(no_title_count, "titles were missing from the data set")
print(no_description_count, "descriptions were missing from the data set")
print(no_publisher_count, "publishers were missing from the data set")
print(no_date_count, "dates were missing from the data set")
