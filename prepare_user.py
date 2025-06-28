import os
def pack_uis():
    uis = open('./src/uis.py', "w+")
    for root, dirs, files in os.walk("./src"):
        for dir in dirs:
            for file in os.listdir(os.path.join(root, dir)):
                if file == "user.ui":
                    ui_file = open(os.path.join(root, dir, file), "r")
                    ui_insides = ''.join(ui_file.readlines()).replace('../img/', ':/img/')
                    ui_insides = ui_insides.replace('<include location="../img.qrc"/>\n','')
                    ui_insides = ui_insides.replace('<resources>\n','').replace('</resources>\n','')
                    ui_insides = ui_insides.replace(' resource="../img.qrc"', '')
                    uis.write(dir + "_ui = '''" + ui_insides + "'''\n")
                    ui_file.close()
    uis.close()

    # os.makedirs('./src/img',exist_ok=True)
    # for svg in os.listdir('./utils/svg'):
    #     png = f'./src/img/{svg.strip().replace(".svg", ".png")}'
    #     os.system(f'inkscape ./utils/svg/{svg} --export-filename="{png}" --export-type="png" --export-width=64')

    qrc = open('./src/img.qrc', "w")
    qrc.write(
        '<RCC>\n'
        '  <qresource prefix="/img">\n'
    )
    for png in os.listdir('./src/img'):
       qrc.write(f'    <file>./img/{png}</file>\n')
    qrc.write(
        '  </qresource>\n'
        '</RCC>'
    )
    qrc.close()
    os.system('pyrcc5 -o ./src/img_rc.py ./src/img.qrc')

if __name__ == "__main__":
    pack_uis()
