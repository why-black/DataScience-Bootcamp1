import timeit
import random
from collections import Counter

def count_uniq(nums):
    counted = {}
    for num in nums:
        if num in counted:
            counted[num] += 1
        else:
            counted[num] = 1
    return counted

def top_ten(elems):
    top = []
    for key in elems:
        count = elems[key]

        if len(top)<10:
            top.append((key, count))
            i = len(top)-1
            while i > 0 and top[i][1] < top[i-1][1]:
                top[i], top[i-1] = top[i-1], top[i]
                i-=1
        else:
            if count > top[0][1]:
                top[0]=(key, count)
                i = 0
                while i + 1 < len(top) and top[i][1] > top[i+1][1]:
                    top[i], top[i+1] = top[i+1], top[i]
                    i += 1

    top.sort(key=lambda x: x[1], reverse=True)
    return {key: count for key, count in top}

def main():
    nums = [random.randint(0,100)for i in range(1000000)]
    start = timeit.default_timer()
    counted = count_uniq(nums)
    print(counted)
    end = timeit.default_timer()
    counted_time = end - start

    start = timeit.default_timer()
    print(top_ten(counted))
    end = timeit.default_timer()
    top10_time = end - start

    start = timeit.default_timer()
    counter = Counter(nums)
    end = timeit.default_timer()
    counter_counted_time = end - start

    start = timeit.default_timer()
    counter_top = dict(counter.most_common(10))
    end = timeit.default_timer()
    counter_top_time = end - start

    print(f"my function: {counted_time:.7f}")
    print(f"Counter: {counter_counted_time:.7f}")
    print(f"my top: {top10_time:.7f}")
    print(f"Counter's top: {counter_top_time:.6f}")

if __name__ == '__main__':
    main()