from lxml import html
import requests
print("hello")
page = requests.get("https://ccl.northwestern.edu/netlogo/docs/dictionary.html")
root = html.fromstring(page.content)
funcs = []
docstrings = []
entries = root.xpath('//div[@class="dict_entry"]')
for func in entries:
    forms = func.xpath('.//h4/span')
    if not forms:
        continue
    for form in forms:
        docstring = func.xpath(".//p[1]")[0].text_content()
        funcs.append(form)
        docstrings.append(docstring.split(".")[0])
results = funcs
with open("signatures.el", 'w') as f:
    f.write("(setq company-netlogo-functions `(\n")
    for sig,docstring in zip(results,docstrings):
        if sig.text:
            func_name = sig.text
        else:
            for el in sig:
                if el.tail:
                    func_name = el.tail.strip().split(" ")[0]
                    break
                
        if func_name and func_name in sig.text_content():        
            elems = sig.text_content().split(" ")
            func = func_name.strip().split(" ")[0]
            str = '( "'  + func + '" ,(concat '
            for elem in elems:
                if not elem.strip() == func:
                    str = str + '(propertize "' + elem + ' " \'face \'italic) '
                else:
                    str =  str +  '"' + elem + ' " '
        str = str + ') . \n"' + " ".join(docstring.replace('"', "'").strip().replace("\n","").split())  + '"'
        str = str+' ) \n';
        f.write(str)
    f.write("))")
        
                
            
    

