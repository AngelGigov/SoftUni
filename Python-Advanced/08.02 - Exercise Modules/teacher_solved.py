# ##authentification.py
# from tkinter import Entry
# from tkmacosx import Button  # windows from tkinter import Button
#
# from buying_page import display_products
# from canvas import root, frame
# from helpers import clean_screen, get_password_hash
# from json import dump, loads
#
#
# def get_users_data():
#     info_data = []  # [{}, {}, ...]
#
#     with open("db/users_information.txt", "r") as users_file:
#         for line in users_file:
#             info_data.append(loads(line))
#
#     return info_data
#
#
# def render_entry():
#     register_button = Button(
#         root,
#         text="Register",
#         bg="green",  # background color
#         fg="white",  # font color
#         bd=0,        # border = 0
#         width=90,
#         height=40,
#         command=register
#     )
#
#     login_button = Button(
#         root,
#         text="Login",
#         bg="blue",
#         fg="white",
#         bd=0,
#         width=90,
#         height=40,
#         command=login
#     )
#
#     frame.create_window(350, 260, window=register_button)
#     frame.create_window(350, 310, window=login_button)
#
#
# def register():
#     clean_screen()
#
#     frame.create_text(100, 50, text="First Name:")
#     frame.create_text(100, 100, text="Last Name:")
#     frame.create_text(100, 150, text="Username:")
#     frame.create_text(100, 200, text="Password:")
#
#     frame.create_window(230, 50, window=first_name_box)
#     frame.create_window(230, 100, window=last_name_box)
#     frame.create_window(230, 150, window=username_box)
#     frame.create_window(230, 200, window=password_box)
#
#     register_button = Button(
#         root,
#         text="Register",
#         bg="green",
#         fg="white",
#         bd=0,
#         width=80,
#         height=40,
#         command=registration
#     )
#
#     frame.create_window(315, 250, window=register_button)
#
#
# def registration():
#     info_dict = {
#         "First name": first_name_box.get(),
#         "Last name": last_name_box.get(),
#         "Username": username_box.get(),
#         "Password": password_box.get(),
#     }
#
#     if check_registration(info_dict):
#         with open("db/users_information.txt", "a") as users_file:
#             info_dict["Password"] = get_password_hash(info_dict["Password"])
#             dump(info_dict, users_file)
#             users_file.write("\n")
#             display_products()
#
#
# def check_registration(info_dict):
#     frame.delete("error")
#
#     for key, value in info_dict.items():
#         if not value.strip():
#             frame.create_text(
#                 200,
#                 300,
#                 text=f"{key} cannot be empty!",
#                 fill="red",
#                 tags="error",
#             )
#
#             return False
#
#     users_data = get_users_data()
#
#     for user in users_data:
#         if user["Username"] == info_dict["Username"]:
#             frame.create_text(
#                 200,
#                 300,
#                 text="Username is already taken!",
#                 fill="red",
#                 tags="error",
#             )
#
#             return False
#
#     return True
#
#
# def login():
#     clean_screen()
#
#     frame.create_text(100, 50, text="Username:")
#     frame.create_text(100, 100, text="Password:")
#
#     frame.create_window(230, 50, window=username_box)
#     frame.create_window(230, 100, window=password_box)
#
#     frame.create_window(300, 150, window=login_button)
#
#
# def logging():
#     if check_login():
#         display_products()
#     else:
#         frame.create_text(
#             200,
#             200,
#             text="Invalid username or password!",
#             fill="red",
#             tags="error",
#         )
#
#
# def check_login():
#     users_data = get_users_data()
#
#     user_username = username_box.get()
#     user_password = get_password_hash(password_box.get())
#
#     for user in users_data:
#         current_user_username = user["Username"]
#         current_user_password = user["Password"]
#
#         if current_user_username == user_username and current_user_password == user_password:
#             return True
#
#     return False
#
#
# def change_login_button_status(event):
#     info = [
#         username_box.get(),
#         password_box.get(),
#     ]
#
#     for el in info:
#         if not el.strip():
#             login_button["state"] = "disabled"
#             break
#     else:
#         login_button["state"] = "normal"
#
#
# first_name_box = Entry(root, bd=0)
# last_name_box = Entry(root, bd=0)
# username_box = Entry(root, bd=0)
# password_box = Entry(root, bd=0, show="*")
#
# login_button = Button(
#     root,
#     text="Login",
#     bg="blue",
#     fg="white",
#     bd=0,
#     command=logging,
# )
#
# login_button["state"] = "disabled"
#
# root.bind("<KeyRelease>", change_login_button_status)
#
# ##buying_page.py
#
# from PIL import ImageTk, Image
# from tkmacosx import Button
# from canvas import frame, root
# from helpers import clean_screen
# from json import load, dump
#
#
# def display_products():
#     clean_screen()
#     display_stock()
#
#
# def display_stock():
#     with open("db/products.json", "r") as stock:
#         info = load(stock)
#
#     x, y = 150, 50
#
#     for item_name, item_info in info.items():
#         # pillow_image = Image.open(item_info["image"])
#         # resized_pillow_image = pillow_image.resize((50, 50))
#         item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
#         images.append(item_img)
#         # keeping the reference to the image so that tkinter doesn't delete it after the function ends
#
#         frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 15))
#         frame.create_image(x, y + 100, image=item_img)
#
#         if item_info["quantity"] > 0:
#             color = "green"
#             text = f"In stock: {item_info['quantity']}"
#
#             item_button = Button(
#                 root,
#                 text="Buy",
#                 bg="green",
#                 fg="white",
#                 font=("Comic Sans MS", 12),
#                 width=50,
#                 command=lambda x=item_name, y=info: buy_product(x, y)
#             )
#
#             frame.create_window(x, y + 220, window=item_button)
#         else:
#             color = "red"
#             text = "Out of stock"
#
#         frame.create_text(x, y + 180, text=text, fill=color, font=("Comic Sans MS", 14))
#
#         x += 200
#
#         if x >= 650:
#             y += 270
#             x = 150
#
#
# def buy_product(product_name, info):
#     info[product_name]["quantity"] -= 1
#
#     with open("db/products.json", "w") as stock:
#         dump(info, stock)
#
#     display_products()
#
#
# images = []
#
# ##canvas.py
# from tkinter import Tk, Canvas
#
#
# def create_root():
#     root = Tk()
#
#     root.title("GUI Shop")
#     root.geometry("700x600")
#     root.resizable(False, False)
#
#     return root
#
#
# def create_frame():
#     frame = Canvas(root, width=700, height=700)
#     frame.grid(row=0, column=0)
#
#     return frame
#
#
# root = create_root()
# frame = create_frame()
#
#
# ##helpers.py
#
# from hashlib import sha256
# from canvas import frame
#
#
# def clean_screen():
#     frame.delete("all")
#
#
# def get_password_hash(password):
#     hash_object = sha256(password.encode())
#     return hash_object.hexdigest()
#
#
# ##main.py
# from authentication import render_entry
# from canvas import root
#
# if __name__ == "__main__":
#     render_entry()
#     root.mainloop()