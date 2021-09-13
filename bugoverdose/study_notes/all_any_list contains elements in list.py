List1 = ['python' ,  'javascript', 'csharp', 'go', 'c', 'c++']
List2 = ['csharp1' , 'go', 'python']

check =  all(item in List1 for item in List2)
 
if check is True:
    print("The list {} contains all elements of the list {}".format(List1, List2))    
else :
    print("No, List1 doesn't have all elements of the List2.")

# The list ['python', 'javascript', 'csharp', 'go', 'c', 'c++'] contains all elements of the list ['csharp', 'go', 'python']

# ==============================================
List1 = ['python' ,  'javascript', 'csharp', 'go', 'c', 'c++']
List2 = ['swift' , 'php', 'python']

check =  any(item in List1 for item in List2)
 
if check is True:
    print("The list {} contains some elements of the list {}".format(List1, List2))    
else :
    print("No, List1 doesn't have any elements of the List2.")

# The list ['python', 'javascript', 'csharp', 'go', 'c', 'c++'] contains some elements of the list ['swift', 'php', 'python']

# ==============================================