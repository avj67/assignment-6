# A program to take in a word from a user and create a dictionary where key value is letters and occurence is value

# Taking input from user
word = input("Enter the word please: ")

# Typecasting to list for convenience
word_list = list(word)

# creating a list without doubles
nodoubles_list = list(set(word_list))

# Creating dictionary with all having base value as 1
main_dict = dict.fromkeys(word_list,0)

# Declaring some variables for later use

count = len(word_list)
d1={}
tempcount= len(word_list)
index=0

print(main_dict)

for i in nodoubles_list:                    #basically gives us value 1 more than i index for next for loop\
    for j in range (index,count):               #checks for common values also adds 1 for starting letter
        if nodoubles_list[index] == word_list[j]:
            main_dict[word_list[index]]+=1
    index+=1
print(main_dict)

#for i in range (tempcount):              #basically gives us value 1 more than i index for next for loop
    #for j in range (i,count):               #checks for common values also adds 1 for starting letter
        #if word_list[i] == word_list[j]:
            #main_dict[word_list[i]]+=1

