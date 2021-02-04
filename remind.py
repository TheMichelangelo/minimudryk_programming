max_weight = int(input("Введіть N: "))
total_weight = 0
total_people = 0
while(total_weight < max_weight):
    a = int(input("Введіть вагу пасажира: "))
    total_weight+=a
    total_people+=1

print("Ліфт поїхав з вагою: "+ str(total_weight))
print("кількість людей у ліфті: "+ str(total_people))

max_road_trip = int(input("Введіть загальну дорогу N: "))
total_road_trip = 0
days = 0
trip_per_day = 1 
while(total_road_trip < max_road_trip):
    days+=1
    total_road_trip +=trip_per_day
    trip_per_day*=2

print("Віталій йшов "+ str(days)+" днів")
print("Загальний пройдений шлях "+ str(total_road_trip))
    

number = int(input("Введіть число: "))
summa = 0
while(number>0):
    ost_number = number%10
    number//=10
    summa+=ost_number

if(summa%3==0):
    print("ділиться на 3")
else  print("не ділиться на 3")

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
while(a!=0 and b!=0):
    if(a>b):
        a=a%b
    else:
        b=b%a
print(a+b)    

