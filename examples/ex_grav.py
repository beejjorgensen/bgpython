def newtons_gravity(m1, m2, r):
   G=6.67430e-11
   
   return G * (m1 * m2) / (r * r)

print(newtons_gravity(10, 20, 30))
print(newtons_gravity(10, 40, 30))
print(newtons_gravity(100, 5, 10))
