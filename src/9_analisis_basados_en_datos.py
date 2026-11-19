print("(a) Edad promedio:", round(atletas["Age"].mean(), 2))

print("(b) Con medalla:", atletas["Medal"].notnull().sum(), "| Sin medalla:", atletas["Medal"].isnull().sum())

print("(c) Estatura promedio oro:", round(atletas[atletas["Medal"] == "Gold"]["Height"].mean(), 2))

print("(d) Ediciones distintas:", atletas["Games"].nunique(), "| Paises NOC distintos:", atletas["NOC"].nunique())

print("(e) Edad mas joven:", atletas["Age"].min(), "| Edad mas vieja:", atletas["Age"].max())

print("(f) Registros por temporada:")
print(atletas["Season"].value_counts())

ediciones_atleta = atletas.groupby("ID")["Games"].nunique()
print("(g) Una sola edicion:", (ediciones_atleta == 1).sum(), "| Mas de una edicion:", (ediciones_atleta > 1).sum())
