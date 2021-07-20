import random

# Generate test values for buiding collapse prediction
rating_num = []
count = 30
three = 0
two = 0
one = 0
while True:
    for i in range(count):
        num = []
        for j in range(9):
            x = random.randint(0, 1)
            num.append(x)

        if num[2] or num[5] or num[7]:
            if three < round(count/3):
                three += 1
                num.append(3)

    
    # if num[1] or num[4] or num[6]:
    #     num.append(2)
    
    # if num[0] or num[3] or num[8]:
    #     num.append(1)
    


    print(num)
    
    rating_num.append(num)
    # print('\n')