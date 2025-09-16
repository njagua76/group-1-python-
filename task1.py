'''
Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

'''

def speed_checker(car_speed):
    speed_limit = 70
    
    if car_speed < speed_limit:
        print("Ok")
    else:
        excess_speed = car_speed - speed_limit
        points = excess_speed // 5
        
        if points > 12:
            print("License suspended")
        else:
            print("Points: " + str(points))

car_speed = int(input("Car speed is: "))
speed_checker(car_speed)