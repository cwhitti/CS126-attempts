# incorrect code that interacts with a tuple
t = (10, 20, 30)
t[0] += 1
if len(t) < 5:
    t.append(40)
    print("t is", t)
    t.reverse()
    print("t is", t)
else:
    t.clear()
