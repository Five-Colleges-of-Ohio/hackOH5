import csv

input_file = './topics-metadata.csv'
output_file = './topics-metadata-with-year.csv'
date_index = 6


ip = open(input_file, encoding = 'utf-8')
op = open(output_file, 'w', encoding = 'utf-8')
writer = csv.writer(op)
rows = list(csv.reader(ip))
rows[0].insert(date_index+1, 'Year')
writer.writerow(rows[0])
for row in rows[1:]:
    #print("before insert row:", row[:8])
    row.insert(date_index+1,row[date_index][:4])
    #print("set", row[date_index], 'to', row[date_index][:4])
    #print("after insert row:", row[:8])        
    writer.writerow(row) 

op.close()
