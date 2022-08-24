import re
#
#
# class BasePerson:
#
#     def is_valid(self, number):
#         is_valid1 = re.search(r"0([1-9]{1})KG([A-Z0-9]{5,7})", number)
#         is_valid2 = re.search(r"([A-Z0-9]{5,8})", number)
#
#         if is_valid1 or is_valid2:
#             if is_valid1:
#                 print("S nomerom brat vse ok ezhe!")
#             elif is_valid2:
#                 print("Menyay nomer brat on staryi!")
#
#         else:
#             print("Nomer invalid ezhe!")
#
#
# v = BasePerson().is_valid(input("type your car number: "))


class SpecialCarNumber:

    def is_valid(self, background,  number):
        diplomat = re.search(r"(CMD|HC|C|D|T)([0-9]{3,5})", number)
        mvd = re.search(r"(MVD|MES|AP|BP)([0-9]{3,5})", number)
        high = re.search(r"([1-9]{1,3})KG", number)

        if number[diplomat.start():diplomat.end()] == number:
            if background == "red" or "Red":
                print("Hello diplomat!")
            else:
                print("net takogo nomera na diplomata!!!")

        elif number[mvd.start():mvd.end()] == number:
            if background == "white" or "White":
                print("Hello MVD!")
            else:
                print("net takogo nomera v MVD!!!")

        elif number[high.start():high.end()] == number:
            if background == "blue" or "Blue":
                print("Hello HIGH GITLER!")
            else:
                print("net takogo nomera HIGH GITLER!!!")




v = SpecialCarNumber().is_valid(number=input("type your car number: "), background = str(input("type your background color: ")))

