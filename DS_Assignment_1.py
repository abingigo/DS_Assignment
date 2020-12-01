#DIsclaimer: This code works in JDoodle, but only on Python 3 and not Python 2

#Function that returns probability of n people having the same birthday in 365 days
def prob(n):
    if n > 365:
        return 1
    c = 1
    for i in range(0, n):
        a = (365 - i) / 365
        c *= a
    return 1 - c
#looping till there is no input
while True:
        try:
            x = prob(int(input()))
            print('%.100f'%x)
        #to avoid error message in online compilers
        except EOFError:
            break
