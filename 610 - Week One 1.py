# Write a short Python function, is_multiple(n, m), that takes
# two integer values and returns True is n is a multiple of m,
# that is, n = mi for some integer i, and False otherwise.

def is_multiple(n, m):
# modulo operator; returns the remainder of dividing n and m 
    if n % m == 0:
        return True
    else:
        return False
n = int(input("Enter a #️⃣: "))
m = int(input("Enter a different #️⃣: "))
print(is_multiple(n, m))
