def write_file(function_binary,write_file_path):
    with open(write_file_path, 'wb') as f:
        f.write(function_binary)
   
def read_data(df):    
    import numpy as np
    import os
    raw_data = df['raw_data'][0]
    raw_data_class = df['raw_data_class'][0]
    function_binary = df['function'][0]
    cwd = os.getcwd()   
    write_file_path = cwd + '/parameter_from_db.py'

    if raw_data_class == 'value':

        print('raw_data is value')
        raw_data = df['raw_data'][0]

    elif raw_data_class == 'function':

        raw_data = np.NaN
        print('raw_data is function')
        if type(function_binary) != type(None):
            write_file(function_binary,write_file_path)
            print('parameter_from_db.py downloaded')

    elif raw_data_class == 'array':
        print('raw_data is array')
        csv_array = raw_data
        csv_array = csv_array.replace("{", "[")
        csv_array = csv_array.replace("}", "]")
        csv_list = eval(csv_array)
        raw_data = csv_list
        raw_data = np.array(raw_data)
#         print(type(function_binary))
        if type(function_binary) != type(None):
            write_file(function_binary,write_file_path)
            print('parameter_from_db.py downloaded')

    return raw_data