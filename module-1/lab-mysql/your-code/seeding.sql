#Challenge 3 - Seeding the Database

INSERT INTO Cars(car_id,manufacturer,modelo,year, color)
VALUES 
("ZM8G7BEUQZ97IH46V",'Peugeot','Rifter',2019,'Red'),
("RKXVNNIHLVVZOUB4M",'Ford','Fusion',2018,'White'),
("HKNDGS7CU31E9Z7JW",'Toyota','RAV4',2018,'Silver'),
("DAM41UDN3CHU2WVF6",'Volvo','V60',2019,'Gray'),
("DAM41UDN3CHU2WVF6",'Volvo','V60 Cross Country',2019,'Gray');

INSERT INTO Costumers(id_costumer,name,phone_num,email,city,state,country,zip)
VALUES 
(10001,'Pablo Picasso','+34 636 17 63 82','-','Paseo de la Chopera, 14','Madrid','Spain',28045),
(20001,'Abraham Lincoln','+1 305 907 7086','-','120 SW 8th St','Miami','United States',33130),
(30001,'Napoléon Bonaparte','+33 1 79 75 40 00','-','40 Rue du Colisée','Paris','France',75008);

INSERT INTO Salesperson(id_staff,name,store)
VALUES 
(00001,'Petey Cruiser','Madrid'),
(00002,'Anna Sthesia','Barcelona'),
(00003,'Paul Molive','Berlin'),
(00004,'Gail Forcewind','Paris'),
(00005,'Paige Turner','Miami'),
(00006,'Bob Frapples','Mexico city'),
(00007,'Walter Melon','Amsterdam'),
(00008,'Shonda Leer','São Paulo');

INSERT INTO Invoices(invoice_num,date,car,costumer,salesperson)
VALUES 
(852399038,'2018-08-22',"3K096I98581DHSNUP",20001,00004),
(731166526,'2018-12-31',"HKNDGS7CU31E9Z7JW",10001,00005),
(271135104,'2019-01-22',"RKXVNNIHLVVZOUB4M",30001,00007);
