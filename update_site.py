from pathlib import Path
root = Path(r'C:\Users\HP\Downloads\glencey')
for path in [root / 'index.html', root / 'project.html']:
    text = path.read_text(encoding='utf-8')
    text = text.replace('See More Project Section', 'View Our Work')
    text = text.replace('handymanservices Diagnosis', 'Property Care Visit')
    text = text.replace(' Property Maintenance', ' Property Care')
    text = text.replace('href="project-details.html"', 'href="project.html"')
    if path.name == 'index.html':
        text = text.replace('assets/img/project/project1-6.jpg', 'assets/img/project/project1-5.jpg')
    if path.name == 'project.html':
        mapping = {
            'project3-1.jpg': 'project1-1.jpg',
            'project3-2.jpg': 'project1-2.jpg',
            'project3-3.jpg': 'project1-3.jpg',
            'project3-4.jpg': 'project1-4.jpg',
            'project3-5.jpg': 'project1-5.jpg',
            'project3-6.jpg': 'project1-7.jpg',
            'project3-7.jpg': 'project1-8.jpg',
            'project3-8.jpg': 'project1-9.jpg',
            'project3-9.jpg': 'project1-1.jpg',
            'project3-10.jpg': 'project1-2.jpg',
            'project3-11.jpg': 'project1-3.jpg',
        }
        for old, new in mapping.items():
            text = text.replace(old, new)
        title_map = {
            'Fixture Sed ut perspiciatis unde omnis iste': 'Interior Painting Refresh',
            'Garbage Disposals': 'Routine Maintenance Visit',
            'showers & Bathtubs repair': 'Bathroom Care & Repairs',
            'Pipe Repair in commercial area': 'Leak Repairs for Busy Spaces',
            'pipe leak in Residential': 'Residential Leak Fixes',
            'Professional Office Deep Cleaning Project': 'Office Deep Cleaning & Presentation',
            'Drywall Repair and Installation': 'Wall Repairs & Finish Touches',
            'Complete Home Renovation Project': 'Home Refresh & Upgrade',
            'Roof and Exterior Work': 'Exterior Upkeep & Protection',
            'Waterproofing and Sealing Services': 'Waterproofing for Peace of Mind',
        }
        for old, new in title_map.items():
            text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
    print('updated', path.name)
