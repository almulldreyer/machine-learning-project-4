CREATE TABLE NBA_2022(
	id SERIAL,
	Team VARCHAR(50),
	WinLoss_Record VARCHAR(50),
	Win_Percentage FLOAT(50),
	MOV FLOAT(10),
	ATS FLOAT(10),
	Cover_Percentage FLOAT(50)
);

CREATE TABLE NBA_2021(
	id SERIAL,
	Team VARCHAR(50),
	WinLoss_Record VARCHAR(50),
	Win_Percentage FLOAT(50),
	MOV FLOAT(10),
	ATS FLOAT(10),
	Cover_Percentage FLOAT(50)
);

CREATE TABLE NBA_2020(
	id SERIAL,
	Team VARCHAR(50),
	WinLoss_Record VARCHAR(50),
	Win_Percentage FLOAT(50),
	MOV FLOAT(10),
	ATS FLOAT(10),
	Cover_Percentage FLOAT(50)
);

CREATE TABLE NBA_19to22(
	id SERIAL,
	Team VARCHAR(50),
	WinLoss_Record VARCHAR(50),
	Win_Percentage FLOAT(50),
	MOV FLOAT(10),
	ATS FLOAT(10),
	Cover_Percentage FLOAT(50)
);

SELECT * FROM NBA_19to22;