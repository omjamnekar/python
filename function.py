def greet_user():
    print("hi there!")
    print("welcome aboard")


print("start")
greet_user()
print("finish")


# start
# hi there!
# welcome aboard
# finish


# PARAMETER FUNCTION

def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print(f"welcome aboard{first_name}")


greet_user('john', 'smith')  # positional argument
greet_user(last_name='smith', first_name='john')  # keyword argument


# greet_user(last_name='smith','john') #keyword argument
# greet_user('smith',first_name='john') #keyword argument
# use keyword argument after positional argument

# return function

def square(number):
    return number * number


print(square(3))


def square1(number):
    print(number * number)


print(square1(3))

massage = input(">")


def emos(massage):
    word = massage.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "🙁"
    }
    output = ""
    for words in word:
        output += emojis.get(words, words) + " "
    return output


f = emos(massage)
print(f)
