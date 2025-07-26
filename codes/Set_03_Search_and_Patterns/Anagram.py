def is_anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)
string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
if is_anagram(string1,string2):
    print("Anagrams")
else:
    print("Not Anagrams")