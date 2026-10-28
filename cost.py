def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print("cost of car rental for 5 days:", rental_car_cost(5))
print("total trip cost to Los Angeles for 5 days with $600 spending money:", trip_cost("Los Angeles", 5, 600))  