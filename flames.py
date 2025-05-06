f = "flames"
n1 = input("enter first name: ")
n2 = input("enter second name: ")
f = list(f)
print(f)

l = [i for i in list(n1) + list(n2) if i != " "]
print(l)

s = set(l)
print(s)

d = {k: l.count(k) for k in l}
print(d)

s = {k for k, v in d.items() if v == 1}
print(s)

m = -(-len(s)//len(f))
print(m)

while len(f) > 1:
    ff = f*m
    ff = ff[:len(s)]
    print(ff)
    f.remove(ff[-1])
    print(f)

fdict = {"f" : "Friends", "l": "Love", "a" : "Affection", "m" : "Marriage", "e" : "Enemies", "s": "Siblings"}
print(fdict)
final = fdict[f[-1]]
print(final)