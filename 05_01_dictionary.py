# Dictionay --> collection of key value pair
# we use {key:value} for dictionary
mydict = {
    "fast":"in a quick manner",
    "krishna":"a coder",
    "marks":[1,2,3],
    "another_dict":{"fast":"quick",
                    "krishna":"player"
    }
}

# priting dictionary
print(mydict)

# priting elements of dictionary 
print(mydict["fast"])
print(mydict["krishna"])
print(mydict["marks"])
print(mydict["another_dict"]["fast"])
print(mydict["another_dict"]["krishna"])


# properties of dictionaries
'''
1.unordered(no indexing) 
2.item assingment supported(mutable) 
3.duplicate keys not allowed
'''
# item assingment
mydict["marks"] = [45,78]
print(mydict)


# dictionary method or functions
print(mydict.keys())            # returns a dict_keys type with all keys which is like a list. we need to typecast in list to assign it to var 
print(mydict.values())          # returns a dict_values type with all values which is like a list. we need to typecast in list to assign it to var
print(mydict.items())           # returns a dict_items type with all key value pairs which is like a list. we need to typecast in list to assign it to var
print(mydict.get("krishna1"))   # do not give error prints none while print(mydict[krishna1]) give key error
# mydict.update(newdict)        # add as well as can replace old key value pair  