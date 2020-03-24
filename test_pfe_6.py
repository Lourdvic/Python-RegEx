import re

research = " Nouvellement, ,brilliantly , intelligemment , étonnamment, Occasionally "

for i in re.finditer(r"\w+ment|\w+ly|\w+ment|\w+emment|\w+amment|\w+y", research):
    print('%d-%d: %s' % (i.start(), i.end(), i.group(0)))