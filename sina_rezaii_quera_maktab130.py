class divar:
    def __init__(self):
         self.users = set()
         self.advertises = {}
         self.favorites = {}
 


    def register(self, username):
         if username in self.users:
            print("invalid username")
         else:
            self.users.add(username)
            self.advertises[username] = []
            self.favorites[username] = []
            print(f"registered successfully : {self.users}")




    def add_advertise(self, username, title):
        if username not in self.users:
            print(f"invalid username")
        else:
        
            found = False
            for x in self.advertises.values():
                if title in x:
                    found = True
                    break

            if found:
                print("invalid title")
            else:
                self.advertises[username].append(title)
                print(f"posted successfully : {title}")




    def rem_advertise(self, username, title):
        if username not in self.users:
            print("invalid username")
        elif title not in self.advertises[username]:
            print("invalid title")
        else:
            self.advertises[username].remove(title)
            print("removed successfully")
 



    def list_my_advertises(self, username):
        if username not in self.users:
            print("invalid username")
        else:
            if self.advertises[username]:
                print(" ".join(self.advertises[username]))
            else:
                print("No adverts posted yet.")



    def add_favorite(self, username, title):
        if username not in self.users:
            print("invalid username")
        found = False
        for q in self.advertises.values():
            if title in q:
                found = True
                break
        if not found:
            print("invalid title")
        elif title in self.favorites[username]:
            print("already favorite")
        else:
            self.favorites[username].append(title)
            print(f"added successfully")



    def rem_favorite(self, username, title):
        if username not in self.users:
            print("invalid username")
        elif title not in self.favorites[username]:
            print("already not favorite")
        else:
            self.favorites[username].remove(title)
            print("removed successfully")



    def list_favorite_advertises(self, username):
        if username not in self.users:
            print("invalid username")
        else:
            if self.favorites[username]:
                print(" ".join(self.favorites[username]))
            else:
                print("no favorite add yet.")
                
 

divvar = divar()

divvar.register("sina")
print("=="*10)
divvar.add_advertise("sina", "car")
print("=="*10)
divvar.register("ali")
print("=="*10)
divvar.add_advertise("ali", "pc")
print("=="*10)
divvar.add_advertise("ali", "pc")
print("=="*10)
divvar.list_my_advertises("ali")
print("=="*10)
divvar.list_my_advertises("sina")
print("=="*10)
divvar.rem_advertise("ali","car")
print("=="*10)
divvar.list_my_advertises("ali")
print("=="*10)
divvar.add_favorite("sina", "car")

divvar.add_favorite("sina", "mobile")

divvar.add_favorite("ali", "pc")

divvar.add_favorite("ali", "phon")

divvar.list_favorite_advertises("ali")

divvar.list_favorite_advertises("ali")