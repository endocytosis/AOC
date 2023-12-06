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
def number_of_combinations(arr):
    valid_combinations = []
    valid_combination = 0
    number_races = len(arr)
    for i in range(number_races):
        valid_combination = 0
        valid_combinations.append(0)
        available_time = arr[i][0]
        print("The available time is: ", available_time)
        record_distance = arr[i][1]
        print("The record distance is: ", record_distance)
        for x in range(1, available_time - 1):
            current_speed = x
            race_time = available_time - current_speed
            distance = current_speed * race_time
            if distance > record_distance:
                print("The current speed is: ", current_speed, ", which for a race time of", race_time, "would result in a total distance of: ", distance, "which is greater than the record distance of: ", record_distance)
                valid_combination += 1
                valid_combinations[i] = valid_combination
    return valid_combinations

time_distance_values = [[38, 241], [94, 1549], [79, 1074], [70, 1091]]
winning_races = number_of_combinations(time_distance_values)
print(winning_races)
product = 1
for i in range(len(winning_races)):
    product *= winning_races[i]

print(product)



