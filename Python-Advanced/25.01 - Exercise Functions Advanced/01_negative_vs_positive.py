def negative_vs_positive(*args):
    positive = sum(el for el in args if el >= 0)
    negative = sum(el for el in args if el < 0)

    print(negative)
    print(positive)


    if abs(negative) > positive:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')

numbers = [int(el) for el in input().split()]

negative_vs_positive(*numbers)