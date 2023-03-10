#! /usr/bin/env python3
import os
import subprocess

USERPROFILE = os.path.expanduser('~')
class Init:
    def __init__(self):
        self.welcome_message = "Welcome NapoTwiixe ! \nAttention, the root password will be asked for certain commands, to switch to sudo mode !\n\nwhat do you want to do\n"
        self.choose = "1) Install Node\n"
        self.choose0 = "2) Install Node for MacOs\n"
        self.choose1 = "3) Install Visual Studio Code For Ubuntu\n"
        self.choose2 = "4) Mkdir && Cd\n"
        self.choose3 = "5) Create File on a desktop\n"

    def run(self):
        print(self.welcome_message, self.choose, self.choose0,  self.choose1, self.choose2, self.choose3)


        choice = input("Please choose one of the following options: 1, 2, 3, 4 or 5: ")
        if choice == "1":
            self.install_node()
        elif choice == "2":
            self.node_macos()
        elif choice == "3":
            self.install_vscode()
        elif choice == "4":
            self.create_folder()
        elif choice == "5":
            self.create_file()
        else:
            print("Invalid choice.")

    # Node.Js Install
    def install_node(self):
        subprocess.run (["sudo", "apt-get", "install", "nodejs"])
        print("Node.Js installed Successfully")
        subprocess.run(["node", "--version"])

        # Add To Path
        path = os.environ['PATH']
        node_path = os.path.join(USERPROFILE, 'node_modules', '.bin')
        if node_path not in path:
            os.environ['PATH'] = node_path + ':' + path
            print("Added node to PATH")

    # Node.Js MacOs
    def node_macos(self):
        subprocess.run(["brew", "install", "node"])
        print("Node.js installed successfully")

        
    # Install VsCode
    def install_vscode(self):
        # DownLoad vscode package
        subprocess.run(["wget", "-O", "code.deb", "https://go.microsoft.com/fwlink/?LinkID=760868"])

        # Install package using dpkg
        subprocess.run(["sudo", "dpkg", "-i", "code.deb"])

        # Install missing dependencies
        subprocess.run(["sudo", "apt-get", "install", "-f"])

        # Run VsCode
        subprocess.run(["code", "."])
        print("Visual Studio Code installed successfully.")


    # Creation of file with extension of your choice (on the desktop)
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


    # Ccreation of a folder with a name of your choice (on the desktop)
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