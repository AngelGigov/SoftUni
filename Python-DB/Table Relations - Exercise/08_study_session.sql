CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	student_name VARCHAR(50)
);

INSERT INTO students(student_name)
VALUES
	('Mila'),
	('Toni'),
	('Ron');

CREATE TABLE exams (
	id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 101 INCREMENT BY 1) PRIMARY KEY,
	exam_name VARCHAR(50)
);

INSERT INTO exams(exam_name)
VALUES
	('Python Advanced'),
	('Python OOP'),
	('PostgreSQL');

CREATE TABLE study_halls (
	id SERIAL PRIMARY KEY,
	study_hall_name VARCHAR(50),
	exam_id INTEGER,
	CONSTRAINT fk_study_halls_exams
		FOREIGN KEY (exam_id)
			REFERENCES exams(id)
);

INSERT INTO study_halls(study_hall_name, exam_id)
VALUES
	('Open Source Hall', 102),
	('Inspiration Hall', 101),
	('Creative Hall', 103),
	('Masterclass Hall', 103),
	('Information Security Hall', 103);

CREATE TABLE students_exams (
	student_id INTEGER,
	exam_id INTEGER,

	CONSTRAINT pk_student_id_exam_id
		PRIMARY KEY (student_id, exam_id),

	CONSTRAINT fk_students_exams_students
		FOREIGN KEY (student_id)
			REFERENCES students(id),

	CONSTRAINT fk_students_exams_exams
		FOREIGN KEY (exam_id)
			REFERENCES exams(id)
);

INSERT INTO students_exams(student_id, exam_id)
VALUES
	(1, 101),
	(1, 102),
	(2, 101),
	(3, 103),
	(2, 102),
	(2, 103);