# write your code here
import random

number_of_friends = int(input("Enter the number of friends joining (including you):"))

if number_of_friends < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    count = 0;
    friends_dict = dict()

    while count < number_of_friends:
        name = input()
        friends_dict[name] = 0
        count += 1
    tot_bill = int(input("Enter the total bill value:"))
    # bill_per_friend = tot_bill / number_of_friends

    lucky_sel = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    lucky_friend = ""
    if lucky_sel == "Yes":
        lucky_friend = random.choice(list(friends_dict.keys()))
        print(f"{lucky_friend} is the lucky one!")
    else:
        print("No one is going to be lucky")

    if lucky_friend in friends_dict.keys():
        bill_per_friend = tot_bill / (number_of_friends - 1)
    else:
        bill_per_friend = tot_bill / number_of_friends

    for k in friends_dict.keys():
        friends_dict[k] = round(bill_per_friend, 2)

    if lucky_sel == "Yes":
        friends_dict[lucky_friend] = 0

    print(friends_dict)
