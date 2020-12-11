import requests
import config


def urban_dict(word):
    """This function will take word as input and then hit the Urban dictionary API and bring meaning back"""

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {}

    querystring["term"] = word

    headers = config.headers

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


user_input = input("Enter the word : ")
output = urban_dict(user_input)
