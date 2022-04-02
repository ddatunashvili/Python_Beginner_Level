# შედარების, ლოგიკური და სპეციალური ოპერატორები
# > = true

print(3 > 2)

# >= true

print(2 >= 0)

# == - false
print(4 == 3)

# არ უდრის !=false

print(7 != 7)

# AND მცდარობა
# 0 and 0 > 0
# 1 and 1 > 1
# 1 and 0 > 0
# -------------------------
# OR ჭეშმარიტება
# 0 or 0 > 0
# 0 or 1 > 1
# 1 or 1 > 1
# -------------------------
# NOT  უარყოფა
# not 0 > 1
# not 1 > 0
# -------------------------

a = True
b = False
print(a and b)
print(not a)
print(not b)
# -------------------------
x = 6
y = 7
print(x and y)
print(x or y)
# -------------------------
a = 6
b = 6
print(a is b)
# -------------------------

# == is - ( x= 257 y=257)[id, type, value]

# x== y true [ value]
# x is y false [ id]
# -------------------------
# is not = true

print(x is not y)
# -------------------------
# in = true true

a = "georgia"
print("g" in a)
print("j" not in a)
# -------------------------
