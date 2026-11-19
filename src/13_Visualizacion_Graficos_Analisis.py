atletas["medalla"].value_counts().plot(kind="bar")
print("La mayoria de filas no tienen medalla (0) y una parte menor si tiene (1)")

fusion["region"].value_counts().head(10).plot(kind="bar")
print("Unas pocas regiones concentran la mayor cantidad de registros")

atletas["Sex"].value_counts().plot(kind="bar")
print("Hay mas registros del sexo masculino que del femenino")

atletas["Season"].value_counts().plot(kind="bar")
print("Hay muchos mas registros en Summer que en Winter")

atletas["Medal"].value_counts().plot(kind="bar")
print("Entre las medallas ganadas, las cantidades de oro, plata y bronce son bastante parejas")