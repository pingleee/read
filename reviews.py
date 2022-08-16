data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
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
print('Len Average is ', sum_len/len(data))