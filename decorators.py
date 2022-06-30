import datetime

def timed_greeting(func):
    hour = datetime.datetime.now().hour
    if 12 <= hour < 22:
        func("My","Name","Is","Hasnain")
        print("\nWhat a Lovely evening It is")

# greeting() Is Passed as a Function to timed_greeting() automatically or internally
# timed_greeting is a decorator for greeting()
@timed_greeting
def greeting(*args):
    print("Greetings")
    for arg in args:
        print(f"{arg}", end= " ")
