what does a software engineer do?

software engineer design and create applicatins to solve the real world problems
software developers
two categories
Front-end developer, Back-end developer,
Front end:HTML, css, bootstrap, javascript, angular, react etc..
Backend: python, django, drf, database

How to become a software engineer?
You can build new skills
Learn --> practice --> attending the interview --> get job.
what are the prerequisites?
must have any degree
decide the skills
must have desktop/laptop
managable english communication
zeal to learn and have to interest

why learn from me?
i will make you understand better
i am taking less fee
installment
i will give guidance
i will motivate the students

Python Introduction:
---------------------
Python is a general purpose high level programming language.

python was developed by Guido van rossam in 1989 while working at national research inst. at netherlands

but officially python was made available to public 1991
D.O.B: Feb 20th 1991

Free and open-source - you can freely use and distribute python. even for commercical use

Easy to learn - python has a very simple synatx.

portable - You can move python programs from one platform to another and run it without any changes

python is recommended as first programming language for beginners.

why learn python?
-----------------
Python is easy to learn, its syntax is easy and code is very readable
python has a lot of applications, it is used for developing, web, desktop, data science, ai, gaming, networking etc..

python allows you to write programms in fewer lines of code than most of the programming languages.

python popularity is growing rapidly.

To print Hello world

Java
----
public class HelloWorld
{
	public static void main(string[] args)
	{
	system.out.println("Hello world");
	}
}

C:
----
#include<stdio.h>
void main()
{
	print("Hello world");
}

python:
-------
print("Hello World")

Getting Started:
-----------------
https://www.python.org/downloads/

download the source file and install

cmd promt

python --version

IDLE(Integrated development learning environment)

vs code
pycharm
atom
eclipse

The name python was selected from the tv show

"The complete montty python's circus" which was broadcasted in bbc channel from 1969 to 1974.


Guido developed python language by taking alomost all programming features form different languages

1. Functional programming features from C
2. Object oriented programming features from C++
3.scripting features from perl and shell script

where we can use python?
-------------------------
1.For developing desktop applications
2.web applications
3.database applications
4.networking prgram
5.developing games
6.data analaysis
7.machine learning
8.AI
9.IOT
etc...

Note:

Internally Google and Youtube use python coding
NASA and NSE applications by python
Top software comapniess like google, microsoft, ibm, yahoo. using python

Identifiers:
-------------
A name in python programme is called identifier

a=100
x='yogi'
d=10.5

def testfunc():
    pass

def 1test():  // not valid identifier
    pass

class Student:
     pass

It can be class name or function name or module name or a variable name

Rules to define identifier in python:
--------------------------------------
1. The only allowed characters in python are:
    ->alphabet symbols(lower/upper)
    ->digits(0-9)
    -> underscore symbol(_)

    cash = 100
    ca$h = 200 (X)
    ca_h = 300
2. Identifier should not start with digit

    123total (X)
    total123

3. Identifiers are case sensitive, bcz python is case sensitive.

  a=100
  print(a)
  print(A) (X)

  _total = 100
  if identifier is starts with underscore then it indicates it is private

4. we can not use reserved words as identifier

   def = 200 (X)
   class =300 (X)

5 There is no length limit for identifier but not recommended use lengthy identifiers.

   a=100
   dfsdhfsdgfgfgfdlfhasdlfsf = 100

java2share  #valid
ca^p        #not valid
_abc_abc_   #valid
def         #not valid
if          #not valid
else        #not valid
1ten        #not valid

Reserved words:
---------------
python has a set of keywords that are reserved words that can not be used as variable names,
function names, or any other identifiers

[
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'async',
    'await',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield'
]

Note: Except 3 reserved words all contains lower alphabets
True, False, None

Data Types:
-----------
a=1000
Data type represent the type of data present inside a variable

In python we are not required to specify the type explicitly

int a = 1000
float b = 10.5

based on the value provided the type will be assigned automatically.
Hence python is Dynamically typed language.

a=1000
b=10.5
c='yogi'
d=True

**Every data type in python is internally implemented as a class

Data types are categarized into different ways:
 1. fundamental data types
 2. Collection data types

 Fundamental data types:
 ------------------------
 Fundamental data types reprasented classes/objects are storing only one value.

object means memory location
 a=100

 eg: int, float, complex, bool, str

 Collection data types:
 ----------------------
 collection type represented classes/objects are stored in group of elements these objects
 are iterable objects

a=10,20,30

every collection type class provides methods to perform operations on elements of those objects.

Eg: list, tuple, set, dict

python contains several inbuilt functions

1.type() --> to check the type of variable
2.id()  --> to get address of object
3.print() --> to print the value

int data type:
--------------
we can use int data type to represent whole numbers(integral values)
eg:
   a = 10
   type(a) ==> <class int>

float data type:
---------------
we can use int data type to represent floating point values(decimal values)
eg:
   f=1.3445
   type(f)  ==> <class float>

complex data type:
------------------
a+bj

a --> real part, b--> imaginary part

3+5j, 10+5.5j, 0.5+0.1j

bool data type:
---------------
we can use int data type to represent boolean values
allowed values are True and False

str type:
---------
A string is sequance of characters enclosed within single quotes or double quotes
s1='yogi' s1="yogi"

Immutable and mutable objects
-----------------------------
Immutable objects:
------------------
The objects which doesn't allow to modify the contents of those objects are known as
Immutable objects


a=10
b=10
c=10

before creating Immutable objects with some content python intrepretor verifies is already
any object is available in memory location with same content or not

if already object is present in memory location with the same content without creating a new
object already existing object address will be given to the reference variable

* all the fundamental data types and tuple are the Immutable objects

* Immutable objects performance is high

* applying iterations on Immutable objects takes less time

mutable objects:
----------------
The objects which allows to modify the content of those objects are known as mutable objects

we can create two different mutable objects with the same content

l=[10,20,30]
x=[10,20,30]
* list, set, dict are the mutable objects
* mutable objects performance is low when compare to Immutable objects
* applying iterations on mutable objects tekes huge time

string Handling:
----------------
Group of characters or sequance of characters is known as string

strings stored in str class object

str class objects can be created in two ways

1.single quotes ' '   or " "
2.triple quotes ''' '''  or """ """

a='yogi' or "yogi"
b='''yogi''' or """yogi"""

single quotes to represent one line string

triple quotes is used to represent multiple line string

every character is reprasented with unque index

it supporting both positive and negative index

positive indexing starts from 0  and negative indexing starts -1

by using the indexing we can read the data from string


iterable objects has predefined function i.e len()

iterable objects are str, list, tuple, set, dict

len() is a builtin function is used to count the number of characters

Reading the data from keyboard:
-------------------------------
we can read the data from the keyboard by calling input() function

input function is predefined function which reads the data in the form of string format only.

Type casting / type conversion:
===============================
int, float, bool, complex, str

input() function reads in the str form

int(a)

float(a)

bool(a)

complex(a)

git:
=====

pushing the code to git repository:
-----------------------------------
--------First Time push the code from New Folder--------
-> open git bash here in new folder
-> git init
-> git add .
-> git commit -m "first commit"
-> git remote add origin '<git url>'
-> git push -u origin master

-----Next All Time from same folder-----
git add .
git commit -m "first commit"
git push

Pull the code from git repository:
-----------------------------------
--------First Time pull the code from git--------

git clone <git url>

-----Next All Time-----
git pull


operators:
----------
operators are the special symbols which are used to perform the operations on the data of the
objects which are pointed by the operands

a=10
b=20

special symbols + , - etc..

python supports fallowing types of operators:

Arthimetic operators
comparision operators
logical (boolean) operators
Bitwise operators
Assignment operators
special operators

Arthimetic operators:
----------------------
Arthimetic operators are used to perform the mathematical operations like
addition, subtaction, multiplication, division, floor division, modulus and exponential

x=15
y=4

comparision operators:
---------------------
comparision operators are used to compare the data of the objects which are pointed by the operands

eg: > , < , ==, !=, >=, <=
x=10
y=12

logical (boolean) operators:
----------------------------
logical operators are used to perform the mathematical logical operations

logical operators are: and , or, not

x=True
y=False

Bitwise operators:
------------------
Bitwise operators converts the data in the form of binary format and performs the operations
on the binary data
bitwise operator gives the results in the form of decimal format

bitwise operators are : & , | , ^ , ~ , >> , <<

x=10
y=4

