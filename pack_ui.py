import os
def pack_uis():
    uis = open('./src/uis.py', "w+")
    for root, dirs, files in os.walk("./src"):
        for file in files:
            if file.endswith(".ui"):
                ui_file = open(os.path.join(root, file), "r")
                uis.write(file.replace('.ui', '_ui') + " = '''" + ''.join(ui_file.readlines()) + "'''\n")
                ui_file.close()
    uis.close()

if __name__ == "__main__":
    pack_uis()
