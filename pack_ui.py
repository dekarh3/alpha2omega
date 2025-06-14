import os
def pack_uis():
    uis = open('./src/uis.py', "w+")
    for root, dirs, files in os.walk("./src"):
        for file in files:
            if file.endswith(".ui"):
                ui_file = open(os.path.join(root, file), "r")
                ui_insides = ''.join(ui_file.readlines()).replace('../img/', ':/img/')
                ui_insides = ui_insides.replace('<include location="../img.qrc"/>\n','')
                ui_insides = ui_insides.replace('<resources>\n','').replace('</resources>\n','')
                ui_insides = ui_insides.replace(' resource="../img.qrc"', '')
                uis.write(file.replace('.ui', '_ui') + " = '''" + ui_insides + "'''\n")
                ui_file.close()
    uis.close()
    qrc = open('./src/img.qrc', "w")
    qrc.write(
        '<RCC>\n'
        '  <qresource prefix="/img">\n'
    )
    for image in os.listdir('./src/img'):
       qrc.write(f'    <file>./img/{image}</file>\n')
    qrc.write(
        '  </qresource>\n'
        '</RCC>'
    )
    qrc.close()
    os.system('pyrcc5 -o ./src/img_rc.py ./src/img.qrc')

if __name__ == "__main__":
    pack_uis()
