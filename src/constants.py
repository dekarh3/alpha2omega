import os.path

app_folder = os.path.expanduser('~')
if not os.path.exists(app_folder):
    app_folder = os.getcwd()
