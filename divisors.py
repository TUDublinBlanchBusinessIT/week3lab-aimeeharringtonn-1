#Aimee Harrington
#08/02/2024
#divisors.py


def divisors(num)
divisors_list=[]
    for i in range(1, num + 1):
        if num % i == 0:
            divisors_list.append(i)
 
    return divisors_list 
