import re
import subprocess

process_res = ['pnputil.exe', '/restart-device']
process_shw = ['pnputil.exe', '/enum-devices', '/connected', '/class', 'ports']

p = subprocess.Popen(process_shw, stdout=subprocess.PIPE, universal_newlines=True)
ser_port = []
for v in p.stdout.readlines():
    print(v.strip())
    case_re = re.search("Instance ID:(.*)", v.strip())
    if case_re:
        ser_port.append(case_re.group(1).strip())
for dev in ser_port:
    print(process_res + [f'{dev}'])
    p = subprocess.Popen(process_res + [f'{dev}'], stdout=subprocess.PIPE, universal_newlines=True)
    [print(v.strip()) for v in p.stdout.readlines()]
