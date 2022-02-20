CREATE TABLE COMPANY
    (Company_ID            INTEGER        NOT NULL        PRIMARY KEY    AUTOINCREMENT,
     Company_Name          VARCHAR(20)    NOT NULL);

CREATE TABLE USER
    (Username              VARCHAR(20)    NOT NULL,
     Password              VARCHAR(20)    NOT NULL,
     Company_ID            INTEGER        NOT NULL,
CONSTRAINT USER_PK PRIMARY KEY (Username),
CONSTRAINT USER_FK FOREIGN KEY (Company_ID) REFERENCES COMPANY (Company_ID));

CREATE TABLE DEPARTMENT
    (Department_ID         INTEGER        NOT NULL        PRIMARY KEY    AUTOINCREMENT,
     Department_Name       VARCHAR(20)    NOT NULL);
     
CREATE TABLE EMPLOYEE
    (Employee_ID           INTEGER        NOT NULL        PRIMARY KEY    AUTOINCREMENT,
     Company_ID            INTEGER        NOT NULL,
     First_Name            VARCHAR(20)    NOT NULL,
     Middle_Name           VARCHAR(20),
     Last_Name             VARCHAR(20)    NOT NULL,
     Gender                VARCHAR(6)     NOT NULL     CHECK (Gender IN ('Male', 'Female')),
     Department_ID         INTEGER        NOT NULL,
     Position              VARCHAR(20)    NOT NULL,
     Regular_Rate          DECIMAL(4,2)   NOT NULL,
     Overtime_Rate         DECIMAL(4,2)   NOT NULL,
     Phone_No              VARCHAR(11),
     Email                 VARCHAR(20),
     House_No              VARCHAR(25),
     Street_Name           VARCHAR(25),
     Subdivision           VARCHAR(25),
     Barangay              VARCHAR(25),
     City                  VARCHAR(25),
     Zip_Code              INTEGER,
UNIQUE (Employee_ID, Company_ID)
CONSTRAINT EMPLOYEE_FK1 FOREIGN KEY (Company_ID) REFERENCES COMPANY (Company_ID),
CONSTRAINT EMPLOYEE_FK2 FOREIGN KEY (Department_ID) REFERENCES DEPARTMENT (Department_ID));

CREATE TABLE SALARY
    (Reference_No         INTEGER         NOT NULL        PRIMARY KEY    AUTOINCREMENT,
     Date                 DATE            NOT NULL,
     Employee_ID          INTEGER         NOT NULL,
     Hours_Worked         DECIMAL(4,2)    NOT NULL,
     SSS                  DECIMAL(10,2)   NOT NULL,
     HDMF                 DECIMAL(10,2)   NOT NULL,
     PhilHealth           DECIMAL(10,2)   NOT NULL,
     Withholding_Tax      DECIMAL(10,2)   NOT NULL,
     Basic_Pay            DECIMAL(10,2)   NOT NULL,
     Overtime_Pay         DECIMAL(10,2)   NOT NULL,
     Net_Pay              DECIMAL(10,2)   NOT NULL,
CONSTRAINT SALARY_FK FOREIGN KEY (Employee_ID) REFERENCES EMPLOYEE (Employee_ID));