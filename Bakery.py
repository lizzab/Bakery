# Ben Lizza
# 10/14/19

# Make a cookie list and a candy list
# Define a function for each category to allow user to input values
# the cookie_input function the user will tell user to enter six values (LOOP) which will be added to the list

cookies = []
candies = []


def cookies_input():
    for i in range(0,6):
        value = int(input("Enter six numbers that will be added to the cookies list: "))
        cookies.append(value)
    print(cookies)


def candies_input():
    for i in range(0,6):
        value_ca = int(input("Enter six values for the candies list: "))
        candies.append(value_ca)
    print(candies)


# define a function that will compute and print the average monthly sales for cookies.


def cookies_avg():
    avg = sum(cookies) / float(len(cookies))
    print(f"The average for cookies are {avg}")


def candies_avg():
    can_avg = sum(candies) / float(len(candies))
    print(f"The average of candies are {can_avg}")

# define functions that will determine the max of both lists
# define functions that will determine the min of both lists


def max_candies():
    ca_value1 = max(candies)
    print(f"The max value of candies: {ca_value1}")


def max_cookies():
    co_value1 = max(cookies)
    print(f"The max value of cookies: {co_value1}")


def min_candies():
    ca_value2 = min(candies)
    print(f"The min value of candies: {ca_value2}")


def min_cookies():
    co_value2 = min(cookies)
    print(f"The min value of cookies: {co_value2}")


cookies_sum = sum(cookies)
candies_sum = sum(candies)

cookies_input()
candies_input()
cookies_avg()
candies_avg()
max_candies()
max_cookies()
min_candies()
min_cookies()

if cookies_sum > candies_sum:
    print("Cookies are the most popular at the Hartwick Bakery!")
else:
    print("Candies are the most popular at the Hartwick Bakery!")

