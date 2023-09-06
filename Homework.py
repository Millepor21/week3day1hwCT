import re
# with open('./user_records.txt') as f:
#     data = f.readlines()

info_pattern = re.compile('([A-z]+\s[A-z]+),\s([0-9]+),\s([A-Z][a-z]+\s?[A-Z]?[a-z]*)')
info_f_name = 'user_records.txt'
# for line in data:
#     result = info_pattern.match(line)
#     if result:
#         print(f'Age: {result.group(2)}, Country: {result.group(3)}')
#     else:
#         print('Invalid record')
# f.close()

def val_or_inval(file_name, regex_pattern):
    with open(f'./{file_name}') as f:
        data = f.readlines()
    count_val = 0
    count_inval = 0
    for line in data:
        result = regex_pattern.match(line)
        if result:
            print(f'Age: {result.group(2)}, Country: {result.group(3)}')
            count_val += 1
        else:
            print('Invalid record')
            count_inval += 1
    f.close()
    print(count_inval, count_val)

val_or_inval(info_f_name, info_pattern)