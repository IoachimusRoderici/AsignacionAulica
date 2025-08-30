CREATE VIEW "Edificios" AS
SELECT 
    Edificio,
	
-- Lunes
	
    CASE
        WHEN "Lunes Inicio" IS NULL OR "Lunes Fin" IS NULL THEN 'Cerrado'
        ELSE "Lunes Inicio" || ' - ' || "Lunes Fin" || 'hs.'
    END AS Lunes,

-- Martes
	
    CASE
        WHEN "Martes Inicio" IS NULL OR "Martes Fin" IS NULL THEN 'Cerrado'
        ELSE "Martes Inicio" || ' - ' || "Martes Fin" || 'hs.'
    END AS Martes,

-- Miércoles

    CASE
        WHEN "Miércoles Inicio" IS NULL OR "Miércoles Fin" IS NULL THEN 'Cerrado'
        ELSE "Miércoles Inicio" || ' - ' || "Miércoles Fin" || 'hs.'
    END AS Miércoles,	
	
-- Jueves

    CASE
        WHEN "Jueves Inicio" IS NULL OR "Jueves Fin" IS NULL THEN 'Cerrado'
        ELSE "Jueves Inicio" || ' - ' || "Jueves Fin" || 'hs.'
    END AS Jueves,

-- Viernes

    CASE
        WHEN "Viernes Inicio" IS NULL OR "Viernes Fin" IS NULL THEN 'Cerrado'
        ELSE "Viernes Inicio" || ' - ' || "Viernes Fin" || 'hs.'
    END AS Viernes,

-- Sábado

    CASE
        WHEN "Sábado Inicio" IS NULL OR "Sábado Fin" IS NULL THEN 'Cerrado'
        ELSE "Sábado Inicio" || ' - ' || "Sábado Fin" || 'hs.'
    END AS Sábado,

-- Domingo

    CASE
        WHEN "Domingo Inicio" IS NULL OR "Domingo Fin" IS NULL THEN 'Cerrado'
        ELSE "Domingo Inicio" || ' - ' || "Domingo Fin" || 'hs.'
    END AS Domingo
	
FROM "Edificios Data";