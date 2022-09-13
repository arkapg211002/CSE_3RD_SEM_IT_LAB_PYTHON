'''
Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates.

NOTE: Generate a random integer between 0 and 6:

0

Generate random integer between 5 and 10, excluding 10:

5

Generate random integer between 0 and 10, with a step of 3:

3

Random date between two dates:

2019-02-17
'''
import random
import datetime
def random_int():
    return random.randrange(0, 6)
def random_int2():
    return random.randrange(5, 10)
def random_int3():
    return random.randrange(0, 11, 3)
def random_date():
    start = datetime.date(2019, 1, 1)
    end = datetime.date(2022, 12, 31)
    return start + datetime.timedelta(
        days=random.randint(0, (end - start).days),
    )
def main():
    print(random_int())
    print(random_int2())
    print(random_int3())
    print(random_date())
if __name__ == '__main__':
    main()

