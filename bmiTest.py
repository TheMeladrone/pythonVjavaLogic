#java logic being used in python

def main():
    weight()
    height()
    answer()

def weight():
    print("Enter in your weight in kg: ", end= "")
    global weight
    weight = float(input()) 

def height():    
    print(f"Enter in your height in meters: ", end= "")
    global height
    height = float(input())

def answer():
    answer = weight / (height * height)
    print(answer)

main()

# Python logic being used 
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2)

)
