--მასწავლებლების ცხრილის შექმნა

CREATE TABLE Teachers (
    ID int, --Primary key
    FirstName varchar(255),
    LastName varchar(255),
    Gender varchar(255),
    [Subject] varchar(255),
    PRIMARY KEY (ID)
);

--მოსწავლეების ცხრილის შექმნა
CREATE TABLE Pupils (
    ID int,
    FirstName varchar(255),
    LastName varchar(255),
    Gender varchar(255),
    Grade int,
    PRIMARY KEY (ID)
);

--დამოკიდებულების ცხრილის შექმნა
CREATE TABLE Pupils_Teachers (
    teacherID int,
    pupilID int,
    FOREIGN KEY (teacherID) REFERENCES Teachers(ID),
    FOREIGN KEY (pupilID) REFERENCES Pupils(ID)
);

--ეს select წამოიღებს ყველა იმ მასწავლებლის სახელს და გვარს რომლებიც ასწავლიან მოსწავლეს, რომელსაც ქვია გიორგი
SELECT 
    teacher.FirstName,
    teacher.LastName
FROM Pupils pupil
LEFT JOIN Pupils_Teachers p_t on pupil.ID = p_t.pupilID and pupil.FirstName = N'გიორგი'
LEFT JOIN Teachers teacher on teacher.ID = p_t.teacherID
GROUP BY teacher.FirstName, teacher.LastName