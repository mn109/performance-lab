import json
import sys

tests_path = sys.argv[1]
values_path = sys.argv[2]
report_path = sys.argv[3]

with open(values_path, 'r', encoding='utf-8') as file:
    values_data = json.load(file)

with open(tests_path, 'r', encoding='utf-8') as file:
    tests_data = json.load(file)

values_dict = {}
for item in values_data['values']:
    values_dict[item['id']] = item['value']


def update_tests(tests):
    stack = list(tests)
    while stack:
        test = stack.pop()
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            stack.extend(test['values'])


update_tests(tests_data['tests'])

with open(report_path, 'w', encoding='utf-8') as file:
    json.dump(tests_data, file, indent=4)
