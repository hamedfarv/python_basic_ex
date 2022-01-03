from timeit import timeit

code1="""
def calc_ex_factor(age):
    if age<=0:
        raise ValueError("Age can not be 0 or less !!")
    return 10/age

try:
    calc_ex_factor(-1)
except ValueError as error:
    print(error)
"""


print ("first_code",timeit(code1,number=10000))
