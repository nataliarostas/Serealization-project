import pickle
from os import path


def save(obj, filename):
   with open(filename, "wb") as f:
       pickle.dump(obj, f)


def load(filename):
   if path.exists(filename):
       with open(filename, "rb") as f:
           return pickle.load(f)
   return None


USERS_FILE = "users.pkl"
users = load(USERS_FILE)
if users is None:
   users = {}


def display_choices(choices):
   for index, choice in enumerate(choices, start=1):
       print(f"{index}. {choice}")


def get_user_choice(choices):
   while True:
       choice = input("Enter your choice: ")
       if choice.isdigit() and 1 <= int(choice) <= len(choices):
           return int(choice)
       print("Invalid choice. Please try again.")


def get_user_path_choice():
   while True:
       path_choice = input("Enter 'L' for left or 'R' for right: ")
       path_choice = path_choice.upper()
       if path_choice == 'L' or path_choice == 'R':
           return path_choice
       print("Invalid choice. Please try again.")


def play_story():
   name = input("Enter your name: ").capitalize()
   if name not in users:
       print ("Welcome," ,name)
       users[name] = ""
   else:
       print("Welcome back,",name)

   save(users, USERS_FILE)  # Save the updated users dictionary

   print("You are lost in the woods and come across two paths. Which path will you choose?")
   path_choice = get_user_path_choice()

   if path_choice == "L":
       print("You follow the left path and come across a river.")
       print("What will you do?")
       display_choices(["Cross the river", "Follow the riverbank"])
       river_choice = get_user_choice([1, 2])

       if river_choice == 1:
           print("You decide to cross the river.")
           print("As you cross the river, you encounter a group of wild animals!")
           display_choices(["Fight them", "Run away"])
           animal_choice = get_user_choice([1, 2])

           if animal_choice == 1:
               print("You bravely fight off the animals and continue your journey.")

           elif animal_choice == 2:
               print("You quickly run away from the animals and find a safe spot.")

       elif river_choice == 2:
           print("You choose to follow the riverbank.")
           print("While walking along the riverbank, you spot a hidden cave.")
           display_choices(["Enter the cave", "Ignore the cave"])
           cave_choice = get_user_choice([1, 2])

           if cave_choice == 1:
               print("You enter the cave and find a valuable treasure.")

           elif cave_choice == 2:
               print("You decide to ignore the cave and continue walking along the riverbank.")

   elif path_choice == "R":
       print("You take the right path.")
       print("The right path leads you to a beautiful meadow.")
       print("What will you do?")
       display_choices(["Rest in the meadow", "Explore further"])
       meadow_choice = get_user_choice([1, 2])

       if meadow_choice == 1:
           print("You decide to rest in the meadow and enjoy the peaceful surroundings.")
           print("A goose is attacking you, what do you do??")
           display_choices(["Fight it", "Run away"])
           goose_choice = get_user_choice([1, 2])

           if goose_choice == 1:
               print("You bravely fight off the goose and continue your journey.")

           elif goose_choice == 2:
               print("You quickly run away from the goose and find a safe spot.")

       elif meadow_choice == 2:
           print("You decide to explore further in the meadow.")
           print("While exploring, you stumble upon an ancient building with people who help you.")
           print("After getting the help, what do you do?")
           display_choices(["stay with them forever", "Thanks them and continue the journey"])
           final_choice = get_user_choice([1, 2])

           if final_choice == 1:
               print("You stay with the people and live happily ever after.")

           elif final_choice == 2:
               print("You move on an explore the rest of the world.")
play_story()