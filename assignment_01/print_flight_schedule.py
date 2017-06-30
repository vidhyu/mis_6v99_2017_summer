# first Lab 
csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
file_name = 'flight_schedule.csv'
def print_flight_schedule(fn, csv_hdr, flt_sched):
    with open(fn,'wt') as f:
        print(csv_hdr, file=f)
        for s in flt_sched:
            print(','.join(s), file=f)
            
airports = [['AUS', 1, 25], ['DAL', 2, 30], ['HOU',3, 35]]

flight_times = [['AUS', 'DAL', 50], ['DAL', 'AUS', 50], ['AUS','HOU', 45 ], ['HOU','AUS', 45 ], ['DAL','HOU', 65 ], ['HOU','DAL', 65 ]]

flights = ['T1','T2','T3','T4','T5','T6' ]

City = ('AUS', 'DAL', 'HOU')

arrival_city = ''
departure_city = ''

if arrival_city == 'AUS' and departure_city == 'DAL':
    flight_time = 50
if arrival_city == 'DAL' and departure_city == 'AUS':
    flight_time = 50
if arrival_city == 'AUS' and departure_city == 'HOU':
    flight_time = 45
if arrival_city == 'HOU' and departure_city == 'AUS':
    flight_time = 45
if arrival_city == 'DAL' and departure_city == 'HOU':
    flight_time = 65
if arrival_city == 'HOU' and departure_city == 'DAL':
    flight_time = 65    

departure_time = 600
departure_time_minutes = ((departure_time//100)*60) + (departure_time%100)

def arrival_time(departure_time_minutes):
    arrival_time_minutes = departure_time_minutes + flight_time
    arrival_time = str(arrival_time_minutes//60) + str(arrival_time_minutes%60)
    return arrival_time

flight_list = []
    

def flight_schedule(flight_list):

    flight_schedule = []
    flight_schedule += flight_list


print_flight_schedule(file_name, csv_header, flight_schedule)