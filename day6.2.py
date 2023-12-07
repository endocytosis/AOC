#More elegant solution
#Possible combinations will fail at the tail ends of speed
#Thus, start at the beginning of speed and count until possible success
#Start at the end of speed and count backwards until possible success
#All remaining values are the possible combinations

starting_time = 38947970
record_distance = 241154910741091
count = starting_time

start_value = 0 
end_value = 0

for i in range(starting_time):
    current_speed = i
    current_distance = i * (starting_time - current_speed)
    if current_distance > record_distance:
        start_value = current_speed
        break

while count > 0: 
    current_speed = count
    current_distance = count * (starting_time - current_speed)
    if current_distance > record_distance:
        end_value = current_speed
        break
    count -= 1

val_range = (end_value - start_value) + 1

print("The starting time is: ", starting_time)
print("The record distance is: ", record_distance)
print("The first successful value is: ", start_value)
print("The last successful value is: ", end_value)
print("The range of possible values is: ", val_range)