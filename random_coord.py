import random

def get_random_coord():

    number = 1 if random.random() < 0.5 else -1
    rand_posX = random.randint(0,935)
    rand_negX = random.randint(1,945)
    rand_posY = random.randint(0,520)
    rand_negY = random.randint(1,460)

    rand_X = random.randint(1, 935)
    rand_Y = random.randint(1, 460)

    signum_x = rand_X * number
    number = 1 if random.random() < 0.5 else -1
    signum_y = rand_Y * number

    return signum_x, signum_y

# print(get_random_coord())