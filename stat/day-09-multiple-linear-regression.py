from sklearn.linear_model import LinearRegression

first = list(map(int, str.split(input(), " ")))
m, n = first[0], first[1]
x = []
y = []
for i in range(n):
    data = input().strip().split(" ")
    x.append(data[:m])
    y.append(data[m:])

lr = LinearRegression()
lr.fit(x, y)
q = int(input())
X = [[*map(float, input().split())] for _ in range(q)]
Y = lr.predict(X)
print('\n'.join('%f'%y for y in Y))