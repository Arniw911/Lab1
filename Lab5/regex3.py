import re
p = re.compile('[a-z]+_[a-z]+')
m = p.findall('gh_hdh_h_d_d_happyd')
print(m)
