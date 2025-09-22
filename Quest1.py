
workers_file = open("workers", "w")
print(workers_file.writable())
workers_file.write("Hello, BootCamp members")
workers_file.close()
#or-- with open("workers_file","w") as file: هذا يخلي الملف يقفل من نفسه تلقائي اذا خلصت الكتابة

workers_file = open("workers","r")
print(workers_file.readable())
print(workers_file.read())
workers_file.close()
#-----------------------------
import string

def clean_text(text):
    text = text.lower()       # تحويل الحروف كلهاإلى صغيرة
    text = text.translate(str.maketrans("", "", string.punctuation))     # إزالة علامات الترقيم
    return text
with open("workers", "r") as file:
    content = file.read()

cleaned_content = clean_text(content)
print(cleaned_content)
#-----------------------------
import json
data_dict = {"id": 1, "text": "Hello World"}
with open("sample.json", "w") as json_file:
    json.dump(data_dict, json_file)
with open("sample.json", "r") as json_file:
    data = json.load(json_file)
print(data["text"])

#-----------------------------
import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.text)
response_json = response.json()
print(response_json["headers"])

#------------------------------

filename = input("Enter the text file name: ")
with open(filename, "r") as file:
    text = file.read()
cleaned_text = clean_text(text)  # استخدم الدالة من File Handling
lines = text.splitlines()
words = cleaned_text.split()
longest_word = max(words, key=len)

stats = {
    "number_of_lines": len(lines),
    "number_of_words": len(words),
    "longest_word": longest_word
}

print(stats)
with open("report.json", "w") as report_file:
    json.dump(stats, report_file, indent=4)
    