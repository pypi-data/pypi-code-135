from random import sample

def random_ty(num=1,reds_pre=None,blue_pre=None):
    result = []
    for n in range(num):
        if reds_pre is None:
            reds = sample([n for n in range(1,36)],5)
        if blue_pre is None:
            blues = sample([n for n in range(1,13)],2)
        
        reds.sort()
        blues.sort()
        result.append(' '.join(reds) + ' + '+ ' '.join(blues))
    return '\n'.join(result)