def flowerbox(nutrient_values):
    a = 0  # f(i - 2)
    b = 0  # f(i - 1)
    for val in nutrient_values:
        a, b = b, max(a + val, b)

    return b


if __name__ == '__main__':
    print(f'flowerbox([3, 10, 3, 1, 2]) = {flowerbox([3, 10, 3, 1, 2])}')
    print(f'flowerbox([9, 10, 9]      ) = {flowerbox([9, 10, 9])}')
