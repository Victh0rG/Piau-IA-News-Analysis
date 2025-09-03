import xml.etree.ElementTree as ET
from xml.dom import minidom
from GoogleNews import GoogleNews as gn

def gnf(query: str):
    gns = gn(period='y')
    gns.setlang('pt')
    gns.search(query)

    return gns.result()

def __init__():
    queries = ["Inteligência Artificial Piauí", "SIA Piauí"]
    news_items = []

    for query in queries:
        entries = gnf(query)
        for entry in entries:
            news_items.append({
                "title": entry['title'],
                "link": entry['link'],
                "description": entry['desc']
            })

            if len(news_items) >= 15:
                break
        if len(news_items) >= 15:
            break

    news_items = news_items[:15]
    if len(news_items) < 10:
        print("Aviso: Menos de 10 notícias encontradas.")

    root = ET.Element("news")

    for item in news_items:
        news_elem = ET.SubElement(root, "item")
        ET.SubElement(news_elem, "title").text = item["title"]
        ET.SubElement(news_elem, "link").text = item["link"]
        ET.SubElement(news_elem, "description").text = item["description"]

    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

    with open("noticias.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)

    print("Arquivo 'noticias.xml' gerado com sucesso!")

__init__()