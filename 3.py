import math

div_num = 6

pattern = 79990000000
end_length = 7
part = 2023
part_length = 4

parts_sum_length = end_length - part_length

for length_1 in range(0, parts_sum_length):
    length_2 = parts_sum_length - length_1

    for part_1 in range(0, 10 ** length_1):
        end_start = (part_1 * 10 ** part_length + part) * 10 ** length_2
        for part_2 in range(0, 10 ** length_2):
            end = end_start + part_2
            end_root = int(math.sqrt(end))

            dividers = 0
            for div in range(1, end_root):
                if end % div == 0:
                    dividers += 2
                    if dividers > div_num:
                        break
            if end % (end_root * end_root) == 0:
                dividers += 1

            if dividers == div_num:
                number = pattern + end
                num_is_prime = 1
                for div in range(2, int(math.sqrt(number)) + 1):
                    if number % div == 0:
                        num_is_prime = 0
                        break
                if num_is_prime:
                    print(number)
