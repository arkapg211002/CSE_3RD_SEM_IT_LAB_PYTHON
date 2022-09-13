'''
Write a Python program to generate a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70.

NOTE: Generate a random alphabetical string:

lGhPpBDqfCgXKzSbGcnmcDWBEZeiqcUqztgvwcXfVyPslOggKdbIxOejJfFMgspqrgskanNYpscJEOVIpYkGGNxQlaqeeubGDbQSBhBedrdOyqOmKPTZvzKmKVoids

Generate a random value between two integers, inclusive:

0

4

1

Generate a random multiple of 7 between 0 and 70:

70
'''
import random
import string
def random_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(100))
def random_int():
    return random.randint(0, 4)
def random_multiple():
    return random.randrange(0, 71, 7)
def main():
    print(random_string())
    print(random_int())
    print(random_multiple())
if __name__ == '__main__':
    main()

