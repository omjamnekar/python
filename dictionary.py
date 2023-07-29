# customer ={
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }
# customer["name"] = "Jack Smith"
# customer["birthdate"] = "jan 1 1980"
# # print(customer.get("birthdate","Jan 1 1980"))
# print(customer["name"])
# print(customer["birthdate"])

# phone = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero",
# }
# str = ""
# number =input("phone")
# for ch in number:
#     str += phone.get(ch,"!") + " "
# print(str)


massage = input(">")
word = massage.split(' ')
emojis ={
    ":)" :"😊",
    ":(" :"🙁"
}

output= ""
for words in word:
    output +=emojis.get(words,words) + " "

print(output)