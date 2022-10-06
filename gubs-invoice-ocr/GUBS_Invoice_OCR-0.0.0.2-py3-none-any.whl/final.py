import os
import json
import argparse
import pymongo


ap = argparse.ArgumentParser()

#Checks if the total amount obtained is valid or not i.e., it should be conly composed of digits, commas and decimals, no alphabets and other characters are allowed
def isValid(total_amount):
    total_amount=total_amount.strip()
    if(len(total_amount)==0):
        print("tr")
        return False
    elif(len(total_amount)>0):
        for ch in total_amount:
            if(ch!="." and ch!="," and ch.isdigit()!=True):
                return False
    return True


#To execute part3.py
def method3(keyword, file):
    keyword=keyword.strip()
    keyword="\""+keyword+"\""
    cmd="python part3.py --pdf "+ file + " --matched_doc "+str(keyword)
    os.system(cmd)
    file = open("out.txt")
    total_amount_3=file.read()
    file.close()
    return total_amount_3    

ap.add_argument("-i", "--pdf", required=True, help="Path to the pdf")
args = vars(ap.parse_args())
file=args["pdf"]

#first executing the first part and getting the required avleus form it

cmd="python part1.py --pdf "+ file
from part1 import total_amount,onboard, flag , matched_doc
total_amount=total_amount.strip()

file=str(file)
file="\""+file+"\""

# os.system("python InvoiceNet/prepare_data.py --data_dir InvoiceNet/train_data4/")
# os.system("python InvoiceNet/train.py --field total_amount --batch_size 2")


if(flag!=-1):      
    #If the file is being onboarded no chceks are applied and part 2 is not executed  
    if(onboard==0):
        #Excuting method 2 
        cmd="python InvoiceNet/predict.py --field total_amount --invoice "+str(file)
        os.system(cmd)

        with open('prediction.json') as f:
            data = json.load(f)
            ml_total_amount=data["total_amount"].strip() # contains the total amount read form method 2

            if(isValid(total_amount) and isValid(ml_total_amount)):
                if(total_amount==ml_total_amount):
                    print("Detected total Amount (Matched method 1 and Method 2): ", total_amount)
                else:
                    if(isValid(ml_total_amount)):
                        print("Detected total Amount (Method 2): ", total_amount)
                    else:
                        total_amount_3=method3(matched_doc, file)
                        if(isValid(total_amount_3)):
                            print("total_amount: ", total_amount_3)
                        else:
                            print("-1")

            else:
                if(isValid(ml_total_amount)):
                    print("Detected total Amount (Method 2): ", total_amount)
                else:
                    total_amount_3=method3(matched_doc, file)
                    if(isValid(total_amount_3)):
                        print("total_amount: ", total_amount_3)
                    else:
                        print("-1")
else:
    total_amount_3=method3(matched_doc, file)
    if(isValid(total_amount_3)):
        print("total_amount: ", total_amount_3)
    else:
        print("-1")
    
     



