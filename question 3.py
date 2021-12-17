# A program to take in a word from a user and create a dictionary where key value is letters and occurence is value

# Taking input from users
word = input("Enter the word please: ")

# Typecasting to list for convenience
word_list = list(word)

# creating a list without doubles
nodoubles_list = list(set(word_list))

# Creating dictionary with all having base value as 1.
main_dict = dict.fromkeys(word_list,0)

# Declaring some variables for later use

count = len(word_list)
d1={}
tempcount= len(word_list)
index=0


print(main_dict)
for i in nodoubles_list:
    for j in range (index,count):
        if i == word_list[j]:
             main_dict[word_list[j]]+=1
    index+=1
print(main_dict)

#what i was using but this gives 1 extra count to double letters because it takes the double letters each  so count +1 extra
#for i in range (tempcount):
    #for j in range (i,count):
        #if word_list[i] == word_list[j]:
            #main_dict[word_list[i]]+=1


