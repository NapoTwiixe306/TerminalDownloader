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
            print("You chose option 3.")
        else:
            print("Invalid choice.")

init = Init()
init.run()

# class Commands:
#     def node():
#         print("ici raccourcis du node install")

#     def npminstall():
#         print("raccourcis du npm install")

#     def mkdircd():
#         print("raccourcis du mkdir (avec nom de fichier) et redirige directement dans le fichier (a coup de cd)")

