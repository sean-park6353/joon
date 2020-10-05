s = {
    'c=': 'c',
    'c-': 'c',
    'dz=': 'd',
    'd-': 'd',
    'lj': 'l',
    'nj': 'n',
    's=': 's',
    'z=': 'z'
}
n = input()
for key, value in s.items():
    n = n.replace(key, value)
print(len(n))
