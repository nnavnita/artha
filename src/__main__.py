import argparse

from vyakarana import svara, alpha

parser = argparse.ArgumentParser(description='Process Sanksrit Grammar')
parser.add_argument('-pp', '--pretty', action='store_true', help='pretty print alphabet details')
parser.add_argument('alphabet', nargs='+', help='alphabet to parse')
args = parser.parse_args()

alphas = []
for a in args.alphabet:
    s = svara.Svara(a)
    if s.kind == None:
        alphas.append(alpha.Alpha(a))
    else:
        alphas.append(svara.Svara(a))

if args.pretty:
    for a in alphas:
        a.display()
