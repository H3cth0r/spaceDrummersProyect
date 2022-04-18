BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Gender" (
	"genderId"	INTEGER UNIQUE,
	"gender"	TEXT UNIQUE,
	PRIMARY KEY("genderId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Country" (
	"countryId"	INTEGER UNIQUE,
	"country"	TEXT UNIQUE,
	PRIMARY KEY("countryId")
);
CREATE TABLE IF NOT EXISTS "Gamesesion" (
	"id"	INTEGER,
	"startTime"	TEXT,
	"endTime"	TEXT,
	"userId"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("userId") REFERENCES "User"
);
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER,
	"name"	NUMERIC,
	"lastName"	TEXT,
	"email"	TEXT NOT NULL UNIQUE,
	"hashedPwd"	TEXT NOT NULL,
	"country"	TEXT,
	"gender"	TEXT,
	"admin"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("country") REFERENCES "Country"("country"),
	FOREIGN KEY("gender") REFERENCES "Gender"("gender")
);
CREATE TABLE IF NOT EXISTS "Gameprofile" (
	"username"	TEXT UNIQUE,
	"userId"	INTEGER UNIQUE,
	"currentLevel"	INTEGER,
	PRIMARY KEY("username"),
	FOREIGN KEY("userId") REFERENCES "User"("id")
);
CREATE TABLE IF NOT EXISTS "Levelstats" (
	"id"	INTEGER,
	"levelId"	INTEGER,
	"username"	TEXT,
	"score"	INTEGER,
	"timeWhenScore"	TEXT,
	"kos"	INTEGER,
	"failedShoots"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Gender" ("genderId","gender") VALUES (1,'Male'),
 (2,'Female'),
 (3,'Other');
INSERT INTO "Country" ("countryId","country") VALUES (1,'Mexico'),
 (2,'USA'),
 (3,'Canada'),
 (4,'Spain'),
 (5,'United Kingdom'),
 (6,'Japan'),
 (7,'Italy'),
 (8,'Germany');
INSERT INTO "Gamesesion" ("id","startTime","endTime","userId") VALUES (1,'2022-03-16 13:42:08','2022-03-16 14:06:33',1),
 (2,'2022-03-15 12:36:18','2022-03-15 13:00:56',2),
 (3,'2022-03-16 13:12:45','2022-03-16 13:17:13',3);
INSERT INTO "User" ("id","name","lastName","email","hashedPwd","country","gender","admin") VALUES (1,'Arturo','Alfaro','AAlfaro@tec.mx','12345678','Mexico','Male','False'),
 (2,'German','Wong','GWong@tec.mx','4442','Italy','Other','True'),
 (3,'Maria','Gonzalez','MGonzalez','8652','Japan','Female','False');
INSERT INTO "Gameprofile" ("username","userId","currentLevel") VALUES ('Alpha',1,2),
 ('Pepo117',2,2),
 ('ToxicV69',3,1);
INSERT INTO "Levelstats" ("id","levelId","username","score","timeWhenScore","kos","failedShoots") VALUES (1,1,'Alpha',3000,'3:03.125',35,5),
 (2,1,'Alpha',3700,'3:34.593',40,3),
 (3,1,'Pepo117',2400,'2:39.788',28,4);
COMMIT;
