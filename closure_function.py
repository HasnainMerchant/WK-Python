# def outer_function():
#     test = 10
#
#     def inner_function(test=test):
#         test += 10
#         print(test)
#
#     return inner_function
#
# ifn = outer_function()
# ifn()

# Python program to illustrate
# nested functions
def outerFunction():
    text = 200
    def innerFunction():
        text = 300
        print(text)

    return innerFunction

ifn = outerFunction()
ifn()