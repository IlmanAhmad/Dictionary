# Import the modules required
import json
import random
from win10toast import ToastNotifier

toaster = ToastNotifier()

# Loading data from json file
# in python dictionary
data = json.load(open("dict.json"))
dict_list = []
# Converting the dictionary into a list
for i in data:
    new_data = (i, data[i])
    dict_list.append(new_data)
# Choose random word every run
choose = random.choice(dict_list)

word = str(choose)
toaster.show_toast(word)


