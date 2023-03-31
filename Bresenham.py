from math import ceil, floor


def line(x1, x2, y1, y2):
    if (x2-x1) != 0:
        m = (y2-y1)/(x2-x1)
    b = y1 - (m * x1)
    return m, b


def line_x(x, m, b):
    return m*x + b


def line_y(y, m, b):
    if m != 0:
        return (y-b)/m


x1, y1 = [int(i)
          for i in input("please input first point coordinates : ").split()]
x2, y2 = [int(i)
          for i in input("please input second point coordinates : ").split()]

m, b = line(x1, x2, y1, y2)
ans = []

xs = list(range(x1, x2+1))
y_xs = []
for i in xs:
    y_xs.append(line_x(i, m, b))

ys = list(range(y1, y2+1))
x_ys = []
for i in ys:
    x_ys.append(line_y(i, m, b))

for i in range(len(xs)):
    ans.append((xs[i], floor(y_xs[i])))

for i in range(len(ys)):
    dot = (floor(x_ys[i]), ys[i])
    if dot not in ans:
        ans.append(dot)

ans.sort()
print(ans)
