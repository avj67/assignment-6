# A program to create an accessible dictionary if items in a shop

shop_list = {"milk": [100, 10], "eggs": [120, 40], "bread": [40, 30], "cheese": [100, 10]}
loop_check = 1
# accessible menu using triple quotes to increase interactivity / favour of users towards software
print(
    '''
=======================================
#        WELCOME TO XYZ GROCERS       #
#        **********************       #
#                                     #
#    (1) Search for an item           #
#    (2) Rename an item               #
#    (3) Minimum and maximum prices   #
=======================================
''')
print()
while True :
    if loop_check >0 :
        option = int(input("Welcome please choose an option: "))

        # searching for an item
        if option == 1:
            print()
            item_search = input("Enter item name please: ")
            case_item_search = item_search.lower() # case sensitvity

            if case_item_search in shop_list:
                for i in shop_list:
                    if case_item_search == i:
                        print("Item: ", i)
                        print("Stock: ", shop_list[i][0])
                        print("Price: ", shop_list[i][1])

            else:
                print("Item not found")

        #  renaming an item
        if option == 2:
            print()
            item_rename = input("Enter item to be renamed please: ")
            case_item_rename = item_rename.lower() # case sensitivity
            new_name = input("Enter the item's new name please: ")


            if case_item_rename in shop_list:
                # dictionary keys are uneditable so what we do is we make a new key with same values and delete old one
                temp_value = shop_list[case_item_rename]
                temp_dict={new_name:temp_value} #creating a temporary dictionary with new key name and old values
                shop_list.pop(case_item_rename) # deletes key with string value matching input from user
                shop_list.update(temp_dict) # adds new name with same stock and price
                print("Item has been renamed")
            else:
                print(item_rename," does not exist in database")

        # 3rd thingy

        else:
            x=1


        print()
        continuity = input("Do you wish to continue? y/n (anything other than y shall be considered as program termination ")
        if continuity == "y":
            loop_check = 1
        else:
            loop_check = 0
    else:
        break
print()
print("Thank you for using our services!")

