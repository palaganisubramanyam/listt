'''
def separate_even_odd():
    n = int(input("Enter the size of the list: "))
    even_list = []
    odd_list = []
    for _ in range(n):
        element = int(input("Enter an integer: "))
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)
    print("The even list:", even_list)
    print("The odd list:", odd_list)
separate_even_odd()
'''

The even list [2, 6]
The odd list [1, 3, 5]
