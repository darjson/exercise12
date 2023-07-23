import random

lottery = set()
while len(lottery) < 6:
    print(lottery)
    ball = random.randint(1,50)
    print(f"Adding {ball}.")
    lottery.add(ball)
    print(len(lottery))
print(sorted(lottery))
print("End")






# # import random
# #
# # x = random.randint(0,50)
# # print(x)
# import random
#
# mylist = []
#
# for i in range(6):
#
#     x = random.randint(1,50)
#     Number = set()
#
#     if x not in mylist:
#         mylist.append(x)
#
# print(mylist)
#
#
# # def generate_lottery_number():
# #   # Generate a random 6-digit lottery number
# #   lottery_number = ""
# #   for i in range(6):
# #     lottery_number += str(random.randint(0,50))
# #   return lottery_number
# # #random.randint = (','.format(generate_lottery_number))
# # print(generate_lottery_number())