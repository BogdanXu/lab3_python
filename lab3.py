# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def problem_1(): 
    def doing_stuff_with_lists(a, b):
        result = []
        result.append(a & b)
        result.append(a | b)
        result.append(a - b)
        result.append(b - a)
        return result
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    
# 2. Write a function that receives a string as a parameter 
#    and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
def problem_2():
    def dictionary_builder(string_input):
        result = dict()
        for c in string_input:
            result[c] = result[c] + 1 if c in result else 1
        return result
    print(dictionary_builder("Ana has apples."))

# 3. Compare two dictionaries without using the operator "==" and return a list of differences as follows: 
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
# a = {'a':1, 'b':2, 'c':2}
# b = {'a':1, 'b':{'c':2}, 'd':[2, 3]
#TODO recursivity
def problem_3():
    def dictionary_comparator(a, b):
        for i in a:
            if i in b:
                if type(a[i]) is not type(b[i]):
                    print("value of key", i, "in the first dictionary is of type", type(a[i]), "while the value of the same key in the second dictionary has type", type(b[i]))
                if a[i] != b[i]:
                    print("value of key", i, "is", a[i], "in the first dictionary and", b[i], "in the second dictionary")
    a = {'a':1, 'b':2}
    b = {'b':2, 'a':1.1}
    dictionary_comparator(a, b)

# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).

def problem_6():
    def doing_stuff_with_list(list_1):
        sorted_list = sorted(list_1)
        sorted_list.append(None)
        x = set(list_1)
        a = 0
        b = 0
        for number in x:
            if number == sorted_list[sorted_list.index(number)+1]:
                b += 1
            else:
                a +=1
        return(a, b)
    print(doing_stuff_with_list([1, 2, 3, 4, 4, 3]))


# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". 
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, 
# until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described

def problem_8():
    def map_the_dictionary(mapping):
        result = []
        first = mapping["start"]
        if first != "start":
            result.append(first)
        second = ""
        while second != mapping[first]:
            second = mapping[first]
            result.append(second)
            first = second
            print(result)
        return result
    print(map_the_dictionary({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
problem_8()