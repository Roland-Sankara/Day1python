list_A= [1,2,3,4,5,6,7,8,9]
list_B = [1,2,3,4,5,6,7]


def Fizzbuzz(list1,list2):
    combined_length = len(list1) + len(list2)
    if (combined_length) % 5 == 0 and (combined_length) % 3 == 0:
        return 'Fizzbuzz'
    elif (combined_length) % 5 == 0:
        return 'Buzz'
    elif (combined_length) % 3 == 0:
        return 'Fizz'
    return (combined_length)


print(Fizzbuzz(list_A,list_B))       