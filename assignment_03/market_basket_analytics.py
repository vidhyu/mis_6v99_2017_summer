# first Assignment
csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
file_name = 'flight_schedule_test.csv'
def print_flight_schedule(fn, csv_hdr, flt_sched):
    with open(fn,'wt') as f:
        print(csv_hdr, file=f)
        for s in flt_sched:
            print(','.join(s), file=f)
            
def arrival_time(departure_time_minutes, flight_time):
    arrival_time_minutes = departure_time_minutes + flight_time
    arrival_time = "%02d"%(arrival_time_minutes//60) + "%02d"%(arrival_time_minutes%60)
    return arrival_time

def departure_time(departure_time_minutes):
    departure_time = "%02d"%(departure_time_minutes//60) + "%02d"%(departure_time_minutes%60)
    return departure_time
    
def minimum_departure_time(departure_time_minutes, arrival_time, city ):
    arrival_time_minutes = (int(arrival_time)//100)*60 + int(arrival_time)%100
    if city == 'AUS':
        ground_time = 25
    if city == 'DAL':
        ground_time = 30
    if city == 'HOU':
        ground_time = 35
    minimum_departure_time_minutes = arrival_time_minutes +  ground_time
    minimum_departure_time = "%02d"%(minimum_departure_time_minutes//60) + "%02d"%(minimum_departure_time_minutes%60)
    return minimum_departure_time   
    
    
def flight_times(arrival_city, departure_city):
    if arrival_city == 'AUS1' and (departure_city == 'DAL1' or departure_city == 'DAL2'):
        flight_time = 50
        return flight_time
    if (arrival_city == 'DAL1' or arrival_city == 'DAL2') and departure_city == 'AUS1':
        flight_time = 50
        return flight_time
    if arrival_city == 'AUS1' and (departure_city == 'HOU1' or departure_city == 'HOU2' or departure_city == 'HOU3'):
        flight_time = 45
        return flight_time
    if (arrival_city == 'HOU1'or arrival_city == 'HOU2' or arrival_city == 'HOU3') and departure_city == 'AUS1':
        flight_time = 45
        return flight_time
    if (arrival_city == 'DAL1' or arrival_city == 'DAL2') and (departure_city == 'HOU1' or departure_city == 'HOU2' or departure_city == 'HOU3'):
        flight_time = 65
        return flight_time
    if (arrival_city == 'HOU1'or arrival_city == 'HOU2' or arrival_city == 'HOU3') and (departure_city == 'DAL1' or departure_city == 'DAL2'):
        flight_time = 65
        return flight_time 
                  

Ground_time = [['AUS', 1, 25], ['DAL', 2, 30], ['HOU',3, 35]]

flights = ['T1','T2','T3','T4','T5','T6' ]

Gates_flights = { 'AUS1': ['T1','0600'], 'DAL1': ['T2','0600'], 'DAL2': ['T3','0600'], 'HOU1': ['T4','0600'],'HOU2': ['T5','0600'], 'HOU3': ['T6','0600'] }

Iteration_flights = { 'AUS1': ['T1','0600'], 'DAL1': ['T2','0600'], 'DAL2': ['T3','0600'], 'HOU1': ['T4','0600'],'HOU2': ['T5','0600'], 'HOU3': ['T6','0600'] }

City_flights = { 'T1': 'AUS1', 'DAL1': 'T2', 'DAL2': 'T3', 'HOU1': 'T4','HOU2': 'T5', 'HOU3': 'T6' }


departure_time_minutes = 360
count = 1

flight_schedule = []

while departure_time_minutes < 1320:
    
    if departure_time_minutes < 1260:
        if count%2 == 1:
            departure = Gates_flights['AUS1'][1]
            Iteration_flights['HOU1'][0] = Gates_flights['AUS1'][0]
            flight_details = [Gates_flights['AUS1'][0],'AUS','HOU', departure, arrival_time(departure_time_minutes,flight_times('AUS1','HOU1')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'HOU')
            Iteration_flights['HOU1'][1] = minimum_departure
            
            departure = Gates_flights['DAL1'][1]
            Iteration_flights['HOU2'][0] = Gates_flights['DAL1'][0]
            flight_details = [Gates_flights['DAL1'][0],'DAL','HOU', departure, arrival_time(departure_time_minutes,flight_times('DAL1','HOU2')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'HOU')
            Iteration_flights['HOU2'][1] = minimum_departure
            
            departure = Gates_flights['DAL2'][1]
            Iteration_flights['HOU3'][0] = Gates_flights['DAL2'][0]
            flight_details = [Gates_flights['DAL2'][0],'DAL','HOU', departure, arrival_time(departure_time_minutes,flight_times('DAL2','HOU3')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'HOU')
            Iteration_flights['HOU3'][1] = minimum_departure
            
            departure = Gates_flights['HOU1'][1]
            Iteration_flights['DAL1'][0] = Gates_flights['HOU1'][0]
            flight_details = [Gates_flights['HOU1'][0],'HOU','DAL', departure, arrival_time(departure_time_minutes,flight_times('HOU1','DAL1')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'DAL')
            Iteration_flights['DAL1'][1] = minimum_departure
            
            departure = Gates_flights['HOU2'][1]
            Iteration_flights['DAL2'][0] = Gates_flights['HOU2'][0]
            flight_details = [Gates_flights['HOU2'][0],'HOU','DAL', departure, arrival_time(departure_time_minutes,flight_times('HOU2','DAL2')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'DAL')
            Iteration_flights['DAL2'][1] = minimum_departure
            
            departure = Gates_flights['HOU3'][1]
            Iteration_flights['AUS1'][0] = Gates_flights['HOU3'][0]
            flight_details = [Gates_flights['HOU3'][0],'HOU','AUS', departure, arrival_time(departure_time_minutes,flight_times('HOU3','AUS1')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'AUS')
            Iteration_flights['AUS1'][1] = minimum_departure
        
   
    
        else:
            departure = Gates_flights['AUS1'][1]
            Iteration_flights['DAL1'][0] = Gates_flights['AUS1'][0]
            flight_details = [Gates_flights['AUS1'][0],'AUS','DAL', departure, arrival_time(departure_time_minutes,flight_times('AUS1','DAL1')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'DAL')
            Iteration_flights['DAL1'][1] = minimum_departure
            
            departure = Gates_flights['DAL1'][1]
            Iteration_flights['AUS1'][0] = Gates_flights['DAL1'][0]
            flight_details = [Gates_flights['DAL1'],'DAL','AUS', departure, arrival_time(departure_time_minutes,flight_times('DAL1','AUS1')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'AUS')
            Iteration_flights['AUS1'][1] = minimum_departure
            
            departure = Gates_flights['DAL2'][1]
            Iteration_flights['HOU1'][0] = Gates_flights['DAL2'][0]
            flight_details = [Gates_flights['DAL2'][0],'DAL','HOU', departure, arrival_time(departure_time_minutes,flight_times('DAL2','HOU1')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'HOU')
            Iteration_flights['HOU1'][1] = minimum_departure
            
            departure = Gates_flights['HOU1'][1]
            Iteration_flights['DAL2'][0] = Gates_flights['HOU1'][0]
            flight_details = [Gates_flights['HOU1'][0],'HOU','DAL', departure, arrival_time(departure_time_minutes,flight_times('HOU1','DAL2')) ]
            flight_schedule += [flight_details]
            minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'DAL')
            Iteration_flights['DAL2'][1] = minimum_departure
        
    else:
        departure = Gates_flights['AUS1'][1]
        Iteration_flights['DAL1'][0] = Gates_flights['AUS1'][0]
        flight_details = [Gates_flights['AUS1'][0],'AUS','DAL', departure, arrival_time(departure_time_minutes,flight_times('AUS1','DAL1')) ]
        flight_schedule += [flight_details]
        minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'DAL')
        Iteration_flights['DAL1'][1] = minimum_departure
        
        departure = Gates_flights['DAL1'][1]
        Iteration_flights['AUS1'][0] = Gates_flights['DAL1'][0]
        flight_details = [Gates_flights['DAL1'][0],'DAL','AUS', departure, arrival_time(departure_time_minutes,flight_times('DAL1','AUS1')) ]
        flight_schedule += [flight_details]
        minimum_departure = minimum_departure_time(departure_time_minutes,flight_details[4],'AUS')
        Iteration_flights['AUS1'][1] = minimum_departure

    
        
    departure_time_minutes += 101
    count +=1
    Gates_flights = Iteration_flights.copy()


#flight_schedule = sorted(flight_schedule, key = lambda x: x[0] + x[3])

print_flight_schedule(file_name, csv_header, flight_schedule)