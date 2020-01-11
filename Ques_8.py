import re
string = 'My Profile on github : https://github.com/harshsharma27/Task_1.git'

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
print("Url : ",url)