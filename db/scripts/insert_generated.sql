USE `recipe_website`;
delete from recipes where title like '%';

INSERT INTO recipes (title, instructions, description, cook_time) VALUES (
        'Flygande Jakob',
        'Bena ur kyckling och lägg i form. Strö över sallads krydda|Vispa grädde ganska fast, blanda ner creme frieche och chilli  sås. Bre över kycklingingen.|Klipp bacon i lagom bitar och stek lätt. Strö jordnötter över formen.|Laga i ugnen i 30 min, 175c.|Server med ris och sallad.',
        'Detta är en jättegod Flygande Jakob utan banan',
        '60');
CALL connect_ingredient_dev('Grillad kyckling','1');
CALL connect_ingredient_dev('Italiensk salladskrydda','2 krdm');
CALL connect_ingredient_dev('Visp grädde','3 dl');
CALL connect_ingredient_dev('Creme freiche','1,5 dl');
CALL connect_ingredient_dev('Chilli sås','1,5 dl');
CALL connect_ingredient_dev('Bacon','2 paket');
CALL connect_ingredient_dev('Salta jordnötter','1 dl');

INSERT INTO recipes (title, instructions, description, cook_time) VALUES (
        'Creme brulee',
        'Sätt ugenen på 160c|Koka upp grädde, mjölk och vaniljstången. Låt stå i 15 min.|Plocka upp vaniljstången|Vispa socker och äggulor tills det bleknar.|Vispa ner gräddblandningen lite i taget i äggsmeten. Dra av skum.|Fördela i formar. Dra av skum|Placera formar i en ugnsform och fyll med varmtvatten upp till hälften av formarnas höjd.|Grädda i ugnen 30-45 min tills smeten är "woobly".|Låt svalna i minst två timmar i kylskåpet.|Plocka ut formar 30 min innan sockring.|Ha på ett lager mer strösocker på varje form och bränn med brännare.|Låt svalna i 5 minuter innan förtäring.',
        'Fantastisk och lätt Creme brulee.',
        '195');
CALL connect_ingredient_dev('Visp grädde','4,5 dl');
CALL connect_ingredient_dev('Mjölk','1,5 dl');
CALL connect_ingredient_dev('Äggulor','6');
CALL connect_ingredient_dev('Strö socker','75g (3/4dl)');
CALL connect_ingredient_dev('Vaniljstång','1');


select ri.amount,i.label, r.*
from recipe_ingredients as ri
    INNER JOIN recipes as r
        on ri.recipe_id = r.recipe_id
    INNER JOIN ingredients as i
        on ri.ingredient_id = i.ingredient_id;
