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
insert into Course (course_number, name, semester_id, department_id)
	values ('CS4500', 'Software Development', 'FALL2016', 1001);

insert into Course (course_number, name, semester_id, department_id)
	values ('CS1200', 'Overview 1','SPRG2015', 1001);
	
-- Enrollment --
insert into Enrollment (user_id, course_number, current_class)
	values (101, 'CS4500', true);
	
insert into Enrollment (user_id, course_number, current_class)
	values (102, 'CS1200', false);
	
insert into Enrollment (user_id, course_number, current_class)
	values (105, 'CS1200', true);
	
-- Community Partner --
insert into Community_Partner (name)
	values ('Service Learning');
	
insert into Community_Partner (name)
	values ('America Scores');
	
-- Project --
insert into Project (name, community_partner_id, start_date, end_date, description, location)
	values ('TimeTracker', 1001, '2016-09-01', '2016-12-20', 'Time Tracker device for Service Learning', Point(42.3398, 71.0892));
	
insert into Project (name, community_partner_id, start_date, end_date, description, location)
	values ('America Scores', 1002, '2016-01-01', '2017-01-01', null, null);
	
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
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (101, 'CS4500', 1001, '2016-08-25', 3, null, 2, 'Worked at Project A', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (102, 'CS4500', 1001, '2016-08-25', 3, null, 2, 'Worked at Project A', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (103, 'CS4500', 1001, '2016-08-25', 3, Point(42.3399, 71.0891), 2, 'Worked at Project A', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (104, 'CS4500', 1001, '2016-08-25', 3, Point(42.3398, 71.0892), 2, 'Worked at Project A', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (105, 'CS4500', 1001, '2016-08-25', 3, null, 2, 'Worked at Project A', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (106, 'CS4500', 1001, '2016-08-25', 3, null, 2, 'Worked at Project A', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (102, 'CS1200', 1002, '2016-12-25', 12, Point(42.3378, 71.0892), 4, 'Worked at Project B', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (103, 'CS1200', 1002, '2016-12-25', 0.25, Point(42.3398, 71.0822), 4, 'Worked at Project B', null);
	
insert into Record (user_id, course_number, project_id, date, total_hours, location, category_id, comments, extra_field)
	values (101, 'CS4500', 1001, '2016-12-15', 12.25, Point(42.3398, 71.0899), 4, 'Worked at Project C', null);
	
	
	
	
	
	
	
