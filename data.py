import datetime

def display_all_train_distances():
    for train_no in trains['Train No.'].unique():
        print("Train '" + trains[trains['Train No.'] == train_no].iloc[0]['train Name'].strip() + "' travelled " + str(train_distance(train_no)) + " kms")

def train_stoppages(train_no):
    return trains[trains['Train No.'] == train_no]

def time_difference(time1, time2):
    return datetime.datetime.strptime(time1, '%H:%M:%S') - datetime.datetime.strptime(time2, '%H:%M:%S')

def train_time(train_no):
    return sum([
        time_difference(train_stoppage['Departure time'], train_stoppage['Arrival time']) for train_stoppage in train_stoppages(train_no)
    ])

def train_distance(train_no):
    return trains[trains['Train No.']==train_no].iloc[-1]['Distance']
