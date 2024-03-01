from docx import Document
import requests
myDoc = "homework.docx"
difficultWords = []
myDict = {}
doc = Document(myDoc)
wordCount = 0
boldWordCount = 0
normalWordCount = 0


for p in doc.paragraphs:
    for word in p.runs:
        wordCount += 1
        if(word.bold):
            difficultWords.append(word.text)
            boldWordCount += 1
            myDict[word.text] = "Undefined"
        else:
            normalWordCount += 1



headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}


for word in difficultWords:
    response = requests.get(f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions", headers=headers)
    data = response.json()
    if 'definitions' in data and data['definitions']:
        try:
            myDict[word] = data['definitions'][0]['definition']
        except IndexError:
            myDict[word] = "Definition not found"
    else:
        myDict[word] = "Definition not found"


print(myDict)
for w,d in myDict.items():
    print(f"WORD: {w} DEFINITION: {d}")

print(f"There are {wordCount} many words in the document")
print(f"There are {boldWordCount} bold words and {normalWordCount} non-bolded words")