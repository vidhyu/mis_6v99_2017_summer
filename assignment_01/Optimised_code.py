# first Assignment
csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
file_name = 'flight_schedule.csv'
def print_flight_schedule(fn, csv_hdr, flt_sched):
    with open(fn,'wt') as f:
        print(csv_hdr, file=f)
        for s in flt_sched:
            print(','.join(s), file=f)

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

Gates_flights = { 'AUS1': 'T1', 'DAL1': 'T2', 'DAL2': 'T3', 'HOU1': 'T4','HOU2': 'T5', 'HOU3': 'T6' }

Iteration_flights = { 'AUS1': 'T1', 'DAL1': 'T2', 'DAL2': 'T3', 'HOU1': 'T4','HOU2': 'T5', 'HOU3': 'T6' }

City_flights = { 'T1': 'AUS1', 'DAL1': 'T2', 'DAL2': 'T3', 'HOU1': 'T4','HOU2': 'T5', 'HOU3': 'T6' }


departure_time_minutes = 360
count = 1

flight_schedule = []

while departure_time_minutes < 1320:
    
    if count%2 == 1:
        Iteration_flights['HOU1'] = Gates_flights['AUS1']
        flight_details = [Gates_flights['AUS1'],'AUS','HOU', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('AUS1','HOU1')) ]
        flight_schedule += [flight_details]
        Iteration_flights['HOU2'] = Gates_flights['DAL1']
        flight_details = [Gates_flights['DAL1'],'DAL','HOU', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('DAL1','HOU2')) ]
        flight_schedule += [flight_details]
        Iteration_flights['HOU3'] = Gates_flights['DAL2']
        flight_details = [Gates_flights['DAL2'],'DAL','HOU', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('DAL2','HOU3')) ]
        flight_schedule += [flight_details]
        Iteration_flights['DAL1'] = Gates_flights['HOU1']
        flight_details = [Gates_flights['HOU1'],'HOU','DAL', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('HOU1','DAL1')) ]
        flight_schedule += [flight_details]
        Iteration_flights['DAL2'] = Gates_flights['HOU2']
        flight_details = [Gates_flights['HOU2'],'HOU','DAL', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('HOU2','DAL2')) ]
        flight_schedule += [flight_details]
        Iteration_flights['AUS1'] = Gates_flights['HOU3']
        flight_details = [Gates_flights['HOU3'],'HOU','AUS', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('HOU3','AUS1')) ]
        flight_schedule += [flight_details]
   
    
    else:
        Iteration_flights['DAL1'] = Gates_flights['AUS1']
        flight_details = [Gates_flights['AUS1'],'AUS','DAL', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('AUS1','DAL1')) ]
        flight_schedule += [flight_details]
        Iteration_flights['AUS1'] = Gates_flights['DAL1']
        flight_details = [Gates_flights['DAL1'],'DAL','AUS', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('DAL1','AUS1')) ]
        flight_schedule += [flight_details]
        Iteration_flights['HOU1'] = Gates_flights['DAL2']
        flight_details = [Gates_flights['DAL2'],'DAL','HOU', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('DAL2','HOU1')) ]
        flight_schedule += [flight_details]
        Iteration_flights['DAL2'] = Gates_flights['HOU1']
        flight_details = [Gates_flights['HOU1'],'HOU','DAL', departure_time(departure_time_minutes), arrival_time(departure_time_minutes,flight_times('HOU1','DAL2')) ]
        flight_schedule += [flight_details]
        
    departure_time_minutes += 100
    count +=1
    Gates_flights = Iteration_flights.copy()


flight_schedule = sorted(flight_schedule, key = lambda x: x[0] + x[3])

print_flight_schedule(file_name, csv_header, flight_schedule)