def sum_of_intervals(intervals):
    intervals.sort(key=lambda i: i[0])
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= new_intervals[-1][1]:
            if intervals[i][1] >= new_intervals[-1][1]:
                new_intervals[-1] = (new_intervals[-1][0], intervals[i][1])
            elif intervals[i][1] < new_intervals[-1][1]:
                new_intervals[-1] = (new_intervals[-1][0], new_intervals[-1][1])
        else:
            new_intervals.append(intervals[i])
    print(intervals)
    print(new_intervals)
    return sum( i[1]-i[0] for i in new_intervals )

intervals = [(1,4), (3,5), (7,10)]
def sum_of_intervals2(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
    return result, len(result)

def sum_of_intervals3(intervals):
    s = 0
    top = float("-inf")
    print("First\ns = %s, top = %s" % (s, top))
    for a, b in sorted(intervals):
        print("(a,b) = (%s, %s)" % (a,b))
        print("Loop")
        if top < a:
            top = a
            print("a = %s" % a)
        if top < b:
            s += b - top
            print("s = %s" % s)
            top = b
            print("top = %s" % top)
    return s
print(sum_of_intervals3(intervals))
