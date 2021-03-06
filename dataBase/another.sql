BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Gamesesion" (
	"id"	INTEGER,
	"startTime"	TEXT,
	"endTime"	TEXT,
	"userId"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("userId") REFERENCES "User" ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Gender" (
	"genderId"	INTEGER UNIQUE,
	"gender"	TEXT UNIQUE,
	PRIMARY KEY("genderId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Countries" (
	"id"	INTEGER,
	"country"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "Levelstats" (
	"id"	INTEGER,
	"levelId"	INTEGER,
	"username"	TEXT,
	"score"	INTEGER,
	"timeWhenScore"	INTEGER,
	"kos"	INTEGER,
	"failedShoots"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("username") REFERENCES "Gameprofile"("username") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER,
	"name"	NUMERIC,
	"lastName"	TEXT,
	"age"	TEXT,
	"email"	TEXT NOT NULL UNIQUE,
	"hashedPwd"	TEXT NOT NULL,
	"country"	TEXT,
	"gender"	TEXT,
	"admin"	TEXT,
	"accountCreation"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("country") REFERENCES "Countries"("country") ON DELETE NO ACTION,
	FOREIGN KEY("gender") REFERENCES "Gender"("gender")ON DELETE NO ACTION
);
CREATE TABLE IF NOT EXISTS "Gameprofile" (
	"username"	TEXT UNIQUE,
	"userId"	INTEGER UNIQUE,
	"currentLevel"	INTEGER,
	PRIMARY KEY("username"),
	FOREIGN KEY("userId") REFERENCES "User"("id") ON DELETE CASCADE
);
INSERT INTO "Gamesesion" VALUES (1,'2022-03-16 13:42:08','2022-03-16 14:06:33',1),
 (2,'2022-03-15 12:36:18','2022-03-15 13:00:56',2),
 (3,'2022-03-16 13:12:45','2022-03-16 13:17:13',3),
 (4,'2022-04-06 11:23:02','2022-04-06 12:00:53',4),
 (5,'2022-03-15 16:47:35','2022-03-15 17:23:11',5),
 (6,'2022-03-28 08:12:57','2022-03-28 08:36:01',6),
 (7,'2022-04-16 19:00:00','2022-04-16 21:30:00',7),
 (8,'2022-04-01 13:07:24','2022-04-01 13:52:47',8),
 (9,'2022-04-08 10:22:09','2022-04-08 11:06:03',9);
INSERT INTO "Gender" VALUES (1,'Male'),
 (2,'Female'),
 (3,'Other');
INSERT INTO "Countries" VALUES (1,'Afganistan'),
 (2,'Albania'),
 (3,'Algeria'),
 (4,'American Samoa'),
 (5,'Andorra'),
 (6,'Angola'),
 (7,'Anguilla'),
 (8,'Antigua & Barbuda'),
 (9,'Argentina'),
 (10,'Armenia'),
 (11,'Aruba'),
 (12,'Australia'),
 (13,'Austria'),
 (14,'Azerbaijan'),
 (15,'Bahamas'),
 (16,'Bahrain'),
 (17,'Bangladesh'),
 (18,'Barbados'),
 (19,'Belarus'),
 (20,'Belgium'),
 (21,'Belize'),
 (22,'Benin'),
 (23,'Bermuda'),
 (24,'Bhutan'),
 (25,'Bolivia'),
 (26,'Bonaire'),
 (27,'Bosnia & Herzegovina'),
 (28,'Botswana'),
 (29,'Brazil'),
 (30,'British Indian Ocean Ter'),
 (31,'Brunei'),
 (32,'Bulgaria'),
 (33,'Burkina Faso'),
 (34,'Burundi'),
 (35,'Cambodia'),
 (36,'Cameroon'),
 (37,'Canada'),
 (38,'Canary Islands'),
 (39,'Cape Verde'),
 (40,'Cayman Islands'),
 (41,'Central African Republic'),
 (42,'Chad'),
 (43,'Channel Islands'),
 (44,'Chile'),
 (45,'China'),
 (46,'Christmas Island'),
 (47,'Cocos Island'),
 (48,'Colombia'),
 (49,'Comoros'),
 (50,'Congo'),
 (51,'Cook Islands'),
 (52,'Costa Rica'),
 (53,'Cote DIvoire'),
 (54,'Croatia'),
 (55,'Cuba'),
 (56,'Curaco'),
 (57,'Cyprus'),
 (58,'Czech Republic'),
 (59,'Denmark'),
 (60,'Djibouti'),
 (61,'Dominica'),
 (62,'Dominican Republic'),
 (63,'East Timor'),
 (64,'Ecuador'),
 (65,'Egypt'),
 (66,'El Salvador'),
 (67,'Equatorial Guinea'),
 (68,'Eritrea'),
 (69,'Estonia'),
 (70,'Ethiopia'),
 (71,'Falkland Islands'),
 (72,'Faroe Islands'),
 (73,'Fiji'),
 (74,'Finland'),
 (75,'France'),
 (76,'French Guiana'),
 (77,'French Polynesia'),
 (78,'French Southern Ter'),
 (79,'Gabon'),
 (80,'Gambia'),
 (81,'Georgia'),
 (82,'Germany'),
 (83,'Ghana'),
 (84,'Gibraltar'),
 (85,'Great Britain'),
 (86,'Greece'),
 (87,'Greenland'),
 (88,'Grenada'),
 (89,'Guadeloupe'),
 (90,'Guam'),
 (91,'Guatemala'),
 (92,'Guinea'),
 (93,'Guyana'),
 (94,'Haiti'),
 (95,'Hawaii'),
 (96,'Honduras'),
 (97,'Hong Kong'),
 (98,'Hungary'),
 (99,'Iceland'),
 (100,'Indonesia'),
 (101,'India'),
 (102,'Iran'),
 (103,'Iraq'),
 (104,'Ireland'),
 (105,'Isle of Man'),
 (106,'Israel'),
 (107,'Italy'),
 (108,'Jamaica'),
 (109,'Japan'),
 (110,'Jordan'),
 (111,'Kazakhstan'),
 (112,'Kenya'),
 (113,'Kiribati'),
 (114,'North Korea'),
 (115,'South Korea'),
 (116,'Kuwait'),
 (117,'Kyrgyzstan'),
 (118,'Laos'),
 (119,'Latvia'),
 (120,'Lebanon'),
 (121,'Lesotho'),
 (122,'Liberia'),
 (123,'Libya'),
 (124,'Liechtenstein'),
 (125,'Lithuania'),
 (126,'Luxembourg'),
 (127,'Macau'),
 (128,'Macedonia'),
 (129,'Madagascar'),
 (130,'Malaysia'),
 (131,'Malawi'),
 (132,'Maldives'),
 (133,'Mali'),
 (134,'Malta'),
 (135,'Marshall Islands'),
 (136,'Martinique'),
 (137,'Mauritania'),
 (138,'Mauritius'),
 (139,'Mayotte'),
 (140,'Mexico'),
 (141,'Midway Islands'),
 (142,'Moldova'),
 (143,'Monaco'),
 (144,'Mongolia'),
 (145,'Montserrat'),
 (146,'Morocco'),
 (147,'Mozambique'),
 (148,'Myanmar'),
 (149,'Nambia'),
 (150,'Nauru'),
 (151,'Nepal'),
 (152,'Netherland Antilles'),
 (153,'Netherlands'),
 (154,'Nevis'),
 (155,'New Caledonia'),
 (156,'New Zealand'),
 (157,'Nicaragua'),
 (158,'Niger'),
 (159,'Nigeria'),
 (160,'Niue'),
 (161,'Norfolk Island'),
 (162,'Norway'),
 (163,'Oman'),
 (164,'Pakistan'),
 (165,'Palau Island'),
 (166,'Palestine'),
 (167,'Panama'),
 (168,'Papua New Guinea'),
 (169,'Paraguay'),
 (170,'Peru'),
 (171,'Phillipines'),
 (172,'Pitcairn Island'),
 (173,'Poland'),
 (174,'Portugal'),
 (175,'Puerto Rico'),
 (176,'Qatar'),
 (177,'Republic of Montenegro'),
 (178,'Republic of Serbia'),
 (179,'Reunion'),
 (180,'Romania'),
 (181,'Russia'),
 (182,'Rwanda'),
 (183,'St Barthelemy'),
 (184,'St Eustatius'),
 (185,'St Helena'),
 (186,'St Kitts-Nevis'),
 (187,'St Lucia'),
 (188,'St Maarten'),
 (189,'St Pierre & Miquelon'),
 (190,'St Vincent & Grenadines'),
 (191,'Saipan'),
 (192,'Samoa'),
 (193,'Samoa American'),
 (194,'San Marino'),
 (195,'Sao Tome & Principe'),
 (196,'Saudi Arabia'),
 (197,'Senegal'),
 (198,'Seychelles'),
 (199,'Sierra Leone'),
 (200,'Singapore'),
 (201,'Slovakia'),
 (202,'Slovenia'),
 (203,'Solomon Islands'),
 (204,'Somalia'),
 (205,'South Africa'),
 (206,'Spain'),
 (207,'Sri Lanka'),
 (208,'Sudan'),
 (209,'Suriname'),
 (210,'Swaziland'),
 (211,'Sweden'),
 (212,'Switzerland'),
 (213,'Syria'),
 (214,'Tahiti'),
 (215,'Taiwan'),
 (216,'Tajikistan'),
 (217,'Tanzania'),
 (218,'Thailand'),
 (219,'Togo'),
 (220,'Tokelau'),
 (221,'Tonga'),
 (222,'Trinidad & Tobago'),
 (223,'Tunisia'),
 (224,'Turkey'),
 (225,'Turkmenistan'),
 (226,'Turks & Caicos Is'),
 (227,'Tuvalu'),
 (228,'Uganda'),
 (229,'United Kingdom'),
 (230,'Ukraine'),
 (231,'United Arab Erimates'),
 (232,'United States of America'),
 (233,'Uraguay'),
 (234,'Uzbekistan'),
 (235,'Vanuatu'),
 (236,'Vatican City State'),
 (237,'Venezuela'),
 (238,'Vietnam'),
 (239,'Virgin Islands (Brit)'),
 (240,'Virgin Islands (USA)'),
 (241,'Wake Island'),
 (242,'Wallis & Futana Is'),
 (243,'Yemen'),
 (244,'Zaire'),
 (245,'Zambia'),
 (246,'Zimbabwe');
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2022-04-19 17:21:23.350705'),
 (2,'auth','0001_initial','2022-04-19 17:21:23.454713'),
 (3,'admin','0001_initial','2022-04-19 17:21:23.532720'),
 (4,'admin','0002_logentry_remove_auto_add','2022-04-19 17:21:23.609726'),
 (5,'admin','0003_logentry_add_action_flag_choices','2022-04-19 17:21:23.669729'),
 (6,'contenttypes','0002_remove_content_type_name','2022-04-19 17:21:23.749734'),
 (7,'auth','0002_alter_permission_name_max_length','2022-04-19 17:21:23.795428'),
 (8,'auth','0003_alter_user_email_max_length','2022-04-19 17:21:23.843437'),
 (9,'auth','0004_alter_user_username_opts','2022-04-19 17:21:23.879436'),
 (10,'auth','0005_alter_user_last_login_null','2022-04-19 17:21:23.927437'),
 (11,'auth','0006_require_contenttypes_0002','2022-04-19 17:21:23.943443'),
 (12,'auth','0007_alter_validators_add_error_messages','2022-04-19 17:21:23.978441'),
 (13,'auth','0008_alter_user_username_max_length','2022-04-19 17:21:24.028446'),
 (14,'auth','0009_alter_user_last_name_max_length','2022-04-19 17:21:24.069452'),
 (15,'auth','0010_alter_group_name_max_length','2022-04-19 17:21:24.110453'),
 (16,'auth','0011_update_proxy_permissions','2022-04-19 17:21:24.141455'),
 (17,'auth','0012_alter_user_first_name_max_length','2022-04-19 17:21:24.186456'),
 (18,'sessions','0001_initial','2022-04-19 17:21:24.221464');
INSERT INTO "django_admin_log" VALUES (1,'2022-04-19 17:26:24.122939','2','Asatruar','[{"added": {}}]',4,1,1);
INSERT INTO "django_content_type" VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$320000$CsuSyqOYRc2IIU60mMUFyZ$9KoDkm54NxrvmYg+0Fu/8Q1PwVoMoj7z4yQZOzIpE9Q=','2022-04-19 18:10:09.023384',1,'Ink1zidoor','','enano223@hotmail.com',1,1,'2022-04-19 17:24:10.096180',''),
 (2,'pbkdf2_sha256$320000$jvT4xlBUlO1nqrmq38BpBX$i5bkN5wFlBfe0PsH2JfgXfc4TDPKmMdUiDfT7PDPAd0=','2022-04-19 17:29:16.389350',0,'Asatruar','','',0,1,'2022-04-19 17:26:23.542065',''),
 (3,'pbkdf2_sha256$320000$oT2IrAx72bIGJDPKthuEJG$2OkVplA6FV5GG6QNvU00UiooNe5qsE73O6mjWsROV4o=','2022-04-22 01:03:38.844952',1,'gar-mir','','gar-mira@hotmail.com',1,1,'2022-04-22 00:00:35.944594','');
INSERT INTO "django_session" VALUES ('y2q6vc37ny90jgkxtnhlo5sx5w44wnic','.eJxVjEEOwiAQRe_C2hBmoHTq0r1nIDBMpWpoUtqV8e7apAvd_vfef6kQt7WErckSpqzOyqrT75YiP6TuIN9jvc2a57ouU9K7og_a9HXO8rwc7t9Bia18a0eGPYNPZJCQRxqSMQIdoYAjjywSIyNYm0boXecYkSz63suQvQP1_gDFzzbb:1nhhhy:3wxOOwDZUVpJ8kPLAA7KeEpEbnen8nQJAk-RgHfDhCs','2022-05-06 01:03:38.850953');
INSERT INTO "Levelstats" VALUES (1,1,'Alpha',3000,3.01,31,5),
 (2,1,'ToxicV69',2400,2.4,28,4),
 (3,1,'Pepo117',5600,4.2,53,3),
 (8,2,'Pepo117',3900,3.3,40,4),
 (9,3,'Pepo117',1700,1.2,19,3),
 (10,1,'YaelGoan',3200,3.1,33,6),
 (11,2,'YaelGoan',2700,2.9,28,4),
 (12,1,'NonWiz',5200,4.2,51,5),
 (13,2,'NonWiz',4000,3.5,40,3),
 (14,3,'NonWiz',1500,1.1,17,4),
 (15,1,'HecThor',2900,2.8,30,3),
 (16,1,'Ink1zidoor',0,0,0,0),
 (17,2,'Ink1zidoor',0,0,0,0),
 (18,3,'Ink1zidoor',0,0,0,0),
 (19,4,'Ink1zidoor',0,0,0,0),
 (20,4,'Ink1zidoor',0,0,0,0),
 (21,4,'Ink1zidoor',0,0,0,0),
 (22,5,'Ink1zidoor',0,0,0,0),
 (23,5,'Ink1zidoor',0,0,0,0),
 (24,5,'Ink1zidoor',0,0,0,0),
 (25,6,'Ink1zidoor',0,0,0,0),
 (26,6,'Ink1zidoor',0,0,0,0),
 (27,6,'Ink1zidoor',0,0,0,0),
 (28,7,'Ink1zidoor',0,0,0,0),
 (29,7,'Ink1zidoor',0,0,0,0),
 (30,7,'Ink1zidoor',0,0,0,0),
 (31,8,'Ink1zidoor',0,0,0,0),
 (32,8,'Ink1zidoor',0,0,0,0),
 (33,8,'Ink1zidoor',0,0,0,0),
 (34,9,'Ink1zidoor',0,0,0,0),
 (35,9,'Ink1zidoor',0,0,0,0),
 (36,9,'Ink1zidoor',0,0,0,0),
 (37,1,'HermanoPepino',3100,3.1,33,4),
 (38,2,'HermanoPepino',3800,3.4,39,5),
 (39,1,'Salmonmonmon',7000,5.2,81,7);
INSERT INTO "User" VALUES (1,'Arturo','Alfaro','2003-04-23','AAlfaro@tec.mx','12345678','Peru','Male','False','2022-04-24'),
 (2,'German','Wong','2001-04-23','GWong@tec.mx','39E12472BB7F2BF23C622D338E16D63F','China','Other','True','2022-04-24'),
 (3,'Maria','Gonzalez','2005-04-23','MGonzalez@tec.mx','8652','France','Female','False','2022-04-24'),
 (4,'Pepe','Gonzalez','2003-04-23','TGonzalez@tec.mx','148853125','France','Male','False','2022-04-24'),
 (5,'Victor Hugo','Portilla','2003-04-23','VhPortilla@tec.mx','343003FB98782D67651D6A74A5D3E3AA','Ireland','Male','True','2022-04-24'),
 (6,'Hector','Miranda','2013-04-23','hMiranda@tec.mx','874AA55B19C5DA732','United States of America','Male','True','2022-04-24'),
 (7,'Misael','Chavez','1988-04-23','MChavez@tec.mx','742698495198AA9615C95EF','Mexico','Male','True','2022-04-24'),
 (8,'Brenda','Flores','2004-04-23','FBrenda@tec.mx','268454953389516351655','France','Female','False','2022-04-24'),
 (9,'Fernada','Ramirez','2004-04-23','FRamirez@tec.mx','654951988846216517AFC','Mexico','Female','False','2022-04-24'),
 (10,'carlitos','carlits','2009-06-16','elcarlitos@tec.mx','39E12472BB7F2BF23C622D338E16D63F','Austria','Female','False','2022-04-24'),
 (11,'pedro','picapiedra','2022-04-12','elpedro@tec.mx','39E12472BB7F2BF23C622D338E16D63F','Azerbaijan','Male','False','2022-04-24'),
 (12,'lolo','loco','2022-04-18','ellolo@tec.mx','39E12472BB7F2BF23C622D338E16D63F','Austria','Male','False','2022-04-24');
INSERT INTO "Gameprofile" VALUES ('Alpha',1,2),
 ('Pepo117',2,4),
 ('ToxicV69',3,2),
 ('YaelGoan',4,3),
 ('NonWiz',5,5),
 ('HecThor',6,2),
 ('Ink1zidoor',7,9),
 ('HermanoPepino',8,3),
 ('Salmonmonmon',9,2),
 ('elcarlitos',10,0),
 ('elpedrito',11,0),
 ('locololo',12,0);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
