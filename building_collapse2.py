# Generate test values for buiding collapse prediction
rating_num = []
for i in range(10):
    num = []
    for j in range(10):
        x = random.randint(0, 1)
        num.append(x)
        print(x, end="")
    rating_num.append(num)
    print('\n')