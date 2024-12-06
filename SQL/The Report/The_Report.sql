SELECT 
    -- PARA COL DEL NOMBRE
    CASE 
        -- CUANDO EL GRADO ES MENOR A 8 SE PONE NULL
        WHEN G.Grade < 8 THEN 'NULL'
        -- SI NO SE COLOCA EL NOMBRE REAL
        ELSE S.Name                   
    END AS Name,
    G.Grade,                         
    S.Marks
-- IMPORATSMO LA TABLAS DONDE SE SACARA LA INFO
FROM STUDENTS S
JOIN GRADES G
-- DE LA TABLA SACAREMOS EL MARK DE MIN Y MAX
ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark 
ORDER BY 
    G.Grade DESC,                    
    CASE 
        WHEN G.Grade >= 8 THEN S.Name  
        ELSE S.Marks                 
    END;