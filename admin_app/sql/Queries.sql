-- get all members names lists
SELECT (First_Name, Last_Name) AS Name FROM Member;

-- get info on PTSessions
SELECT PTSession_ID, Location, Trainer_ID FROM Personal_Training_Session;

-- get all billing history for a member
SELECT * FROM Billing WHERE Member_ID = 2;

-- get all broken equipment checks
SELECT * FROM Equipment_Condition WHERE Is_Broken = true;

-- get all trainers and their associated names from Member
SELECT Trainer.Trainer_ID, Member.First_Name, Member.Last_Name
FROM Trainer
JOIN Member ON Trainer.Member_ID = Member.Member_ID;

-- get all health metrics for a member
SELECT * FROM Health_Metrics WHERE Member_ID = 1;

-- get admin info
SELECT Admin.Admin_ID, Member.First_Name, Member.Last_Name
FROM Admin
JOIN Member ON Admin.Member_ID = Member.Member_ID;

-- update sleep health of a member from poor to good
UPDATE Health_Metrics
SET Sleep = 'Good'
WHERE Member_ID = 1;

-- reward more loyalty points to a member
UPDATE Member
SET Loyalty_Points = Loyalty_Points + 10
WHERE Member_ID = 1;

-- insert new PTSession
INSERT INTO Personal_Training_Session (Member_ID, Location, Date, Start_Time, End_Time, Trainer_ID)
VALUES (1, 'Gym A', '2023-12-31', '08:00:00', '09:00:00', 1);

-- add new billing record
INSERT INTO Billing (Member_ID, Amount, Due_Date, Is_Paid, Loyalty_Points)
VALUES (1, 100.00, '2023-12-31', false, 5.00);

-- delete log entry
DELETE FROM Personal_Training_Log
WHERE PTSLog_ID = 1;


-- POPULATE DATABASE --
INSERT INTO Member (First_Name, Last_Name, Date_of_Birth, Loyalty_Points)
VALUES ('John', 'Doe', '1990-01-15', 50.00),
       ('Daffy', 'Duck', '1985-05-20', 30.00),
       ('Donald', 'Duck', '1986-05-20', 30.00),
       ('Mickey', 'Mouse', '1993-09-08', 10.00);

-- Inserting data into the Trainer table
INSERT INTO Trainer (Member_ID)
VALUES ((SELECT Member_ID FROM Member WHERE First_Name = 'John' AND Last_Name = 'Doe')),
       ((SELECT Member_ID FROM Member WHERE First_Name = 'Daffy' AND Last_Name = 'Duck')),
       ((SELECT Member_ID FROM Member WHERE First_Name = 'Donald' AND Last_Name = 'Duck')),
       ((SELECT Member_ID FROM Member WHERE First_Name = 'Mickey' AND Last_Name = 'Mouse'));

-- Inserting data into the Health_Metrics table
INSERT INTO Health_Metrics (Member_ID, Heart_Rate, Sleep)
VALUES (5, 70, 'Good'),
       (6, 65, 'Poor'),
       (7, 80, 'Sporatic');

-- Inserting data into the Personal_Fitness_Goals table
INSERT INTO Personal_Fitness_Goals (Goal, Member_ID)
VALUES ('Jump higher', 7),
       ('Build muscle', 8),
       ('Improve dexterity', 6);

-- Inserting data into the Event table
INSERT INTO Event (Location, Date, Trainer_ID, Event_Type, Capacity, Event_Name)
VALUES ('Gym A', '2023-12-15', 8, 'Workout', 30, 'Fitness Class A'),
       ('Gym B', '2023-12-20', 9, 'Yoga', 20, 'Yoga Workshop'),
       ('Outdoor Park', '2023-12-25', 10, 'Running', 50, 'Morning Run');

-- Inserting data into the Personal_Training_Session table
INSERT INTO Personal_Training_Session (Member_ID, Location, Date, Start_Time, End_Time, Trainer_ID)
VALUES (5, 'Gym A', '2023-12-10', '10:00:00', '11:00:00', 7),
       (6, 'Gym B', '2023-12-12', '14:00:00', '15:00:00', 8),
       (7, 'Outdoor Pavillion', '2023-12-14', '07:00:00', '08:00:00', 9);

-- Inserting data into the Personal_Training_Log table
INSERT INTO Personal_Training_Log (PTSession_ID, Notes)
VALUES (10, 'Focused on cardio and strength training'),
       (11, 'Transitionned into yoga poses and pilates stretches'),
       (12, 'Emphasized interval running, completed endurance test');

-- Inserting data into the Billing table
INSERT INTO Billing (Member_ID, Amount, Due_Date, Is_Paid, Loyalty_Points)
VALUES (5, 50.00, '2023-12-20', true, 5.00),
       (6, 75.00, '2023-12-22', false, 2.50),
       (7, 30.00, '2023-12-18', true, 7.00);

-- Inserting data into the Room_Booking table
INSERT INTO Room_Booking (Trainer_ID, Purpose, Location, Date, Start_Time, End_Time)
VALUES (8, 'Training Session', 'Gym A', '2023-12-10', '12:00:00', '13:00:00'),
       (9, 'Yoga Class', 'Gym B', '2023-12-15', '16:00:00', '17:00:00'),
       (10, 'Running Group', 'Outdoor Park', '2023-12-18', '08:00:00', '09:00:00');

-- Inserting data into the Admin table
INSERT INTO Admin (Member_ID)
VALUES (5), (6);

-- Inserting data into the Equipment_Condition table
INSERT INTO Equipment_Condition (Admin_ID, Date_Checked, Description, Is_Broken, Location, Equipment_Type)
VALUES (3, '2023-12-05', 'Treadmill noise complaint, motor sqeaks', true, 'Gym A', 'Treadmill'),
       (4, '2023-12-08', 'Yoga mat frayed', false, 'Gym B', 'Yoga Mat');