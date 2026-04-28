import re
product_descriptions = """
qqq
Frame Material: Asian Wood"""
materials = []
product_descriptions = product_descriptions.replace('Materials & Care', '').replace('\n','换行').split('换行')
# print(product_descriptions)
for j in product_descriptions:
    materials_ = re.findall(r'(.*?)Material\s*(.*?)(?:\n|$)', j, re.DOTALL)
    # print(materials_)
    for i in materials_:
        i = [m for m in i]
        material = ''.join(i)
        materials.append(material)
material = ';'.join(materials).replace('Material Type','Material ').replace('Material','Material ')
print(material)
