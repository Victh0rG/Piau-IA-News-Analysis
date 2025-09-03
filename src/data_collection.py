import xml.etree.ElementTree as ET
from xml.dom import minidom
from GoogleNews import GoogleNews
import csv
import logging
import os

logging.basicConfig(level=logging.INFO)

def collect_news(queries=["Inteligência Artificial Piauí", "SIA Piauí"], limit=15, output_dir='data/raw'):
    """Coleta notícias e salva em XML e CSV."""
    gn = GoogleNews(period='y', lang='pt')
    news_items = []
    for query in queries:
        gn.search(query)
        entries = gn.result()
        for entry in entries:
            news_items.append({
                "title": entry['title'],
                "link": entry['link'],
                "description": entry['desc']
            })
            if len(news_items) >= limit:
                break
        if len(news_items) >= limit:
            break

    os.makedirs(output_dir, exist_ok=True)
    xml_path = os.path.join(output_dir, 'noticias.xml')
    csv_path = os.path.join(output_dir, 'noticias.csv')

    news_items = news_items[:15]
    # Salva XML
    root = ET.Element("news")
    for item in news_items:
        news_elem = ET.SubElement(root, "item")
        ET.SubElement(news_elem, "title").text = item["title"]
        ET.SubElement(news_elem, "link").text = item["link"]
        ET.SubElement(news_elem, "description").text = item["description"]
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(xml_str)

    # Converte para CSV
    tree = ET.parse(xml_path)
    items = tree.findall(".//item")
    headers = [child.tag for child in items[0]]
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for item in items:
            row = [child.text for child in item]
            writer.writerow(row)

    logging.info(f"Notícias coletadas e salvas em {xml_path} e {csv_path}")
    return csv_path