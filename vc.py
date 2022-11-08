# author: Samikshya Ghimire gsamikshy0@gmail.com


# # take user input
# ch = input("Enter a character: ")
# # keep ch in lowercase
# ch = ch.lower()
# # check if a character is vowel or consonant
# if(ch =='i' or ch =='O' or ch =='o' or ch =='U' or ch =='u'):
#     print(ch, "is a Vowel")
# else:
#     print(ch, "is a Consonant")


# string = input("Enter a character: ")
# for x in string:
#   if(string =='A' or string =='a' or string =='E' or string =='e' or string =='I' or string =='i' or string =='O' or string =='o' or string =='U' or string =='u'):
#     print(string, "is a Vowel")
#   else:
#     print(string, "is a Consonant")
#     break

# string= raw_input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)



# #take user input
# ch = input('Enter the ch :')
# count = 0
# #keep ch in lowercase
# ch = ch.lower()
# for i in ch:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         #if True
#         count+=1
# #check if any vowel found
# if count == 0:
#     print('No vowels found')
# else:
#     print('Total vowels are :' + str(count))


# # #take user input
# ch = input('Enter the ch :')
# count = 0
# #keep ch in lowercase
# ch = ch.lower()
# for i in ch:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         #if True
#         count+=1
# #check if any consonant found
# if count == 0:
#     print('Error')
# # else:
# #     print('Total vowels are :' + str(count))
# len_word = len(ch)
# Consonant = len_word - count
# print ('Total consonant are :' + str(Consonant))

# #define all vowels in a list
# vowels = ['a', 'e', 'i', 'o', 'u']

# #input a string and transform it to lower case
# str = input("Enter a string: ").lower()

# #define counter variable for consonants
# c_ctr = 0

# #iterate through the characters of the input string 
# for x in str:
#     #if character is in the vowel list,
#     #update the vowel counter otherwise update consonant counter
#     if x != 'vowels':
# #output the values of the counters
#       print ("Consonants: ", c_ctr)



# lst1 = ['a', 'b', 'c']
# lst2 = ['b', 'c', 'd']
# result = lst1+lst2
# result.sort()
# print('List in Ascending Order: ', result)

# lst1 = [1, 2, 3, 4]
# lst2 = [2, 3, 4, 5, 6] 
# result = lst1+lst2
# my_set = set(result)
# my_new_list = list(my_set)
# my_new_list.sort()
# print("List of unique numbers : ",my_new_list)

