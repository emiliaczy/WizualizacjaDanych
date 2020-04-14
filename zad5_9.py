def samogloska(data):
    for i in data:
         if i in ("a","e","i","o","u","y"):
             yield i


s = samogloska("uniwersytet")
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))