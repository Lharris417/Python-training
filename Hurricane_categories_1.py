user_input = input("What is the category")

user_input = int(user_input)
if user_input == 1:
    print("74-94mph")
elif user_input == 2:
    print("96-110mph")
elif user_input == 3:
    print("111-129mph")
elif user_input == 4:
    print("130-156mph")
elif user_input == 5:
    print("157+mph")
else:
    print("This is not a category")
