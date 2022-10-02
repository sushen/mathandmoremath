"""
Example 1 : Using Negative number we can define number
"""
number_line = -1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5
print(f'Line number: {number_line}\n')

"""
Example 2 : Using Negative number we can define weather
"""
# when I am in canada. The weather in there is
normal_day = 36
summer_day = 52
cold_day = -25
print(f"Normal Day : {normal_day}\n")

"""
Example 3 : Using Negative number we can define Accounts Profit and Loss in business
"""

day_1_profit = 5000
day_2_profit = 7000
day_3_loss = -3000
day_4_loss = -4000
day_5_profit = 5000
line_of_profit_and_loss = 5000, 5000, 7000, -3000, -4000
print(f"line_of_profit_and_loss: {line_of_profit_and_loss}\n")

"""
Example 4 : Using Negative number we can define temperature of ice
"""

temperature = -25
print(f"temperature: {temperature}\n" )

"""
Example 4 : Using Negative number we can define Power of your glasses
"""
power = -90


"""
Example 5 : Using Negative number we can define How a ship will float. How a boat floats on water.
Because the density of water is less then the boat.
"""
water_density = int(input("Enter the water density: "))
ship_density: int = int(input("Enter the ship density: "))
air_density = int(input("Enter the air density: "))
ship_density_with_air = int(ship_density + air_density)
less_density = (int(ship_density_with_air - water_density))
# print(f"less density is: {less_density}")
man_density = 10
man_in_ship = int(less_density / man_density)
print(f"Total people will catch on the ship is: {man_in_ship}")
