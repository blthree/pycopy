try:
    try:
        from ucollections import deque
    except ImportError:
        from collections import deque
except ImportError:
    print("SKIP")
    raise SystemExit


d = deque((), 2)
print(len(d))
print(bool(d))

try:
    d.popleft()
except IndexError:
    print("IndexError")

print(d.append(1))
print(len(d))
print(bool(d))
print(d.popleft())
print(len(d))

d.append(2)
print(d.popleft())

d.append(3)
d.append(4)
print(len(d))
print(d.popleft(), d.popleft())
try:
    d.popleft()
except IndexError:
    print("IndexError")

d.append(5)
d.append(6)
d.append(7)
print(len(d))
print(d.popleft(), d.popleft())
print(len(d))
try:
    d.popleft()
except IndexError:
    print("IndexError")
