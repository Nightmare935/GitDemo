x = " its ,me, himanshu kaushik !!!!"

print(x.upper())
print(x.lower())
# to remove a white space we use strip function 
print(x.strip())
#to replace a letter with other we use replace function
print(x.replace('i','h'))
#split method is returns a list of items that are saperated bs a specified separator
print(x.split(','))

age = "36"
txt = "my name is himanshu kaushik , I am "+ age

print(txt)
#if the age is of integer type so it canot be concatinate like that 

# F-string
age1 = 36
text = f"i am Himanshu , i am {age1}"#these {} are known as placeholders which can be used to store variables functions and modifier

print(text)

#add a placeholder for the price variable
price = 90
statement = f"The price of the product is {price}"
print(statement)

#we can also use operators in the placeholder
# Enter the indian amount and it will gices you to its eauevalent dollar value

rupees = 100
value = f"The conversion in dollar is equal to {83 * rupees}"

print(value)