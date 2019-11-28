import re

scriptflag = 0

import sys
stringToCombine=''

for inp in sys.stdin:
    N=str(inp)
    
    a=re.sub(r'<script>.*</script>','', N)
    
    if re.search(r'</script>',a):
        
        scriptflag=0
        a=re.sub(r'.*</script>','', a)
    
        
        
    
    
    if re.search(r'<script>',a):
    
        scriptflag=1
        a=re.sub(r'<script>.*','', a)
        
        stringToCombine = stringToCombine+a
        
    if scriptflag == 0:
        stringToCombine = stringToCombine+a.rstrip()

print(stringToCombine)