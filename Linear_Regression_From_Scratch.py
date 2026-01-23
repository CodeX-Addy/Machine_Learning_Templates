x = [1,2,3,4,5]
y = [2,4,6,8,10]

## To finding out the mean

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

numerator = 0
denominator = 0

for i in range(len(x)):
  numerator += (x[i] - x_mean) * (y[i] - y_mean)
  denominator += (x[i] - x_mean) ** 2

m = numerator/denominator

c = y_mean - m*x_mean
