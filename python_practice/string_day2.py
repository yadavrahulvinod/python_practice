Name = "Radha Krishna"
print(Name[1]) #string can be indexed too
print(Name.upper())
print(Name)
print(Name.lower())
print(Name.find("k"))
print(Name.find("K"))
print(Name.find("Kris"))
print(Name.replace(" ",""))

print(dir(Name)) 
'''
[' __add__ ', ' __class__ ', ' __contains__ ', ' __delattr__ ', ' __dir__ ', ' __doc__ ', ' __eq__ ', ' __format__ ', ' __ge__ ', 
' __getattribute__ ', ' __getitem__ ', ' __getnewargs__ ', ' __getstate__ ', ' __gt__ ', ' __hash__ ', ' __init__ ', ' __init_subclass__ ',
 ' __iter__ ', ' __le__ ', ' __len__ ', ' __lt__ ', ' __mod__ ', ' __mul__ ', ' __ne__ ', ' __new__ ', ' __reduce__ ', ' __reduce_ex__ ', 
 ' __repr__ ', ' __rmod__ ', ' __rmul__ ', ' __setattr__ ', ' __sizeof__ ', ' __str__ ', ' __subclasshook__ ', ' capitalize ', ' casefold ', 
 ' center ', ' count ', ' encode ', ' endswith ', ' expandtabs ', ' find ', ' format ', ' format_map ', ' index ', ' isalnum ', ' isalpha ', 
 ' isascii ', ' isdecimal ', ' isdigit ', ' isidentifier ', ' islower ', ' isnumeric ', ' isprintable ', ' isspace ', ' istitle ', ' isupper ',
'join ', ' ljust ', ' lower ', ' lstrip ', ' maketrans ', ' partition ', ' removeprefix ', ' removesuffix ', ' replace ', ' rfind ', ' rindex ',
 ' rjust ', ' rpartition ', ' rsplit ', ' rstrip ', ' split ', ' splitlines ', ' startswith ', ' strip ', ' swapcase ', ' title ', ' translate ', 
 ' upper ', ' zfill ']'''

firstname= "rahul"
middlename ="vinod"
lastname="yadav"
#formatated concatination in string

print("--------"*19)
print(f"hello data engineer {firstname} {middlename} {lastname} aka DE")
print("--------"*19)
print(Name.endswith("a")) 



# multi-line comment is a string in it self if we assign it to someting and if not then its a comment

"""
hello multiline string
""" 

multiline_string = """
 hello multiline
 string
"""

print(multiline_string)

#additional tips mentioned below
#\ is a escape caracter
#\n is next line string command
#\t just add tabs   

"slicing begains from here"

stest = "iot master sheet"
   #start index : ending index : step size
print(stest[11  :      16      :     2]) # o/p : sheet
print(stest[8:])
print(stest[:8])
print(stest[:])
print(stest[-5:])
print(stest[-8:len(stest)])
print(stest[-5:-1])
index = stest.find(" ")+1
print(stest[index:len(stest)])

print(stest[::-1]) # to reverse a string 
print(stest.index("e"))
print(stest.capitalize())
print(stest.split("a"))
print(stest.strip()) #it removes left sides spaces and right side spaces only not inbetween the string

print(stest.replace(" ","_")) # this replace all the occurace of a specific caracter passed init

ex="1,2013-07-25 00:00:00.0,11599,CLOSED "

new = ex.split(",")# it takes a string and returns a list and splits the entire string by as that character occurance is found
print(new[3].strip())# o/p : CLOSED











