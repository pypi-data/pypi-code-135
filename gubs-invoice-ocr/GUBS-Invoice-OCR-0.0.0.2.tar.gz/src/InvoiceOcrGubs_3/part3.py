import os
import json
import argparse
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re
import pymongo

#Mongo DB Connection
connection = pymongo.MongoClient('127.0.0.1:27017')
db = connection.invoiceocr

#Getting the pdf and matched template's keyword from the rguments passed in the command line
ap = argparse.ArgumentParser()
ap.add_argument("--pdf", required=True, help="Path to the pdf")
ap.add_argument("--matched_doc", required=True, help="Keyowrd for doc")

args = vars(ap.parse_args())
images = convert_from_path(args["pdf"])
keyword=args["matched_doc"]

#Getting the mongo db document of the matched template
matched_invoice=db.invoices.find({"keyword": keyword.strip()})


count=0
for invoice in matched_invoice:
    count+=1
    start=invoice["match_start"] #Starting word in sandwich technique that will be searched for
    end=invoice["match_end"] #Ending word in sandwich technique that will be searched for

#if no starting word can be found   
if(start=="-1"):
    count=0
flag=-1


#Finally searching for the matched startinga and ending kwyword and returning the amount stored b/w them
if count==1:
    no_of_pages=len(images)
    for i in range(len(images)):
        images[i].save('pag0' + '.jpg', 'JPEG')
        text = str(pytesseract.image_to_string(
                Image.open(r"page0.jpg"), lang='eng'))
        lines = text.split("\n")

        #Removing Blank lines
        non_empty_lines = [line for line in lines if line.strip() != ""]

        string_without_empty_lines = ""
        for line in non_empty_lines:
              string_without_empty_lines += line + "\n"

        text=string_without_empty_lines


        print("text: ", text)
        print("start: ", start)
        print("end: ", end)
        print(text)

        #Searching for a string that has start and end and any string stored in between in it in the text of the pdf
        regex=start+"[\S\n]"+end
        start_end=re.search(f'\s{start}'+'.*'+f'\s{end}', text)
        if(start_end==None):
            continue

        #If the start and end is found 
        if(start_end!=None):
            flag=0
            text=start_end.group()

            #regex to get the amount stored between the start and end words
            amount_regex="[0-9.,]+"
            total_amount_3=re.search(amount_regex, text)
            total_amount_3=total_amount_3.group()
            total_amount_3=total_amount_3.strip()
            print("total_amount found: ", total_amount_3)
            #Total read from out.txt in final.py
            with open('out.txt', 'w') as f:
                f.write(total_amount_3)
    #If no amount is found, write fase to indicate in the temporaray output file
    if(flag==-1):
        with open('out.txt', 'w') as f:
                f.write("false")
else:
    with open('out.txt', 'w') as f:
                f.write("false2")
    print("-1")






