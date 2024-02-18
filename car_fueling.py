def car_fueling(total_distance, max_tank_distance, stops_list):
    
    difference_stop = 0
    remaining_tank = max_tank_distance
    remaining_distance = total_distance
    n = len(stops_list)
    i = 1
    total_stops = 0
    
    current = 0
    for stop in stops_list:
        
        
        
        if remaining_distance:
            
            if current==0:
                difference_stop = 0
            elif current>0:
                difference_stop = stop - current 
            
            if difference_stop>max_tank_distance:
                return -1
            
            remaining_distance = total_distance - stop
            
            remaining_tank -= difference_stop
            
            if remaining_tank < difference_stop and remaining_tank < stop:
                
                remaining_tank = max_tank_distance
                
                total_stops+=1

            
        current = stop
        
    return total_stops

total_distance = 85
max_tank_distance = 20
stops_list = [15, 30, 45, 60, 75]

result = car_fueling(total_distance, max_tank_distance, stops_list)

print(result)
