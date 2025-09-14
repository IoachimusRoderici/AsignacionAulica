CREATE TABLE IF NOT EXISTS "Edificios" (
	"Edificio"	TEXT NOT NULL UNIQUE,
	"Lunes"	TEXT,
	"Martes"	TEXT,
	"Miercoles"	TEXT,
	"Jueves"	TEXT,
	"Viernes"	TEXT,
	"Sabado"	TEXT,
	"Domingo"	TEXT,
	PRIMARY KEY("Edificio")
);

CREATE TABLE IF NOT EXISTS "Aulas" (
	"Aula"	TEXT NOT NULL,
	"Edificio"	TEXT NOT NULL,
	"Preferencia"	TEXT NOT NULL DEFAULT 'True',
	"Capacidad"	INTEGER NOT NULL DEFAULT 0,
	"Lunes"	TEXT DEFAULT NULL,
	"Martes"	TEXT DEFAULT NULL,
	"Miercoles"	TEXT DEFAULT NULL,
	"Jueves"	TEXT DEFAULT NULL,
	"Viernes"	TEXT DEFAULT NULL,
	"Sabado"	TEXT DEFAULT NULL,
	"Domingo"	TEXT DEFAULT NULL,
	PRIMARY KEY("Aula","Edificio"),
	FOREIGN KEY("Edificio") REFERENCES "Edificios"("Edificio")
);

CREATE TABLE IF NOT EXISTS "Aulas Dobles" (
	"Primera"	TEXT NOT NULL,
	"Segunda"	TEXT NOT NULL,
	PRIMARY KEY("Primera","Segunda"),
	FOREIGN KEY("Primera") REFERENCES "Aulas"("Aula") ON UPDATE CASCADE,
	FOREIGN KEY("Segunda") REFERENCES "Aulas"("Aula") ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Carreras" (
	"Carrera"	TEXT NOT NULL,
	"Preferencia de Edificio"	TEXT NOT NULL,
	PRIMARY KEY("Carrera"),
	FOREIGN KEY("Preferencia de Edificio") REFERENCES "Edificios"("Edificio")
);

CREATE TABLE IF NOT EXISTS "Materias" (
	"Codigo"	TEXT NOT NULL,
	"Nombre"	TEXT NOT NULL,
	"Comision"	TEXT,
	"Año"	INTEGER NOT NULL DEFAULT 1,
	"Carrera"	TEXT,
	PRIMARY KEY("Codigo","Nombre"),
	FOREIGN KEY("Carrera") REFERENCES "Carreras"("Carrera") ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Clases" (
	"Materia"	TEXT NOT NULL,
	"Dia"	TEXT NOT NULL,
	"Horario"	TEXT NOT NULL,
	FOREIGN KEY("Materia") REFERENCES "Carreras"("Carrera")
);
