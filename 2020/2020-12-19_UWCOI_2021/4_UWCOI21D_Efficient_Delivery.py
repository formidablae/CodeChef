N, M, K = map(int, input().split())
deliveries = []
important_roads_x = {}
important_roads_y = {}
for deliv in range(K):
    x_start, y_start, x_end, y_end = map(int, input().split())
    deliveries.append([x_start, y_start, x_end, y_end])
    min_x = min(x_start, x_end)
    max_x = max(x_start, x_end)
    for x in range(min_x, max_x + 1):
        important_roads_x[x] += abs(y_start - y_end)
    min_y = min(y_start, y_end)
    max_y = max(y_start, y_end)
    for y in range(min_y, max_y + 1):
        important_roads_y[y] += abs(x_start - x_end)
