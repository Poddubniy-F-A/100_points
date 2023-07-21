import math

divider = 23

num_pattern = 79990000000
end_pattern = 2360000
space_length = 4

prime_numbers = 0
for i in range(0, 10 ** space_length):
    end = end_pattern + i

    if end % divider == 0:
        number = num_pattern + end
        prime_numbers += 1
        for div in range(2, int(math.sqrt(number)) + 1):
            if number % div == 0:
                prime_numbers -= 1
                break
print(prime_numbers)
