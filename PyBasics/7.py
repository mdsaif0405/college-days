
limit = 10
m = int (input('Enter ur count for candies : '))
i = 1

while i <= m :
    if m > limit:
        print('that much candies are not available...')
        print('plz take less than 10 candies')
        break
    print('candy')
    i += 1
