# Limpia pantalla
clear

# Creacion de BD y tablas 
mysql -t -v -u admin -padmin < DDS.sql
# Inserción de datos
mysql -t -v -u admin -padmin < DMS.sql
# Creación de las vistas
mysql -t -v -u admin -padmin < Views.sql
# Creación de Funciones
mysql -t -v -u admin -padmin < Functions.sql
# Creación de Procedimientos Almacenados
mysql -t -v -u admin -padmin < Procedures.sql
# Creación de Triggers
mysql -t -v -u admin -padmin < Triggers.sql
