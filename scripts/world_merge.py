import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def merge():
    # Load the outputs of inventory.py
    df_items = pd.read_csv('world_output_items.csv')
    df_equipment = pd.read_csv('world_output_equipment.csv')
    df_tool = pd.read_csv('world_output_tool.csv')
    df_layered = pd.read_csv('world_output_layered.csv')
    df_general = pd.DataFrame(data={'Item Name':0,'Quantity Possessed':0,'Item Level':0,'Item Experience':0,'Item Rarity':0,'Item Category':0,'Item Subcategory':0},index=(0,1))

    # Fill in the items
    for i in range(len(df_items)):
        s = {'Item Name':df_items.iloc[i,1],'Quantity Possessed':df_items.iloc[i,2],'Item Level':0,'Item Experience':0,'Item Rarity':df_items.iloc[i,5],'Item Category':df_items.iloc[i,6],'Item Subcategory':0}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the equipment
    for i in range(len(df_equipment)):
        s = {'Item Name':df_equipment.iloc[i,3],'Quantity Possessed':df_equipment.iloc[i,6],'Item Level':df_equipment.iloc[i,4],'Item Experience':df_equipment.iloc[i,5],'Item Rarity':df_equipment.iloc[i,7],'Item Category':df_equipment.iloc[i,8],'Item Subcategory':df_equipment.iloc[i,9]}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the tools
    for i in range(len(df_tool)):
        s = {'Item Name':df_tool.iloc[i,0],'Quantity Possessed':1,'Item Level':0,'Item Experience':df_tool.iloc[i,1],'Item Rarity':df_tool.iloc[i,2],'Item Category':'Palico Gadgets','Item Subcategory':0}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the layered armor    
    for i in range(len(df_layered)):
        s = {'Item Name':df_layered.iloc[i,2],'Quantity Possessed':1,'Item Level':0,'Item Experience':0,'Item Rarity':df_layered.iloc[i,3],'Item Category':'Layered Armor','Item Subcategory':df_layered.iloc[i,4]}
        df_general = df_general.append(s,ignore_index=True)

    # Clean and output the data
    df_general = df_general.groupby(df_general['Item Name']).aggregate({'Quantity Possessed':'sum','Item Level':'max','Item Experience':'max','Item Rarity':'first','Item Category':'first','Item Subcategory':'first'})
    df_general.to_csv(r'world_output.csv',encoding='utf-8')