#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

(n, k) = map(int, input().split(' '))

ans = 0
for i in range(n):
    if int(input()) % k == 0: ans += 1
print(ans)
