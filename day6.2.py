#Determine number of ways you could beat 
#the record in each race, find product

#Read time and distance data as an 
#array, each entry is an individual race, with [time][distance]
#values

#Number of ways function - loops through 
#array, checks values for t = 1 (speed 1)
#through t = maxTime - 1 (can't hold for entire
#time duration)
#For each hold time calculated, this
#hold time will = speed, then find 
#time - hold_time = time_remaining
#time_remaining * speed = distance
#If distance > distance in table then this is 
#a valid way to win the race, this will go
#into a new array, find the product of all values in this array



#More elegant solution
#Possible combinations will fail at the tail ends of speed
#Thus, start at the beginning of speed and count until possible success
#Start at the end of speed and count backwards until possible success
#All remaining values are the possible combinations
def number_of_combinations(arr):
    number_races = len(arr)
    for i in range(number_races):
        valid_combination = 0
        valid_combinations.append(0)
        available_time = arr[i][0]
        print("The available time is: ", available_time)
        record_distance = arr[i][1]
        print("The record distance is: ", record_distance)
        end = available_time
        while end > 0:
            current_speed = end
            race_time = available_time - current_speed
            distance = current_speed * race_time
            if distance > record_distance:
                start_value = current_speed
                break
        for x in range(1, available_time - 1):
            current_speed = x
            race_time = available_time - current_speed
            distance = current_speed * race_time
            if distance > record_distance:
                initial_value = current_speed
                break
        
time_distance_values = [[38947970, 241154910741091]]
winning_races = number_of_combinations(time_distance_values)
print(winning_races)
product = 1
for i in range(len(winning_races)):
    product *= winning_races[i]

print(product)



