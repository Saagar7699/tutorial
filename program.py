# class whatsapp:
#     contacts = {}
#     def __init__(self):
#         while True:
#             print("1.Add contacts", "2.For chat","3.For display_msgs",
#                   "4.For clear_chat", "5.For exit",sep = '\n')
#             choice == input("enter the choice:")
#             if choice == '1':
#                 self.add_contacts()
#             elif choice == '2':
#                 self.chat()
#             elif choice == '3':
#                 self.display()
#             elif choice == '4':
#                 self.clear
#             elif choice == '5':
#                 print("Exit")
#     def chat(self,data = None):
#         if data == None:
#             data = self.contacts
#         name = input("Enter the name :")
#         if name in data:
#             while True:
#                 msg = input("Enter the msg :")
#                 data[name].append(msg)
#                 print("enter 1 for another 2 for stop...")
#                 choice = input("Enter the choice :")
#                 if choice == '2':
#                     break
#     def display(self,data = None):
#         if data == None:
#             data = self.contacts
#         name = input("Enter the name :").lower()
#         if name in data:
#             print(data[name])
#     def clear_msg(self,data = None):
#         if data == None:
#             data = self.contacts
#         name = input("Enter the name :")
#         if name in data:
#             data[name].clear()
#     @classmethod
#     def add_contacts(cls,data = None):
#         if data == None:
#             data = cls.contacts
#         name = input("Enter the name :")
#         if name not in data:
#             data[name] = []
#             print("Contacts Saved Successfully...!!")
#         else:
#             print("Already name is exist..")
# class Insta(whatsapp):
#     friends = {}
#     def __init__(self):
#         while True:
#             print("1.Send friend request", "2.For chat", 
#                   "3.For display_msgs", "4.For clear_chat", "5.For exit", sep = '\n')
#             choice = input("Enter the choice :")
#             if choice == '1':
#                 self.friend_request()
#             elif choice == '2':
#                 self.chat()
#             elif choice == '3':
#                 self.display()
#             elif choice == '4':
#                 self.clear_msg()
#             elif choice == '5':
#                 print("Exit..")
#                 break
#     def chat(self):
#         super().chat(self.friends)
#     def display(self):
#         super().display(self.friends)
#     def clear_msg(self):
#         super().clear_msg(self.friends)
#     @classmethod
#     def friend_request(cls):
#         super().add_contacts(cls.friends)
# a = Insta()
                
################## Hybrid Inheritance #######################


class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(B,C):
    pass
print(D.mro()) # Cannot create a consistent method resolution


class Sample:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        out = []
        if len(self.a) < len(other.a):
            x = self.a
            y = other.a
        else:
            x = other.a       
            y = self.a
        i = 0
        while i<len(x):
            out.append(self.a[i] + other.a[i])
            i+=1
        c = y[i:]
        return out + c
o1 = Sample([1,2,3])
o2 = Sample([4,5,6,7,8,9])
print(o1 + o2)

class Sample:
    def __init__(self,a):
        self.a = a
    def __sub__(self,other):
        x = self.a
        y = other.a
        out = ''
        for i in x:
            if i not in y:
                out += i
            else:
                if x.count(i) > y.count(i):
                    z = x.count(i) - y.count(i)
                    for k in range(x.count(j)-1):
                        out += i
        for j in y:
            if j not in x:
                out += j
            else:
                if y.count(j) > x.count(j):
                    z = y.count(i) - x.count(i)
                    for k in range(z):
                        out += i
        return out          
o1 = Sample(["hailooo"])
o2 = Sample(["hello"])
print(o1 - o2) 


class Demo(tuple):
    def __init__(self,a):
        self.a = a
    def __mul__(self,other):
        if type(other) != int:
            return "2nd operand should be int"
        out = ()
        for i in self.a:
            out += (i*other,)   
        return out            
o1 = Demo((1,2,3))
o2 = Demo((4,5,6))
print(o1 * 2)
print(o1*o2)



class Demo:
    def __init__(self,a):
        self.a = a
    def __sub__(self,other):
        x = self.a
        y = other.a
        out = ""
        for i in x:
            if i not in y:
                out+=i
            else:
                if x.count(i) > y.count(i) and out.count(i) < y.count(i):
                    out += i
        for j in y:
            if j not in x:
                out += j
            else:
                if y.count(j) > x.count(j) and out.count(j) < x.count(j):
                    out += j
        return out
o1 = Demo("hailoooo")
o2 = Demo("helloooooo")
print(o1-o2)


class A(complex):
    def __init__(self,x):
        self.x = x
        
    def __add__(self,other):
        return self.x + other.x   
o1 = A(4)
o2 = A(5)
o3 = A(7)
print(o1+o2+o3)


class A(int):
    def __init__(self,x):
        self.x = x
        
    def __add__(self,other):
        return self.x + other.x   
o1 = A(27)
o2 = A(34)
o3 = A(56)
print(o1+o2+o3)


class A(float):
    def __init__(self,x):
        self.x = x     
    def __add__(self,other):
        return self.x + other.x
o1 = A(4.0)
o2 = A(5.5)
o3 = A(7.8)
print(o1+o2+o3)


class A(str):
    def __init__(self,x):
        self.x = x
       
o1 = A("\nHello..!")   
o2 = A("\nPrasanna..") 
o3 = A("\nHow are you...?")
print(o1,o2,o3)


class Demo:
    a = 10
    def method(self):
        print("In demo class")
class Sample:
    obj = Demo()
s = Sample()
print(s.obj.a)
s.obj.method()


