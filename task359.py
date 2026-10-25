date_input = input()

parts = date_input.split('/')

month_num = int(parts[0])
day = parts[1]
year = parts[2]

months = [
    "", "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

month_name = months[month_num]

print(f"{month_name} {day}, {year}")