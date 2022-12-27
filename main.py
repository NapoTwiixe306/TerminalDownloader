import os

USERPROFILE = os.path.expanduser('~')
class Init:
    def __init__(self):
        self.welcome_message = "Welcome NapoTwiixe !\n"
        self.choose = "1) Install Node\n"
        self.choose1 = "2) Install Python\n"
        self.choose2 = "3) Mkdir && Cd\n"

    def run(self):
        print(self.welcome_message, self.choose, self.choose1, self.choose2)


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

init = Init()
init.run()

# class Commands:
#     def node():
#         print("ici raccourcis du node install")

#     def npminstall():
#         print("raccourcis du npm install")

#     def mkdircd():
#         print("raccourcis du mkdir (avec nom de fichier) et redirige directement dans le fichier (a coup de cd)")

