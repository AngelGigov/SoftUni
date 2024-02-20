# # ex_1
#
# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#
#     try:
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number must be an integer")
#
#     line = input()
#
# line = input()
#
# while line != "Remove":
#     searched = line
#
#     try:
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print("Number does not exist in dictionary")
#
#     line = input()
#
# line = input()
#
# while line != "End":
#     searched = line
#     try:
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#
#     line = input()
#
# print(numbers_dictionary)

#ex_2
# from re import findall
#
#
# class NameTooShortError(Exception):
#     pass
#
#
# class MustContainAtSymbolError(Exception):
#     pass
#
#
# class InvalidDomainError(Exception):
#     pass
#
#
# class MoreThanOneAtSymbol(Exception):
#     pass
#
#
# class InvalidNameError(Exception):
#     pass
#
#
# VALID_DOMAINS = ("com", "bg", "org", "net")
# MIN_NAME_SYMBOLS_COUNT = 4
#
# pattern_name = r'\w+'  # a1234_ -> [a1234_]; a??123 -> [a, 123]
#
# email = input()
#
# while email != "End":
#
#     if email.count("@") > 1:
#         raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
#     if "@" not in email:
#         raise MustContainAtSymbolError("Email must contain @!")
#     if len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
#         raise NameTooShortError("Name must be more than 4 characters!")
#     if email.split(".")[-1] not in VALID_DOMAINS:
#         raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
#     if findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
#         raise InvalidNameError("Name must contain only letters, digits and underscores!")
#
#     print("Email is valid")
#
#     email = input()

#ex_3
import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()  # download the image

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image  # keeps reference to the image


def get_image_url() -> str:
    headers = {
        "Authorization": "YOUR API KEY"
    }

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    return result['openai']['items'][0]["image_resource_url"]


def render_image():
    print("clicked")

    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("AI Image Generator")
window.geometry("500x350")  # width x height

error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")

input_field = tk.Entry(window, width=14)
input_field.place(x=165, y=20)

image_label = tk.Label(window)
image_label.place(x=125, y=70)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=300, y=18)

window.mainloop()