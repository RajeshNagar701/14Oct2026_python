"""
Python Variables

A variable can have a short name (like x and y) or a more descriptive 
name (age, carname, total_volume).


=> There 3 way to assign value

1)site_name = 'programiz.pro'       // single value
2)a, b, c =  5, 3.2, 'Hello'        // multiple values
3)site1 = site2  = 'programiz.com'  // same value in 2 variables


=====================================================

Rules for Naming Python Variables a-z 0-9 _

Names should have a combination of letters in lowercase (a to z) 
or uppercase (A to Z) or digits (0 to 9) or an underscore (_)
Python is case-sensitive. So num and Num are different variables

Legal variable names:

    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"


Illegal variable names:

    2myvar = "John"
    my-var = "John"
    my var = "John"
    
==========================================================================  

Multi Words Variable Names

myVariableName = "John"   # Camel Case     smallCaps 
MyVariableName = "John"   # Pascal Case    starts with a capital letter:
my_variable_name = "John" # Snake Case     underscore character:

=========================================================================

Many Values to Multiple Variables

    x, y, z = "Orange", "Banana", "Cherry"
    
One Value to Multiple Variables
    
    x = y = z = "Orange"


Unpack a Collection

    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)

========================================================================


In the print() function, you output multiple variables, separated by a comma:
You can also use the + operator to output multiple variables:

    x = "Python"
    y = "is"
    z = "awesome"
    print(x, y, z)
    print(x + y + z)

===========================================================


   types of variable
   1) Primitives 
        int     5 -5 0
        float   10.5
        char    'A'
        string  "HELLO"
        boolean true / false
        
   2) Non Primitives / collection

    list   [5,6,"hello"]
    tuple  (5,6,"hello")
    set    {5,6, "hello"}
    disc   { id:1, name:"raj", age:35, mobile:"12365478" }
    


Python Literals
    
1)Python Numeric Literals  : Integer, Float, and Complex
    
    Integer Literals : 5, -11, 0, 12
    Floating-Point : 2.5, 6.76, 0.0, -9.45
    Complex Literals : 6+9j, 2+3j
    

2)Python String Literals

    "This is a string."

3)Python Boolean Literals

    is_pass = True :     True and False

4)Character Literals in Python

    some_character = 'S'


5)Special Literal in Python

    value = None
    
============================================================    

Collection Literals

    # list literal
    fruits = ["apple", "mango", "orange"] 
    print(fruits)

    # tuple literal
    numbers = (1, 2, 3)  / 1,2,3
    print(numbers)

    # set literal
    vowels = {'a', 'e', 'i' , 'o', 'u'} 
    print(vowels)

    # dictionary literal
    alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
    print(alphabets)


"""






