number = int(input("enter the number you want to find out if it is a prime number or not:"))
prime = 0  

for i in range (2,number):
    if number%i == 0:
        prime +=1
        break 


if prime == 0:
    print(number, "number is prime.")
else:
    print(number,"number is not prime.")

         

