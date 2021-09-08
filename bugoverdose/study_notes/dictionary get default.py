# get() method takes maximum of two parameters:
dict.get(key, value) 
# key - key to be searched in the dictionary
# value (optional) - Value to be returned if the key is not found. The default value is None.

# ==================================================================
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
# Name:  Phill

print('Age: ', person.get('age'))
# Age:  22

# no default value => None when key is not found
print('Salary: ', person.get('salary'))
# Salary:  None

# default value => return the value when key is not found
print('Salary: ', person.get('salary', 0.0))
# Salary:  0.0

# ==================================================================