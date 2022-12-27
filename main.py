import os

USERPROFILE = os.path.expanduser('~')


class MyClass:
    def __init__(self):
        self.welcome_message = "Welcome to MyClass!"

    def run(self):
        print(self.welcome_message)

        choice = input("Please choose one of the following options: 1, 2, or 3: ")
        if choice == "1":
            print("You chose option 1.")
        elif choice == "2":
            print("You chose option 2.")
        elif choice == "3":
            self.create_folder()
        else:
            print("Invalid choice.")

    def create_folder(self):
        desktop = os.path.join(USERPROFILE, 'Desktop')
        folder_name = input("Please enter the name for the new folder: ")
        folder_path = os.path.join(desktop, folder_name)
        try:
            os.mkdir(folder_path)
            print("Folder created successfully.")
            os.chdir(folder_path)
            print("Changed directory to " + folder_path)
        except OSError:
            print("Error: Could not create folder.")

my_class = MyClass()
my_class.run()

# class Commands:
#     def node():
#         print("ici raccourcis du node install")
#         USERPROFILE = os.path.expanduser('~')

#     def npminstall():
#         print("raccourcis du npm install")

#     def mkdircd():
#         print("raccourcis du mkdir (avec nom de fichier) et redirige directement dans le fichier (a coup de cd)")

