sudo apt install postgresql postgresql-contrib
sudo -i -u postgres

psql

CREATE DATABASE lab3;
\c lab3

CREATE TABLE faculty
(
	id SERIAL,
	course_name varchar(100) UNIQUE NOT NULL,
	deans_office varchar(100) NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO faculty (course_name, deans_office)
VALUES ('09.03.01', 'Gorodnichev M.G.');
INSERT INTO faculty (course_name, deans_office)
VALUES ('15.03.04', 'Ievlev O.P.');

SELECT * FROM faculty;

CREATE TABLE student_group
(
	id SERIAL,
	group_number varchar(100) UNIQUE NOT NULL,
	faculty varchar(100) NOT NULL REFERENCES faculty(course_name),
	PRIMARY KEY (id)
);

INSERT INTO student_group (group_number, faculty)
VALUES ('BVT2201', '09.03.01');
INSERT INTO student_group (group_number, faculty)
VALUES ('BVT2204', '09.03.01');
INSERT INTO student_group (group_number, faculty)
VALUES ('VVT2201', '15.03.04');
INSERT INTO student_group (group_number, faculty)
VALUES ('VVT2204', '15.03.04');

SELECT * FROM student_group;

CREATE TABLE students
(
	id SERIAL,
	name varchar(100) NOT NULL,
	passport varchar(100) NOT NULL,
	group_number varchar(100) NOT NULL REFERENCES student_group(group_number),
	PRIMARY KEY (id)
);

INSERT INTO students (name, passport, group_number)
VALUES ('Bob', '13 13 101101', 'BVT2201');

SELECT * FROM students;