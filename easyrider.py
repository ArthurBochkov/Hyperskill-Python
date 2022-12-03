import json
import re

class EasyDriver:

    fields = {'bus_id':(int,True,''),
              'stop_id':(int, True, ''),
              'stop_name':(str, True, '[A-Z][\w\s]+ (Road|Avenue|Boulevard|Street)$'),
               'next_stop':(int, True, ''),
              'stop_type':(str, False, '^(S|O|F)$'),
              'a_time':(str, True, '^(0\d|1\d|2[1-4]):([0-5][0-9]|60)$')
              }


    def __init__(self, text):
        self.text = json.loads(text)
        self.errors = {}


    def check(self, d, prm, tp, mandatory):
        self.errors.setdefault(prm, 0)
        if isinstance(d[prm], tp) == False:
            self.errors[prm] += 1
        elif mandatory and str(d[prm]) == '':
            self.errors[prm] += 1
        elif prm == 'stop_type' and not d[prm] in ['S','O','F','']:
            self.errors[prm] += 1


    def check_fields(self):
        for d in self.text:
            for key, value in self.fields.items():
                self.errors.setdefault(key, 0)
                if isinstance(d[key], value[0]) == False:
                    self.errors[key] += 1
                elif value[1] and str(d[key]) == '':
                    self.errors[key] += 1
                elif str(d[key]) != '' and not (value[2] == '' or re.match(value[2], d[key])):
                    #print(value[2], d[key])
                    self.errors[key] += 1

        s = sum([value for key, value in self.errors.items()])
        print(f'Format validation: {s} errors')
        for key, value in self.errors.items():
            if value != 0 or (s==0 and key in ['stop_name', 'stop_type', 'a_time']):
                print(f'{key}: {value}')

    def check_bus(self):
        bus = {}
        for d in self.text:
            bus.setdefault(d['bus_id'],0)
            bus[d['bus_id']] += 1
        for key,value in bus.items():
            print(f'bus_id: {key}, stops: {value}')


    def check_line(self):
        lines = {}
        start_stop = set()
        transfer_stop = {}
        finish_stop = set()

        for d in self.text:
            lines.setdefault(d['bus_id'], '')
            lines[d['bus_id']] += d['stop_type']
            if d['stop_type'] == 'S':
                start_stop.add(d['stop_name'])
            elif d['stop_type'] == 'F':
                finish_stop.add(d['stop_name'])
            transfer_stop.setdefault(d['stop_name'], set())
            transfer_stop[d['stop_name']].add(d['bus_id'])
        transfer_stop = sorted([key for key, value in transfer_stop.items() if len(value) > 1])

        fl_error = False
        for key, value in lines.items():
            if 'F' not in value or 'S' not in value:
                print(f'There is no start or end stop for the line: {key}.')
                fl_error = True
                break
        if not fl_error:
            print(f'Start stops: {len(start_stop)} {sorted(list(start_stop))}')
            print(f'Transfer stops: {len(transfer_stop)} {transfer_stop}')
            print(f'Start stops: {len(finish_stop)} {sorted(list(finish_stop))}')


    def check_time(self):
        time_errors = {}
        for bus_id in set([d['bus_id'] for d in self.text]):
            #print(bus_id)
            tm = ''
            for d in [d for d in self.text if d['bus_id'] == bus_id]:
                #print(d['a_time'])
                if d['a_time'] <= tm:
                    time_errors[d['bus_id']] = d['stop_name']
                    break
                tm = d['a_time']
        print('Arrival time test:')
        if (time_errors):
            for key, value in time_errors.items():
                print(f'bus_id line {key}: wrong time on station {value}')
        else:
            print('OK')


    def check_demand(self):

        lines = {}
        start_stop = set()
        transfer_stop = {}
        finish_stop = set()
        stop_errors = []

        for d in self.text:
            lines.setdefault(d['bus_id'], '')
            lines[d['bus_id']] += d['stop_type']
            if d['stop_type'] == 'S':
                start_stop.add(d['stop_name'])
            elif d['stop_type'] == 'F':
                finish_stop.add(d['stop_name'])
            transfer_stop.setdefault(d['stop_name'], set())
            transfer_stop[d['stop_name']].add(d['bus_id'])
        transfer_stop = set(sorted([key for key, value in transfer_stop.items() if len(value) > 1]))

        #print(start_stop)
        #print(transfer_stop)
        #print(finish_stop)
        for d in self.text:
            if d['stop_type'] == 'O' and (d['stop_name'] in start_stop or d['stop_name'] in transfer_stop or d['stop_name'] in finish_stop):
                stop_errors.append(d['stop_name'])
        print('On demand stops test:')
        if stop_errors:
            print(f'Wrong stop type: {sorted(stop_errors)}')
        else:
            print('OK')


    def start(self):
        self.check_demand()


if __name__ == '__main__':
    driver = EasyDriver(input())
    driver.start()