from sys import argv
import pandas as pd

def arg_handler():
    Rfam_clasf=argv[1]
    infernal_data=argv[2]
    output_path=argv[3]    

    return Rfam_clasf,infernal_data,output_path
    
def append_categories(category_data,infernal_data,level):
    infernal_data=infernal_data.copy()
    category_data=category_data.copy()
    infernal_data["Category"]="-"

    for row in category_data.index:
        family=category_data.loc[row,"family"]
        try:
            category=category_data.loc[row,"category"].split(";")[level]
        except IndexError:
            category=category_data.loc[row,"category"].split(";")[0]
        #print(family,category)
        infernal_data.loc[infernal_data.loc[:,"accession"]==family,"Category"]=category

    return infernal_data
    
def main():
    Rfam_clasf,infernal_data,output_path=arg_handler()
    Rfam_clasf=pd.read_csv(Rfam_clasf, sep="\t",names=["family","desc","category"])
    infernal_data=pd.read_csv(infernal_data, sep="\t")
    
    data=append_categories(Rfam_clasf,infernal_data,0)
    ax=data.loc[:,"Category"].value_counts().plot.pie(figsize=(10,10))
    ax.figure.savefig(output_path+"_1.png")
    ax.cla()
    
    data_1=append_categories(Rfam_clasf,infernal_data,1)
    data_1=data_1.copy()
    ax_1=data_1.loc[:,"Category"].value_counts().plot.pie(figsize=(10,10))
    ax_1.figure.savefig(output_path+"_2.png")
    
main()