list_of_docs=[{'name':'John','age':30},{'name':'Jane','age':25},
              {'name':'Bob','age':35}]
sorted_list=sorted(list_of_docs,key=lambda x:x['age'])
print("Sorted list of dictionaries:", sorted_list)