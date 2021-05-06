USE master
GO

IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'SwimmingDB'
)
CREATE DATABASE SwimmingDB
GO

-- Create tables
USE SwimmingDB
CREATE TABLE Cities (
    CityName VARCHAR(30) PRIMARY KEY
);

CREATE TABLE Clubs (
    ShortName CHAR(5) PRIMARY KEY,
    ClubName VARCHAR(70),
    CityName VARCHAR(30),
    FOREIGN KEY (CityName) REFERENCES Cities(CityName)
);

CREATE TABLE Coaches (
    CoachID INT IDENTITY(1, 1) PRIMARY KEY,
    LastName VARCHAR(50),
    FirstName VARCHAR(50),
    ClubShortName CHAR(5),
    FOREIGN KEY (ClubShortName) REFERENCES Clubs(ShortName)

);

CREATE TABLE Swimmers (
    SwimmerID INT IDENTITY(1, 1) PRIMARY KEY,
    LastName VARCHAR(50),
    FirstName VARCHAR(50),
    Sex INT CHECK (Sex IN (0, 1, 2)), -- 0=Not Known 1=Male 2=Female  
                                    -- see:https://en.wikipedia.org/wiki/ISO/IEC_5218 
    ClubShortName CHAR(5),
    CoachID INT,
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID),
    FOREIGN KEY (ClubShortName) REFERENCES Clubs(ShortName)
);

CREATE TABLE Distances (
    DistanceName VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Starts (
    StartID INT IDENTITY(1,1) PRIMARY KEY,
    SwimmerID INT REFERENCES Swimmers(SwimmerID),
    StartDate DATE,
    SwimTime TIME(2),
    DistanceName VARCHAR(50) REFERENCES Distances(DistanceName)
);
GO

-- Insert data
INSERT INTO Cities
VALUES 
    ('Warszawa'),
    ('Wrocław'),
    ('Poznań')

INSERT INTO Clubs
VALUES
    ('G8WAW', 'G8 Bielany Warszawa', 'Warszawa'),
    ('WAPOZ', 'Warta Poznań', 'Poznań'),
    ('JUWRO', 'Juvenia Wrocław', 'Wrocław')

INSERT INTO Distances
VALUES 
    ('50 dowolny'),
    ('100 dowolny'),
    ('200 motylkowy')


INSERT INTO Coaches 
    (LastName, FirstName, ClubShortName)
VALUES
    ('Wołkow', 'Paweł', 'G8WAW'),
    ('Drynkowski', 'Łukasz', 'G8WAW'),
    ('Szymański', 'Michał', 'WAPOZ'),
    ('Widanka', 'Grzegorz', 'JUWRO')

INSERT INTO Swimmers 
    (LastName, FirstName, Sex, ClubShortName, CoachID)
VALUES 
    ('Tchórz', 'Alicja', 2, 'JUWRO', 4),
    ('Majchrzak', 'Kacper', 1, 'WAPOZ', 3),
    ('Stokowski', 'Kacper', 1, 'G8WAW', 1)

INSERT INTO Starts 
    (SwimmerID, StartDate, SwimTime, DistanceName)
VALUES 
    (1, '2021-04-28', '00:00:25.67', '50 dowolny'),
    (2, '2021-04-29', '00:00:49.32', '100 dowolny'),
    (3, '2021-04-28', '00:00:50.71', '100 dowolny')
