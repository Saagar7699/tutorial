print(10)

print("PRASANNA")

name1 = "qspiders"
result1 = name1.upper()
print(result1)

name2 = "PRASANNA"
result2 = name2.lower()
print(result2)

name3 = "pAvI"
result3 = name3.swapcase()
print(result3)

sentence1 = 'hello how are YOU'
result4 = sentence1.capitalize()
print(result4)

movie1 = "hum AApke haIN KAun"
result5 = movie1.title()
print(result5)

dialogue = "dont trouble the trouble"
result6 = dialogue.split()
print(result6)

dialogue = "mokke kadha ani peekesthe peeka kostha"
res7 = dialogue.split()
print(res7)

movie2 = "BAHUBALI PART 1"
result7 = movie2.isupper()
print(result7)

movie3 = "Majili"
result8 = movie3.islower()
print(result8)

movie4 = "auto nagar surya"
result9 = movie4.isalpha()
print(result9)

mov = "yemayachesave"
res10 = mov.isalpha()
print(res10)

movie5 = "100"
result10 = movie5.isnumeric()
print(result10)

movie6 = "bahubalipart2"
result11 = movie6.isalnum()
print(result11)

sentence2 = "java is an excellent language"
result12 = sentence2.replace("java","python")
print(result12)

sentence3 = "she sells sea shells on the sea shore"
result13 = sentence3.find("crab")
print(result13)

sentence4 = "sea the moon"
result14 = sentence4.find("sea")
print(result14)

message = "hii prasanna"
part = message[2:7]
print(part)

memes = "arey entra ila vunnaru"
index = memes[3:10:1]
print(index)

sample = "hii everyone , how are you"
output = sample[3:-18:2]
print(output)

sentence5 = "darsha is a good boy,he is very cute and he is my small son"
# result15 = sentence.index=[10:20:1]
# print(result15)

string = "don't trouble the trouble if you trouble the trouble, trouble troubles you i'm not the trouble i'm the truth"
print(string[-30:50:3])


#######  TOPIC : LIST[]  #######-------

cars = ["porsche","thar","audi","jaguar"]
print(cars[-1])

cars.append("royal")
print(cars)

copy_of_cars = cars.copy()
print(copy_of_cars)

copy_of_cars.clear()
print(copy_of_cars)
print(bool(copy_of_cars))

colors = ["blue","white","yellow","green",'black',"black","black","pink"]
res1 = colors.count("blue")
print(res1)

res2 = colors.count("black")
print(res2)

fruits = ["orange","grapes","mango","watermelon","jackfruit"]
fruits.insert(-1,"apple")
print(fruits)

fruits.remove("watermelon")
print(fruits)

res3 = fruits.pop()
print(res3)
print(fruits)

res4 = fruits.pop(0)
print(res4)
print(fruits)

companies = ["google","microsoft","ibm","infosys"]
extra_elements = ["tcs","wipro","oracle","mondelez"]

companies.extend(extra_elements)
print(companies)

movies = ["majili","josh","100%love","premam","thandel","manam"]
movies.insert(-2,"venkymama")
print(movies)

movies.remove("100%love")
print(movies)

movies.remove("josh")
print(movies)

countries = {"india","USA","maldives","srilanka","jammu kashmir","india"}
print(countries)

countries.add("germany")
print(countries)

copy_of_countries = countries.copy()
print(copy_of_countries)

copy_of_countries.clear()
print(copy_of_countries)

birds = {"pigeon","peacock","sparrow","parrot","crow"}
birds.remove("crow")
print(birds)

birds.add("hen")
print(birds)

birds.discard("duck")
print(birds)

languages = {"telugu","hindi","english","kannada","tamil"}
print(languages)

languages.add("urdu")
print(languages)

copy_of_languages = languages.copy()
print(languages)

languages.remove("kannada")
print(languages)

set1 = {1,2,3,4,5,6}
set2 = {4,5,7,8,9}
result15 = set1.union(set2)
print(result15)
print(set1)

result16 = set1.intersection(set2)
print(result16)

result17 = set1.difference(set2)
print(result17)

result18 = set1.difference(set2)
print(result18)

result19 = set1.symmetric_difference(set2)
print(result19)

set1.update(set2)
print(set1)

set1.intersection_update(set2)
print(set1)

set1.difference_update(set2)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)

####################control statements###################




#if score >= 90 :
 #   print ("your gift is MOBILE....Congratulations")
#elif score > 80 :
  #  print("your gift is cycle....")
#elif score > 70 :
  #  print("your gift is watch....")
#elif score > 60 :
 #   print ("your gift is books....go study well....")
#elif score > 50 :
  #  print("your gift is belt....")
#else :
   # print ("Shut up your mouth...go and sit study....")

    #################### - While Loop- #########################

# n = int(input())
# for i in range(n) :
#     for j in range(n):
#         if i == 0 or j == 0 or j == n-1 or i==n//2 :
#            print("*",end = ' ')
#         else :
#            print(" ",end = ' ')
#     print()


# for i in range(5) :
#   for j in range(5) :
#     if j==0 or i==o or i==2 or j==4 and (i==1 or i==2) :
#       print('*',end='')
#     else :
#       print(' ',end= ' ')
#   print()


#n=5
#for i in range(n):
 # for j in range(i+1):
  #  print('*',end=' ')
  #else:
   # print(' ',end=' ')
  #print()

#n = 5
#for i in range(n):
 # for j in range(i-1):
  #  print('*',end=' ')
  #else:
   # print(' ',end=' ')
  #print()


#for row in range(n):
 # for column in range(n):
  #  if row >= column:
   #   print("*", end = " ")
    #else:
     # print(" ", end = " ")
  #print()
  
 ######################-------- if else statements -------####################### 
 
#n = int(input("enter the data:"))
#if n%2==0:
 # print(n**2)
#else:
 # print(n**3)

n = int(input("enter the number:"))
if 0<=n<=9:
 print("It is a number")
else:
 print("It's not a number")
  
 
#char = input("enter the char:")
#if not ('A'<=char<='Z' or 'a'<=char<='Z' or '0'<=char<='9'):
#if char.isalnum()==False:
 # print(f"{char} it is Special Character")
#else:
 # print(f"{char} Not a special character")
  
#n = eval(input("enter the data:"))
#if bool(n)==False:
 # print(f"{n} It is Default Value")
#else:
 # print(f"{n} not Default value")


#a = input("enter the str:")
#import keyword
#b = keyword.kwlist
#if a in b:
 # print("It is Keyword")
#else:
  #print("Not a keyword")
  
  
#n = eval(input("enter the data:"))
#if type(n) in [list,set,dict]:
 # print("It is mutable")
#else:
 # print("It is immutable")
 

#og_location1 = "Bangalore"
#og_location2 = "kadapa"
#location1 = input("enter the location1:")
#location2 = input("enter the location2:")
#if location1==og_location1:
  #if location2==og_location2:
   # print("Invalid Details")
  #else:
 #   print("Register")
#else:
#  print("login")

# n = int(input("enter the value:"))
# if n%2==0:
#   if n%15==0:
#     print(f'{n} is even and multiple of 15')
#   else:
#     print(f"{n} is multiple of 15 but not even")
# else:
#   print(f"{n} is not even")
  
# og_username = "prasanna"
# og_password = "prasa@2025"
# username = input("enter the username:")
# password = input("enter the password:")
# if username == og_username:
#   if username == og_password:
#     print("Invalid Password")
#   else:
#     print("Login")
# else:
#   print("Invalid username")  
  
# s = input("enter the str:")
# out = ''
# i = -1
# while i>=-len(s):
#   out = out + s[i]
#   i-=1
# print(out)

# s = input("enter the str:")
# i = 0
# out = ''
# while i<len(s):
#   if 'A'<=s[i]<='Z':
#     out = out + s[i]
#   i+=1
# print(out)

# l = eval(input("enter the list:"))
# out = []
# i = 0
# while i<len(l):
#   if type(l[i])==int:
#     #out.append(l[i])
#     out = out + [l[i]]
#   i+=1
# print(out)

# l = eval(input("enter the list:"))
# out = []
# i = 0
# while i<len(l):
#   if type(l[i]) in [int,bool,complex,float]:
#     out.append(l[i])
#     out = out + [l[i]]
#   i = i+1
#   i+=1 
# print(out)

# t = eval(input("enter the tuple:"))
# out = ()
# i = 0
# while i<len(t):
#   if type(t[i]) == complex:
#     out = out + (t[i],)
#   i+=1
# print(out)

# l = eval(input("enter the list:"))
# out = []
# i = 0
# while i<len(l):
#   if type(l[i]) == str and l[i] == l[i][::-1]:
#     out.append(l[i])
#   i+=1
# print(out)

# n = input("enter the str:")
# u,l,num,spe = '','','',''
# i = 0
# while i<len(n):
#   if 'A'<=n[i]<='Z':
#     u+=n[i]
#   elif 'a'<=n[i]<='z':
#     l+=n[i]
#   elif '0'<=n[i]<='9':
#     num+=n[i]
#   else:
#     spe+=n[i]
#   i+=1
# print(u,l,num,spe,sep='/n',end ='')

####################### for loop programms #########################

for i in 'python':
  print(i)
  
for i in [1,2,3]:
  print(i)
  
for i in {45,56,89}:
  print(i)
  
for i in {1:2,3:4,5:6}:
  print(i)
  
for i in {1:2,3:4,5:6}.values():
  print(i)
  
for i in {1:2,3:4,5:6}.items():
  print(i)
  
n = [12,3.6,'hai',[0],{4,5},{1:2},3+4j,(3,5)]
out = []
for i in n:
  if type(i) in [str,list,tuple,set,dict]:
    out.append(i)
print(out)

n = [25,56,'hello',[5,6,8],(5,8),3+8j,(58,96),'hello']
out = []
for i in n:
  if type(i) in [str,list,tuple,set,dict]:
    out.append(i)
print(out)

# n = eval(input("enter the collection:"))
# count = 0
# for i in n:
#   out+=1
# print(count)  #wrong

# for i in range(65,91):
#   print(chr(i),end=' ')
  
# for i in range(97,122):
#   print(chr(i),end=' ')
  
# n = {1,45,56,85,86,35,84,26}
# out = set()
# for i in n:
#   if type(i)==int and i%2==0:
#     out.add(i)
# print(out)

# n = [5,8,9,10,15]
# out = 0
# for i in n:
#   if i>out:
#     out=i
# print(out)

# n = ['data.db','python.py','file.html','document.xml']
# out = []
# for i in n:
#   a = i.split('.')
#   out.append(a[-1])
# print(out)

# s = "python is very easy to understandable"
# a = s.split()
# out = a[0]
# for i in a:
#   if len(i) > len(out):
#     out = i
# print(out)

# l = ['hai','hello',45,'hai',56,45,[1,2],(1,45),5.0,5+3j,4+6j]
# out = []
# for i in l:
#   if i not in out:
#     out.append(i)
# print(out)

# n = eval(input("enter the dict:"))
# out = {}
# for i in n:
#   if type(i)==type(n[i]):
#     out[i]=n[i]
# print(out)

# n = eval(input("enter the dict:"))
# out = {}
# for i in n:
#   if type(n[i]) not in [list,set,dict]:
#     out[n[i]]=i
# print(out)

# a = 'aabbbccddabd'
# out = ''
# for i in a:
#   if i not in out:
#     b = a.count(i)
#     out = out + i + str(b)
# print(out)

# n = {"Amazon.com","Flipkart.gov","Whatsapp.in"}
# out = {}
# for i in n:
#   a = i.split('.')
#   out[a[-1]]=a[0]
# print(out)

# n = {"Amazon.com","Flipkart.gov","Whatsapp.in","meesho.com","myntra.in","Ajio.gov"}
# out = {}
# for i in n:
#   a = i.split('.')
#   if a[-1] not in out:
#     out[a[-1]] = [a[0]]
#   else:
#     out[a[-1]].append(a[0])
# print(out)

# i = 0
# while i <= 10:
#   if i == 7:
#     break
#   print(i)
#   i+=1

###################### Pattern matching ######################

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i+j>=n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()
  
# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i>=j:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i+j<=n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i<=j:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     print(j+1, end=" ")
#   print()
  
# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     print(i+1, end=" ")
#   print()
  
# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     print(chr(i+65), end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     print(chr(j+65), end=" ")
#   print()
  
# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i>=j:
#       print(chr(j+65), end=" ")
#   print()

#       (or)

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     print(chr(j+65), end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i):
#     print(i+0, end=" ")
#   print()

########## (or)

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i):
#     if i>=j:
#       print(i+0, end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i):
#     print(j+1, end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     print(i+1+j, end=" ")
#   print()
  
# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i+j<=n-1:
#       print(chr(i+65), end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   k=0
#   for j in range(n):
#     if i+j>=n-1:
#       print(chr(k+65), end=" ")
#       k+=1
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# k=1
# for i in range(n):
#   for j in range(i+1):
#     print(k, end=" ")
#     if k==9:
#       k=1
#     else:
#       k+=1
#   print()

# n = int(input("enter the value:"))
# k=65
# for i in range(n):
#   for j in range(i+1):
#     print(chr(k), end=" ")
#     if k==90:
#       k=65
#     else:
#       k+=1
#   print() 

# n = int(input("enter the value:"))
# for i in range(n):
#   k=1
#   for j in range(n):
#     if i+j>=n-1:
#       print(k, end=" ")
#       k+=1
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     print((i+1)*(j+1), end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     if i%2==0:
#       print(j+1, end=" ")
#     else:
#       print((j+1)**2, end=" ")
  # print()

############### Pattern Matchings On 'VOWELS' ####################

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or i==n//2 or j==n-1:
#       print("*", end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if j==0 or (i==n//2 or j<=n//2) or (i+j==n-1 and j>=n//2) or (i==j and i>=n//2):
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or i==n//2:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==n//2:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==j or j==0 or j==n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==n-1 or j==0 or j==n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or i>=n-1 or i==n//2:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or i>=n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or i>=n-1 or j==n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or j==n-1 or i==n//2:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")

#   for j in range(n):
#     if i==j or j==0 or j==n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")

#   for j in range(n):
#     if i==n-1 or j==0 or j==n-1:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

#################### Functions ######################

##### Function Without Arguments and Without Return ######
# def Add():
#   a = int(input("enter the value1:"))
#   b = int(input("enter the value2:"))
#   print(a+b)
# Add()

### fun with arg and withour return ###
# def Add(a,b):
#   print(a+b)
# Add(5,8)
# (or)
# Add(int(input("enter val1:")),int(input("enter the val2:")))

####### Fun Without arg and with return ######
# def Add():
#   a = int(input("enter the val1:"))
#   b = int(input("enter the val2:"))
#   return(a+b),a,b
# x,y,z = Add()

# def Add():
#   a = int(input("enter the val1:"))
#   b = int(input("enter the val2:"))
#   return(a+b)
# print(Add())

### Function with arg and with return ###
def Add(a,b):
  return (a+b),a,b
print(Add(5,9))

def Isupper(string):
  for i in string:
    if 'a'<=i<='z':
      return False
    else:
      return True
print(Isupper("PRASANNA@2025$"))

def extract(List):
  out = []
  for i in List:
    if type(i) in [str,list,tuple,set,dict]:
      out.append(i)
  return out
print(extract([12,3.4,3+4j,{3:4},'string',[1],(9,1)]))

def Upper(s):
  out = ''
  for i in s:
    if 'a'<=i<='z':
      out+=chr(ord(i)-32)
    else:
      out+=i
  return out
print(Upper("PrAsAnNa@2025$"))

def alno(n):
  out = ''
  for i in n:
    if not("a"<=i<="z" or "A"<=i<="Z" or "1"<=i<="9"):
      return False
    else:
      return True
print(alno("Prasanna@321"))

def lower(n):
  out = ""
  for i in n:
    if "A"<=i<="Z":
      out = chr(ord(i)+32)
    else:
      out+=i
  return out
print(lower("Python"))

def Keys(n):
  out = []
  for i in n:
    out.append(i)
  return out
print(Keys({1:2,3:4,5:6}))

def Reverse(l):
  j=-1
  for i in range(0,len(l)//2):
    l[i],l[j] = l[j],l[i]
    j-=1
  return l
print(Reverse(['hai',78,True,9+5j,15,[3,5],(3,2),'hello']))

# def homogeneous(l):
#   for i in range(l,len(l)):
#     if type(l[0])!=type(l[i]):
#       return False
#   return True
# print(homogeneous([1,5,6,8,2.6]))

def mutable(t):
  out = ()
  for i in range(len(t)):
    if type(t(i) in [list,set,dict]):
      out+=(t[i])
  return out
print(mutable(1,2,[2],{1:3},{45,73}))
  
  
############# Functions ###################

# class Bank:
#   Bank_Name = "SBI"
#   Bank_Loc = "BTM"
# C1 = Bank()
# C1.Name = "Prasanna"
# C1.Phno = 9160310454
# C1.email = "prasanna@gmail.com"
# C1.add = "Kadapa"
# C1.acc = 8456123 
# print(C1.Name,C1.Phno,C1.email,C1.add,C1.acc,sep = '\n')
# print()
# print(Bank.Bank_Name,Bank.Bank_Loc,sep='\n')
# print()
# C2 = Bank()
# C2.Name = "Pavithra"
# C2.Phno = 8160113202
# C2.email = "pavi@gmail.com"
# C2.add = "Mangalore"
# C2.acc = 845612
# print(C2.Name,C2.Phno,C2.email,C2.add,C2.acc,sep='\n')
  
##############################

# class Bank:
#   Bank_Name = "SBI"
#   Bank_loc = "BTM"
  
#   def __init__(self,Name,Phno,email,add,acc):
#     self.Cust_name = Name
#     self.Cust_phno = Phno
#     self.Cust_email = email
#     self.Cust_add = add
#     self.Cust_acc = acc
# C1 = Bank("Prasanna",9160310454,"prasanna@gmail.com","Bengaluru",45689)
# C2 = Bank("Pavi",8106113202,"pavi@gmail.com","Mangalore",859423)
# print(C1.Cust_name,C1.Cust_phno,C1.Cust_email,C1.Cust_add,C1.Cust_acc,sep = '\n')
# print()
# print(C2.Cust_name,C2.Cust_phno,C2.Cust_email,C2.Cust_add,C2.Cust_acc,sep = '\n')
# print()

###########################

# class Hospital:
#   Hospital_Name = "Appolo"
#   Hospital_Loc = "Bengaluru"
#   Hospital_Doctor_Name = "Chakravarthi"
#   Hospital_Patient_Name = "Prasanna"
#   def __init__(self,Name,phno,tokenNo,Age,Gender):
#     self.Patient_Name = Name
#     self.Patient_phno = phno
#     self.Patient_tokenNo = tokenNo
#     self.Patient_Age = Age
#     self.Patient_Gender = Gender
# P1 = Hospital("Prasanna",9160310454,101,21,"Female")
# P2 = Hospital("Pavithra",8160113202,102,23,"Female")
# P3 = Hospital("Kalpana",8156230464,103,28,"Female")
# P4 = Hospital("Bunny",5894612301,104,34,"Male")
# P5 = Hospital("Sunny",7456123459,105,39,"Male")
# print(P1.Patient_Name,P1.Patient_phno,P1.Patient_tokenNo,P1.Patient_Age,P1.Patient_Gender,sep='\n')
# print()
# print(P2.Patient_Name,P2.Patient_phno,P2.Patient_tokenNo,P2.Patient_Age,P2.Patient_Gender,sep = '\n')
# print()
# print(P3.Patient_Name,P3.Patient_phno,P3.Patient_tokenNo,P3.Patient_Age,P3.Patient_Gender,sep = '\n')
# print()
# print(P4.Patient_Name,P4.Patient_phno,P4.Patient_tokenNo,P4.Patient_Age,P4.Patient_Gender,sep = '\n')
# print()
# print(P5.Patient_Name,P5.Patient_phno,P5.Patient_tokenNo,P5.Patient_Age,P5.Patient_Gender,sep = '\n')

# #############################

# class Institute:
#   I_Name = "Qspiders"
#   Branch_Loc = "BTM"
#   def __init__(self,Name,phno,email,degree,YOP):
#     self.Name = Name
#     self.phno = phno
#     self.email = email
#     self.degree = degree
#     self.YOP = YOP
#   def disp_info(self):
#     print(f'Name:{self.Name}',f'phno:{self.phno}',f'email:{self.email}',f'degree:{self.degree}',f'YOP:{self.YOP}')
#   def up_email(self,new):
#     self.email=new
# Prasanna = Institute("Prasanna",9160310454,"prasanna@gmail.com","B.Sc",2023)
# Pavi = Institute("Pavi",8130113202,"pavi@gmail.com","B.Tech",2022)
# Prasanna.disp_info()
# Institute.disp_info(Prasanna)
# print()
# Pavi.up_email("Pavi123@gmail.com")
# Pavi.disp_info()

################################

# class Company:
#   C_Name = "Wipro"
#   C_Loc = "Bengaluru"
#   C_Headquarters = "Marthahalli"
#   def __init__(self,ename,empID,Job,sal,Loc):
#     self.ename = ename
#     self.empID = empID
#     self.Job = Job
#     self.sal = sal
#     self.Loc = Loc
#   def disp_info(self):
#     print(f'ename:{self.ename}',f'empID:{self.empID}',\
#       f'Job:{self.Job}',\
#         f'sal:{self.sal}',\
#           f'Loc:{self.Loc}',sep='\n')
#   def up_email(self,new):
#     self.email = new
#   def up_sal(self,new):
#     self.sal = new
#   def up_Job(self,new):
#     self.Job = new
#   def up_Loc(self,new):
#     self.Loc = new
    
# Pavi = Company("Pavi",54321,"Test Engineer",25000,"Bengaluru")
# Hari = Company("Hari",51432,"QA Tester",30000,"Hyderabad")
# Siva = Company("Siva",51433,"Test Lead",45000,"Vizag")
# Akhila = Company("Akhila",51434,"Business Analyst",50000,"USA")
# Venky = Company("Venky",54135,"Developer",50000,"Mumbai")
# Pavi.up_email("pavi123@gmail.com")
# Pavi.disp_info()
# print()
# Siva.up_sal("50000")
# Siva.disp_info()
# print()
# Venky.up_Loc("Chennai")
# Venky.disp_info()
# print()
# Akhila.up_Job("Automation Engineer")
# Akhila.disp_info()
# print()
# Hari.up_Loc("Delhi")
# Hari.disp_info()

##############################

# class Institute:
#   I_Name = "Qspider"
#   Branch_Loc = "BTM"
#   def __init__(self,Name,Number,email,degree,YOP,balance):
#     self.Name = Name
#     self.Number = Number
#     self.email = email
#     self.degree = degree
#     self.YOP = YOP
#     self.balance = balance
#   def disp_info(self):
#     print(f'Name:{self.Name}',f'Number:{self.Number}',f'Email:{self.email}',f'Degree:{self.degree}',f'YOP:{self.YOP}',f'Balance:{self.balance}',sep='\n')
#   def up_email(self,new):
#     self.email = new
#   def deposit(self,amt):
#     self.balance = self.add(self.balance,amt)
#   def withdrawl (self,amt):
#     if self.balance < amt:
#       print("Insufficient Balance")
#     else:
#       self.balance = self.sub(self.balance,amt)
#   @classmethod
#   def disp_class(cls):
#     print(f'Institute Name:{cls.I_Name}',f'Branch location:{cls.Branch_Loc}',sep='\n')
#   @classmethod
#   def up_loc(cls,new):
#     cls.Branch_Loc = new
#   @staticmethod
#   def add(a,b):
#     return a+b
#   @staticmethod 
#   def sub(a,b):
#     return a-b
# Prasanna = Institute('Prasanna',9160310454,'prasa@gmail.com','B.sc',2023,1000)
# Pavithra = Institute('Pavithra',8106113202,'pavi@gmail.com','B.Tech',2022,500)
# Prasanna.deposit(20000)
# print()
# Prasanna.disp_info()
# Pavithra.withdrawl(100)
# print()
# Prasanna.withdrawl(8000)
# Prasanna.disp_info()
# print()
# Pavithra.disp_info()

############################

# class Library:
#   L_Books = {'Python':10, 'sql':14, 'Web tech':4, 'selenium':7}
#   limit = 3
#   def __init__(self,sname,sid,sphno,semail,sbook=[]):
#     self.Name = sname
#     self.Id = sid
#     self.Phno = sphno
#     self.email = semail
#     self.books = sbook
#   def disp_info(self):
#     print(f'Name:{self.Name}',f'Id:{self.Id}',f'Phno:{self.phno}',f'Email:{self.email}',f'books:{self.books}',sep='\n')
#   def print(self):
#     print(self.books)
#   def issue_book(self):
#     self.display_books()
#     B_Name = input('\nenter the book name:').lower()
#     if B_Name in self.L_Books and self.L_Books[B_Name] > 0:
#       if B_Name not in self.books and len(self.books) < self.limit:
#         Library.L_Books[B_Name]-=1
#         self.books.append(B_Name)
#       else:
#         print('\nLimit exceeded\n')
#     else:
#       print(f'\n{B_Name} is not available\n') 
#   def return_book(self):
#     print('\nRETURNING BOOK\n')
#     B_Name = input('enter the book name:').lower()
#     if B_Name in self.books:
#       self.books.remove(B_Name)
#       Library.L_Books[B_Name]+=1
#     else:
#       self.print()
#       print('\nBook is not exist in your list\n')
#   @classmethod
#   def display_books(cls):
#     print('\nBooks available in library...\n')
#     for i in cls.L_Books:
#       print(f'{i} --> {cls.L_Books[i]}',sep='\n')
# s1 = Library("Prasanna",58,9160310454,"prasanna@gmail.com")
# s1.issue_book()
# s1.print()
# s1.issue_book()
# s1.print()
# s1.issue_book()
# s1.print()
# # s1.issue_book()
# s1.print()
# s1.return_book()
# s1.print()   

# #########################

# class Flipkart:
#   F_Products = {'tops'== [340,150],'Kurtis'== [850,180],'Sarees'==[1200,146],'Jeans'==[600,160],'western'== [1100,190]}
#   def __init__(self,Pname,PID,Price,cart={}):
#     self.Name = Pname
#     self.Id = PID
#     self.Price = Price
#   def disp_info(self):
#     print(f'Name:{self.Name}',f'PID:{self.PID}',f'price:{self.Price}',sep='\n')
#   def print(self):
#     print(self.products)
    
#   def Buy_Product(self):
#     print('\nBUY PRODUCT\n')
#     P_Name = input('search for the product:').lower()
#     if P_Name in self.F_Products:
#       self.books.add(P_Name)
#       Flipkart.F_Products[P_Name]+=1
#     else:
#       self.print()
#       print('\nThere are no searching products\n')
  
#   # def Bill_product(self):
#   #   print('\nBILL FOR THE PRODUCT\n')
#   #   P_Name = input('enter the bill:')
#   @classmethod
#   def display_products(cls):
#     print('\nProduct is Available...\n')
#     for i in cls.F_Products:
#       print(f'{i}--> {cls.F_Products[i]}',sep='\n')
# P1 = Flipkart('Prasanna','0DB4532189',1200)
# P1.Buy_Product()
# P1.print()
# P1.Buy_Product()
# P1.print()
# P1.Buy_Product()
# P1.print()    

































############## You Tube Pattern #################

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(n):
#     print("*", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     print("*",end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i,n):
#     print("*", end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i,n):
#     print(" ",end=" ")
#   for j in range(i+1):
#     print("*",end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     print(" ",end=" ")
#   for i in range(i,n):
#     print("*",end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i,n):
#     print("*",end=" ")
#   for j in range(i):
#     print(" ",end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n):
#   for j in range(i+1):
#     print(" ",end=" ")
#   for j in range(i,n-1):
#     print("*",end=" ")
#   print()

# n = int(input("enter the value:"))
# for i in range(n-1):
#   for j in range(i,n):
#     print(" ",end=" ")
#   for j in range(i):
#     print("*",end=" ")
  
  # for j in range(i+1):
  #   print("*",end=" ")
  # for j in range(i,n-1):
  #   print(" ",end=" ")
  # for j in range(i,n):
  #   print("*",end=" ")
  # print()

