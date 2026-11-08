import timeit

def loop(emails):
    res = []
    for email in emails:
        if email.split('@')[1]== 'gmail.com':
            res.append(email)
    return res

def comprehension(emails):
    return [email for email in emails if email.split('@')[1]== 'gmail.com']

def use_map(emails):
    return list(map(lambda email: email if email.split('@')[1] == 'gmail.com' else None, emails))

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5
    loop_time = timeit.timeit(lambda: loop(emails), number=900000)
    comp_time = timeit.timeit(lambda: comprehension(emails), number=900000)
    map_time = timeit.timeit(lambda: use_map(emails), number=900000)
    print(loop(emails))
    print(comprehension(emails))
    print(use_map(emails))

    times = [(loop_time, 'loop'), (comp_time, 'list comprehension'), (map_time, 'map')]
    sorted_times = sorted(times, key=lambda x: x[0])

    print(f'It is better to use a {sorted_times[0][1]}')
    print(f"{sorted_times[0][0]} vs {sorted_times[1][0]} vs {sorted_times[2][0]}")

if __name__ == '__main__':
    main()