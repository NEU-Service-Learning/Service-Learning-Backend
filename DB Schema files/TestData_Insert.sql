-- Administrator --
insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Lisa', 'Service', 'service-learning@northeastern.edu', 'servicelearning4life', 'admin', true, '2016-11-20', '2016-09-01');

-- Students --
insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Sameer', 'Barde', 'barde.s@husky.neu.edu', 'password123', 'student', true, '2016-11-20', '2016-09-01' );

insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Joe', 'Chen', 'chen.jo@husky.neu.edu', 'password123', 'student', true, '2016-11-20', '2016-09-01');

insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Luke', 'Starr', 'starr.lu@husky.neu.edu', 'password123','student', true, '2016-11-20', '2016-09-01');
    
insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Ryan', 'Lough', 'lough.r@husky.neu.edu', 'password123', 'student', true, '2016-11-20', '2016-09-01');

insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Theodore', 'Tsapakos', 'tsapakos.t@husky.neu.edu', 'password123', 'student', true, '2016-11-20', '2016-09-01');

insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Erik', 'Kaasila', 'kaasila.e@husky.neu.edu', 'password123', 'student', true, '2016-11-20', '2016-09-01');
    
-- Instructor --
insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Mike', 'Weintraub', 'weintraub.m@northeastern.edu', 'password123', 'instructor', true, '2016-11-20', '2016-09-01');

insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Kevin', 'James', 'james.k@northeastern.edu', 'password123', 'student, instructor', true, '2016-11-20', '2016-09-01');
    
insert into User (first_name, last_name, username, pwd, groups, is_active, last_login, date_joined)
	values ('Kevin', 'Smith', 'james.s@northeastern.edu', 'password123', 'instructor', false, '2015-11-20', '2012-09-01');
    
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

insert into Department (name, college_id)
	values ('Mathematics' , 1003);
    

-- Course --
insert into Course (course_number, name, department_id)
	values ('CS4500', 'Software Development', 1001);

insert into Course (course_number, name, department_id)
	values ('CS1200', 'Overview 1', 1001);
    
-- Semester --
insert into Semester (name, start_date, end_date, is_active)
	values ('FALL2016', '2016-08-31', '2016-12-25', true);
    
insert into Semester (name, start_date, end_date, is_active)
	values ('SPRG2017', '2017-01-08', '2017-06-01', false);


-- Enrollment --
insert into Enrollment (user_id, course_number, semester_name, meeting_days, meeting_start_time, meeting_end_time, is_active)
	values (102, 'CS4500', 'FALL2016', 'MWR', '08:00', '09:15', true);
	
insert into Enrollment (user_id, course_number, semester_name, meeting_days, meeting_start_time, meeting_end_time, is_active)
	values (103, 'CS1200', 'FALL2014', 'T', '02:50', '04:30', false);
	
insert into Enrollment (user_id, course_number, semester_name, meeting_days, meeting_start_time, meeting_end_time, is_active)
	values (108, 'CS4500', 'FALL2016', 'TF', '09:50' ,'11:30', true);
	
-- Community Partner --
insert into Community_Partner (name)
	values ('Service Learning');
	
insert into Community_Partner (name)
	values ('America Scores');
	
-- Project --
insert into Project (name, course_number, community_partner_id, start_date, end_date, description, location)
	values ('TimeTracker', 'CS4500', 1001, '2016-09-01', '2016-12-20', 'Time Tracker device for Service Learning', Point(42.3398, 71.0892));
	
insert into Project (name, course_number, community_partner_id, start_date, end_date, description, location)
	values ('America Scores', 'CS4500', 1002, '2016-01-01', '2017-01-01', null, null);
	
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
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (1 , 1001, '2016-08-25', null, 3, null, 2, true, 'Worked at Project A', null);
	
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (2, 1001, '2016-08-25', '08:00', 8.3, null, 2, true, 'Worked at Project A', null);
	
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (1, 1001, '2016-08-25', '08:00', 10, Point(42.3399, 71.0891), 2, false, 'Worked at Project A', null);
	
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (1, 1001, '2016-08-28', '08:00', 1.20, Point(42.3399, 71.0891), 2, true, 'Worked at Project A', null);
	
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (2, 1002, '2016-08-25', '08:00', 5.4, null, 2, false, 'Worked at Project B', null);
	
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (1, 1002, '2016-10-25', '11:00', 5, null, 2, true, null, null);
	
insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (1, 1002, '2016-09-28', '08:00', 4, Point(42.3399, 71.0881), 2, false, 'Worked at Project B', null);

insert into Record (enrollment_id, project_id, date, start_time, total_hours, location, category_id, is_active, comments, extra_field)
	values (1, 1002, '2016-09-28', '08:00', 10, Point(42.3299, 71.0884), 2, true, 'Worked at Project B', null);

	
	
	
	
	
