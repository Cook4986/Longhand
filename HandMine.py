

####Image prep + cloud-based handwriting transcription + text mining###
###Matt Cook 2021###
###Requires HandPrint (https://github.com/caltechlibrary/handprint) from Mike Hucka

#Run Handprint from local directory
!handprint --service microsoft "xxx" --no-grid --extended --output "xxx"

#xxx = directory pathnames

####Bag-of-Words txt output and string search from HandPrint transcriptions. MNC - 5/21
###Built to work with HandPrint, by Mike Hucka: 

import os
import sys
import re

#paths
cardPath = 'xxx'#urls
outPath = 'xxx' #output 
textOut = 'xxx'#Bag-of-Words
searchOut = 'xxx'#user search output
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
        #print("\n")
        #print((headers[count]))
        contents = open(outPath + "/document-" + str(count + 1) + ".handprint-microsoft.txt", "r") #read card transcription
        transcriptions.append(contents.read())
        #print(transcriptions[count])
        #print("\n")
        BoW.write(transcriptions[count]) #write transcriptions to disk
        BoW.write("\n")
        count = count + 1
        #print("\n")    
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
        #print("\n")
        print("No such string found in transcription " + str(count))
        #print("\n")
        count = count + 1
search.close()

print("\n")
print("have a nice day")
        
###To DO
### more inclusive search
### new line in BoW, between cards
### LocateXT integration


# In[32]:


### text mining/topic modeling
import gensim
import nltk

#TO-DO: tokenize


# In[ ]:




