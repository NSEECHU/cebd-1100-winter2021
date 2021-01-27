# import sys
# print("Hello World")
# print(2+3)
#
#
# x = ("apple", "banana", "cherry")
# print(type(x))
#
# print(len(sys.argv) -1)
# print (sys.argv[0])
# print (sys.argv[1])
# print (sys.argv[2])

def tri_recursion(k):
    if (k > 0):
        result = tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Results")
tri_recursion(6)
