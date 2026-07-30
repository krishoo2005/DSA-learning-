#day 2 

#printing numbers from  1 to n 

# n=5
# i=1
# while i<=5:
#     print(i,end=" ")
#     i+=1



# recursion  use in factorial 

# def factorial(n):
#     if n==0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(3))


# recursive stack
# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end="")
# fun(3)


def function(n):
    if n==0:
        return
    print(n)
    function(n-1)
    print(n)
function(2)    