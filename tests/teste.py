import sys
from pathlib import Path


file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


print('x'*32)
print('xxxxWELCOLL TO MY FIRST GAMExxxx')
print('x'*32)