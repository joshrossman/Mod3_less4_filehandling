import os

def list_directory_contents(path):
    my_path = os.listdir(path)
    print(my_path)

while True:
    my_path =input("Please include path, and program will list out directories and files. Or 'EXIT' to exit.")
    if my_path.lower()=="exit":
        break
    else:
        try:
            list_directory_contents(my_path)
        except Exception as e:
            print("Unable to list files based on directory given. Error: {e}")
