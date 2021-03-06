import os
import sys
import subprocess
import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))

def decode():
    # Decode the binary file
    subprocess.call("C:/Program Files/010 Editor/010Editor.exe saves/MH3U_user -template:templates/MH3U_template.bt -script:scripts/MH3U_editor.1sc -noui")

    # Load the file
    df = pd.read_csv('saves/MH3U_user.csv')
    df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)

    # Export save
    df.to_csv(r'saves/MH3U_user.csv',index=False)