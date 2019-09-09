
import json
import time
from datetime import datetime
from datetime import timezone


def start():
    class Test_Suite:
        log_in = {}
        suites_in = {}
        def __init__(self, json1, json2):
            for (json_logs, json_suites) in zip(json1['logs'], json2['suites']):
                all_in = {}
                all_in['name'] = json_logs['test']
                all_in['status'] = json_logs['output']
                time_in = int(json_logs['time'])
                self.log_in[time_in] = all_in
                for elem in json_suites['cases']:
                    all_in = {}
                    DATE_FORMAT = "%A, %d-%b-%y %H:%M:%S %Z"
                    all_in['name'] = elem['name']
                    all_in['status'] = elem['errors']
                    time_in = datetime.strptime(elem['time'], DATE_FORMAT)
                    time_in = int(time_in.replace(tzinfo=timezone.utc).timestamp())
                    self.suites_in[time_in] = all_in

                # self.name.append(json['suites'][0]['cases'][0]['name'])
                # self.errors.append(json['suites'][0]['cases'][0]['errors'])
                # self.time.append(json['suites'][0]['cases'][0]['time'])

        def print(self):
            print('+++')
            print(self.log_in)
            print('+++')
            print(self.suites_in)

    class Test_Capture:
        expected = []
        actual = []
        time = []
        list_in = []

        def __init__(self, json):
            for i in json['captures']:
                # print(i)
                all_in = {}
                all_in['expected'] = i['expected']
                all_in['actual'] = i['actual']
                self.list_in.append(all_in)
                self.expected.append(i['expected'])
                self.actual.append(i['actual'])
                self.time.append(i['time'])

        def print(self):
            print(self.expected, self.actual, self.time)

    # Read JSON data into the datastore variable
    with open('logs', 'r') as f:
        datastore_logs = json.load(f)
        print(datastore_logs)
        # logs = Test_Log(datastore_logs)
        # logs.print()
        print("----------")

    with open('suites', 'r') as f1:
        with open('logs', 'r') as f2:
            datastore_suites = json.load(f1)
            datastore_logs = json.load(f2)
            suites = Test_Suite(datastore_logs, datastore_suites)
            suites.print()

        # datastore_suites = json.load(f)
        # print(datastore_suites)
        # suites = Test_Suite(datastore_suites)
        # suites.print()
        # f.close()
    with open('captures', 'r') as f:
        datastore_captures = json.load(f)
        print(datastore_captures)
        captures = Test_Capture(datastore_captures)
        captures.print()
        f.close()

    ###########
    results = {'results': []}

    for i, j in zip(suites.log_in, suites.suites_in):
        print("@@@@")
        k = {**i, **j}
        print(k)
        results['results'].append(k)

    ###########

    with open('data.txt', 'w') as outfile:
        json.dump(results, outfile)

    ##########

    for (item, time_in) in zip(captures.expected, captures.time):
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
        # a="7/2/10 2:00" #pass the date which is to be formatted to DATE_FORMAT
        print(item, time_in)
        # print(time.localtime(time_in))
        # print(datetime.strptime(str(time_in),DATE_FORMAT))
        print(time.strptime(time_in, DATE_FORMAT))
        # print(datetime.strptime(time_in,DATE_FORMAT))
        # print(type(time.strptime(time_in,DATE_FORMAT)))

    for time_in in results.time:
        DATE_FORMAT = "%A, %d-%b-%y %H:%M:%S %Z"
        # a="7/2/10 2:00" #pass the date which is to be formatted to DATE_FORMAT
        print(item, time_in)
        # print(time.localtime(time_in))
        # print(datetime.strptime(str(time_in),DATE_FORMAT))
        print(time.strptime(time_in, DATE_FORMAT))
        # print(datetime.strptime(time_in,DATE_FORMAT))
        # print(type(time.strptime(time_in,DATE_FORMAT)))

    print("----------")
    print(logs.name)
    for name, status, expected, output in suites.__dict__.items():
        print(attr, value)
