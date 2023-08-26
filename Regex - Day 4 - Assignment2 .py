#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import shutil
import webbrowser
import pywhatkit as kit

def display_os_info():
    print("OS System Information:")
    print("OS Name:", os.name)
    print("User:", os.getlogin())
    print("Current Directory:", os.getcwd())

def create_folder_on_desktop(folder_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop_path, folder_name)
    
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created on Desktop.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists on Desktop.")

def copy_file_to_folder(source_file, destination_folder):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    source_path = os.path.join(desktop_path, source_file)
    destination_path = os.path.join(desktop_path, destination_folder, source_file)
    
    try:
        shutil.copy(source_path, destination_path)
        print(f"File '{source_file}' copied to '{destination_folder}' folder.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found on Desktop.")

def search_on_google(query):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(number, message)

user_input = input("Enter a task number (1-5): ")

if user_input == "1":
    display_os_info()
elif user_input == "2":
    folder_name = "regex"
    create_folder_on_desktop(folder_name)
elif user_input == "3":
    source_file = input("Enter the name of the file to copy: ")
    destination_folder = "regex"
    copy_file_to_folder(source_file, destination_folder)
elif user_input == "4":
    search_query = "software"
    search_on_google(search_query)
elif user_input == "5":
    receiver_number = "+919983034111"
    message = "This is Python Assignment given by tushar sir"
    send_whatsapp_message(receiver_number, message)
else:
    print("Invalid input. Please enter a valid task number.")


# In[ ]:




