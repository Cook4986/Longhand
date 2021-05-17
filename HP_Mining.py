### HP_Mining
### Text mining with HandPrint (https://github.com/caltechlibrary/handprint) output
### MNC - 5/21 (mncook.net)

#Run Handprint in iPython notebook using URLs from .txt file
#Local configuration required before this step
#see https://github.com/caltechlibrary/handprint for setup instructions and documentation
get_ipython().system('handprint --service microsoft --from-file "xxxx" --no-grid --extended --output "xxxx"')

####Bag-of-Words txt output and string search from HandPrint transcriptions
import os
import sys
import re

#paths
cardPath = 'xxxx'#text list of target files or urls
outPath = 'xxxx' #Handprint output directory
textOut = 'xxxx'#Bag-of-Words output
searchOut = 'xxxx'#user search output 
listFiles = os.listdir(outPath)
count = 0

#declarations
headers = [] 
transcriptions = []
BoW = open(textOut, "a")

#user search
search = open(searchOut, "a")
inputString = input("Search document for: ")
inputString = str(inputString)

#generate header list
with open (cardPath, 'rt') as myfile: 
    for line in myfile:
        headers.append(line)

#append headers and transcriptions to bag-of-words 
for file in sorted (listFiles):
    if not file.startswith('.') and file.endswith (".handprint-microsoft.txt"):
        BoW.write(headers[count]) #write card location to disk
        print("\n")
        print((headers[count]))
        contents = open(outPath + "/document-" + str(count + 1) + ".handprint-microsoft.txt", "r") #read card transcription
        transcriptions.append(contents.read())
        print(transcriptions[count])
        print("\n")
        BoW.write(transcriptions[count]) #write transcriptions to disk
        BoW.write("\n")
        count = count + 1
        print("\n")    
BoW.close()


#search
BoW = open(textOut, "r")
count = 0

while count < len(headers):
    if inputString in transcriptions[count]:
        print(headers[count])
        print(transcriptions[count])
        search.write("\n")
        search.write(headers[count])
        search.write(transcriptions[count])
        search.write("\n")
        print("\n")
        count = count + 1
    elif inputString not in transcriptions[count]:
        print("\n")
        print("No such string found in transcription " + str(count))
        print("\n")
        count = count + 1
search.close()

print("\n")
print("have a nice day")
        
