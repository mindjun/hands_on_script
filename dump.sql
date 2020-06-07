PRAGMA foreign_keys=OFF;

DROP TABLE IF EXISTS ab_permission;
CREATE TABLE IF NOT EXISTS `ab_permission` (

	id INTEGER NOT NULL, 

	name VARCHAR(100) NOT NULL, 

	PRIMARY KEY (id), 

	UNIQUE (name)

);

INSERT INTO ab_permission VALUES(14,'Copy Role');

INSERT INTO ab_permission VALUES(5,'can_add');

INSERT INTO ab_permission VALUES(15,'can_chart');

INSERT INTO ab_permission VALUES(4,'can_delete');

INSERT INTO ab_permission VALUES(9,'can_download');

INSERT INTO ab_permission VALUES(6,'can_edit');

INSERT INTO ab_permission VALUES(17,'can_hello');

INSERT INTO ab_permission VALUES(3,'can_list');

INSERT INTO ab_permission VALUES(16,'can_message');

INSERT INTO ab_permission VALUES(8,'can_show');

INSERT INTO ab_permission VALUES(2,'can_this_form_get');

INSERT INTO ab_permission VALUES(1,'can_this_form_post');

INSERT INTO ab_permission VALUES(7,'can_userinfo');

INSERT INTO ab_permission VALUES(13,'menu_access');

INSERT INTO ab_permission VALUES(10,'resetmypassword');

INSERT INTO ab_permission VALUES(11,'resetpasswords');

INSERT INTO ab_permission VALUES(12,'userinfoedit');

DROP TABLE IF EXISTS ab_view_menu;
CREATE TABLE IF NOT EXISTS `ab_view_menu` (

	id INTEGER NOT NULL, 

	name VARCHAR(100) NOT NULL, 

	PRIMARY KEY (id), 

	UNIQUE (name)

);

INSERT INTO ab_view_menu VALUES(7,'AuthDBView');

INSERT INTO ab_view_menu VALUES(16,'Base Permissions');

INSERT INTO ab_view_menu VALUES(1,'IndexView');

INSERT INTO ab_view_menu VALUES(12,'List Roles');

INSERT INTO ab_view_menu VALUES(9,'List Users');

INSERT INTO ab_view_menu VALUES(3,'LocaleView');

INSERT INTO ab_view_menu VALUES(21,'MyView');

INSERT INTO ab_view_menu VALUES(20,'Permission on Views/Menus');

INSERT INTO ab_view_menu VALUES(15,'PermissionModelView');

INSERT INTO ab_view_menu VALUES(19,'PermissionViewModelView');

INSERT INTO ab_view_menu VALUES(5,'ResetMyPasswordView');

INSERT INTO ab_view_menu VALUES(4,'ResetPasswordView');

INSERT INTO ab_view_menu VALUES(11,'RoleModelView');

INSERT INTO ab_view_menu VALUES(10,'Security');

INSERT INTO ab_view_menu VALUES(14,'User''s Statistics');

INSERT INTO ab_view_menu VALUES(8,'UserDBModelView');

INSERT INTO ab_view_menu VALUES(6,'UserInfoEditView');

INSERT INTO ab_view_menu VALUES(13,'UserStatsChartView');

INSERT INTO ab_view_menu VALUES(2,'UtilView');

INSERT INTO ab_view_menu VALUES(17,'ViewMenuModelView');

INSERT INTO ab_view_menu VALUES(18,'Views/Menus');

DROP TABLE IF EXISTS ab_role;
CREATE TABLE IF NOT EXISTS `ab_role` (

	id INTEGER NOT NULL, 

	name VARCHAR(64) NOT NULL, 

	PRIMARY KEY (id), 

	UNIQUE (name)

);

INSERT INTO ab_role VALUES(1,'Admin');

INSERT INTO ab_role VALUES(2,'Public');

DROP TABLE IF EXISTS ab_user;
CREATE TABLE IF NOT EXISTS `ab_user` (

	id INTEGER NOT NULL, 

	first_name VARCHAR(64) NOT NULL, 

	last_name VARCHAR(64) NOT NULL, 

	username VARCHAR(64) NOT NULL, 

	password VARCHAR(256), 

	active BOOLEAN, 

	email VARCHAR(64) NOT NULL, 

	last_login DATETIME, 

	login_count INTEGER, 

	fail_login_count INTEGER, 

	created_on DATETIME, 

	changed_on DATETIME, 

	created_by_fk INTEGER, 

	changed_by_fk INTEGER, 

	PRIMARY KEY (id), 

	UNIQUE (username), 

	CHECK (active IN (0, 1)), 

	UNIQUE (email), 

	FOREIGN KEY(created_by_fk) REFERENCES ab_user (id), 

	FOREIGN KEY(changed_by_fk) REFERENCES ab_user (id)

);

INSERT INTO ab_user VALUES(1,'admin','admin','admin','pbkdf2:sha256:50000$m2U3dt1i$5e14e32b491074a6b094988a99997708e0f9c6d2e2863bcf731c13b7e4118be9',1,'admin','2018-07-27 23:58:06.013398',1,0,'2018-07-27 23:57:42.112119','2018-07-27 23:57:42.112140',NULL,NULL);

DROP TABLE IF EXISTS ab_register_user;
CREATE TABLE IF NOT EXISTS `ab_register_user` (

	id INTEGER NOT NULL, 

	first_name VARCHAR(64) NOT NULL, 

	last_name VARCHAR(64) NOT NULL, 

	username VARCHAR(64) NOT NULL, 

	password VARCHAR(256), 

	email VARCHAR(64) NOT NULL, 

	registration_date DATETIME, 

	registration_hash VARCHAR(256), 

	PRIMARY KEY (id), 

	UNIQUE (username)

);

DROP TABLE IF EXISTS ab_permission_view;
CREATE TABLE IF NOT EXISTS `ab_permission_view` (

	id INTEGER NOT NULL, 

	permission_id INTEGER, 

	view_menu_id INTEGER, 

	PRIMARY KEY (id), 

	UNIQUE (permission_id, view_menu_id), 

	FOREIGN KEY(permission_id) REFERENCES ab_permission (id), 

	FOREIGN KEY(view_menu_id) REFERENCES ab_view_menu (id)

);

INSERT INTO ab_permission_view VALUES(1,1,4);

INSERT INTO ab_permission_view VALUES(3,1,5);

INSERT INTO ab_permission_view VALUES(5,1,6);

INSERT INTO ab_permission_view VALUES(2,2,4);

INSERT INTO ab_permission_view VALUES(4,2,5);

INSERT INTO ab_permission_view VALUES(6,2,6);

INSERT INTO ab_permission_view VALUES(7,3,8);

INSERT INTO ab_permission_view VALUES(19,3,11);

INSERT INTO ab_permission_view VALUES(29,3,15);

INSERT INTO ab_permission_view VALUES(31,3,17);

INSERT INTO ab_permission_view VALUES(33,3,19);

INSERT INTO ab_permission_view VALUES(8,4,8);

INSERT INTO ab_permission_view VALUES(20,4,11);

INSERT INTO ab_permission_view VALUES(9,5,8);

INSERT INTO ab_permission_view VALUES(21,5,11);

INSERT INTO ab_permission_view VALUES(10,6,8);

INSERT INTO ab_permission_view VALUES(22,6,11);

INSERT INTO ab_permission_view VALUES(11,7,8);

INSERT INTO ab_permission_view VALUES(12,8,8);

INSERT INTO ab_permission_view VALUES(23,8,11);

INSERT INTO ab_permission_view VALUES(13,9,8);

INSERT INTO ab_permission_view VALUES(24,9,11);

INSERT INTO ab_permission_view VALUES(14,10,8);

INSERT INTO ab_permission_view VALUES(15,11,8);

INSERT INTO ab_permission_view VALUES(16,12,8);

INSERT INTO ab_permission_view VALUES(17,13,9);

INSERT INTO ab_permission_view VALUES(18,13,10);

INSERT INTO ab_permission_view VALUES(26,13,12);

INSERT INTO ab_permission_view VALUES(28,13,14);

INSERT INTO ab_permission_view VALUES(30,13,16);

INSERT INTO ab_permission_view VALUES(32,13,18);

INSERT INTO ab_permission_view VALUES(34,13,20);

INSERT INTO ab_permission_view VALUES(25,14,11);

INSERT INTO ab_permission_view VALUES(27,15,13);

INSERT INTO ab_permission_view VALUES(35,16,21);

INSERT INTO ab_permission_view VALUES(36,17,21);

DROP TABLE IF EXISTS ab_user_role;
CREATE TABLE IF NOT EXISTS `ab_user_role` (

	id INTEGER NOT NULL, 

	user_id INTEGER, 

	role_id INTEGER, 

	PRIMARY KEY (id), 

	UNIQUE (user_id, role_id), 

	FOREIGN KEY(user_id) REFERENCES ab_user (id), 

	FOREIGN KEY(role_id) REFERENCES ab_role (id)

);

INSERT INTO ab_user_role VALUES(1,1,1);

DROP TABLE IF EXISTS ab_permission_view_role;
CREATE TABLE IF NOT EXISTS `ab_permission_view_role` (

	id INTEGER NOT NULL, 

	permission_view_id INTEGER, 

	role_id INTEGER, 

	PRIMARY KEY (id), 

	UNIQUE (permission_view_id, role_id), 

	FOREIGN KEY(permission_view_id) REFERENCES ab_permission_view (id), 

	FOREIGN KEY(role_id) REFERENCES ab_role (id)

);

INSERT INTO ab_permission_view_role VALUES(1,1,1);

INSERT INTO ab_permission_view_role VALUES(2,2,1);

INSERT INTO ab_permission_view_role VALUES(3,3,1);

INSERT INTO ab_permission_view_role VALUES(4,4,1);

INSERT INTO ab_permission_view_role VALUES(5,5,1);

INSERT INTO ab_permission_view_role VALUES(6,6,1);

INSERT INTO ab_permission_view_role VALUES(7,7,1);

INSERT INTO ab_permission_view_role VALUES(8,8,1);

INSERT INTO ab_permission_view_role VALUES(9,9,1);

INSERT INTO ab_permission_view_role VALUES(10,10,1);

INSERT INTO ab_permission_view_role VALUES(11,11,1);

INSERT INTO ab_permission_view_role VALUES(12,12,1);

INSERT INTO ab_permission_view_role VALUES(13,13,1);

INSERT INTO ab_permission_view_role VALUES(14,14,1);

INSERT INTO ab_permission_view_role VALUES(15,15,1);

INSERT INTO ab_permission_view_role VALUES(16,16,1);

INSERT INTO ab_permission_view_role VALUES(17,17,1);

INSERT INTO ab_permission_view_role VALUES(18,18,1);

INSERT INTO ab_permission_view_role VALUES(19,19,1);

INSERT INTO ab_permission_view_role VALUES(20,20,1);

INSERT INTO ab_permission_view_role VALUES(21,21,1);

INSERT INTO ab_permission_view_role VALUES(22,22,1);

INSERT INTO ab_permission_view_role VALUES(23,23,1);

INSERT INTO ab_permission_view_role VALUES(24,24,1);

INSERT INTO ab_permission_view_role VALUES(25,25,1);

INSERT INTO ab_permission_view_role VALUES(26,26,1);

INSERT INTO ab_permission_view_role VALUES(27,27,1);

INSERT INTO ab_permission_view_role VALUES(28,28,1);

INSERT INTO ab_permission_view_role VALUES(29,29,1);

INSERT INTO ab_permission_view_role VALUES(30,30,1);

INSERT INTO ab_permission_view_role VALUES(31,31,1);

INSERT INTO ab_permission_view_role VALUES(32,32,1);

INSERT INTO ab_permission_view_role VALUES(33,33,1);

INSERT INTO ab_permission_view_role VALUES(34,34,1);

INSERT INTO ab_permission_view_role VALUES(35,35,1);

INSERT INTO ab_permission_view_role VALUES(36,36,1);

