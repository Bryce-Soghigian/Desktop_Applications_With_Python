import csv


with open('solar_system.csv') as data:
    csv_reader = csv.reader(data, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} has a radius of  {row[1]} km \n is {row[3]}km away from teh sun \n and has a tilt of {row[5]}')
            line_count += 1
    print(f'Processed {line_count} lines.')