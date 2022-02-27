import math
    
def solution(fees, records):
    record_cache_map = {}
    record_result_map = {}
    record_fee_map = {}
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    answer = []
    
    for record in records:
        time, record_id, isIn = record_spliter(record)
        if isIn == True:
            record_cache_map[record_id] = time
        else:
            if record_id in record_result_map:
                record_result_map[record_id] += get_time(record_cache_map[record_id], time)
            else:
                record_result_map[record_id] = get_time(record_cache_map[record_id], time)
                
            record_cache_map[record_id] = -1
            
    for record_id in record_cache_map:
        if record_cache_map[record_id] != -1:
            if record_id in record_result_map:
                record_result_map[record_id] += get_time(record_cache_map[record_id], 23 * 60 + 59)
            else:
                record_result_map[record_id] = get_time(record_cache_map[record_id], 23 * 60 + 59)
                
    for record_id in record_result_map:
        record_fee_map[record_id] = get_fee(base_time, base_fee, unit_time, 
                                            unit_fee, record_result_map[record_id])
    sorted_keys = sorted(record_fee_map.keys())
    return get_result(sorted_keys, record_fee_map)

def get_result(sorted_keys, record_fee_map):
    ans = []
    for key in sorted_keys:
        ans.append(record_fee_map[key])
    return ans

def get_time(in_time, out_time):
    return out_time - in_time

def get_fee(base_time, base_fee, unit_time, unit_fee, total_time):
    if total_time <= base_time:
        return base_fee
    
    rest_time = total_time - base_time
    return base_fee + ((math.ceil(rest_time / unit_time)) * unit_fee)

def record_spliter(record):
    split_record= record.split(" ")
    split_time = split_record[0].split(":")
    time = int(split_time[0]) * 60 + int(split_time[1])
    record_id = split_record[1]
    isIn = split_record[2] == "IN"
    return time, record_id, isIn