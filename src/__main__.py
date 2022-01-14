import argparse

from vyakarana import svara

parser = argparse.ArgumentParser(description='Process Sanksrit Grammar')
parser.add_argument('-pp', '--pretty', action='store_true', help='pretty print svara details')
parser.add_argument('svaras', nargs='+', help='svara(s)')
args = parser.parse_args()

svaras = []
for sv in args.svaras:
    svaras.append(svara.Svara(sv))

if args.pretty:
    for sv in svaras:
        sv.display()
