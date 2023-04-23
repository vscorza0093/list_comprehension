# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

x = 2
y = 2
z = 2
n = 3

final_list = []

for num_x in range(0, x + 1):
    for num_y in range(0, y + 1):
        for num_z in range(0, z + 1):
            num_list = []
            num_list.append(num_x)
            num_list.append(num_y)
            num_list.append(num_z)

            if (num_x + num_y + num_z is not n):
                final_list.append(num_list)

# for num in final_list:
#    print(num)

# print(final_list)

# x = range(int(x + 1))
# y = range(int(y + 1))
# z = range(int(z + 1))

# print([[a, b, c] for a in x for b in y for c in z])
# for n in matrix:
#    print(n)


print([[a, b, c] for a in range(x + 1)
      for b in range(y + 1) for c in range(z + 1) if a + b + c != n])
