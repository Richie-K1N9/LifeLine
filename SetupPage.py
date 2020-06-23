name = (input("Hello and welcome to Lifeline, please enter your name: "))
print("Hello," + name)
age = (input("Please enter your age: "))

height = float(input("Enter height in meters: "))

weight = float(input("Enter weight in kg: "))

bmi = weight/(height**2)

bmi2 = round(bmi,2)


print("Your BMI is: {0} and you are: ".format(bmi2), end='')

if ( bmi < 16):
   print("severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy")

elif ( bmi >= 25 and bmi < 30):
   print("overweight")

elif ( bmi >=30 and bmi <35):
   print("severely overweight")


