def is_prime(n):
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


if __name__ == '__main__':
    for number in is_prime(25):
        print(number)
