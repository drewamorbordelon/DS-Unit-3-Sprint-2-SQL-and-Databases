
GET_CHARACTERS = """
    SELECT * 
    FROM charactercreator_character;
"""


EXPLAIN SELECT =???  # QUESTION???
"""
SELECT `character_id, name` are 
selecting particular columns. 
"""
SELECT character_id, name  # SELECT *, SELECT (DISTINCT name), SELECT COUNT (*)
"""
LIMIT 10, limit by number of rows (10)
"""
FROM charactercreator_character LIMIT 10
"""
Filtering rows with a condition `WHERE`
"""
WHERE character_id > 50  # or... character_id BETWEEN 51 AND 54 (inclusive)
"""
Another condition
"""
AND character_id < 55;  # using BETWEEN then get rid of this line of code



TABLE_charactercreator = """
SELECT * 
FROM charactercreator_character;
"""
# --Viewing the entire table

TOTAL_characters = """
SELECT COUNT(*)
FROM charactercreator_character; 
""" 
# -- Counts the number of character_ids = total number of characters
# -- Total number of characters = 302 rows
# -- returns 1 table---> COUNT(*)
                    # --1     302

DISTINCT_names = """
SELECT COUNT(DISTINCT (name)) 
FROM charactercreator_character;
"""
# -- Counts the number of unique/distinct names
# -- Distinct names = 297

TOTAL_items = """
SELECT COUNT(DISTINCT(item_id))
FROM charactercreator_character_inventory;
"""
# -- Total number of items in charactercreator_inventory = 174


NUM_weapons = """
SELECT COUNT(item_ptr_id)
FROM armory_weapon;
"""
# -- Total number of weapons = 37

ITEMS_each_character = """
SELECT cc.character_id, cci.item_id, cc.name
FROM charactercreator_character as cc
LEFT JOIN charactercreator_character_inventory as cci
ON cci.character_id = cc.character_id
LIMIT 20;
"""






SELECT name, COUNT(*) 
FROM charactercreator_character
GROUP BY name;   #  Group by name
-- Viewing duplicates in a table


SELECT name, COUNT(*) 
FROM charactercreator_character
GROUP BY 1  #  Group by the 1st column
ORDER BY 2 DESC;  #  Order by the 2nd column (default is smallest to greatest)   
                  #  DESC  = greatest to smallest 
-- Discovering duplicates in a table


SELECT name, COUNT(*) 
FROM charactercreator_character
GROUP BY 1  #  Group by the 1st column
ORDER BY 2 DESC  #  Order by the 2nd column (default is smallest to greatest)   
                 #  DESC  = greatest to smallest 
LIMIT 5;         #  Only viewing the first 5


"""
JOIN
"""
SELECT character_id, name, item_id  FROM charactercreator_character;
INNER JOIN armory_item    #  INNER JOIN only joins corresponding rows
ON name = name;
WHERE character_id < 21;

SELECT character_id, name, item_id  FROM charactercreator_character;
JOIN armory_item    #  INNER JOIN only joins corresponding rows
ON name = name;
WHERE character_id BETWEEN 40 AND 50;

"""
Without JOIN AKA 'IMPLICIT' INNER JOIN
"""
SELECT character_id, name, item_id 
From charactercreator_character, armory_item    # without JOIN
WHERE name = name
AND character_id < 21


"""
Queries result in tables that can be queried!(Silly but can be useful)
"""
SELECT * FROM
(SELECT * FROM charactercreator_character);

"""
Joining > 2 tables (IMPLICIT JOINS)
"""
SELECT cc.character_id, cc.name, ai.item_id, ai.name
FROM charactercreator_character AS cc,     #  ALIASing with cc, ai, aw
armory_item AS ai, 
armory_weapoon AS aw
WHERE ai.name = cc.name 
AND ai.item_id = aw.item_ptr_id;

"""
Use a subquery to make a temp table to query from
"""
SELECT character_id, COUNT(DISTINCT item_id) FROM     #  Added this code
(SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name  # adding more ALIAS
FROM charactercreator_character AS cc, 
armory_weapoon AS aw
WHERE ai.name = cc.name 
AND ai.item_id = aw.item_ptr_id)
GROUP BY 1 
ORDER BY 2 DEC;

"""
Average of a column
"""
SELECT character_id, AVG(item_id) FROM     #  Added this code
(SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name  # adding more ALIAS
FROM charactercreator_character AS cc, 
armory_weapoon AS aw
WHERE ai.name = cc.name 
AND ai.item_id = aw.item_ptr_id)
GROUP BY 1 
ORDER BY 2 DEC;