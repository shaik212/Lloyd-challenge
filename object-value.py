from functools import reduce

#Take the key input from user and stores it in a variable k
k = input("Enter the keys: ")

#Function is defined to take object and keys as input
def deep_get(dictionary,keys, default=None ):

    #Reduce and lambda to check the key value and return the output
    a = reduce(lambda z, key: z.get(key, default) if isinstance(z, dict) else default, keys.split("/"), dictionary)

    #If Condition to make sure there is no output in partial correct key is passed
    if isinstance(a, str):
        return a
    else:
        return None


object = {'a':{'b':{'c':'d'}}}

#Call the function and pass the values in it, print the return output
print (deep_get(object, k))
