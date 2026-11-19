atletas["medalla"]=atletas['Medal'].map(lambda x: 1 if x in["Gold","Silver","Bronze"] else 0)
display(atletas)
duplicados=atletas[atletas["ID"].duplicated()==True]
print(atletas.shape[0]-duplicados.shape[0])
#print(atletas["ID"].nunique())
