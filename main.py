import os

USERPROFILE = os.path.expanduser('~')
class Init:
    def __init__(self):
        self.welcome_message = "Welcome NapoTwiixe !\n"
        self.choose = "1) Install Node\n"
        self.choose1 = "2) Install Visual Studio Code\n"
        self.choose2 = "3) Mkdir && Cd\n"
        self.choose3 = "4) Create File on a desktop\n"

    def run(self):
        print(self.welcome_message, self.choose, self.choose1, self.choose2, self.choose3)


        choice = input("Please choose one of the following options: 1, 2, 3 or 4: ")
        if choice == "1":
            print("You chose option 1.")
        elif choice == "2":
            print("You chose option 2.")
        elif choice == "3":
            self.create_folder()
        elif choice == "4":
            self.create_file()
        else:
            print("Invalid choice.")

    # Creation de fichier avec extension au choix ( sur le bureau)
    def create_file(self):
        desktop = os.path.join(USERPROFILE, 'Desktop')
        file_name = input("Please enter the name for the new file: ")
        file_extension = input("Please enter the extension for the new file (e.g. .txt): ")
        file_path = os.path.join(desktop, file_name + file_extension)
        try:
            with open(file_path, 'w') as f:
                f.write("This is a test file.")
            print("File created successfully at " + file_path)
        except OSError:
            print("Error: Could not create file.")
    # Creation d'un dossier avec nom au choix ( sur le bureau)
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

