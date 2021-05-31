import requests
import re
import os
#url = 'https://whsmarthome.hwcloudtest.cn:8443/device/'


#url1 = url+'version.json'

#strhtml = requests.get(url)

#pattern = re.compile('>.*<')

#site = pattern.findall(str(strhtml.text))


#print(site)
#print(type(strhtml.text))
#print(str(strhtml.text))

def match(url, site):
    try:
	print(url)
	#if site == 'd/' or site == 'h5_001/':
	    #return
	if (('.json' in site) or ('.png' in site) or ('.rpk' in site) or ('.zip' in site) or ('.html' in site) or ('.mp4' in site) or ('.jar' in site) or ('.properties' in site) or ('.cql' in site) or ('.apk' in site)) and (('/' not in site)):
	    url1 = url + site
	    html1 = requests.get(url1)
	    if not os.path.exists("./"+url[40:]):
		os.makedirs("./"+url[40:])
	    with open("./"+url[40:]+site, "wb+") as f:
		f.write(html1.content)
	    return
	
	else:
	    html = requests.get(url+site)
	    pattern = re.compile('>.*</a>')
	    sites = pattern.findall(str(html.text))
	    for a in sites:
		if ">../</a>" not in a:
		#print(a)
	    	    match(url+site, a[1:len(a)-4])
    
	return
    except UnicodeEncodeError:
	print("UnicodeEncodeError appear"+url+site)


match('https://whsmarthome.hwcloudtest.cn:8443/', 'device/')
