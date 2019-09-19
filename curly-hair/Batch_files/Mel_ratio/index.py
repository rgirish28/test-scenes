import numpy
import jinja2 

templateLoader = jinja2.FileSystemLoader(searchpath="./") 
templateEnv = jinja2.Environment(loader=templateLoader) 
TEMPLATE_FILE = "template.appleseed" 
template = templateEnv.get_template(TEMPLATE_FILE)
for i in range(0,21):
    for j in range(1,6):
        template.stream(melanin=0.05*i,redness=0.2*j).dump("mel_ratio_"+str(i)+"_"+str(j)+".appleseed")  # this is where to put args to the template renderer

