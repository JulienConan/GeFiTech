import json

from technician import Technician

with  open('datas/base_v1.json', 'r') as f:
    data = json.load(f)

tech = Technician(data['Event_1']['local_technician']['foh_technician'])
print(tech)
