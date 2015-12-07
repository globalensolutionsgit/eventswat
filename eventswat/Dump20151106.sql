CREATE DATABASE  IF NOT EXISTS `evewat` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `evewat`;
-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: evewat
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add category',7,'add_category'),(20,'Can change category',7,'change_category'),(21,'Can delete category',7,'delete_category'),(22,'Can add sub category',8,'add_subcategory'),(23,'Can change sub category',8,'change_subcategory'),(24,'Can delete sub category',8,'delete_subcategory'),(25,'Can add city',9,'add_city'),(26,'Can change city',9,'change_city'),(27,'Can delete city',9,'delete_city'),(28,'Can add college',10,'add_college'),(29,'Can change college',10,'change_college'),(30,'Can delete college',10,'delete_college'),(31,'Can add department',11,'add_department'),(32,'Can change department',11,'change_department'),(33,'Can delete department',11,'delete_department'),(34,'Can add college department',12,'add_collegedepartment'),(35,'Can change college department',12,'change_collegedepartment'),(36,'Can delete college department',12,'delete_collegedepartment'),(37,'Can add premium price info',13,'add_premiumpriceinfo'),(38,'Can change premium price info',13,'change_premiumpriceinfo'),(39,'Can delete premium price info',13,'delete_premiumpriceinfo'),(40,'Can add postevent',14,'add_postevent'),(41,'Can change postevent',14,'change_postevent'),(42,'Can delete postevent',14,'delete_postevent'),(43,'Can add organizer',15,'add_organizer'),(44,'Can change organizer',15,'change_organizer'),(45,'Can delete organizer',15,'delete_organizer'),(46,'Can add feedback',16,'add_feedback'),(47,'Can change feedback',16,'change_feedback'),(48,'Can delete feedback',16,'delete_feedback'),(49,'Can add userprofile',17,'add_userprofile'),(50,'Can change userprofile',17,'change_userprofile'),(51,'Can delete userprofile',17,'delete_userprofile'),(52,'Can add payu details',18,'add_payudetails'),(53,'Can change payu details',18,'change_payudetails'),(54,'Can delete payu details',18,'delete_payudetails'),(55,'Can add site banner',19,'add_sitebanner'),(56,'Can change site banner',19,'change_sitebanner'),(57,'Can delete site banner',19,'delete_sitebanner'),(58,'Can add banner price',20,'add_bannerprice'),(59,'Can change banner price',20,'change_bannerprice'),(60,'Can delete banner price',20,'delete_bannerprice'),(61,'Can add mainbanner',21,'add_mainbanner'),(62,'Can change mainbanner',21,'change_mainbanner'),(63,'Can delete mainbanner',21,'delete_mainbanner');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$AAlOAAcgPrxP$Wuqb9q6WiqUu0b0Hwn0UPBleJjVAr8Dz6wVe4Fb9rNI=','2015-11-06 10:12:20',1,'root','','','root@gmail.com',1,1,'2015-10-30 10:50:30'),(2,'pbkdf2_sha256$12000$mqv8I39GKm26$n6eZCF81XkCB1R8pQkzBagmWFnJ8sV1PpsbgFz/ARKg=','2015-11-06 05:18:58',0,'ramya','','','suramya2894@gmail.com',0,1,'2015-10-30 10:51:36'),(3,'pbkdf2_sha256$12000$m4nX1jWrZPBb$hay6hmVtRze7aVQi15nqAyLyWobQxWEWn/2WyC2tzDU=','2015-11-02 05:21:28',0,'priya','','','avbmail93@gmail.com',0,1,'2015-11-02 05:21:19');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banner_bannerprice`
--

DROP TABLE IF EXISTS `banner_bannerprice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `banner_bannerprice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `price` double DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page` (`page`,`position`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner_bannerprice`
--

LOCK TABLES `banner_bannerprice` WRITE;
/*!40000 ALTER TABLE `banner_bannerprice` DISABLE KEYS */;
/*!40000 ALTER TABLE `banner_bannerprice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banner_mainbanner`
--

DROP TABLE IF EXISTS `banner_mainbanner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `banner_mainbanner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mainbanner` varchar(100) NOT NULL,
  `price` double DEFAULT NULL,
  `admin_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner_mainbanner`
--

LOCK TABLES `banner_mainbanner` WRITE;
/*!40000 ALTER TABLE `banner_mainbanner` DISABLE KEYS */;
/*!40000 ALTER TABLE `banner_mainbanner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banner_sitebanner`
--

DROP TABLE IF EXISTS `banner_sitebanner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `banner_sitebanner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `banner` varchar(100) NOT NULL,
  `link` varchar(200) DEFAULT NULL,
  `pageurl` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `price` double DEFAULT NULL,
  `startdate` datetime NOT NULL,
  `enddate` datetime NOT NULL,
  `duration` int(11) DEFAULT NULL,
  `admin_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner_sitebanner`
--

LOCK TABLES `banner_sitebanner` WRITE;
/*!40000 ALTER TABLE `banner_sitebanner` DISABLE KEYS */;
/*!40000 ALTER TABLE `banner_sitebanner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_category`
--

DROP TABLE IF EXISTS `college_event_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_category`
--

LOCK TABLES `college_event_category` WRITE;
/*!40000 ALTER TABLE `college_event_category` DISABLE KEYS */;
INSERT INTO `college_event_category` VALUES (1,'Engineering');
/*!40000 ALTER TABLE `college_event_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_city`
--

DROP TABLE IF EXISTS `college_event_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(150) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `country_code` varchar(10) DEFAULT NULL,
  `country_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_city`
--

LOCK TABLES `college_event_city` WRITE;
/*!40000 ALTER TABLE `college_event_city` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_college`
--

DROP TABLE IF EXISTS `college_event_college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collegetype_id` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `college_name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `college_event_college_5a885087` (`collegetype_id`),
  KEY `college_event_college_b376980e` (`city_id`),
  CONSTRAINT `city_id_refs_id_ee0fd1a3` FOREIGN KEY (`city_id`) REFERENCES `college_event_city` (`id`),
  CONSTRAINT `collegetype_id_refs_id_b61b14dd` FOREIGN KEY (`collegetype_id`) REFERENCES `college_event_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_college`
--

LOCK TABLES `college_event_college` WRITE;
/*!40000 ALTER TABLE `college_event_college` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_collegedepartment`
--

DROP TABLE IF EXISTS `college_event_collegedepartment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_collegedepartment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `college_event_collegedepartment_69d14838` (`department_id`),
  CONSTRAINT `department_id_refs_id_620c1a1d` FOREIGN KEY (`department_id`) REFERENCES `college_event_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_collegedepartment`
--

LOCK TABLES `college_event_collegedepartment` WRITE;
/*!40000 ALTER TABLE `college_event_collegedepartment` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_collegedepartment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_collegedepartment_college`
--

DROP TABLE IF EXISTS `college_event_collegedepartment_college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_collegedepartment_college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collegedepartment_id` int(11) NOT NULL,
  `college_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `collegedepartment_id` (`collegedepartment_id`,`college_id`),
  KEY `college_event_collegedepartment_college_84c61854` (`collegedepartment_id`),
  KEY `college_event_collegedepartment_college_ac3b121a` (`college_id`),
  CONSTRAINT `collegedepartment_id_refs_id_a5c5306c` FOREIGN KEY (`collegedepartment_id`) REFERENCES `college_event_collegedepartment` (`id`),
  CONSTRAINT `college_id_refs_id_01889fba` FOREIGN KEY (`college_id`) REFERENCES `college_event_college` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_collegedepartment_college`
--

LOCK TABLES `college_event_collegedepartment_college` WRITE;
/*!40000 ALTER TABLE `college_event_collegedepartment_college` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_collegedepartment_college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_department`
--

DROP TABLE IF EXISTS `college_event_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_department`
--

LOCK TABLES `college_event_department` WRITE;
/*!40000 ALTER TABLE `college_event_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_feedback`
--

DROP TABLE IF EXISTS `college_event_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `comments` longtext NOT NULL,
  `rating` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_feedback`
--

LOCK TABLES `college_event_feedback` WRITE;
/*!40000 ALTER TABLE `college_event_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_organizer`
--

DROP TABLE IF EXISTS `college_event_organizer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_organizer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `postevent_id` int(11) NOT NULL,
  `organizer_name` varchar(50) NOT NULL,
  `organizer_mobile` varchar(50) NOT NULL,
  `organizer_email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_event_organizer_c5c7cdeb` (`postevent_id`),
  CONSTRAINT `postevent_id_refs_id_bb60ce1a` FOREIGN KEY (`postevent_id`) REFERENCES `college_event_postevent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_organizer`
--

LOCK TABLES `college_event_organizer` WRITE;
/*!40000 ALTER TABLE `college_event_organizer` DISABLE KEYS */;
INSERT INTO `college_event_organizer` VALUES (1,6,'DFD','7894561223,7894561221','ramya@globalensolutions.com'),(2,7,'GF','9874563100,7894561221,7894561223','suramya2894@gmail.com'),(3,9,'ramya','7898789871,7898789872','suramya2894@gmail.com'),(4,10,'ramya','7481945284','suramya2894@gmail.com'),(5,11,'dfshdfh','7412589630,7410256389','suramya2894@gmail.com'),(6,12,'dffaf','9874563100,7894561221','suramya2894@gmail.com'),(7,13,'gfgf','7894561223,7894561222,7894561221','suramya2894@gmail.com'),(8,14,'surya','9874563100,7894561221,7894561222','suramya2894@gmail.com'),(9,1,'kalai R','7898789871,7898789872','kalai@gmail.com'),(10,14,'rmaya','9874563100,7894561221','suramya2894@gmail.com'),(12,14,'hdbif','78955,7899456615232','suramya2894@gmail.com'),(13,15,'ramya','7894561223,7894561222,7894561221','suramya2894@gmail.com'),(14,16,'cvcvc','7894561223,7894561224,7894561225,7894561226','suramya2894@gmail.com');
/*!40000 ALTER TABLE `college_event_organizer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_postevent`
--

DROP TABLE IF EXISTS `college_event_postevent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_postevent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `event_title` varchar(50) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `category_id` int(11) NOT NULL,
  `eventtype_id` int(11) DEFAULT NULL,
  `eventdescription` longtext NOT NULL,
  `address` longtext NOT NULL,
  `state` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `college` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `poster` varchar(500) DEFAULT NULL,
  `admin_status` tinyint(1) NOT NULL,
  `payment` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_event_postevent_6f33f001` (`category_id`),
  KEY `college_event_postevent_7a4f8c6c` (`eventtype_id`),
  CONSTRAINT `category_id_refs_id_11fce88a` FOREIGN KEY (`category_id`) REFERENCES `college_event_category` (`id`),
  CONSTRAINT `eventtype_id_refs_id_c3b9140f` FOREIGN KEY (`eventtype_id`) REFERENCES `college_event_subcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_postevent`
--

LOCK TABLES `college_event_postevent` WRITE;
/*!40000 ALTER TABLE `college_event_postevent` DISABLE KEYS */;
INSERT INTO `college_event_postevent` VALUES (1,'ramya','suramya2894@gmail.com',7894561230,'dcsaf','2015-10-31','2015-10-31',1,1,'fd','fd','f','ff','f','f','/events/s1.jpeg',0,0),(2,'ramya','suramya2894@gmail.com',7881545567,'gf','2015-10-31','2015-10-31',1,1,'fg','zxd','sd','ss','s','s','/events/s2.jpeg',0,0),(3,'ramya','suramya2894@gmail.com',76767676676,'vb','2015-10-31','2015-10-31',1,1,'vb','v','b','b','bbb','b','/events/s3.jpeg',0,0),(4,'ramya','suramya2894@gmail.com',7894561230,'vd','2015-10-31','2015-10-31',1,1,'gdfg','vc','v','v','v','v','/events/s3.jpeg',0,0),(5,'ramya','suramya2894@gmail.com',76767676676,'xf','2015-10-31','2015-10-31',1,1,'dfd','fd','f','f','f','f','/events/s4.jpeg',1,0),(6,'ramya','suramya2894@gmail.com',7894561223,'VD','2015-10-31','2015-10-31',1,1,'FDDS','FDSFD','FD','DS','DSF','DFS','/events/l.jpeg',1,0),(7,'ramya','suramya2894@gmail.com',7881545567,'FGHGH','2015-10-31','2015-10-31',1,1,'HGG','GH','GFH','GF','GG','GH','/events/s4.jpeg',1,0),(8,'root','root@gmail.com',7881545567,'try for mobile number','2015-11-03','2015-11-03',1,1,'vsdbvd','dgf','fg','fgf','fgf','fgf','/events/s2.jpeg',1,0),(9,'root','root@gmail.com',7894561230,'fgfg','2015-11-03','2015-11-03',1,1,'fgf','xcx','xcc','xczzxxz','cx','cxx','/events/logo.jpg',1,0),(10,'root','root@gmail.com',7894561230,'fhgh','2015-11-04','2015-11-04',1,1,'ghg','./;gffdgf','SXDS','SDs','sdsd','sds','/events/s1.jpeg',1,0),(11,'priya','avbmail93@gmail.com',7881545567,'fshf','2015-11-02','2015-11-03',1,1,'hfdshdfh','hfdshdf','sdafds','gsdagsd','dsgasdg','dgsagsdg','/events/images3.jpeg',1,0),(12,'ramya','suramya2894@gmail.com',76767676676,'hfd','2015-11-05','2015-11-05',1,1,'dfdf','dfd','dfd','fd','fd','dfd','/events/dsds.jpeg',0,0),(13,'ramya','suramya2894@gmail.com',7894561230,'fgf','2015-11-12','2015-11-12',1,1,'gf','gfg','gh','gg','hg','gh','/events/img/logo_150.png',0,0),(14,'ramya','suramya2894@gmail.com',7894561230,'fdsgf','2015-11-12','2015-11-12',1,1,'fgfff','dfd','dfg','dfd','dfd','dfd','/events/index4.jpeg',0,0),(15,'ramya','suramya2894@gmail.com',7881545567,'bfgq','2015-11-06','2015-11-06',1,1,'df','dfd','fgf','fgf','fgf','fgf','/events/index1.jpeg',0,0),(16,'ramya','suramya2894@gmail.com',7881545567,'bgjckhg','2015-11-11','2015-11-11',1,1,'nfkng','cfvcv','fgf','fgf','fg','ffg','/events/s2.jpeg',0,0);
/*!40000 ALTER TABLE `college_event_postevent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_premiumpriceinfo`
--

DROP TABLE IF EXISTS `college_event_premiumpriceinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_premiumpriceinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `premium_price` double DEFAULT NULL,
  `currency` varchar(10) NOT NULL,
  `purpose` varchar(30) NOT NULL,
  `month` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_premiumpriceinfo`
--

LOCK TABLES `college_event_premiumpriceinfo` WRITE;
/*!40000 ALTER TABLE `college_event_premiumpriceinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_event_premiumpriceinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_subcategory`
--

DROP TABLE IF EXISTS `college_event_subcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_subcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `icon` varchar(100) NOT NULL,
  `hover_icon` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_subcategory`
--

LOCK TABLES `college_event_subcategory` WRITE;
/*!40000 ALTER TABLE `college_event_subcategory` DISABLE KEYS */;
INSERT INTO `college_event_subcategory` VALUES (1,'subcategory/icon/workshop_4.png','subcategory/icon/workshop_hover_3.png','Workshop');
/*!40000 ALTER TABLE `college_event_subcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_subcategory_category`
--

DROP TABLE IF EXISTS `college_event_subcategory_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_subcategory_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `subcategory_id` (`subcategory_id`,`category_id`),
  KEY `college_event_subcategory_category_790ef9fb` (`subcategory_id`),
  KEY `college_event_subcategory_category_6f33f001` (`category_id`),
  CONSTRAINT `category_id_refs_id_e7da638a` FOREIGN KEY (`category_id`) REFERENCES `college_event_category` (`id`),
  CONSTRAINT `subcategory_id_refs_id_fccefbaa` FOREIGN KEY (`subcategory_id`) REFERENCES `college_event_subcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_subcategory_category`
--

LOCK TABLES `college_event_subcategory_category` WRITE;
/*!40000 ALTER TABLE `college_event_subcategory_category` DISABLE KEYS */;
INSERT INTO `college_event_subcategory_category` VALUES (1,1,1);
/*!40000 ALTER TABLE `college_event_subcategory_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-10-30 10:52:29',1,7,'1','Engineering',1,''),(2,'2015-10-30 10:52:58',1,8,'1','Workshop',1,''),(3,'2015-11-02 05:24:49',1,15,'4','ramya',2,'Changed organizer_mobile.'),(4,'2015-11-02 05:25:02',1,15,'3','ramya',2,'Changed organizer_mobile.'),(5,'2015-11-02 05:26:50',1,15,'2','GF',2,'No fields changed.'),(6,'2015-11-02 05:27:01',1,15,'1','DFD',2,'Changed organizer_mobile.'),(7,'2015-11-02 05:27:18',1,15,'1','DFD',2,'Changed organizer_email.'),(8,'2015-11-02 05:37:54',1,14,'11','fshf',2,'Changed admin_status.'),(9,'2015-11-02 05:38:01',1,14,'10','fhgh',2,'Changed admin_status.'),(10,'2015-11-02 05:38:11',1,14,'9','fgfg',2,'Changed admin_status.'),(11,'2015-11-02 05:38:24',1,14,'8','try for mobile number',2,'Changed admin_status.'),(12,'2015-11-02 05:38:32',1,14,'7','FGHGH',2,'Changed admin_status.'),(13,'2015-11-02 05:38:42',1,14,'6','VD',2,'Changed admin_status.'),(14,'2015-11-02 05:39:08',1,14,'5','xf',2,'Changed admin_status.'),(15,'2015-11-02 05:57:36',1,15,'4','ramya',2,'Changed organizer_mobile.'),(16,'2015-11-05 05:22:07',1,15,'8','surya',2,'No fields changed.'),(17,'2015-11-05 05:24:01',1,15,'9','kalai',1,''),(18,'2015-11-05 05:24:29',1,15,'9','kalai',2,'Changed organizer_mobile.'),(19,'2015-11-05 05:24:42',1,15,'9','kalai R',2,'Changed organizer_name.'),(20,'2015-11-05 05:24:52',1,15,'9','kalai R',2,'Changed organizer_mobile.'),(21,'2015-11-05 06:55:24',1,14,'14','fdsgf',2,'No fields changed.'),(22,'2015-11-05 06:55:39',1,14,'14','fdsgf',2,'Changed organizer_mobile for organizer \"surya\".'),(23,'2015-11-05 06:56:04',1,14,'14','fdsgf',2,'Added organizer \"surya1\".'),(24,'2015-11-05 06:56:25',1,14,'14','fdsgf',2,'Changed organizer_name for organizer \"rmaya\".'),(25,'2015-11-05 06:56:49',1,14,'14','fdsgf',2,'Added organizer \"bfhdbj\".'),(26,'2015-11-05 06:57:43',1,14,'14','fdsgf',2,'Deleted organizer \"bfhdbj\".'),(27,'2015-11-05 07:53:00',1,14,'14','fdsgf',2,'No fields changed.'),(28,'2015-11-05 07:53:45',1,14,'14','fdsgf',2,'Added organizer \"hdbif\".'),(29,'2015-11-06 10:13:37',1,19,'None','www.google.com',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'category','college_event','category'),(8,'sub category','college_event','subcategory'),(9,'city','college_event','city'),(10,'college','college_event','college'),(11,'department','college_event','department'),(12,'college department','college_event','collegedepartment'),(13,'premium price info','college_event','premiumpriceinfo'),(14,'postevent','college_event','postevent'),(15,'organizer','college_event','organizer'),(16,'feedback','college_event','feedback'),(17,'userprofile','events','userprofile'),(18,'payu details','payu','payudetails'),(19,'site banner','banner','sitebanner'),(20,'banner price','banner','bannerprice'),(21,'mainbanner','banner','mainbanner');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2kjpm15b304gv7onhcl3v99uw1t4htoc','N2E2MzdkOGEyMzIwZTE5MjdlZTlmMGU2YjdlNzEyMmVjZTlmNWUxMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2015-11-13 10:51:41'),('9srv368r8cl90u1q93sw0q9z282wk053','N2E2MzdkOGEyMzIwZTE5MjdlZTlmMGU2YjdlNzEyMmVjZTlmNWUxMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2015-11-19 05:08:53'),('bk44si8a3uyas4376peybwtm74q7lrd8','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-11-19 04:51:18'),('bu250agdzeqxzq59hxtt9r4d2gablsk9','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-11-19 06:18:14'),('e3dzpttx7lo1qwm68nb9dzwnaj3c6hwc','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-11-19 05:25:42'),('gaaztpywat8pr6y22rjj9begc7h8w5ot','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-11-16 05:57:59'),('kxkfa5dspk9gdvdi7811ii1gignxtrhy','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-11-19 06:55:07'),('n60ui3lra3qgs2h5p6u2tk2486ntst8i','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-11-20 10:12:20'),('pb8lo8tqakp80yu7w4mgm2b0nqxo3loc','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-11-19 08:05:59'),('qheq8o71gki2tcopj4dgr6eepuuopb3a','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-11-13 10:52:17'),('u8pl5takz78a5ubjr6tygv777r8s6orx','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-11-14 11:00:31'),('w8k0evs8sy2grhwxda4gnqjdomkjndi5','N2E2MzdkOGEyMzIwZTE5MjdlZTlmMGU2YjdlNzEyMmVjZTlmNWUxMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2015-11-18 05:24:51'),('xqusnc5rxbb6508rwkl7g4t67arvlnpk','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-11-19 07:52:20');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_userprofile`
--

DROP TABLE IF EXISTS `events_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `confirmation_code` varchar(500) NOT NULL,
  `is_subscribed` tinyint(1) NOT NULL,
  `is_emailverified` tinyint(1) NOT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `college_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `events_userprofile_b376980e` (`city_id`),
  KEY `events_userprofile_ac3b121a` (`college_id`),
  KEY `events_userprofile_69d14838` (`department_id`),
  CONSTRAINT `city_id_refs_id_695016a4` FOREIGN KEY (`city_id`) REFERENCES `college_event_city` (`id`),
  CONSTRAINT `college_id_refs_id_c0400547` FOREIGN KEY (`college_id`) REFERENCES `college_event_college` (`id`),
  CONSTRAINT `department_id_refs_id_d664371b` FOREIGN KEY (`department_id`) REFERENCES `college_event_department` (`id`),
  CONSTRAINT `user_id_refs_id_acf68b2c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_userprofile`
--

LOCK TABLES `events_userprofile` WRITE;
/*!40000 ALTER TABLE `events_userprofile` DISABLE KEYS */;
INSERT INTO `events_userprofile` VALUES (1,2,'7894561230','',0,0,NULL,NULL,NULL,NULL),(2,3,'7894561230','',0,0,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `events_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payu_payudetails`
--

DROP TABLE IF EXISTS `payu_payudetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payu_payudetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mihpayid` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `txnid` varchar(50) DEFAULT NULL,
  `amount` double DEFAULT NULL,
  `productinfo` varchar(500) DEFAULT NULL,
  `error_Message` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payu_payudetails`
--

LOCK TABLES `payu_payudetails` WRITE;
/*!40000 ALTER TABLE `payu_payudetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `payu_payudetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews_review`
--

DROP TABLE IF EXISTS `reviews_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `rating` smallint(5) unsigned DEFAULT NULL,
  `content` longtext NOT NULL,
  `date` datetime NOT NULL,
  `event_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews_review`
--

LOCK TABLES `reviews_review` WRITE;
/*!40000 ALTER TABLE `reviews_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracking_bannedip`
--

DROP TABLE IF EXISTS `tracking_bannedip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracking_bannedip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_address` char(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracking_bannedip`
--

LOCK TABLES `tracking_bannedip` WRITE;
/*!40000 ALTER TABLE `tracking_bannedip` DISABLE KEYS */;
/*!40000 ALTER TABLE `tracking_bannedip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracking_untrackeduseragent`
--

DROP TABLE IF EXISTS `tracking_untrackeduseragent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracking_untrackeduseragent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracking_untrackeduseragent`
--

LOCK TABLES `tracking_untrackeduseragent` WRITE;
/*!40000 ALTER TABLE `tracking_untrackeduseragent` DISABLE KEYS */;
/*!40000 ALTER TABLE `tracking_untrackeduseragent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracking_visitor`
--

DROP TABLE IF EXISTS `tracking_visitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracking_visitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session_key` varchar(40) NOT NULL,
  `ip_address` varchar(20) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `user_agent` varchar(255) NOT NULL,
  `referrer` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `page_views` int(10) unsigned NOT NULL,
  `session_start` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `session_key` (`session_key`,`ip_address`),
  KEY `tracking_visitor_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_b0052837` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracking_visitor`
--

LOCK TABLES `tracking_visitor` WRITE;
/*!40000 ALTER TABLE `tracking_visitor` DISABLE KEYS */;
INSERT INTO `tracking_visitor` VALUES (12,'n60ui3lra3qgs2h5p6u2tk2486ntst8i','127.0.0.1',1,'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0','unknown','/',14,'2015-11-06 10:11:08','2015-11-06 10:14:18');
/*!40000 ALTER TABLE `tracking_visitor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-06 15:44:58
