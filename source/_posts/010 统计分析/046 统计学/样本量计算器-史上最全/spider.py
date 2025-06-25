import requests
from pyquery import PyQuery as pq

def getCatLinks(url):
    html = requests.get(url).text
    links = []
    for a in pq(html).find('#menu2>a'):
        links.append([pq(a).text(), pq(a).attr('href')])
    return links

def parse_table(shorturl):
    url = 'https://www.campbellcollaboration.org/escalc/' + shorturl.strip('../')
    html = requests.get(url).text
    table = pq(html).find('#frm>table>tbody').html()
    return table

if __name__ == '__main__':
    import json
    data = {}
    for name, url in [
        ('mindff', 'https://www.campbellcollaboration.org/escalc/html/EffectSizeCalculator-SMD-main.php'), 
        ('crr', 'https://www.campbellcollaboration.org/escalc/html/EffectSizeCalculator-R-main.php'), 
        ('or', 'https://www.campbellcollaboration.org/escalc/html/EffectSizeCalculator-OR-main.php'), 
    ]:
        lks = getCatLinks(url)
        tabls = data.get(name, [])
        for name2, url2 in lks:
            tabls.append({
                'name': name2,
                'table': parse_table(url2),
            })
        data[name] = tabls
    with open(r'D:\mysites\blog-backend\source\_posts\样本量计算器-史上最全\data.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
    