import math


def main():
    # learn_str_func(False)
    # learn_number_func(True)
    learn_list_tuple_set_func(True)


def learn_list_tuple_set_func(learn):
    """ learning List, Tuple, and Set"""
    fruits = ["apple", "banana", "cherry", "dates"]
    # print(fruits)
    # print(len(fruits))
    # print(f"{fruits[0]} {fruits[3]}")
    # print(
    #     f"{fruits[-1]} {fruits[-3]}"
    # )  # - means opposite direction and 0 = apple; -1 is always the end of the list
    # print(fruits[0:2])  # 0, 1
    # print(fruits[:2])  # empty before : => start of the list
    # print(fruits[2:3])  # 2
    # print(fruits[2:])  # 2,..., end; empty after : => end of the list

    # fruits.append("fig")  # append 'fig' at the end - "in-place"
    # print(fruits)

    # fruits.insert(0, "fig")  # insert 'fig' at location=0 - "in-place"
    # print(fruits)

    # fruits.insert(3, "fig")
    # print(fruits)

    # new_fruits = ["fig", "grapes"]
    # print(new_fruits)
    # print(*new_fruits)

    # fruits.append(new_fruits)
    # print(fruits)

    # fruits.insert(3, new_fruits)
    # print(fruits)

    # fruits.extend(new_fruits) # a
    # print(fruits)

    # fruits.remove("apple")  # removes apple in-place
    # print(fruits)

    # popped_fruit = fruits.pop()  # returns last item in-place
    # print(popped_fruit)
    # print(fruits)

    # fruits.reverse()
    # print(fruits)
    # fruits.sort()
    # print(fruits)
    # fruits.sort(reverse=True)
    # print(fruits)
    # print(sorted(fruits), " - ", fruits)  # sorted() is not in-place

    # print(fruits.index("cherry"))
    # print("cherry" in fruits)

    # print(fruits.index("grapes")) # generates error
    # print("grapes" in fruits)

    # for fruit in fruits:
    #     print(fruit)

    # for index, fruit in enumerate(fruits):
    #     print(index, ": ", fruit)

    # for index, fruit in enumerate(fruits, start=123):
    #     print(index, ": ", fruit)

    # fruits_str = ", ".join(fruits)
    # print(fruits_str)
    # fruits_str = "{}, fig".format(fruits_str)
    # print(fruits_str)
    # fruits_2 = fruits_str.split(", ")
    # print(fruits_2)

    # numbers = [1, 5, 18, 1999, 2020]
    # print(min(numbers))
    # print(max(numbers))
    # print(sum(numbers))

    # fruits_copy = fruits  # List is MUTABLE
    # print(id(fruits), ": ", fruits)
    # print(id(fruits_copy), ": ", fruits_copy)
    # fruits_copy[3] = "figs"
    # print(id(fruits), ": ", fruits)

    # list + access + modify => use list
    # list + access => use tuple (no modification, so not much methods)
    # tup_fruits = ("apple", "banana", "cherry", "dates")  # Tuple is IMMUTABLE
    # print(tup_fruits)

    # tup_fruits[2] = "fig"
    # print(tup_fruits)


def learn_number_func(learn):
    #    num = 3
    #    print(type(num))
    #    num = 3.14
    #    print(type(num))
    num1 = 7
    num2 = 3
    # print("Addition: ", (num1 + num2))
    # print("Subtraction: ", (num1 - num2))
    # print("Multiplication: ", (num1 * num2))
    # print("Division: ", (num1 / num2))
    # print("Floor Division: ", (num1 // num2))
    # print("Exponent: ", (num1 ** num2))
    # print("Modulus: ", (num1 % num2))
    # print("Absolute: ", abs(-num1))
    # print("Round: ", round(num1 / num2))
    # print("Round: ", round(math.pi, 5))
    # print("++: ", num1++) # not available
    # num1 = num1 + 1
    # print("increment by 1: ", num1)
    # num1 += 9  # num1 = num1 + 1
    # print("increment by 9: ", num1)
    # num1 *= 2
    # print("multiplied by 2: ", num1)

    # print("Equal: ", (num1 == num2))
    # print("Not Equal: ", (num1 != num2))
    # print("Greater than: ", (num1 > num2))
    # print("Less than: ", (num1 < num2))
    # print("Greater OR equal: ", (num1 >= num2))
    # print("Less OR equal: ", (num1 <= num2))

    print("apple" == "aPple")  # The characters in both strings are compared one by one
    print("apple" > "aPple")
    print("Unicode of a: ", ord("p"), "\n", "Unicode of A: ", ord("P"))

    num1 = "7"
    num2 = "3"
    print(num1 + num2)  # for string, + concatenates
    print(int(num1) + int(num2))  # for numbers, + adds


def learn_str_func(learn):
    if learn == True:
        msg = "Hello World Hello hello hello World"
        # print(msg)
        # print(type(msg))
        # print(len(msg))

        # print(msg[1])
        # print(msg[0:5]) #0=included but 5=not included i.e. 0,1,2,3,4
        # print(msg[:5]) # before : => empty means start from beginning

        # print(msg[6:]) #6,7,...end

        # print(msg.lower())
        # print(msg.upper())
        # print(msg.count('Hello'),'\n')
        # print(msg.count('World'))
        # print(msg.lower().count('hello'))
        # 'Hello World Hello hello hello World'
        # print(msg.find('world')) # case sensitive - not found = -1
        # print(msg.find('World'))
        # print('World' in msg)
        # print(msg.find('World',7))

        # print(msg.replace("hello", "Hello"))
        a = 1
        first_str = "Hello"
        second_str = "World"
        msg = first_str + " " + second_str  # \t
        # msg = '{} {}. We\'re learning python...story....first, second'.format(first_str, second_str)
        # msg = '{1} {0}. We\'re learning python...story....first, second'.format(first_str, second_str)
        # msg = f'{first_str} {second_str}. We\'re learning python...story....first, second'
        print(msg)


main()