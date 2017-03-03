N,X = input().split()
N,X = int(N), int(X)
subject = []
for i in range(X):
    subject.append(list(map(float, input().split())))
average = []
for i in range(X):
    average = average + [subject[i]]
zipped = zip(*average)
for el in zipped:
    print(sum(el)/X)
