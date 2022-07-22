'''
info = {
    "name" : "Mahesh",
    "address" : "Belauri",
    "contact_no" : 9806437128,
    "is_good" : True
}
info['faculty'] = "BCA"
info["is_good"] = False
print(info.get('birthdate')) # removes the keyError if key is not present in the dictionary
print(info.get('birthdate', 'Magh 15 2057'))
print(info)
'''

# Exercise---------------------------
user_input = input("Phone: ")
dictionary = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output =""
for ch in user_input:
    output += dictionary.get(ch, "!") + " "
print(output)
