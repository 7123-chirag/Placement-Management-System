create database placementguideDB;
use placementguideDB;
CREATE TABLE Users
(
    UserID INT IDENTITY(1,1) PRIMARY KEY,

    FullName NVARCHAR(100) NOT NULL,

    Email NVARCHAR(150) UNIQUE NOT NULL,

    PasswordHash NVARCHAR(255) NOT NULL,

    Branch NVARCHAR(50) NOT NULL,

    College NVARCHAR(150) NOT NULL,

    CreatedAt DATETIME DEFAULT GETDATE()
);
select * from users
select*from users
CREATE TABLE ResumeAnalysis (

    AnalysisID INT IDENTITY(1,1) PRIMARY KEY,

    UserID INT NOT NULL,

    ResumeFile NVARCHAR(255),

    ATSScore FLOAT,

    FoundSkills NVARCHAR(MAX),

    MissingSkills NVARCHAR(MAX),

    UploadDate DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)

);
CREATE TABLE PlacementPredictions (

    PredictionID INT IDENTITY(1,1) PRIMARY KEY,

    UserID INT NOT NULL,

    CGPA FLOAT,

    Skills INT,

    Projects INT,

    Internships INT,

    Certifications INT,

    Coding FLOAT,

    Communication FLOAT,

    DSA INT,

    Backlogs INT,

    PlacementChance FLOAT,

    CreatedAt DATETIME DEFAULT GETDATE(),

    FOREIGN KEY(UserID)
    REFERENCES Users(UserID)

);
CREATE TABLE InterviewHistory (

    InterviewID INT IDENTITY(1,1) PRIMARY KEY,

    UserID INT NOT NULL,

    Company NVARCHAR(100),

    Role NVARCHAR(100),

    InterviewType NVARCHAR(50),

    Difficulty NVARCHAR(50),

    DateTaken DATETIME DEFAULT GETDATE(),

    FOREIGN KEY(UserID)
    REFERENCES Users(UserID)

);
select * from  ResumeAnalysis
SELECT * FROM PlacementPredictions;
SELECT TOP 1 * FROM PlacementPredictions;
SELECT TOP 1 * FROM ResumeAnalysis;