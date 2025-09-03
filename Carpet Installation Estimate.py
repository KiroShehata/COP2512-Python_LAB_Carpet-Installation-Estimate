#User Inputs
carpet_price = float(input("Enter carpet price: "))
room_width = int(input('Enter room width: '))
room_length = int(input('Enter room length: '))

#Calculations

room_sqrft = room_width * room_length
total_carpet_price = (carpet_price * room_sqrft) + (carpet_price * room_sqrft * .20)
labor_cost = room_sqrft * .75
carpet_tax = (total_carpet_price + labor_cost) * .07
final_cost = total_carpet_price + labor_cost + carpet_tax

#Displays

print(f'Room: {room_sqrft} sq ft')
print(f'Carpet ${total_carpet_price:.2f}')
print(f'Labor: ${labor_cost:.2f}')
print(f'Tax: ${carpet_tax:.2f}')
print(f'Cost: ${final_cost:.2f}')
