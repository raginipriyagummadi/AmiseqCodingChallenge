import json
import io

def scrutizeTheData(input_filename, output_filename):
    with io.open(input_filename, 'r') as fb:
        data = json.load(fb)

    output_data = {}
    for val in data:
        if val['cty'] not in output_data:
            output_data[val['cty']] = dict()
        if val['hse'] not in output_data[val['cty']]:
            output_data[val['cty']][val['hse']] = []

        output_data[val['cty']][val['hse']].append(val['nm'])

    with io.open(output_filename, 'w') as fc:
        json.dump(output_data, fc, indent=4, sort_keys=True)

scrutizeTheData(input_filename ='./data/data1.json', output_filename = './data/output_data1.json')