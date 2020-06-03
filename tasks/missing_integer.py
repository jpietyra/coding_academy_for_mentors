# Write a function:
#
#     def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].
#


def solution(a):
    result = 1
    a.sort()
    for i in a:
        if i <= 0:
            continue
        elif result < i:
            return result
        else:
            result = i + 1
    return result

