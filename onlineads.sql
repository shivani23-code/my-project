# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                 127.0.0.1
# Database:             onlineads
# Server version:       5.4.3-beta-community
# Server OS:            Win32
# Target-Compatibility: Standard ANSI SQL
# HeidiSQL version:     3.1 RC1 Revision: 1064
# --------------------------------------------------------

/*!40100 SET CHARACTER SET latin1;*/
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'onlineads'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "onlineads" /*!40100 DEFAULT CHARACTER SET latin1 */;

USE "onlineads";


#
# Table structure for table 'feedback'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "feedback" (
  "cdate" varchar(50) DEFAULT NULL,
  "clientname" varchar(50) DEFAULT NULL,
  "prodname" varchar(50) DEFAULT NULL,
  "prodtype" varchar(50) DEFAULT NULL,
  "feedback" varchar(50) DEFAULT NULL,
  "description" varchar(250) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'feedback'
#

# (No data found.)



#
# Table structure for table 'postads'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "postads" (
  "postid" int(11) NOT NULL AUTO_INCREMENT,
  "ownername" varchar(50) DEFAULT NULL,
  "contact" varchar(50) DEFAULT NULL,
  "vname" varchar(50) DEFAULT NULL,
  "vtype" varchar(50) DEFAULT NULL,
  "vnumber" varchar(50) DEFAULT NULL,
  "vmodelno" varchar(50) DEFAULT NULL,
  "vmodelname" varchar(50) DEFAULT NULL,
  "postalcode" varchar(50) DEFAULT NULL,
  "address" varchar(250) DEFAULT NULL,
  "noofowner" varchar(50) DEFAULT NULL,
  "description" varchar(250) DEFAULT NULL,
  "price" varchar(50) DEFAULT NULL,
  "video" varchar(250) DEFAULT NULL,
  PRIMARY KEY ("postid")
) AUTO_INCREMENT=3 /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'postads'
#

/*!40000 ALTER TABLE "postads" DISABLE KEYS;*/
LOCK TABLES "postads" WRITE;
REPLACE INTO "postads" ("postid", "ownername", "contact", "vname", "vtype", "vnumber", "vmodelno", "vmodelname", "postalcode", "address", "noofowner", "description", "price", "video") VALUES
	(1,'Siva','6586523652','Honda','Two Wheeler','TN1234','10','Asta','123456','cbe','First Owner','immediate sale','900000','car6.jpg');
REPLACE INTO "postads" ("postid", "ownername", "contact", "vname", "vtype", "vnumber", "vmodelno", "vmodelname", "postalcode", "address", "noofowner", "description", "price", "video") VALUES
	(2,'Siva','6586523652','Honda','Two Wheeler','TN1234','10','Asta','123456','dfgd','First Owner','gdfgdf','900000','car6.jpg');
UNLOCK TABLES;
/*!40000 ALTER TABLE "postads" ENABLE KEYS;*/


#
# Table structure for table 'prebook'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "prebook" (
  "ownername" varchar(50) DEFAULT NULL,
  "vnumber" varchar(50) DEFAULT NULL,
  "vname" varchar(50) DEFAULT NULL,
  "username" varchar(50) DEFAULT NULL,
  "contact" varchar(50) DEFAULT NULL,
  "email" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'prebook'
#

/*!40000 ALTER TABLE "prebook" DISABLE KEYS;*/
LOCK TABLES "prebook" WRITE;
REPLACE INTO "prebook" ("ownername", "vnumber", "vname", "username", "contact", "email") VALUES
	('Siva','TN1234','Honda','dhana','6586523652','dhanajay15@gmail.com');
REPLACE INTO "prebook" ("ownername", "vnumber", "vname", "username", "contact", "email") VALUES
	('','','','','','');
UNLOCK TABLES;
/*!40000 ALTER TABLE "prebook" ENABLE KEYS;*/


#
# Table structure for table 'register'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "register" (
  "Regid" int(11) NOT NULL AUTO_INCREMENT,
  "rname" varchar(50) DEFAULT NULL,
  "gender" varchar(50) DEFAULT NULL,
  "contact" varchar(50) DEFAULT NULL,
  "email" varchar(50) DEFAULT NULL,
  "Address" varchar(250) DEFAULT NULL,
  "city" varchar(50) DEFAULT NULL,
  "role" varchar(50) DEFAULT NULL,
  "uname" varchar(50) DEFAULT NULL,
  "password" varchar(50) DEFAULT NULL,
  PRIMARY KEY ("Regid")
) AUTO_INCREMENT=3 /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'register'
#

/*!40000 ALTER TABLE "register" DISABLE KEYS;*/
LOCK TABLES "register" WRITE;
REPLACE INTO "register" ("Regid", "rname", "gender", "contact", "email", "Address", "city", "role", "uname", "password") VALUES
	(1,'priya','Female','6586523652','sranjithapfdfgdfg276@gmail.com','cbe','dfgdf','Seller','priya','priya');
REPLACE INTO "register" ("Regid", "rname", "gender", "contact", "email", "Address", "city", "role", "uname", "password") VALUES
	(2,'Ranji','Female','6586523652','dgfd','fgdf','gdfgdf','Buyer','dhana','dhana');
UNLOCK TABLES;
/*!40000 ALTER TABLE "register" ENABLE KEYS;*/


#
# Table structure for table 'vehicledetails'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "vehicledetails" (
  "ownername" varchar(50) DEFAULT NULL,
  "vnumber" varchar(50) DEFAULT NULL,
  "vname" varchar(50) DEFAULT NULL,
  "vmodelno" varchar(50) DEFAULT NULL,
  "vmodelname" varchar(50) DEFAULT NULL,
  "pincode" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'vehicledetails'
#

/*!40000 ALTER TABLE "vehicledetails" DISABLE KEYS;*/
LOCK TABLES "vehicledetails" WRITE;
REPLACE INTO "vehicledetails" ("ownername", "vnumber", "vname", "vmodelno", "vmodelname", "pincode") VALUES
	('Siva','TN1234','Honda','10','Asta','123456');
UNLOCK TABLES;
/*!40000 ALTER TABLE "vehicledetails" ENABLE KEYS;*/
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/
