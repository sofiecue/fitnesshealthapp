
CREATE TABLE Member (
    Member_ID SERIAL PRIMARY KEY,
    First_Name varchar(20) NOT NULL,
    Last_Name varchar(20) NOT NULL,
    Date_of_Birth DATE DEFAULT CURRENT_DATE,
    Loyalty_Points numeric(12,2) CHECK (Loyalty_Points > 0)
);

CREATE TABLE Trainer (
    Trainer_ID SERIAL PRIMARY KEY,
    Member_ID SERIAL REFERENCES Member(Member_ID)
);


CREATE TABLE Health_Metrics (
    Health_Metrics_ID SERIAL PRIMARY KEY,
    Member_ID SERIAL,
    Heart_Rate		numeric(3,0) check (Heart_Rate > 0),
    Sleep varchar(8),
	foreign key (Member_ID) REFERENCES Member
		on delete set null
);

CREATE TABLE Personal_Fitness_Goals (
    PFG_ID SERIAL,
	Goal TEXT NOT NULL,
	primary key (PFG_ID),
    Member_ID SERIAL REFERENCES Member
		on delete set null
);

CREATE TABLE Event (
    Event_ID SERIAL PRIMARY KEY,
    Location varchar(15),
    Date DATE DEFAULT CURRENT_DATE,
	Trainer_ID SERIAL,
    Event_Type varchar(15),
    Capacity numeric(4,0),
    Event_Name varchar(15) NOT NULL,
	foreign key (Trainer_ID) REFERENCES Trainer
		on delete set null
);

CREATE TABLE Personal_Training_Session (
    PTSession_ID SERIAL PRIMARY KEY,
    Member_ID SERIAL REFERENCES Member(Member_ID),
    Location varchar(20) NOT NULL,
    Date DATE DEFAULT CURRENT_DATE,
    Start_Time TIME,
    End_Time TIME,
    Trainer_ID SERIAL REFERENCES Trainer(Trainer_ID)
);

CREATE TABLE Personal_Training_Log (
    PTSLog_ID SERIAL PRIMARY KEY,
    PTSession_ID SERIAL REFERENCES Personal_Training_Session(PTSession_ID),
    Notes text
);

CREATE TABLE Billing (
    Bill_ID SERIAL PRIMARY KEY,
    Member_ID SERIAL REFERENCES Member(Member_ID),
    Amount numeric(8,2),
    Due_Date DATE DEFAULT CURRENT_DATE,
    Is_Paid boolean,
    Loyalty_Points numeric(12,2) CHECK (Loyalty_Points >= 0)
);

CREATE TABLE Room_Booking (
    Room_ID SERIAL PRIMARY KEY,
    Trainer_ID SERIAL REFERENCES Trainer(Trainer_ID),
    Purpose varchar(25),
    Location varchar(15),
    Date DATE DEFAULT CURRENT_DATE,
    Start_Time TIME,
    End_Time TIME
);

CREATE TABLE Admin (
    Admin_ID SERIAL PRIMARY KEY,
    Member_ID SERIAL REFERENCES Member(Member_ID)
);


CREATE TABLE Equipment_Condition (
    ECondition_ID SERIAL PRIMARY KEY,
    Admin_ID SERIAL REFERENCES Admin(Admin_ID),
    Date_Checked DATE DEFAULT CURRENT_DATE,
    Description text,
    Is_Broken boolean,
    Location varchar(15),
    Equipment_Type varchar(15)
);
