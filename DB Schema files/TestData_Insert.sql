-- Administrator --
insert into Administrator (first_name, last_name, user, pwd)
	values ('Lisa', 'Service', 'service-learning@northeastern.edu', 'servicelearning4life');

-- Students --
insert into Student (first_name, last_name, user, pwd)
	values ('Sameer', 'Barde', 'barde.s@husky.neu.edu', 'password123');

insert into Student (first_name, last_name, user, pwd)
	values ('Joe', 'Chen', 'chen.jo@husky.neu.edu', 'password123');

insert into Student (first_name, last_name, user, pwd)
	values ('Luke', 'Starr', 'starr.lu@husky.neu.edu', 'password123');
    
insert into Student (first_name, last_name, user, pwd)
	values ('Ryan', 'Lough', 'lough.r@husky.neu.edu', 'password123');

insert into Student (first_name, last_name, user, pwd)
	values ('Theodore', 'Tsapakos', 'tsapakos.t@husky.neu.edu', 'password123');

insert into Student (first_name, last_name, user, pwd)
	values ('Erik', 'Kaasila', 'kaasila.e@husky.neu.edu', 'password123');
    
-- College --
insert into College (name)
	values ('College of Computer and Information Science');
    
insert into College (name)
	values ('D\'Amore-McKim School of Business');
    
insert into College (name)
	values ('College of Science');
    
insert into College (name)
	values ('Bouvé College of Health Sciences');
    
insert into College (name)
	values ('School of Law');

-- Department --
insert into Department (name, college_id)
	values ('Computer Science' , 1001);
    
insert into Department (name, college_id)
	values ('Biology' , 1003);
    
-- Instructor --
insert into Instructor (first_name, last_name, user, pwd, role)
	values ('Mike', 'Weintraub', 'weintraub.m@northeastern.edu', 'password123', true);

insert into Instructor (first_name, last_name, user, pwd, role)
	values ('Kevin', 'James', 'james.k@northeastern.edu', 'password123', true);
    
insert into Instructor (first_name, last_name, user, pwd, role)
	values ('Kevin', 'Smith', 'james.s@northeastern.edu', 'password123', false);
    
-- Course --
insert into Course (course_no, name, semester_id, instructor_id, start_date, end_date, department_id)
	values ('CS4500', 'Software Development', 'FALL2016', 101, '2016-09-01', '2016-12-20', 1001);

insert into Course (course_no, name, semester_id, instructor_id, start_date, end_date, department_id)
	values ('CS1200', 'Overview 1','Spring2015', 102, '2016-08-01', '2017-01-01', 1001);
	
-- Enrollment --
insert into Enrollment (student_id, course_no, current_class)
	values (101, 'CS4500', true);
	
insert into Enrollment (student_id, course_no, current_class)
	values (102, 'CS1200', false);
	
insert into Enrollment (student_id, course_no, current_class)
	values (105, 'CS1200', true);
	
-- Community Partner --
insert into Community_Partner (name)
	values ('Service Learning');
	
insert into Community_Partner (name)
	values ('America Scores');
	
-- Project --
insert into Project (name, community_partner_id, start_date, end_date, description)
	values ('TimeTracker', 1001, '2016-09-01', '2016-12-20', 'Time Tracker device for Service Learning');
	
insert into Project (name, community_partner_id, start_date, end_date, description)
	values ('America Scores', 1002, '2016-01-01', '2017-01-01', null);
	
-- Project Location --
insert into Project_Location (project_id, name, location)
	values (1001, 'Northeastern University', Point(42.3398, 71.0892));
	
insert into Project_Location (project_id, name, location)
	values (1002, 'Roxbury', Point(42.3152, 71.0914));
	
-- Record_Category --
insert into Record_Category (name)
	values ('Direct Service');

insert into Record_Category (name)
	values ('Training Events');
	
insert into Record_Category (name)
	values ('Individual Planning/Research/Projects');
	
insert into Record_Category (name)
	values ('Team Planning/Group Work');
	
-- Record --
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (101, 'CS4500', 1001, '2016-08-25', 3, 1, 2, 'Worked at Project A', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (102, 'CS4500', 1001, '2016-08-25', 3, 1, 2, 'Worked at Project A', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (103, 'CS4500', 1001, '2016-08-25', 3, 1, 2, 'Worked at Project A', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (104, 'CS4500', 1001, '2016-08-25', 3, 1, 2, 'Worked at Project A', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (105, 'CS4500', 1001, '2016-08-25', 3, 1, 2, 'Worked at Project A', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (106, 'CS4500', 1001, '2016-08-25', 3, 1, 2, 'Worked at Project A', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (102, 'CS1200', 1002, '2016-12-25', 12, 2, 4, 'Worked at Project B', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (103, 'CS1200', 1002, '2016-12-25', .25, 2, 4, 'Worked at Project B', null);
	
insert into Record (student_id, course_no, project_id, date, total_hours, location_id, category_id, comments, extra_field)
	values (101, 'CS4500', 1001, '2016-12-15', 12.25, 2, 4, 'Worked at Project C', null);
	
	
	
	
	
	
	
