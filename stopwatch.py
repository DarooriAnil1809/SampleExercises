import time

def print_time(total_seconds):
    total_mins = total_seconds/60
    seconds = int(total_seconds % 60)
    hours = int(total_seconds/60)
    mins = int(total_seconds % 60)
    print("TIme Spend : {}h:{}m:{}s".format(hours,mins,seconds))
input("Press any key to start")
start_time = time.time()
print('Counting time...')
input("press any key to stop:")
stop_time = time.time()

print_time(stop_time - start_time)