import json
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
        capture_in = {}

        def __init__(self, json):
            for i in json['captures']:
                # print(i)
                all_in = {}
                all_in['expected'] = i['expected']
                all_in['actual'] = i['actual']
                DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
                t = datetime.strptime(i['time'], DATE_FORMAT)
                t = int(t.replace(tzinfo=timezone.utc).timestamp())
                self.capture_in[t] = all_in

        def print(self):
            print(self.capture_in)

    # Read JSON data into the datastore variable
    with open('logs', 'r') as f:
        datastore_logs = json.load(f)
        print("------")
        print(datastore_logs)

    with open('suites', 'r') as f1:
        with open('logs', 'r') as f2:
            datastore_suites = json.load(f1)
            datastore_logs = json.load(f2)
            suites = Test_Suite(datastore_logs, datastore_suites)
            print("------")
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

    ########### merge into one json ########
    results = {'results': []}

    k = {**suites.suites_in, **suites.log_in}
    for i in captures.capture_in:
        print(i)
        for j in k:
            if i == j:
                k[j]['expected'] = captures.capture_in[i]['expected']
                k[j]['actual'] = captures.capture_in[i]['actual']
    results['results'].append(k)

    ########### write results ###########

    with open('data.txt', 'w') as outfile:
        json.dump(results, outfile)
