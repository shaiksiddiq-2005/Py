# Strings and it's methods 
# In python the strings are IMMUTABLE

# NOTE Methods won't modifies the original string, they a new strings


name = "Shaik siddiq";
age = 20;

# .upper()
# It converts the entire string into upperCase
print(name.upper()); #SHAIK SIDDIQ
print(name); # Shaik siddiq ----------> It won't update the original string.


# .lower()
# It converts the entire string into lowerCase
print(name.lower());


# .find(string)
# It returns the index of the find(string)
print(name.find("siddiq"));  # ----> 6, because siddiq starts from 6th index
print(name.find("i")); # -------> 3, because i found at 3rd index


#.replace("string","string")
# It replace the string with another string
print(name.replace("q", "kkkkkkk")); # ------->Shaik siddikkkkkk
print(name.replace("Shaik", "Abubakar")) #-----> Abubakar siddiq
print(name.replace("z", "abubakar")); # -------> Shaik siddiq (z not found, so same text will be displayed)


# Presence(in)
# it takes a value and checks whethere avaiable in the given string and returns an output in Boolean
print("S" in name ); #  -----> True
print("z" in name); #   ------> False (z is not available in name)
print("siddiw" in name); #  ------> false ( siddiw is not available in name-- Shaik siddiq)




# Test
item1 = int(input("Enter the price of item1: "));
item2 = int(input("Enter the price of item2: "));
item3 = int(input("Enter the price of item3: "));

billAmount = item1 + item2 + item3;
print("Total Bill Amount is :", billAmount);

avgPrice = billAmount/3;
print("Average Price of items:", avgPrice);


#Test

superHero = input("Enter superHero Name: ");
startsWith_s = superHero.lower();
print(startsWith_s)

print ( "s" in startsWith_s);