box = []

def riang(x):
   return int(x[x.index("#") + 1:])

while True:
   order = input()

   if order == "DONE": break

   box.insert(riang, order)