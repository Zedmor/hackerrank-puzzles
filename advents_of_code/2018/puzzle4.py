import re

# params = re.findall('#(\d+)\s@ (\d+),(\d+):\s(\d+)x(\d+)', claim)[0]
# self.id, self.x, self.y, self.width, self.height = map(int, params)
from collections import defaultdict, Counter
from datetime import datetime
from itertools import groupby
from pprint import pprint

from dateutil import parser

def guard_grouper(it):
    group = []
    while True:
        line = next(it)
        if 'Guard' in line and group:
            yield group
            group = [line]
        else:
            group.append(line)

def extract_ts(log_record):
    ts = re.search(r'\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]', log_record)
    stamp = parser.parse(ts.groups()[0])
    return stamp


def sortkey(log_record):
    return extract_ts(log_record)


def find_sleepy_minute(intervals):
    intervals = [(st.minute, et.minute) for (st, et) in intervals]
    s_intervals = sorted(intervals)
    cntr = defaultdict(int)
    for i in range(60):
        for r in s_intervals:
            if r[0] <= i < r[1]:
                cntr[i] += 1
    return max(cntr.items(), key=lambda t: t[1])

def id_extractor(group):
    return re.findall('#(\d+)\s', group[0])[0]


def find_most_slept_minute(sleep_intervals):
    sleeps = defaultdict(list)
    for i in range(60):
        for guard in sleep_intervals.keys():
            for interval in sleep_intervals[guard]:
                if interval[0] <= i < interval[1]:
                    sleeps[i].append(guard)
    # pprint(sleeps)
    return sleeps


def main():
    """
    >>> main()
    """
    sleep_time = defaultdict(list)
    sleep_intervals = defaultdict(list)
    with open('input-4.txt') as f:
        timestamps = f.read().splitlines()
    sorted_ts = sorted(timestamps, key=sortkey)
    # pprint(sorted_ts)
    records = guard_grouper(iter(sorted_ts))
    sorted_records = sorted(records, key=id_extractor)
    groupped_records = groupby(sorted_records, id_extractor)
    for guard_id, guard_records in groupped_records:
        for guard_record in guard_records:
            # pprint(guard_record)
            for record in guard_record:
                if 'falls asleep' in record:
                    sleep_start = extract_ts(record)
                if 'wakes up' in record:
                    sleep_time[guard_id].append((extract_ts(record) - sleep_start).total_seconds()/60)
                    sleep_intervals[guard_id].append((sleep_start.time().minute, extract_ts(record).time().minute))
        # print(sleep_intervals[guard_id], sleep_time[guard_id])

    most_sleepy = find_most_slept_minute(sleep_intervals)
    cntr = [(k, Counter(l)) for k, l in most_sleepy.items()]

    top_min = max(cntr, key=lambda t: max(t[1].values()))
    # print(cntr)
    print(top_min)

    # cntrs = [k: Counter(l) for k, l in most_sleepy.items()]

    # guards_sleep_time = {k: sum(v) for k, v in sleep_time.items()}
    # print(guards_sleep_time)
    # print(sleep_intervals)
    # sleepy_guard = sorted(guards_sleep_time.items(), key=lambda t: t[1], reverse=True)[0][0]
    # print(sleepy_guard)
    #
    # most_sleepy_minute = find_sleepy_minute(sleep_intervals[sleepy_guard])
    #
    # print(most_sleepy_minute[0])
    #
    # result = int(sleepy_guard) * most_sleepy_minute[0]
    #
    # print(result)

    # print(most_sleepy_minute[0] * sleepy_guard)

    # max_sleep_time = max(sleep_time[sleepy_guard])
    # print(max_sleep_time)
