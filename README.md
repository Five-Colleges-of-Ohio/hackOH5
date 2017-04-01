# hackOH5
OH5 student newspaper hacking

1. input dir with all XML files
2. empty output directory to store all text
3. metadata output filename


To get data from the XML to (cleanish) files for Task Modeling: 

These will need to be hard-coded into the XMLprocessor.py:
    An input directory with (only) the list of XML files
    An empty output directory
    A metadata output filename

Then run the XML processor (using python3 xmlprocessor.py). You should now have a metadata file in your same directory as the program, and you should have an output directory full of plaintext files.

These will need to be hard-coded into the OCR_cleaner:
    An input directory (should be the same as the output directory from the xmlprocessor)
    An empty output directory
    A path to a large dictionary file (we used https://github.com/dwyl/english-words)

Then run the OCR_cleaner (python3 OCR_cleaner.py)

You should now have an output directory full of cleaned OCR text of the dictionaries, with ID's that correspond to the metadata file.

     




