# Type casting is done by the programer!
# which is used to change the type of an variable --- int(), float(), str();


# Bydefault all the input statements considered into Strings
age = input("Enter age: ");
print(age, type(age)) #Expected O/P ----> 20 int, but it gives ---- 20 str

#So that we use type casting;

Age = input("Enter the age");
Age = int(Age);
print(Age, type(Age)) # O/P -----> 20 int

