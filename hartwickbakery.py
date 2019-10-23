# Eddie Carpio
# 10/14/2019
# program will process 6 months of hartwick bakery's sales records.
cookies = []
candy = []


def cookies_input():
    for i in range(0, 6):
        cookies.append(int(input(">")))


def candy_input():
    for i in range(0, 6):
        candy.append(int(input(">")))


def meanofcookies():
    average1 = total1 / 6
    return print(f"The average of cookies is...{average1}")


def meanofcandy():
    average2 = total2 / 6
    return print(f"the average of candy sold is...{average2}")


def maximumofcookies():
    return print(f"Your maximum number of cookies sold in one month is {max(cookies)}")


def maximumofcandy():
    return print(f"Your maximum number of cookies sold in one month is {max(candy)}")

def minimumofcookies():
    return print(f"Your minimum number of cookies sold in one month is {min(cookies)}")

def minimumofcandy():
    return print(f"Your minimum number of candy sold in one month is {min(candy)}")

print("Cookie sales per month")
cookies_input()
total1 = int(sum(cookies))

print("Candy sales per month")
candy_input()
total2 = int(sum(candy))
meanofcookies()
meanofcandy()
maximumofcookies()
maximumofcandy()
minimumofcookies()
minimumofcandy()
if sum(candy) > sum(cookies):
    print("The more popular item at the bakery is candy!")
elif sum(cookies) > sum(candy):
    print("The more popular item at the bakery is cookies!")

