import json
import io
import pandas as pd

def filterJsonData(input_filename , output_filename, output_filename2 ):
    with io.open('C:\\Users\gumma\OneDrive\Desktop\study\data2.json', 'r') as fb:
        data = json.load(fb)

    #getting the keys   -- Point 2
    keys = []
    for val in data['meta']['view']['columns']:
        keys.append(val['name'])

    output_data = mapKeysToData(keys, data)
    final_output_data = filterData(output_data)
    writeIntoFiles(final_output_data, output_filename, output_filename2)

def mapKeysToData(keys, data):
    # Map the keys to the values in the data and create a dict that has the keychecks.  --- Point 2 and 3
    output_data = []
    key_checks = ["Child's First Name", "Gender", "Ethnicity", "Year of Birth", "Rank", "Count"]
    for val in data['data']:
        output_data1 = dict()
        count = 0
        for key in keys:
            if key in key_checks:
                output_data1[key] = dict()
                output_data1[key] = val[count]
            count += 1
        output_data.append(output_data1)
    return output_data

def filterData(output_data):
    # Filter as per the requirement -- Point 4
    final_output_data = {}
    for element in output_data:
        if element['Year of Birth'] == '2012' or element['Year of Birth'] == '2013' or element[
            'Year of Birth'] == '2014':
            if element['Child\'s First Name'] not in final_output_data:
                final_output_data[element['Child\'s First Name']] = dict()
            if element['Ethnicity'] not in final_output_data[element['Child\'s First Name']]:
                final_output_data[element['Child\'s First Name']][element['Ethnicity']] = 0

            final_output_data[element['Child\'s First Name']][element['Ethnicity']] += int(element['Count'])
    return final_output_data

def  writeIntoFiles(final_output_data, output_filename, output_filename2) :
    # Write to Json and CSV  -- Point 5

    with io.open(output_filename, 'w') as fc:
        json.dump(final_output_data, fc, indent=4, sort_keys=True)

    output_csv = pd.DataFrame(final_output_data)
    output_csv = output_csv.fillna('-')
    output_csv.to_csv(output_filename2)


filterJsonData(input_filename ='./data/data2.json', output_filename = './data/output_data2.json', output_filename2 = './data/output_csv_dict.csv')