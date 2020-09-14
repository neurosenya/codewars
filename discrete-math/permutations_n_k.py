from math import factorial

n, k = map(int, input().split())

initial_numbers = [str(i) for i in range(0, n)]

answer = []
num_perm = 4 * 3 * 2


def permut(nums, perm, k):

   # if len(answer) == num_perm:
   #     return answer

    if len(perm) == k:
        return perm

    avail_nums = list( set(nums) - set(perm) )

    for i in avail_nums:
        new_nums = avail_nums.copy()
        new_nums.remove(i)
        answer.append(permut(new_nums, perm + str(i), k))
    return answer

answer = permut(initial_numbers, '', k)
answer = [ i for i in answer if type(i) == str]
for i in sorted(answer):
    print(' '.join(list(i)))


