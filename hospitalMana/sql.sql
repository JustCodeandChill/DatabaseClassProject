insert into Department values ('CRD','Cardiology');
insert into Department values ('ERD','Emergency');
insert into Department values ('NED','Neurology');
insert into Department values ('ICU','Intensive Crew Unit');
insert into Department values ('GYD','Gynecology');
insert into Department values ('GEN','General Med');

select * from Department

insert into Medicine values ('M01','Vicodin',100);
insert into Medicine values ('M02','Simvastatin',110);
insert into Medicine values ('M03','Lisinopril',140);
insert into Medicine values ('M04','Levothyroxine',120);
insert into Medicine values ('M05','Azithromycin',130);
insert into Medicine values ('M06','Metformin',90);
insert into Medicine values ('M07','Lipitor',60);
insert into Medicine values ('M08','Amlodipine',85);
insert into Medicine values ('M09','Amoxicillin',70);
insert into Medicine values ('M10','Hydrochlorothiazide',50);

select * from Medicine

insert into Doctor values ('D01','Lisa','Stephens','4/Dec/1978','F',300000,22000,'ERD');
insert into Doctor values ('D02','Angela','Ortiz','13/Oct/1973','F',280000,50000,'CRD');
insert into Doctor values ('D03','Amy','White','14/Nov/1972','F',320000,78000,'GEN');
insert into Doctor values ('D04','Kimberly','Matthews','2/Jan/1981','F',270000,null,'GYD');
insert into Doctor values ('D05','Michelle','Perry','21/Feb/1986','F',310000,48000,'ICU');
insert into Doctor values ('D06','Jason','Arnold','24/March/1979','M',290000,32000,'NED');
insert into Doctor values ('D07','James','Briggs','20/June/1974','M',340000,null,'ERD');
insert into Doctor values ('D08','John','Dunn','1/May/1988','M',350000,10000,'CRD');
insert into Doctor values ('D09','Micheal','Mann','19/Sep/1969','M',240000,60000,'GEN');
insert into Doctor values ('D10','Christopher','Allen','14/Oct/1972','M',210000,80000,'ICU');
select * from Doctor

insert into doctor_specialize values ('Pain medicine','D01');
insert into doctor_specialize values ('Transplant cardio','D02');
insert into doctor_specialize values ('Adolescent medicine','D03');
insert into doctor_specialize values ('Fetal medicine','D04');
insert into doctor_specialize values ('Hand Surgery','D05');
insert into doctor_specialize values ('Child neurology','D06');
insert into doctor_specialize values ('Emergency service','D07');
insert into doctor_specialize values ('Cardiovascular','D08');
insert into doctor_specialize values ('General Surgery','D09');
insert into doctor_specialize values ('Intensive Surgery','D10');
select * from doctor_specialize

insert into Nurse values ('N01','Thea','Roberts','19/March/1981','F',100000,15000,'ERD',null);
insert into Nurse values ('N02','Gabrielle','Luna','10/Sep/1981','F',140000,10000,'CRD',null);
insert into Nurse values ('N03','Adele','Lee','30/Oct/1981','F',95000,25000,'GEN',null);
insert into Nurse values ('N04','Marie','Sandoval','28/July/1984','F',120000,9000,'GYD',null);
insert into Nurse values ('N05','Beth','Haynes','6/Oct/1984','F',88000,18000,'ICU',null);
insert into Nurse values ('N06','Elmer','Owen','4/Dec/1984','M',150000,12500,'NED',null);
insert into Nurse values ('N07','Johnny','Holt','25/Jan/1985','M',100000,24000,'ERD','N01');
insert into Nurse values ('N08','Bernard','Fox','3/April/1985','M',102000,12000,'CRD','N02');
insert into Nurse values ('N09','William','Riley','11/May/1988','M',108000,13000,'GEN','N03');
insert into Nurse values ('N10','Zack','Vargas','4/June/1988','M',107000,10900,'GEN','N09');
select * from Nurse;

insert into Room values ('R01','N01');
insert into Room values ('R02','N02');
insert into Room values ('R03','N03');
insert into Room values ('R04','N04');
insert into Room values ('R05','N05');
insert into Room values ('R06','N06');
insert into Room values ('R07','N07');
insert into Room values ('R08','N08');
insert into Room values ('R09','N09');
insert into Room values ('R10','N10');
insert into Room values ('R11','N01');
select * from Room;

insert into Patient values ('P01','Barnaby','Atkinson','M','1/Jan/1998','817188489','D01','N01','R01');
insert into Patient values ('P02','Dayna','Falconer','F','6/Feb/1987','719232592','D02','N02','R02');
insert into Patient values ('P03','Elliot','Lawrence','M','8/March/1968','468009254','D03','N03','R03');
insert into Patient values ('P04','Will','Jewell','M','21/May/1985','573137202','D04','N04','R04');
insert into Patient values ('P05','Meagan','Harrelson','F','14/June/1976','548557465','D05','N05','R05');
insert into Patient values ('P06','Cameron','Kemp','M','17/April/1969','723078672','D06','N06','R06');
insert into Patient values ('P07','Hannah','Harrison','F','9/Dec/1977','881305238','D07','N07','R07');
insert into Patient values ('P08','Janna','Moore','F','19/Oct/2000','856835720','D08','N08','R08');
insert into Patient values ('P09','Dean','Hillam','F','12/Nov/1992','841074292','D09','N09','R09');
insert into Patient values ('P10','Ella','Pond','F','18/Aug/1999','898612434','D10','N10','R10');
insert into Patient values ('P11','Jason','Law','F','12/Aug/1989','704128454','D01','N01','R11');
select * from Patient;