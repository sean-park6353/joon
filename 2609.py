n, m = map(int, input().split())

n_y = []
m_y = []
n_b = []
m_b = []
for i in range(1, n+1):
    if n % i == 0:
        n_y.append(i)

for i in range(1, m+1):
    if m % i == 0:
        m_y.append(i)

for i in range(1, n+1):
    if n % i == 0:
        n_y.append(i)

gcd = max(list(set(m_y) & set(n_y)))
print(gcd)
lcm = int((m/gcd)*(n/gcd)*gcd)
print(lcm)
