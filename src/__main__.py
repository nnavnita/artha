import argparse

from vyakarana import svara

parser = argparse.ArgumentParser(description='Process Sanksrit Grammar')
parser.add_argument('-pp', '--pretty', action='store_true', help='pretty print svara details')
parser.add_argument('svara', nargs='+', help='svara')
args = parser.parse_args()

sv = []
for s in args.svara:
    sv.append(svara.Svara(s))

if args.pretty:
    for s in sv:
        s.display()
