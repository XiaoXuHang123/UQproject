import os
import re

# Read all csp codes
with open('csp_handshake_revised.txt') as f:
    src = f.read()

# Parse one line in process, translate from csp to ap
def parseProcessLine(cod, pna):
    global ap, apdc
    if None != re.search(r'(\w+)!(\w+)', cod):
        m = re.search(r'(\w+)!(\w+)', cod)
        ap += '\tout(%s,%s);\n' % (m[1], m[2])
    elif None != re.search(r'(\w+)\?(\[[^\]]+\])?(\w+)', cod):
        m = re.search(r'(\w+)\?(\[[^\]]+\])?(\w+)', cod)
        ap += '\tin(%s,%s);\n' % (m[1], m[3])
    elif None != re.search(r'\w+\s*\{\s*(\w+)\s*=\s*new\s*(\w+)\(([\w\., ]*)\)\s*;\s*\}', cod):
        m = re.search(r'\w+\s*\{\s*(\w+)\s*=\s*new\s*(\w+)\(([\w\., ]*)\)\s*;\s*\}', cod)
        if m[2].lower().find('enc') != -1:
            apdc += 'fun %s(bitstring, pkey): bitstring.\n' % m[2]
        if m[2].lower().find('dec') != -1:
            apdc += 'reduc forall m:bitstring, k:key; %s(%s(m,k),k)=m.\n' % (m[2],m[2].replace('Dec','Enc'))
        ap += '\tlet %s = %s(%s) in\n' % (m[1], m[2], m[3])
    elif cod.find('GetSignMsg') != -1:# @HARD
        apdc += 'type sskey.\ntype spkey.\n\nfun spk(sskey): spkey.\nfun sign(bitstring, sskey): bitstring.\n\nreduc forall m: bitstring, k: sskey; getmess(sign(m,k))=m.\nreduc forall m: bitstring, k: sskey; checksign(sign(m,k),spk(k))=m.\n'
        ap += '\tlet checksign = checksign(adec,pkB) in\n'
    elif cod.find('new Pair(') != -1:
        ap += '\tlet sign= sign((pkB,k),pkX)\n'# @HARD
    elif cod == '%s(%s);' % (pna[0],pna[1]): #collect the loop process names
        ap + ''
        funloop.append(pna[0])
    else:
        tmp = ('\t%s\n' % cod)
        for f in funloop:
            tmp = tmp.replace('%s(' % f, '!%s(' % f)#
        ap += tmp

# Parse variables that declared at beginning of csp codes
def parseDeclare(cod):
    global ap,apdc
    if None != re.search(r'var<Key>\s+\w+\s*=\s*new\s+Key\(\)\s*;', cod, re.M|re.I|re.S):# @HARD
        apdc += 'type key.\n'
    if None != re.search(r'var<PKey>\s+\w+\s*=\s*new\s+', cod, re.M|re.I|re.S):# @HARD
        apdc += 'type pkey.\n'

# ap codes
ap = '\n'
# ap declarations
apdc = '\n'
# loop-process names
funloop = []
parseDeclare(src)
# Extract channel and translate
c = re.compile(r'channel\s+(\w+)\s+\d+\s*;', re.I|re.M|re.S).findall(src)
for i in c:
    ap += 'free %s:channel.\n' % (i)
# Extract variable and translate
v = re.compile(r'var\s+(\w+)\s*;', re.I|re.M|re.S).findall(src)
for i in v:
    ap += 'free %s:bitstring [private].\n' % (i)
ap += '\n'
#process names
pn = re.compile(r'(\w+)\(([\w, ]*)\)=', re.I|re.M|re.S).findall(src)
#print(pn)
pcnt = len(pn)   # How many processes?
prc = []
for i in range(0,pcnt-1):  # Get process codes
    prc.append(src[src.find("%s(%s)=" % (pn[i][0],pn[i][1])) : src.find("%s(%s)=" % (pn[i+1][0],pn[i+1][1]))].strip())
prc.append(src[src.find("%s(%s)=" % (pn[i+1][0],pn[i+1][1])):].strip())
for i in range(0,pcnt):
    if pcnt - i > 1:
        ap += 'let %s(%s)=\n' % (pn[i][0],pn[i][1])
    else: # Last process, which is THE MAIN process. @HARD
        ap += 'process\n	new skA4:skey;\n	new skB6:sskey;\n	let pkA7 = pk(skA4) in\n	out(c,pkA7);\n	let pkB8 = spk(skB) in\n	out(c,pkB8);\n'
    lines = re.split('\s*->\s*', prc[i][prc[i].find('=')+1:])
    #print(lines)
    for j in lines:  # Parse process codes line by line
        j = j.strip().strip('	')
        parseProcessLine(j, pn[i])
    ap += '\n'

# OK, let's print translated codes
print(apdc + ap)
