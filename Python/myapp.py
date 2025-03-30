# object oriented programming
# class Book:
#     material="Paper"
#     cover="paperback"
#     all_book=[]

# print(Book.cover)
# print(Book.material)
# print(Book.all_book)

# my_book = Book()
# print(my_book.material)
# print(my_book.cover)
# print(my_book.all_book)

# class Tree:
#     trunk = True
#     branches = True
#
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

# class House:
#     construction = "building"
#     elevator = True
#
# new_house = House()

# class Angel:
#     color="white"
#     feature="wings"
#     home="Heaven"
#
# An_angel = Angel()
# print(An_angel.color)
# print(An_angel.feature)
# print(An_angel.home)
#
#
# class Demon:
#     color="red"
#     feature="horns"
#     home="Hell"
#
# A_demon = Demon()
# print(A_demon.color)
# print(A_demon.feature)
# print(A_demon.home)

# class RockBand:
#     genre="gospel"
#     n_members=3
#     key_instruments=['drums','microphone','guitar','piano']
#
# myrock_band = RockBand()
# print(myrock_band.genre)
# print(myrock_band.n_members)
# print(myrock_band.key_instruments)
#
# trading = [1,2]
# # trading.append(3)
# trading.insert(0,"num")
# print(trading)
#
# update_versions =[1.2, 3.5, 2]
# for version in update_versions:
#     print(version+1)
# #
# todo_list = []
# while True:
#     if not todo_list:
#         print('Your ToDo list is empty')
#     else:
#         index = 1
#         for task in todo_list:
#             print(f"{index}.{task}")
#             index += 1
#
#     print("Options: ")
#     print("1) Add Task")
#     print("2) Remove Task")
#     print("3) Quit")
#
#     choice = input("Enter your choice(1, 2, or 3): ")
#
#     if choice == "1":
#         new_task = input("Enter the task: ")
#
#         todo_list.append(new_task)
#         print(f"Task {new_task} added!")
#
#     elif choice == "2":
#         if todo_list == []:
#             print("It's empty")
#         else:
#             print(todo_list.pop())
#         print("Removing task")
#     elif choice == "3":
#         print("Quitting")
#         break
