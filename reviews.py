data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print('Finished. Total amount is :', len(data))

# My tried ver.
t = 0
total = 0
while t < len(data):
    total = total + len(data[t])
    t = t + 1
average = total / len(data)
print(average)

# Answer
sum_len = 0
for d in data:
    sum_len += len(d)
print('Len Average is ', sum_len / len(data))

#filter len < 100
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('lenth under 100 char are :', len(new))
print('No.1 is:\n', new[0])