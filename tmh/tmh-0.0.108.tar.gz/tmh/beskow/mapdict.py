import phonemap
import sys

# mapdict - do phoneset maping on a tab-separated phonetic dictionary
# each row is assumed to be 'word<TAB>transcription'

# synopsis:
# python mapdict.py infile ?outfile?

from_bet = 'STA'
to_bet = 'MTM'

pm = phonemap.phonemap(from_bet,to_bet,mapfile='phonemap.tsv')


try:
    f = open(sys.argv[2],'w')
except:
    f = sys.stdout

for line in open(sys.argv[1]):
    txt,trans = line.strip().split('\t')
    newtrans = pm.map(pm.splitphonestring(trans))
    f.write('{}\t{}\n'.format(txt,' '.join(newtrans)))