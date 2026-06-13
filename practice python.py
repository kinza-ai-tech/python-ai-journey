#variable
name= "kinza."
age=21
city="lahore."
print("my name is" ,name)
print("i am ",age, "years old.")
print("i live in ",city)
print(" 🌸My Portfolio🌸 " )
print("Hi my name is", name,"\nI am ",age, "years old.","\nI live in ",city,  )

#if/else 
     
marks=40
if marks >=80:
    print("Grade A")
elif marks >=70:
    print("Grade B")
elif marks >=60:
    print("Grade C")
else:
    print("Fail")        
#loops
for i in range(1,11):
    print(i)
for i in range(1,11):
    if i%2==0:
        print(i, "is even")

#list

fruits=["banana","apple","mango","cherry"]
for fruit in fruits:
    print(fruit)
fruits.append("grapes")
print(fruits)

for fruit in fruits:
    if len(fruit)>5:
       print(fruit)

#functions

def add_number(a,b):
    result=a+b
    print(result)
def great_person(name):
    print("Hello",name, "! welcome.")
answer=add_number(10,20)
print(answer)             
great_person("ahmad")
great_person("ali")

#dictionary

student={
    "name":"kinza",
    "age":21,
    "cgpa":3.4,
    "city":"lahore"

}
print(student["name"])
print(student["cgpa"])

student["universty"]="comsats"
student["skin colour"]="fair"
print(student)

#function with real logic
def calculate_grade





