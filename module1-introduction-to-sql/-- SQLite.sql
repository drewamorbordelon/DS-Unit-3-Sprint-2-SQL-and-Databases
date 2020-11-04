-- SQLite

SELECT * FROM armory_item;

SELECT COUNT(*) FROM charactercreator_character;

-- SELECT COUNT(*) FROM armory_item;

SELECT COUNT(DISTINCT (name)) 
FROM charactercreator_character;

SELECT DISTINCT(name)
FROM charactercreator_character
LIMIT 10;

SELECT character_id, name
FROM charactercreator_character;
-- WHERE character_id >= 50
-- AND character_id < 55;

SELECT character_id, name
FROM charactercreator_character
WHERE character_id between 50 AND 54;

-- What are the duplicate names??
-- SELECT name, COUNT(*)
-- FROM charactercreator_character
-- GROUP BY name
-- ORDER BY COUNT(*)DESC
-- LIMIT 5;

-- SELECT *
-- FROM charactercreator_character as cc
-- LEFT JOIN charactercreator_fighter as cf 
-- ON cf.character_ptr_id = cc.character_id;

-- How many total Items?
-- SELECT COUNT(DISTINCT(item_ptr_id))
-- FROM armory_weapon;

-- SELECT COUNT(item_ptr_id)
-- FROM armory_weapon;


-- SELECT COUNT(DISTINCT(character_id, ai.name, ai.item_id))  
-- FROM charactercreator_character_inventory as cci
-- INNER JOIN armory_item as ai    -- INNER JOIN only joins corresponding rows
-- ON name = name
-- WHERE character_id < 21;



-- SELECT character_id, COUNT(DISTINCT item_id) FROM     -- Added this code
-- (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name  -- adding more ALIAS
-- FROM charactercreator_character AS cc, 
-- armory_weapon AS aw
-- WHERE ai.name = cc.name 
-- AND ai.item_id = aw.item_ptr_id)
-- GROUP BY 1 
-- ORDER BY 2 DESC;


-- SELECT character_id, name, item_id  FROM charactercreator_character as cc
-- INNER JOIN armory_item as ai   -- INNER JOIN only joins corresponding rows
-- ON name = name
-- WHERE character_id < 21;

-- SELECT name, COUNT(*) 
-- FROM charactercreator_character
-- GROUP BY 1 --  Group by the 1st column
-- ORDER BY 2 DESC;



-- SELECT character_id, AVG(item_id) FROM     --  Added this code
-- (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name  -- adding more ALIAS
-- FROM charactercreator_character AS cc, 
-- armory_weapon AS aw
-- WHERE ai.name = cc.name 
-- AND ai.item_id = aw.item_ptr_id)
-- GROUP BY 1 
-- ORDER BY 2 DESC;
