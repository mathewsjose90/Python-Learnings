'''
Min platforms needed for the trains
'''


def min_platforms_needed(arrival_times, departure_times):
    min_platforms = 1
    arrival_times.sort()
    departure_times.sort()
    i = j = 0
    train_count = len(arrival_times)
    while i < train_count and j < train_count:
        if arrival_times[i] < departure_times[j]:
            i += 1
            min_platforms += 1
        else:
            j += 1
            min_platforms -= 1
    return min_platforms


arrival_times = [900, 940, 950, 1100, 1500, 1800,945]
departure_times = [910, 1200, 1120, 1130, 1900, 2000,2100]
print(min_platforms_needed(arrival_times, departure_times))
