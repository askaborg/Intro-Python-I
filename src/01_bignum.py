# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE


def two_to_the(n):
    """
    Function two_to_the(n) returns 2 to the nth power.
    When n is not zero, two_to_the(n) returns 2 * two_to_the(n - 1).
    When n is zero two_to_the(n) returns 1 or 2 to the 0th power.

    In the case of two_to_the(5), the function returns 2 * two_to_the(4)
    two_to_the(4) becomes 2 * two_to_the(3)
    two_to_the(3) becomes 2 * two_to_the(2)
    two_to_the(2) becomes 2 * two_to_the(1)
    two_to_the(1) becomes 2 * two_to_the(0) or 1
    Substituting two_to_the(5) we get 2 * 2 * 2 * 2 * 2 * 1 thus 2 to the power of 5
    """
    if n == 0:
        return 1
    else:
        return 2 * two_to_the(n-1)
print("Recursive:")
print(two_to_the(997))

print("Math:")
print (2 ** 65536)