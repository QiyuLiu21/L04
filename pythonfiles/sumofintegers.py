def sointegers():
    try:
        num = input()
        int_num = int(num)
    except:
        print('Wrong input...BYE!')
        return 
    sum = 0
    for i in range(int_num+1):
        print(f' adding{sum} and {i}')
        sum += i
        print(sum)
    return sum
sointegers()


