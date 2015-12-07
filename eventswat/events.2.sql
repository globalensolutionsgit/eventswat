-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: evewat
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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$vCrrMMPhvmS2$lt914hR8SVW3ZaRTF5ykBXxAAW0VDZPEdn/vavFreic=','2015-10-12 08:15:34',1,'root','','','root@gmail.com',1,1,'2015-10-10 19:58:23'),(2,'pbkdf2_sha256$12000$f3e22CpM6SIN$51IvZvIBlknImOuILBzOyMc/NCoxlskgazzQfk2uRiY=','2015-10-10 23:49:18',0,'sastha','','','saisasthaa@gmail.com',1,1,'2015-10-10 22:10:33'),(3,'pbkdf2_sha256$12000$wcz3vqTGFzJZ$7V2B+Bv0Bi4WMcDi4YLBRRSDoVmlmFghJSruDaTHGlE=','2015-10-11 06:17:04',0,'Babaprasanna','','','kpbabp@gmail.com',0,1,'2015-10-11 06:17:04'),(4,'pbkdf2_sha256$12000$3DLp55CJWIZY$jbGq46P8bb4dkdErNmcksMJ+smtZ0lMOdo3yWTkDyPc=','2015-10-11 06:22:41',0,'kp','','','kpppp@ooo.com',0,1,'2015-10-11 06:22:41'),(5,'pbkdf2_sha256$12000$OAEVTkuz0Ywt$Pl9qt/oPyplHgL8oxFjchlrq1fwygQ1HAcPln2E0NIo=','2015-10-11 10:33:08',0,'Pretheev','','','pretheevraj@gmail.com',0,1,'2015-10-11 06:47:03'),(7,'pbkdf2_sha256$12000$rj3yTdgyTXiv$ROgrxEtaeNSw+W4SucJG2Ie9s+F0S2Frm7UjbPaVfgM=','2015-10-11 09:15:47',0,'test','','','test@test.com',0,1,'2015-10-11 09:15:47'),(8,'pbkdf2_sha256$12000$hOBio4kbBfMJ$inLzt2v9o2tCor/rVaNAueQHR/38x3NW/4TGfTmsbRo=','2015-10-11 19:28:47',0,'muthu','','','spmuthu21@gmail.com',0,1,'2015-10-11 09:24:10'),(17,'pbkdf2_sha256$12000$zKLcAkqAsoNe$1bEJGPDpeD6JGbA0iwjl9ZxGfBA0JupTYKEUUB1o8Lg=','2015-10-11 14:31:35',0,'deepak','','','deepak@globalensolutions.com',0,1,'2015-10-11 14:31:33'),(20,'pbkdf2_sha256$12000$u490eds0KKnV$IMQ1G7yXncfLrx+ji2Q2Qgvoua7yNdnWXghF26el388=','2015-10-11 16:46:30',0,'Suriya','','','suriyachandran26@gmail.com',0,1,'2015-10-11 16:46:28'),(21,'pbkdf2_sha256$12000$z1KcqwXsXXjP$3RNToyOZ9AtLm/p9SPtwYTe4YXA6xmgjoyUQPiOw7/Y=','2015-10-11 17:02:43',0,'teste','','','testtest@gmail.com',0,1,'2015-10-11 17:02:40'),(23,'pbkdf2_sha256$12000$O1kK2jPi0OeN$zsoNbGkhu5RNuKp3F+ZZReD8q35Ml6KWexahbRGJN3g=','2015-10-11 19:35:15',0,'eventswat','','','eventswat@gmail.com',0,1,'2015-10-11 19:35:13'),(24,'pbkdf2_sha256$12000$QUZhj0DEjqKb$W4ur9CU+8hxLfCghJCF2u6f/pmlDH0euJLvg5oAJKy8=','2015-10-12 03:18:03',0,'baba','','','babaprasanna@gmail.com',0,1,'2015-10-12 03:08:57'),(25,'pbkdf2_sha256$12000$WNrFi99aC1h5$YFC/yhj6gLCy1ZTXKuRpHdugqEbaFAZr04DTAjPp77o=','2015-10-12 05:33:39',0,'Pradeepa','','','rpradeepa812@gmail.com',0,1,'2015-10-12 05:33:37'),(26,'pbkdf2_sha256$12000$j0y4cnVXlIxx$7LUZPQv9GNyIzNas4ZZ32UB7zw+57ivrxseZlRZFn5k=','2015-10-12 07:14:24',0,'priya','','','avbmail93@gmail.com',0,1,'2015-10-12 07:14:22');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner_bannerprice`
--

LOCK TABLES `banner_bannerprice` WRITE;
/*!40000 ALTER TABLE `banner_bannerprice` DISABLE KEYS */;
INSERT INTO `banner_bannerprice` VALUES (1,'/','bottom',500,60),(2,'event/','left',500,30),(3,'event/','right',300,30);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner_mainbanner`
--

LOCK TABLES `banner_mainbanner` WRITE;
/*!40000 ALTER TABLE `banner_mainbanner` DISABLE KEYS */;
INSERT INTO `banner_mainbanner` VALUES (1,'static/mainbanner/slide22_1.jpg',1200,1),(2,'static/mainbanner/header02_2.jpg',1200,1),(3,'static/mainbanner/msajce-induction-day_1.png',1200,1),(4,'static/mainbanner/grad15_1.jpg',1200,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner_sitebanner`
--

LOCK TABLES `banner_sitebanner` WRITE;
/*!40000 ALTER TABLE `banner_sitebanner` DISABLE KEYS */;
INSERT INTO `banner_sitebanner` VALUES (2,'static/banners/gallery7-2_7.jpg','','/','bottom',500,'2015-10-13 20:18:51','2015-11-13 20:18:51',NULL,1),(3,'static/banners/11986990_921600724599048_6309821011303801096_n.jpg','','/','bottom',500,'2015-10-10 20:18:52','2015-11-09 20:18:52',NULL,1),(4,'static/banners/1_5.jpg','','/','bottom',500,'2015-10-10 20:18:52','2015-11-09 20:18:52',NULL,1),(5,'static/banners/Tri_Aug_3.jpg','','/','bottom',500,'2015-10-10 20:18:51','2015-11-09 20:18:51',NULL,1),(6,'static/banners/2.png','','event/','left',500,'2015-10-10 20:18:52','2015-11-09 20:18:52',NULL,1),(7,'static/banners/1_6.jpg','','event/','right',300,'2015-10-10 20:18:52','2015-11-09 20:18:52',NULL,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_category`
--

LOCK TABLES `college_event_category` WRITE;
/*!40000 ALTER TABLE `college_event_category` DISABLE KEYS */;
INSERT INTO `college_event_category` VALUES (2,'Arts & Science'),(1,'Engineering'),(3,'Management'),(4,'Medical'),(5,'Others'),(6,'POLYTECHNIC');
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
) ENGINE=InnoDB AUTO_INCREMENT=1625 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_city`
--

LOCK TABLES `college_event_city` WRITE;
/*!40000 ALTER TABLE `college_event_city` DISABLE KEYS */;
INSERT INTO `college_event_city` VALUES (1,'Pondicherry','Pondicherry',NULL,NULL),(2,'Chennai','Tamilnadu',NULL,NULL),(3,'Adilabad','Andhra Pradesh',NULL,NULL),(4,'Adoni','Andhra Pradesh',NULL,NULL),(5,'Amadalavalasa','Andhra Pradesh',NULL,NULL),(6,'Amalapuram','Andhra Pradesh',NULL,NULL),(7,'Anakapalle','Andhra Pradesh',NULL,NULL),(8,'Anantapur','Andhra Pradesh',NULL,NULL),(9,'Badepalle','Andhra Pradesh',NULL,NULL),(10,'Banganapalle','Andhra Pradesh',NULL,NULL),(11,'Bapatla','Andhra Pradesh',NULL,NULL),(12,'Bellampalle','Andhra Pradesh',NULL,NULL),(13,'Bethamcherla','Andhra Pradesh',NULL,NULL),(14,'Bhadrachalam','Andhra Pradesh',NULL,NULL),(15,'Bhainsa','Andhra Pradesh',NULL,NULL),(16,'Bheemunipatnam','Andhra Pradesh',NULL,NULL),(17,'Bhimavaram','Andhra Pradesh',NULL,NULL),(18,'Bhongir','Andhra Pradesh',NULL,NULL),(19,'Bobbili','Andhra Pradesh',NULL,NULL),(20,'Bodhan','Andhra Pradesh',NULL,NULL),(21,'Chilakaluripet','Andhra Pradesh',NULL,NULL),(22,'Chirala','Andhra Pradesh',NULL,NULL),(23,'Chittoor','Andhra Pradesh',NULL,NULL),(24,'Cuddapah','Andhra Pradesh',NULL,NULL),(25,'Devarakonda','Andhra Pradesh',NULL,NULL),(26,'Dharmavaram','Andhra Pradesh',NULL,NULL),(27,'Eluru','Andhra Pradesh',NULL,NULL),(28,'Farooqnagar','Andhra Pradesh',NULL,NULL),(29,'Gadwal','Andhra Pradesh',NULL,NULL),(30,'Gooty','Andhra Pradesh',NULL,NULL),(31,'Gudivada','Andhra Pradesh',NULL,NULL),(32,'Gudur','Andhra Pradesh',NULL,NULL),(33,'Guntakal','Andhra Pradesh',NULL,NULL),(34,'Guntur','Andhra Pradesh',NULL,NULL),(35,'Hanuman Junction','Andhra Pradesh',NULL,NULL),(36,'Hindupur','Andhra Pradesh',NULL,NULL),(37,'Hyderabad','Andhra Pradesh',NULL,NULL),(38,'Ichchapuram','Andhra Pradesh',NULL,NULL),(39,'Jaggaiahpet','Andhra Pradesh',NULL,NULL),(40,'Jagtial','Andhra Pradesh',NULL,NULL),(41,'Jammalamadugu','Andhra Pradesh',NULL,NULL),(42,'Jangaon','Andhra Pradesh',NULL,NULL),(43,'Kadapa','Andhra Pradesh',NULL,NULL),(44,'Kadiri','Andhra Pradesh',NULL,NULL),(45,'Kagaznagar','Andhra Pradesh',NULL,NULL),(46,'Kakinada','Andhra Pradesh',NULL,NULL),(47,'Kalyandurg','Andhra Pradesh',NULL,NULL),(48,'Kamareddy','Andhra Pradesh',NULL,NULL),(49,'Kandukur','Andhra Pradesh',NULL,NULL),(50,'Karimnagar','Andhra Pradesh',NULL,NULL),(51,'Kavali','Andhra Pradesh',NULL,NULL),(52,'Khammam','Andhra Pradesh',NULL,NULL),(53,'Koratla','Andhra Pradesh',NULL,NULL),(54,'Kothagudem','Andhra Pradesh',NULL,NULL),(55,'Kothapeta','Andhra Pradesh',NULL,NULL),(56,'Kovvur','Andhra Pradesh',NULL,NULL),(57,'Kurnool','Andhra Pradesh',NULL,NULL),(58,'Kyathampalle','Andhra Pradesh',NULL,NULL),(59,'Macherla','Andhra Pradesh',NULL,NULL),(60,'Machilipatnam','Andhra Pradesh',NULL,NULL),(61,'Madanapalle','Andhra Pradesh',NULL,NULL),(62,'Mahbubnagar','Andhra Pradesh',NULL,NULL),(63,'Mancherial','Andhra Pradesh',NULL,NULL),(64,'Mandamarri','Andhra Pradesh',NULL,NULL),(65,'Mandapeta','Andhra Pradesh',NULL,NULL),(66,'Manuguru','Andhra Pradesh',NULL,NULL),(67,'Markapur','Andhra Pradesh',NULL,NULL),(68,'Medak','Andhra Pradesh',NULL,NULL),(69,'Miryalaguda','Andhra Pradesh',NULL,NULL),(70,'Mogalthur','Andhra Pradesh',NULL,NULL),(71,'Nagari','Andhra Pradesh',NULL,NULL),(72,'Nagarkurnool','Andhra Pradesh',NULL,NULL),(73,'Nandyal','Andhra Pradesh',NULL,NULL),(74,'Narasapur','Andhra Pradesh',NULL,NULL),(75,'Narasaraopet','Andhra Pradesh',NULL,NULL),(76,'Narayanpet','Andhra Pradesh',NULL,NULL),(77,'Narsipatnam','Andhra Pradesh',NULL,NULL),(78,'Nellore','Andhra Pradesh',NULL,NULL),(79,'Nidadavole','Andhra Pradesh',NULL,NULL),(80,'Nirmal','Andhra Pradesh',NULL,NULL),(81,'Nizamabad','Andhra Pradesh',NULL,NULL),(82,'Nuzvid','Andhra Pradesh',NULL,NULL),(83,'Ongole','Andhra Pradesh',NULL,NULL),(84,'Palacole','Andhra Pradesh',NULL,NULL),(85,'Palasa Kasibugga','Andhra Pradesh',NULL,NULL),(86,'Palwancha','Andhra Pradesh',NULL,NULL),(87,'Parvathipuram','Andhra Pradesh',NULL,NULL),(88,'Pedana','Andhra Pradesh',NULL,NULL),(89,'Peddapuram','Andhra Pradesh',NULL,NULL),(90,'Pithapuram','Andhra Pradesh',NULL,NULL),(91,'Pondur','Andhra pradesh',NULL,NULL),(92,'Ponnur','Andhra Pradesh',NULL,NULL),(93,'Proddatur','Andhra Pradesh',NULL,NULL),(94,'Punganur','Andhra Pradesh',NULL,NULL),(95,'Puttur','Andhra Pradesh',NULL,NULL),(96,'Rajahmundry','Andhra Pradesh',NULL,NULL),(97,'Rajam','Andhra Pradesh',NULL,NULL),(98,'Ramachandrapuram','Andhra Pradesh',NULL,NULL),(99,'Ramagundam','Andhra Pradesh',NULL,NULL),(100,'Rayachoti','Andhra Pradesh',NULL,NULL),(101,'Rayadurg','Andhra Pradesh',NULL,NULL),(102,'Renigunta','Andhra Pradesh',NULL,NULL),(103,'Repalle','Andhra Pradesh',NULL,NULL),(104,'Sadasivpet','Andhra Pradesh',NULL,NULL),(105,'Salur','Andhra Pradesh',NULL,NULL),(106,'Samalkot','Andhra Pradesh',NULL,NULL),(107,'Sangareddy','Andhra Pradesh',NULL,NULL),(108,'Sattenapalle','Andhra Pradesh',NULL,NULL),(109,'Siddipet','Andhra Pradesh',NULL,NULL),(110,'Singapur','Andhra Pradesh',NULL,NULL),(111,'Sircilla','Andhra Pradesh',NULL,NULL),(112,'Srikakulam','Andhra Pradesh',NULL,NULL),(113,'Srikalahasti','Andhra Pradesh',NULL,NULL),(115,'Suryapet','Andhra Pradesh',NULL,NULL),(116,'Tadepalligudem','Andhra Pradesh',NULL,NULL),(117,'Tadpatri','Andhra Pradesh',NULL,NULL),(118,'Tandur','Andhra Pradesh',NULL,NULL),(119,'Tanuku','Andhra Pradesh',NULL,NULL),(120,'Tenali','Andhra Pradesh',NULL,NULL),(121,'Tirupati','Andhra Pradesh',NULL,NULL),(122,'Tuni','Andhra Pradesh',NULL,NULL),(123,'Uravakonda','Andhra Pradesh',NULL,NULL),(124,'Venkatagiri','Andhra Pradesh',NULL,NULL),(125,'Vicarabad','Andhra Pradesh',NULL,NULL),(126,'Vijayawada','Andhra Pradesh',NULL,NULL),(127,'Vinukonda','Andhra Pradesh',NULL,NULL),(128,'Visakhapatnam','Andhra Pradesh',NULL,NULL),(129,'Vizianagaram','Andhra Pradesh',NULL,NULL),(130,'Wanaparthy','Andhra Pradesh',NULL,NULL),(131,'Warangal','Andhra Pradesh',NULL,NULL),(132,'Yellandu','Andhra Pradesh',NULL,NULL),(133,'Yemmiganur','Andhra Pradesh',NULL,NULL),(134,'Yerraguntla','Andhra Pradesh',NULL,NULL),(135,'Zahirabad','Andhra Pradesh',NULL,NULL),(136,'Rajampet','Andra Pradesh',NULL,NULL),(137,'Along','Arunachal Pradesh',NULL,NULL),(138,'Bomdila','Arunachal Pradesh',NULL,NULL),(139,'Itanagar','Arunachal Pradesh',NULL,NULL),(140,'Naharlagun','Arunachal Pradesh',NULL,NULL),(141,'Pasighat','Arunachal Pradesh',NULL,NULL),(142,'Abhayapuri','Assam',NULL,NULL),(143,'Amguri','Assam',NULL,NULL),(144,'Anandnagaar','Assam',NULL,NULL),(145,'Barpeta','Assam',NULL,NULL),(146,'Barpeta Road','Assam',NULL,NULL),(147,'Bilasipara','Assam',NULL,NULL),(148,'Bongaigaon','Assam',NULL,NULL),(149,'Dhekiajuli','Assam',NULL,NULL),(150,'Dhubri','Assam',NULL,NULL),(151,'Dibrugarh','Assam',NULL,NULL),(152,'Digboi','Assam',NULL,NULL),(153,'Diphu','Assam',NULL,NULL),(154,'Dispur','Assam',NULL,NULL),(156,'Gauripur','Assam',NULL,NULL),(157,'Goalpara','Assam',NULL,NULL),(158,'Golaghat','Assam',NULL,NULL),(159,'Guwahati','Assam',NULL,NULL),(160,'Haflong','Assam',NULL,NULL),(161,'Hailakandi','Assam',NULL,NULL),(162,'Hojai','Assam',NULL,NULL),(163,'Jorhat','Assam',NULL,NULL),(164,'Karimganj','Assam',NULL,NULL),(165,'Kokrajhar','Assam',NULL,NULL),(166,'Lanka','Assam',NULL,NULL),(167,'Lumding','Assam',NULL,NULL),(168,'Mangaldoi','Assam',NULL,NULL),(169,'Mankachar','Assam',NULL,NULL),(170,'Margherita','Assam',NULL,NULL),(171,'Mariani','Assam',NULL,NULL),(172,'Marigaon','Assam',NULL,NULL),(173,'Nagaon','Assam',NULL,NULL),(174,'Nalbari','Assam',NULL,NULL),(175,'North Lakhimpur','Assam',NULL,NULL),(176,'Rangia','Assam',NULL,NULL),(177,'Sibsagar','Assam',NULL,NULL),(178,'Silapathar','Assam',NULL,NULL),(179,'Silchar','Assam',NULL,NULL),(180,'Tezpur','Assam',NULL,NULL),(181,'Tinsukia','Assam',NULL,NULL),(182,'Amarpur','Bihar',NULL,NULL),(183,'Araria','Bihar',NULL,NULL),(184,'Areraj','Bihar',NULL,NULL),(185,'Arrah','Bihar',NULL,NULL),(186,'Asarganj','Bihar',NULL,NULL),(187,'Aurangabad','Bihar',NULL,NULL),(188,'Bagaha','Bihar',NULL,NULL),(189,'Bahadurganj','Bihar',NULL,NULL),(190,'Bairgania','Bihar',NULL,NULL),(191,'Bakhtiarpur','Bihar',NULL,NULL),(192,'Banka','Bihar',NULL,NULL),(193,'Banmankhi Bazar','Bihar',NULL,NULL),(194,'Barahiya','Bihar',NULL,NULL),(195,'Barauli','Bihar',NULL,NULL),(196,'Barbigha','Bihar',NULL,NULL),(197,'Barh','Bihar',NULL,NULL),(198,'Begusarai','Bihar',NULL,NULL),(199,'Behea','Bihar',NULL,NULL),(200,'Bettiah','Bihar',NULL,NULL),(201,'Bhabua','Bihar',NULL,NULL),(202,'Bhagalpur','Bihar',NULL,NULL),(203,'Bihar Sharif','Bihar',NULL,NULL),(204,'Bikramganj','Bihar',NULL,NULL),(205,'Bodh Gaya','Bihar',NULL,NULL),(206,'Buxar','Bihar',NULL,NULL),(207,'Chandan Bara','Bihar',NULL,NULL),(208,'Chanpatia','Bihar',NULL,NULL),(209,'Chhapra','Bihar',NULL,NULL),(210,'Colgong','Bihar',NULL,NULL),(211,'Dalsinghsarai','Bihar',NULL,NULL),(212,'Darbhanga','Bihar',NULL,NULL),(213,'Daudnagar','Bihar',NULL,NULL),(214,'Dehri-on-Sone','Bihar',NULL,NULL),(215,'Dhaka','Bihar',NULL,NULL),(216,'Dighwara','Bihar',NULL,NULL),(217,'Dumraon','Bihar',NULL,NULL),(218,'Fatwah','Bihar',NULL,NULL),(219,'Forbesganj','Bihar',NULL,NULL),(220,'Gaya','Bihar',NULL,NULL),(221,'Gogri Jamalpur','Bihar',NULL,NULL),(222,'Gopalganj','Bihar',NULL,NULL),(223,'Hajipur','Bihar',NULL,NULL),(224,'Hilsa','Bihar',NULL,NULL),(225,'Hisua','Bihar',NULL,NULL),(226,'Islampur','Bihar',NULL,NULL),(227,'Jagdispur','Bihar',NULL,NULL),(228,'Jamalpur','Bihar',NULL,NULL),(229,'Jamui','Bihar',NULL,NULL),(230,'Jehanabad','Bihar',NULL,NULL),(231,'Jhajha','Bihar',NULL,NULL),(232,'Jhanjharpur','Bihar',NULL,NULL),(233,'Jogabani','Bihar',NULL,NULL),(234,'Kanti','Bihar',NULL,NULL),(235,'Katihar','Bihar',NULL,NULL),(236,'Khagaria','Bihar',NULL,NULL),(237,'Kharagpur','Bihar',NULL,NULL),(238,'Kishanganj','Bihar',NULL,NULL),(239,'Lakhisarai','Bihar',NULL,NULL),(240,'Lalganj','Bihar',NULL,NULL),(241,'Madhepura','Bihar',NULL,NULL),(242,'Madhubani','Bihar',NULL,NULL),(243,'Maharajganj','Bihar',NULL,NULL),(244,'Mahnar Bazar','Bihar',NULL,NULL),(245,'Makhdumpur','Bihar',NULL,NULL),(246,'Maner','Bihar',NULL,NULL),(247,'Manihari','Bihar',NULL,NULL),(248,'Marhaura','Bihar',NULL,NULL),(249,'Masaurhi','Bihar',NULL,NULL),(250,'Mirganj','Bihar',NULL,NULL),(251,'Mokameh','Bihar',NULL,NULL),(252,'Motihari','Bihar',NULL,NULL),(253,'Motipur','Bihar',NULL,NULL),(254,'Munger','Bihar',NULL,NULL),(255,'Murliganj','Bihar',NULL,NULL),(256,'Muzaffarpur','Bihar',NULL,NULL),(257,'Narkatiaganj','Bihar',NULL,NULL),(258,'Naugachhia','Bihar',NULL,NULL),(259,'Nawada','Bihar',NULL,NULL),(260,'Nokha','Bihar',NULL,NULL),(261,'Patna','Bihar',NULL,NULL),(262,'Piro','Bihar',NULL,NULL),(263,'Purnia','Bihar',NULL,NULL),(264,'Rafiganj','Bihar',NULL,NULL),(265,'Rajgir','Bihar',NULL,NULL),(266,'Ramnagar','Bihar',NULL,NULL),(267,'Raxaul Bazar','Bihar',NULL,NULL),(268,'Revelganj','Bihar',NULL,NULL),(269,'Rosera','Bihar',NULL,NULL),(270,'Saharsa','Bihar',NULL,NULL),(271,'Samastipur','Bihar',NULL,NULL),(272,'Sasaram','Bihar',NULL,NULL),(273,'Sheikhpura','Bihar',NULL,NULL),(274,'Sheohar','Bihar',NULL,NULL),(275,'Sherghati','Bihar',NULL,NULL),(276,'Silao','Bihar',NULL,NULL),(277,'Sitamarhi','Bihar',NULL,NULL),(278,'Siwan','Bihar',NULL,NULL),(279,'Sonepur','Bihar',NULL,NULL),(280,'Sugauli','Bihar',NULL,NULL),(281,'Sultanganj','Bihar',NULL,NULL),(282,'Supaul','Bihar',NULL,NULL),(283,'Warisaliganj','Bihar',NULL,NULL),(284,'Ahiwara','Chhattisgarh',NULL,NULL),(285,'Akaltara','Chhattisgarh',NULL,NULL),(286,'Ambagarh Chowki','Chhattisgarh',NULL,NULL),(287,'Ambikapur','Chhattisgarh',NULL,NULL),(288,'Arang','Chhattisgarh',NULL,NULL),(289,'Bade Bacheli','Chhattisgarh',NULL,NULL),(290,'Balod','Chhattisgarh',NULL,NULL),(291,'Baloda Bazar','Chhattisgarh',NULL,NULL),(292,'Bemetra','Chhattisgarh',NULL,NULL),(293,'Bhatapara','Chhattisgarh',NULL,NULL),(294,'Bilaspur','Chhattisgarh',NULL,NULL),(295,'Birgaon','Chhattisgarh',NULL,NULL),(296,'Champa','Chhattisgarh',NULL,NULL),(297,'Chirmiri','Chhattisgarh',NULL,NULL),(298,'Dalli-Rajhara','Chhattisgarh',NULL,NULL),(299,'Dhamtari','Chhattisgarh',NULL,NULL),(300,'Dipka','Chhattisgarh',NULL,NULL),(301,'Dongargarh','Chhattisgarh',NULL,NULL),(302,'Durg-Bhilai Nagar','Chhattisgarh',NULL,NULL),(303,'Gobranawapara','Chhattisgarh',NULL,NULL),(304,'Jagdalpur','Chhattisgarh',NULL,NULL),(305,'Janjgir','Chhattisgarh',NULL,NULL),(306,'Jashpurnagar','Chhattisgarh',NULL,NULL),(307,'Kanker','Chhattisgarh',NULL,NULL),(308,'Kawardha','Chhattisgarh',NULL,NULL),(309,'Kondagaon','Chhattisgarh',NULL,NULL),(310,'Korba','Chhattisgarh',NULL,NULL),(311,'Mahasamund','Chhattisgarh',NULL,NULL),(312,'Mahendragarh','Chhattisgarh',NULL,NULL),(313,'Mungeli','Chhattisgarh',NULL,NULL),(314,'Naila Janjgir','Chhattisgarh',NULL,NULL),(315,'Raigarh','Chhattisgarh',NULL,NULL),(316,'Raipur','Chhattisgarh',NULL,NULL),(317,'Rajnandgaon','Chhattisgarh',NULL,NULL),(318,'Sakti','Chhattisgarh',NULL,NULL),(319,'Tilda Newra','Chhattisgarh',NULL,NULL),(320,'Amli','Dadra & Nagar Haveli',NULL,NULL),(321,'Silvassa','Dadra and Nagar Haveli',NULL,NULL),(322,'Daman and Diu','Daman & Diu',NULL,NULL),(323,'Daman and Diu','Daman & Diu',NULL,NULL),(324,'Asola','Delhi',NULL,NULL),(325,'Delhi','Delhi',NULL,NULL),(326,'Aldona','Goa',NULL,NULL),(327,'Curchorem Cacora','Goa',NULL,NULL),(328,'Madgaon','Goa',NULL,NULL),(329,'Mapusa','Goa',NULL,NULL),(330,'Margao','Goa',NULL,NULL),(331,'Marmagao','Goa',NULL,NULL),(332,'Panaji','Goa',NULL,NULL),(333,'Ahmedabad','Gujarat',NULL,NULL),(334,'Amreli','Gujarat',NULL,NULL),(335,'Anand','Gujarat',NULL,NULL),(336,'Ankleshwar','Gujarat',NULL,NULL),(337,'Bharuch','Gujarat',NULL,NULL),(338,'Bhavnagar','Gujarat',NULL,NULL),(339,'Bhuj','Gujarat',NULL,NULL),(340,'Cambay','Gujarat',NULL,NULL),(341,'Dahod','Gujarat',NULL,NULL),(342,'Deesa','Gujarat',NULL,NULL),(343,'\"Dharampur',' India\"',NULL,NULL),(344,'Dholka','Gujarat',NULL,NULL),(345,'Gandhinagar','Gujarat',NULL,NULL),(346,'Godhra','Gujarat',NULL,NULL),(347,'Himatnagar','Gujarat',NULL,NULL),(348,'Idar','Gujarat',NULL,NULL),(349,'Jamnagar','Gujarat',NULL,NULL),(350,'Junagadh','Gujarat',NULL,NULL),(351,'Kadi','Gujarat',NULL,NULL),(352,'Kalavad','Gujarat',NULL,NULL),(353,'Kalol','Gujarat',NULL,NULL),(354,'Kapadvanj','Gujarat',NULL,NULL),(355,'Karjan','Gujarat',NULL,NULL),(356,'Keshod','Gujarat',NULL,NULL),(357,'Khambhalia','Gujarat',NULL,NULL),(358,'Khambhat','Gujarat',NULL,NULL),(359,'Kheda','Gujarat',NULL,NULL),(360,'Khedbrahma','Gujarat',NULL,NULL),(361,'Kheralu','Gujarat',NULL,NULL),(362,'Kodinar','Gujarat',NULL,NULL),(363,'Lathi','Gujarat',NULL,NULL),(364,'Limbdi','Gujarat',NULL,NULL),(365,'Lunawada','Gujarat',NULL,NULL),(366,'Mahesana','Gujarat',NULL,NULL),(367,'Mahuva','Gujarat',NULL,NULL),(368,'Manavadar','Gujarat',NULL,NULL),(369,'Mandvi','Gujarat',NULL,NULL),(370,'Mangrol','Gujarat',NULL,NULL),(371,'Mansa','Gujarat',NULL,NULL),(372,'Mehmedabad','Gujarat',NULL,NULL),(373,'Modasa','Gujarat',NULL,NULL),(374,'Morvi','Gujarat',NULL,NULL),(375,'Nadiad','Gujarat',NULL,NULL),(376,'Navsari','Gujarat',NULL,NULL),(377,'Padra','Gujarat',NULL,NULL),(378,'Palanpur','Gujarat',NULL,NULL),(379,'Palitana','Gujarat',NULL,NULL),(380,'Pardi','Gujarat',NULL,NULL),(381,'Patan','Gujarat',NULL,NULL),(382,'Petlad','Gujarat',NULL,NULL),(383,'Porbandar','Gujarat',NULL,NULL),(384,'Radhanpur','Gujarat',NULL,NULL),(385,'Rajkot','Gujarat',NULL,NULL),(386,'Rajpipla','Gujarat',NULL,NULL),(387,'Rajula','Gujarat',NULL,NULL),(388,'Ranavav','Gujarat',NULL,NULL),(389,'Rapar','Gujarat',NULL,NULL),(390,'Salaya','Gujarat',NULL,NULL),(391,'Sanand','Gujarat',NULL,NULL),(392,'Savarkundla','Gujarat',NULL,NULL),(393,'Sidhpur','Gujarat',NULL,NULL),(394,'Sihor','Gujarat',NULL,NULL),(395,'Songadh','Gujarat',NULL,NULL),(396,'Surat','Gujarat',NULL,NULL),(397,'Talaja','Gujarat',NULL,NULL),(398,'Thangadh','Gujarat',NULL,NULL),(399,'Tharad','Gujarat',NULL,NULL),(400,'Umbergaon','Gujarat',NULL,NULL),(401,'Umreth','Gujarat',NULL,NULL),(402,'Una','Gujarat',NULL,NULL),(403,'Unjha','Gujarat',NULL,NULL),(404,'Upleta','Gujarat',NULL,NULL),(405,'Vadnagar','Gujarat',NULL,NULL),(406,'Vadodara','Gujarat',NULL,NULL),(407,'Valsad','Gujarat',NULL,NULL),(408,'Vapi','Gujarat',NULL,NULL),(409,'Vapi','Gujarat',NULL,NULL),(410,'Veraval','Gujarat',NULL,NULL),(411,'Vijapur','Gujarat',NULL,NULL),(412,'Viramgam','Gujarat',NULL,NULL),(413,'Visnagar','Gujarat',NULL,NULL),(414,'Vyara','Gujarat',NULL,NULL),(415,'Wadhwan','Gujarat',NULL,NULL),(416,'Wankaner','Gujarat',NULL,NULL),(417,'Adalaj','Gujrat',NULL,NULL),(418,'Adityana','Gujrat',NULL,NULL),(419,'Alang','Gujrat',NULL,NULL),(420,'Ambaji','Gujrat',NULL,NULL),(421,'Ambaliyasan','Gujrat',NULL,NULL),(422,'Andada','Gujrat',NULL,NULL),(423,'Anjar','Gujrat',NULL,NULL),(424,'Anklav','Gujrat',NULL,NULL),(425,'Antaliya','Gujrat',NULL,NULL),(426,'Arambhada','Gujrat',NULL,NULL),(427,'Atul','Gujrat',NULL,NULL),(428,'Ballabhgarh','Hariyana',NULL,NULL),(429,'Ambala','Haryana',NULL,NULL),(430,'Ambala','Haryana',NULL,NULL),(431,'Asankhurd','Haryana',NULL,NULL),(432,'Assandh','Haryana',NULL,NULL),(433,'Ateli','Haryana',NULL,NULL),(434,'Babiyal','Haryana',NULL,NULL),(435,'Bahadurgarh','Haryana',NULL,NULL),(436,'Barwala','Haryana',NULL,NULL),(437,'Bhiwani','Haryana',NULL,NULL),(438,'Charkhi Dadri','Haryana',NULL,NULL),(439,'Cheeka','Haryana',NULL,NULL),(440,'Ellenabad 2','Haryana',NULL,NULL),(441,'Faridabad','Haryana',NULL,NULL),(442,'Fatehabad','Haryana',NULL,NULL),(443,'Ganaur','Haryana',NULL,NULL),(444,'Gharaunda','Haryana',NULL,NULL),(445,'Gohana','Haryana',NULL,NULL),(446,'Gurgaon','Haryana',NULL,NULL),(447,'Haibat(Yamuna Nagar)','Haryana',NULL,NULL),(448,'Hansi','Haryana',NULL,NULL),(449,'Hisar','Haryana',NULL,NULL),(450,'Hodal','Haryana',NULL,NULL),(451,'Jhajjar','Haryana',NULL,NULL),(452,'Jind','Haryana',NULL,NULL),(453,'Kaithal','Haryana',NULL,NULL),(454,'Kalan Wali','Haryana',NULL,NULL),(455,'Kalka','Haryana',NULL,NULL),(456,'Karnal','Haryana',NULL,NULL),(457,'Ladwa','Haryana',NULL,NULL),(458,'Mahendragarh','Haryana',NULL,NULL),(459,'Mandi Dabwali','Haryana',NULL,NULL),(460,'Narnaul','Haryana',NULL,NULL),(461,'Narwana','Haryana',NULL,NULL),(462,'Palwal','Haryana',NULL,NULL),(463,'Panchkula','Haryana',NULL,NULL),(464,'Panipat','Haryana',NULL,NULL),(465,'Pehowa','Haryana',NULL,NULL),(466,'Pinjore','Haryana',NULL,NULL),(467,'Rania','Haryana',NULL,NULL),(468,'Ratia','Haryana',NULL,NULL),(469,'Rewari','Haryana',NULL,NULL),(470,'Rohtak','Haryana',NULL,NULL),(471,'Safidon','Haryana',NULL,NULL),(472,'Samalkha','Haryana',NULL,NULL),(473,'Shahbad','Haryana',NULL,NULL),(474,'Sirsa','Haryana',NULL,NULL),(475,'Sohna','Haryana',NULL,NULL),(476,'Sonipat','Haryana',NULL,NULL),(477,'Taraori','Haryana',NULL,NULL),(478,'Thanesar','Haryana',NULL,NULL),(479,'Tohana','Haryana',NULL,NULL),(480,'Yamunanagar','Haryana',NULL,NULL),(481,'Arki','Himachal Pradesh',NULL,NULL),(482,'Baddi','Himachal Pradesh',NULL,NULL),(483,'Bilaspur','Himachal Pradesh',NULL,NULL),(484,'Chamba','Himachal Pradesh',NULL,NULL),(485,'Dalhousie','Himachal Pradesh',NULL,NULL),(486,'Dharamsala','Himachal Pradesh',NULL,NULL),(487,'Hamirpur','Himachal Pradesh',NULL,NULL),(488,'Mandi','Himachal Pradesh',NULL,NULL),(489,'Nahan','Himachal Pradesh',NULL,NULL),(490,'Shimla','Himachal Pradesh',NULL,NULL),(491,'Solan','Himachal Pradesh',NULL,NULL),(492,'Sundarnagar','Himachal Pradesh',NULL,NULL),(493,'Jammu','Jammu & Kashmir',NULL,NULL),(494,'Achabbal','Jammu and Kashmir',NULL,NULL),(495,'Akhnoor','Jammu and Kashmir',NULL,NULL),(496,'Anantnag','Jammu and Kashmir',NULL,NULL),(497,'Arnia','Jammu and Kashmir',NULL,NULL),(498,'Awantipora','Jammu and Kashmir',NULL,NULL),(499,'Bandipore','Jammu and Kashmir',NULL,NULL),(500,'Baramula','Jammu and Kashmir',NULL,NULL),(501,'Kathua','Jammu and Kashmir',NULL,NULL),(502,'Leh','Jammu and Kashmir',NULL,NULL),(503,'Punch','Jammu and Kashmir',NULL,NULL),(504,'Rajauri','Jammu and Kashmir',NULL,NULL),(505,'Sopore','Jammu and Kashmir',NULL,NULL),(506,'Srinagar','Jammu and Kashmir',NULL,NULL),(507,'Udhampur','Jammu and Kashmir',NULL,NULL),(508,'Amlabad','Jharkhand',NULL,NULL),(509,'Ara','Jharkhand',NULL,NULL),(510,'Barughutu','Jharkhand',NULL,NULL),(511,'Bokaro Steel City','Jharkhand',NULL,NULL),(512,'Chaibasa','Jharkhand',NULL,NULL),(513,'Chakradharpur','Jharkhand',NULL,NULL),(514,'Chandrapura','Jharkhand',NULL,NULL),(515,'Chatra','Jharkhand',NULL,NULL),(516,'Chirkunda','Jharkhand',NULL,NULL),(517,'Churi','Jharkhand',NULL,NULL),(518,'Daltonganj','Jharkhand',NULL,NULL),(519,'Deoghar','Jharkhand',NULL,NULL),(520,'Dhanbad','Jharkhand',NULL,NULL),(521,'Dumka','Jharkhand',NULL,NULL),(522,'Garhwa','Jharkhand',NULL,NULL),(523,'Ghatshila','Jharkhand',NULL,NULL),(524,'Giridih','Jharkhand',NULL,NULL),(525,'Godda','Jharkhand',NULL,NULL),(526,'Gomoh','Jharkhand',NULL,NULL),(527,'Gumia','Jharkhand',NULL,NULL),(528,'Gumla','Jharkhand',NULL,NULL),(529,'Hazaribag','Jharkhand',NULL,NULL),(530,'Hussainabad','Jharkhand',NULL,NULL),(531,'Jamshedpur','Jharkhand',NULL,NULL),(532,'Jamtara','Jharkhand',NULL,NULL),(533,'Jhumri Tilaiya','Jharkhand',NULL,NULL),(534,'Khunti','Jharkhand',NULL,NULL),(535,'Lohardaga','Jharkhand',NULL,NULL),(536,'Madhupur','Jharkhand',NULL,NULL),(537,'Mihijam','Jharkhand',NULL,NULL),(538,'Musabani','Jharkhand',NULL,NULL),(539,'Pakaur','Jharkhand',NULL,NULL),(540,'Patratu','Jharkhand',NULL,NULL),(541,'Phusro','Jharkhand',NULL,NULL),(542,'Ramngarh','Jharkhand',NULL,NULL),(543,'Ranchi','Jharkhand',NULL,NULL),(544,'Sahibganj','Jharkhand',NULL,NULL),(545,'Saunda','Jharkhand',NULL,NULL),(546,'Simdega','Jharkhand',NULL,NULL),(547,'Tenu Dam-cum- Kathhara','Jharkhand',NULL,NULL),(548,'Arasikere','Karnataka',NULL,NULL),(549,'Bangalore','Karnataka',NULL,NULL),(550,'Belgaum','Karnataka',NULL,NULL),(551,'Bellary','Karnataka',NULL,NULL),(552,'Chamrajnagar','Karnataka',NULL,NULL),(553,'Chikkaballapur','Karnataka',NULL,NULL),(554,'Chintamani','Karnataka',NULL,NULL),(555,'Chitradurga','Karnataka',NULL,NULL),(556,'Gulbarga','Karnataka',NULL,NULL),(557,'Gundlupet','Karnataka',NULL,NULL),(558,'Hassan','Karnataka',NULL,NULL),(559,'Hospet','Karnataka',NULL,NULL),(560,'Hubli','Karnataka',NULL,NULL),(561,'Karkala','Karnataka',NULL,NULL),(562,'Karwar','Karnataka',NULL,NULL),(563,'Kolar','Karnataka',NULL,NULL),(564,'Kota','Karnataka',NULL,NULL),(565,'Lakshmeshwar','Karnataka',NULL,NULL),(566,'Lingsugur','Karnataka',NULL,NULL),(567,'Maddur','Karnataka',NULL,NULL),(568,'Madhugiri','Karnataka',NULL,NULL),(569,'Madikeri','Karnataka',NULL,NULL),(570,'Magadi','Karnataka',NULL,NULL),(571,'Mahalingpur','Karnataka',NULL,NULL),(572,'Malavalli','Karnataka',NULL,NULL),(573,'Malur','Karnataka',NULL,NULL),(574,'Mandya','Karnataka',NULL,NULL),(575,'Mangalore','Karnataka',NULL,NULL),(576,'Manvi','Karnataka',NULL,NULL),(577,'Mudalgi','Karnataka',NULL,NULL),(578,'Mudbidri','Karnataka',NULL,NULL),(579,'Muddebihal','Karnataka',NULL,NULL),(580,'Mudhol','Karnataka',NULL,NULL),(581,'Mulbagal','Karnataka',NULL,NULL),(582,'Mundargi','Karnataka',NULL,NULL),(583,'Mysore','Karnataka',NULL,NULL),(584,'Nanjangud','Karnataka',NULL,NULL),(585,'Pavagada','Karnataka',NULL,NULL),(586,'Puttur','Karnataka',NULL,NULL),(587,'Rabkavi Banhatti','Karnataka',NULL,NULL),(588,'Raichur','Karnataka',NULL,NULL),(589,'Ramanagaram','Karnataka',NULL,NULL),(590,'Ramdurg','Karnataka',NULL,NULL),(591,'Ranibennur','Karnataka',NULL,NULL),(592,'Robertson Pet','Karnataka',NULL,NULL),(593,'Ron','Karnataka',NULL,NULL),(594,'Sadalgi','Karnataka',NULL,NULL),(595,'Sagar','Karnataka',NULL,NULL),(596,'Sakleshpur','Karnataka',NULL,NULL),(597,'Sandur','Karnataka',NULL,NULL),(598,'Sankeshwar','Karnataka',NULL,NULL),(599,'Saundatti-Yellamma','Karnataka',NULL,NULL),(600,'Savanur','Karnataka',NULL,NULL),(601,'Sedam','Karnataka',NULL,NULL),(602,'Shahabad','Karnataka',NULL,NULL),(603,'Shahpur','Karnataka',NULL,NULL),(604,'Shiggaon','Karnataka',NULL,NULL),(605,'Shikapur','Karnataka',NULL,NULL),(606,'Shimoga','Karnataka',NULL,NULL),(607,'Shorapur','Karnataka',NULL,NULL),(608,'Shrirangapattana','Karnataka',NULL,NULL),(609,'Sidlaghatta','Karnataka',NULL,NULL),(610,'Sindgi','Karnataka',NULL,NULL),(611,'Sindhnur','Karnataka',NULL,NULL),(612,'Sira','Karnataka',NULL,NULL),(613,'Sirsi','Karnataka',NULL,NULL),(614,'Siruguppa','Karnataka',NULL,NULL),(615,'Srinivaspur','Karnataka',NULL,NULL),(616,'Talikota','Karnataka',NULL,NULL),(617,'Tarikere','Karnataka',NULL,NULL),(618,'Tekkalakota','Karnataka',NULL,NULL),(619,'Terdal','Karnataka',NULL,NULL),(620,'Tiptur','Karnataka',NULL,NULL),(621,'Tumkur','Karnataka',NULL,NULL),(622,'Udupi','Karnataka',NULL,NULL),(623,'Vijayapura','Karnataka',NULL,NULL),(624,'Wadi','Karnataka',NULL,NULL),(625,'Yadgir','Karnataka',NULL,NULL),(626,'Adoor','Kerala',NULL,NULL),(627,'Akathiyoor','Kerala',NULL,NULL),(628,'Alappuzha','Kerala',NULL,NULL),(629,'Ancharakandy','Kerala',NULL,NULL),(630,'Aroor','Kerala',NULL,NULL),(631,'Ashtamichira','Kerala',NULL,NULL),(632,'Attingal','Kerala',NULL,NULL),(633,'Avinissery','Kerala',NULL,NULL),(634,'Chalakudy','Kerala',NULL,NULL),(635,'Changanassery','Kerala',NULL,NULL),(636,'Chendamangalam','Kerala',NULL,NULL),(637,'Chengannur','Kerala',NULL,NULL),(638,'Cherthala','Kerala',NULL,NULL),(639,'Cheruthazham','Kerala',NULL,NULL),(640,'Chittur-Thathamangalam','Kerala',NULL,NULL),(641,'Chockli','Kerala',NULL,NULL),(642,'Erattupetta','Kerala',NULL,NULL),(643,'Guruvayoor','Kerala',NULL,NULL),(644,'Irinjalakuda','Kerala',NULL,NULL),(645,'Kadirur','Kerala',NULL,NULL),(646,'Kalliasseri','Kerala',NULL,NULL),(647,'Kalpetta','Kerala',NULL,NULL),(648,'Kanhangad','Kerala',NULL,NULL),(649,'Kanjikkuzhi','Kerala',NULL,NULL),(650,'Kannur','Kerala',NULL,NULL),(651,'Kasaragod','Kerala',NULL,NULL),(652,'Kayamkulam','Kerala',NULL,NULL),(653,'Kochi','Kerala',NULL,NULL),(654,'Kodungallur','Kerala',NULL,NULL),(655,'Kollam','Kerala',NULL,NULL),(656,'Koothuparamba','Kerala',NULL,NULL),(657,'Kothamangalam','Kerala',NULL,NULL),(658,'Kottayam','Kerala',NULL,NULL),(659,'Kozhikode','Kerala',NULL,NULL),(660,'Kunnamkulam','Kerala',NULL,NULL),(661,'Malappuram','Kerala',NULL,NULL),(662,'Mattannur','Kerala',NULL,NULL),(663,'Mavelikkara','Kerala',NULL,NULL),(664,'Mavoor','Kerala',NULL,NULL),(665,'Muvattupuzha','Kerala',NULL,NULL),(666,'Nedumangad','Kerala',NULL,NULL),(667,'Neyyattinkara','Kerala',NULL,NULL),(668,'Ottappalam','Kerala',NULL,NULL),(669,'Palai','Kerala',NULL,NULL),(670,'Palakkad','Kerala',NULL,NULL),(671,'Panniyannur','Kerala',NULL,NULL),(672,'Pappinisseri','Kerala',NULL,NULL),(673,'Paravoor','Kerala',NULL,NULL),(674,'Pathanamthitta','Kerala',NULL,NULL),(675,'Payyannur','Kerala',NULL,NULL),(676,'Peringathur','Kerala',NULL,NULL),(677,'Perinthalmanna','Kerala',NULL,NULL),(678,'Perumbavoor','Kerala',NULL,NULL),(679,'Ponnani','Kerala',NULL,NULL),(680,'Punalur','Kerala',NULL,NULL),(681,'Quilandy','Kerala',NULL,NULL),(682,'Shoranur','Kerala',NULL,NULL),(683,'Taliparamba','Kerala',NULL,NULL),(684,'Thiruvalla','Kerala',NULL,NULL),(685,'Thiruvananthapuram','Kerala',NULL,NULL),(686,'Thodupuzha','Kerala',NULL,NULL),(687,'Thrissur','Kerala',NULL,NULL),(688,'Tirur','Kerala',NULL,NULL),(689,'Vadakara','Kerala',NULL,NULL),(690,'Vaikom','Kerala',NULL,NULL),(691,'Varkala','Kerala',NULL,NULL),(692,'Kavaratti','Lakshadweep',NULL,NULL),(693,'Ashok Nagar','Madhya Pradesh',NULL,NULL),(694,'Balaghat','Madhya Pradesh',NULL,NULL),(695,'Betul','Madhya Pradesh',NULL,NULL),(696,'Bhopal','Madhya Pradesh',NULL,NULL),(697,'Burhanpur','Madhya Pradesh',NULL,NULL),(698,'Chhatarpur','Madhya Pradesh',NULL,NULL),(699,'Dabra','Madhya Pradesh',NULL,NULL),(700,'Datia','Madhya Pradesh',NULL,NULL),(701,'Dewas','Madhya Pradesh',NULL,NULL),(702,'Dhar','Madhya Pradesh',NULL,NULL),(703,'Fatehabad','Madhya Pradesh',NULL,NULL),(704,'Gwalior','Madhya Pradesh',NULL,NULL),(705,'Indore','Madhya Pradesh',NULL,NULL),(706,'Itarsi','Madhya Pradesh',NULL,NULL),(707,'Jabalpur','Madhya Pradesh',NULL,NULL),(708,'Katni','Madhya Pradesh',NULL,NULL),(709,'Kotma','Madhya Pradesh',NULL,NULL),(710,'Lahar','Madhya Pradesh',NULL,NULL),(711,'Lundi','Madhya Pradesh',NULL,NULL),(712,'Maharajpur','Madhya Pradesh',NULL,NULL),(713,'Mahidpur','Madhya Pradesh',NULL,NULL),(714,'Maihar','Madhya Pradesh',NULL,NULL),(715,'Malajkhand','Madhya Pradesh',NULL,NULL),(716,'Manasa','Madhya Pradesh',NULL,NULL),(717,'Manawar','Madhya Pradesh',NULL,NULL),(718,'Mandideep','Madhya Pradesh',NULL,NULL),(719,'Mandla','Madhya Pradesh',NULL,NULL),(720,'Mandsaur','Madhya Pradesh',NULL,NULL),(721,'Mauganj','Madhya Pradesh',NULL,NULL),(722,'Mhow Cantonment','Madhya Pradesh',NULL,NULL),(723,'Mhowgaon','Madhya Pradesh',NULL,NULL),(724,'Morena','Madhya Pradesh',NULL,NULL),(725,'Multai','Madhya Pradesh',NULL,NULL),(726,'Murwara','Madhya Pradesh',NULL,NULL),(727,'Nagda','Madhya Pradesh',NULL,NULL),(728,'Nainpur','Madhya Pradesh',NULL,NULL),(729,'Narsinghgarh','Madhya Pradesh',NULL,NULL),(730,'Narsinghgarh','Madhya Pradesh',NULL,NULL),(731,'Neemuch','Madhya Pradesh',NULL,NULL),(732,'Nepanagar','Madhya Pradesh',NULL,NULL),(733,'Niwari','Madhya Pradesh',NULL,NULL),(734,'Nowgong','Madhya Pradesh',NULL,NULL),(735,'Nowrozabad','Madhya Pradesh',NULL,NULL),(736,'Pachore','Madhya Pradesh',NULL,NULL),(737,'Pali','Madhya Pradesh',NULL,NULL),(738,'Panagar','Madhya Pradesh',NULL,NULL),(739,'Pandhurna','Madhya Pradesh',NULL,NULL),(740,'Panna','Madhya Pradesh',NULL,NULL),(741,'Pasan','Madhya Pradesh',NULL,NULL),(742,'Pipariya','Madhya Pradesh',NULL,NULL),(743,'Pithampur','Madhya Pradesh',NULL,NULL),(744,'Porsa','Madhya Pradesh',NULL,NULL),(745,'Prithvipur','Madhya Pradesh',NULL,NULL),(746,'Raghogarh-Vijaypur','Madhya Pradesh',NULL,NULL),(747,'Rahatgarh','Madhya Pradesh',NULL,NULL),(748,'Raisen','Madhya Pradesh',NULL,NULL),(749,'Rajgarh','Madhya Pradesh',NULL,NULL),(750,'Ratlam','Madhya Pradesh',NULL,NULL),(751,'Rau','Madhya Pradesh',NULL,NULL),(752,'Rehli','Madhya Pradesh',NULL,NULL),(753,'Rewa','Madhya Pradesh',NULL,NULL),(754,'Sabalgarh','Madhya Pradesh',NULL,NULL),(755,'Sagar','Madhya Pradesh',NULL,NULL),(756,'Sanawad','Madhya Pradesh',NULL,NULL),(757,'Sarangpur','Madhya Pradesh',NULL,NULL),(758,'Sarni','Madhya Pradesh',NULL,NULL),(759,'Satna','Madhya Pradesh',NULL,NULL),(760,'Sausar','Madhya Pradesh',NULL,NULL),(761,'Sehore','Madhya Pradesh',NULL,NULL),(762,'Sendhwa','Madhya Pradesh',NULL,NULL),(763,'Seoni','Madhya Pradesh',NULL,NULL),(764,'Seoni-Malwa','Madhya Pradesh',NULL,NULL),(765,'Shahdol','Madhya Pradesh',NULL,NULL),(766,'Shajapur','Madhya Pradesh',NULL,NULL),(767,'Shamgarh','Madhya Pradesh',NULL,NULL),(768,'Sheopur','Madhya Pradesh',NULL,NULL),(769,'Shivpuri','Madhya Pradesh',NULL,NULL),(770,'Shujalpur','Madhya Pradesh',NULL,NULL),(771,'Sidhi','Madhya Pradesh',NULL,NULL),(772,'Sihora','Madhya Pradesh',NULL,NULL),(773,'Singrauli','Madhya Pradesh',NULL,NULL),(774,'Sironj','Madhya Pradesh',NULL,NULL),(775,'Sohagpur','Madhya Pradesh',NULL,NULL),(776,'Tarana','Madhya Pradesh',NULL,NULL),(777,'Tikamgarh','Madhya Pradesh',NULL,NULL),(778,'Ujhani','Madhya Pradesh',NULL,NULL),(779,'Ujjain','Madhya Pradesh',NULL,NULL),(780,'Umaria','Madhya Pradesh',NULL,NULL),(781,'Vidisha','Madhya Pradesh',NULL,NULL),(782,'Wara Seoni','Madhya Pradesh',NULL,NULL),(783,'Ahmednagar','Maharashtra',NULL,NULL),(784,'Akola','Maharashtra',NULL,NULL),(785,'Amravati','Maharashtra',NULL,NULL),(786,'Aurangabad','Maharashtra',NULL,NULL),(787,'Baramati','Maharashtra',NULL,NULL),(788,'Chalisgaon','Maharashtra',NULL,NULL),(789,'Chinchani','Maharashtra',NULL,NULL),(790,'Devgarh','Maharashtra',NULL,NULL),(791,'Dhule','Maharashtra',NULL,NULL),(792,'Dombivli','Maharashtra',NULL,NULL),(793,'Durgapur','Maharashtra',NULL,NULL),(794,'Ichalkaranji','Maharashtra',NULL,NULL),(795,'Jalna','Maharashtra',NULL,NULL),(796,'Kalyan','Maharashtra',NULL,NULL),(797,'Latur','Maharashtra',NULL,NULL),(798,'Loha','Maharashtra',NULL,NULL),(799,'Lonar','Maharashtra',NULL,NULL),(800,'Lonavla','Maharashtra',NULL,NULL),(801,'Mahad','Maharashtra',NULL,NULL),(802,'Mahuli','Maharashtra',NULL,NULL),(803,'Malegaon','Maharashtra',NULL,NULL),(804,'Malkapur','Maharashtra',NULL,NULL),(805,'Manchar','Maharashtra',NULL,NULL),(806,'Mangalvedhe','Maharashtra',NULL,NULL),(807,'Mangrulpir','Maharashtra',NULL,NULL),(808,'Manjlegaon','Maharashtra',NULL,NULL),(809,'Manmad','Maharashtra',NULL,NULL),(810,'Manwath','Maharashtra',NULL,NULL),(811,'Mehkar','Maharashtra',NULL,NULL),(812,'Mhaswad','Maharashtra',NULL,NULL),(813,'Miraj','Maharashtra',NULL,NULL),(814,'Morshi','Maharashtra',NULL,NULL),(815,'Mukhed','Maharashtra',NULL,NULL),(816,'Mul','Maharashtra',NULL,NULL),(817,'Mumbai','Maharashtra',NULL,NULL),(818,'Murtijapur','Maharashtra',NULL,NULL),(819,'Nagpur','Maharashtra',NULL,NULL),(820,'Nalasopara','Maharashtra',NULL,NULL),(821,'Nanded-Waghala','Maharashtra',NULL,NULL),(822,'Nandgaon','Maharashtra',NULL,NULL),(823,'Nandura','Maharashtra',NULL,NULL),(824,'Nandurbar','Maharashtra',NULL,NULL),(825,'Narkhed','Maharashtra',NULL,NULL),(826,'Nashik','Maharashtra',NULL,NULL),(827,'Navi Mumbai','Maharashtra',NULL,NULL),(828,'Nawapur','Maharashtra',NULL,NULL),(829,'Nilanga','Maharashtra',NULL,NULL),(830,'Osmanabad','Maharashtra',NULL,NULL),(831,'Ozar','Maharashtra',NULL,NULL),(832,'Pachora','Maharashtra',NULL,NULL),(833,'Paithan','Maharashtra',NULL,NULL),(834,'Palghar','Maharashtra',NULL,NULL),(835,'Pandharkaoda','Maharashtra',NULL,NULL),(836,'Pandharpur','Maharashtra',NULL,NULL),(837,'Panvel','Maharashtra',NULL,NULL),(838,'Parbhani','Maharashtra',NULL,NULL),(839,'Parli','Maharashtra',NULL,NULL),(840,'Parola','Maharashtra',NULL,NULL),(841,'Partur','Maharashtra',NULL,NULL),(842,'Pathardi','Maharashtra',NULL,NULL),(843,'Pathri','Maharashtra',NULL,NULL),(844,'Patur','Maharashtra',NULL,NULL),(845,'Pauni','Maharashtra',NULL,NULL),(846,'Pen','Maharashtra',NULL,NULL),(847,'Phaltan','Maharashtra',NULL,NULL),(848,'Pulgaon','Maharashtra',NULL,NULL),(849,'Pune','Maharashtra',NULL,NULL),(850,'Purna','Maharashtra',NULL,NULL),(851,'Pusad','Maharashtra',NULL,NULL),(852,'Rahuri','Maharashtra',NULL,NULL),(853,'Rajura','Maharashtra',NULL,NULL),(854,'Ramtek','Maharashtra',NULL,NULL),(855,'Ratnagiri','Maharashtra',NULL,NULL),(856,'Raver','Maharashtra',NULL,NULL),(857,'Risod','Maharashtra',NULL,NULL),(858,'Sailu','Maharashtra',NULL,NULL),(859,'Sangamner','Maharashtra',NULL,NULL),(860,'Sangli','Maharashtra',NULL,NULL),(861,'Sangole','Maharashtra',NULL,NULL),(862,'Sasvad','Maharashtra',NULL,NULL),(863,'Satana','Maharashtra',NULL,NULL),(864,'Satara','Maharashtra',NULL,NULL),(865,'Savner','Maharashtra',NULL,NULL),(866,'Sawantwadi','Maharashtra',NULL,NULL),(867,'Shahade','Maharashtra',NULL,NULL),(868,'Shegaon','Maharashtra',NULL,NULL),(869,'Shendurjana','Maharashtra',NULL,NULL),(870,'Shirdi','Maharashtra',NULL,NULL),(871,'Shirpur-Warwade','Maharashtra',NULL,NULL),(872,'Shirur','Maharashtra',NULL,NULL),(873,'Shrigonda','Maharashtra',NULL,NULL),(874,'Shrirampur','Maharashtra',NULL,NULL),(875,'Sillod','Maharashtra',NULL,NULL),(876,'Sinnar','Maharashtra',NULL,NULL),(877,'Solapur','Maharashtra',NULL,NULL),(878,'Soyagaon','Maharashtra',NULL,NULL),(879,'Talegaon Dabhade','Maharashtra',NULL,NULL),(880,'Talode','Maharashtra',NULL,NULL),(881,'Tasgaon','Maharashtra',NULL,NULL),(882,'Tirora','Maharashtra',NULL,NULL),(883,'Tuljapur','Maharashtra',NULL,NULL),(884,'Tumsar','Maharashtra',NULL,NULL),(885,'Uran','Maharashtra',NULL,NULL),(886,'Uran Islampur','Maharashtra',NULL,NULL),(887,'Wadgaon Road','Maharashtra',NULL,NULL),(888,'Wai','Maharashtra',NULL,NULL),(889,'Wani','Maharashtra',NULL,NULL),(890,'Wardha','Maharashtra',NULL,NULL),(891,'Warora','Maharashtra',NULL,NULL),(892,'Warud','Maharashtra',NULL,NULL),(893,'Washim','Maharashtra',NULL,NULL),(894,'Yevla','Maharashtra',NULL,NULL),(895,'Uchgaon','Maharastra',NULL,NULL),(896,'Udgir','Maharastra',NULL,NULL),(897,'Umarga','Maharastra',NULL,NULL),(898,'Umarkhed','Maharastra',NULL,NULL),(899,'Umred','Maharastra',NULL,NULL),(900,'Vadgaon Kasba','Maharastra',NULL,NULL),(901,'Vaijapur','Maharastra',NULL,NULL),(902,'Vasai','Maharastra',NULL,NULL),(903,'Virar','Maharastra',NULL,NULL),(904,'Vita','Maharastra',NULL,NULL),(905,'Yavatmal','Maharastra',NULL,NULL),(906,'Yawal','Maharastra',NULL,NULL),(907,'Imphal','Manipur',NULL,NULL),(908,'Kakching','Manipur',NULL,NULL),(909,'Lilong','Manipur',NULL,NULL),(910,'Mayang Imphal','Manipur',NULL,NULL),(911,'Thoubal','Manipur',NULL,NULL),(912,'Jowai','Meghalaya',NULL,NULL),(913,'Nongstoin','Meghalaya',NULL,NULL),(914,'Shillong','Meghalaya',NULL,NULL),(915,'Tura','Meghalaya',NULL,NULL),(916,'Aizawl','Mizoram',NULL,NULL),(917,'Champhai','Mizoram',NULL,NULL),(918,'Lunglei','Mizoram',NULL,NULL),(919,'Saiha','Mizoram',NULL,NULL),(920,'Dimapur','Nagaland',NULL,NULL),(921,'Kohima','Nagaland',NULL,NULL),(922,'Mokokchung','Nagaland',NULL,NULL),(923,'Tuensang','Nagaland',NULL,NULL),(924,'Wokha','Nagaland',NULL,NULL),(925,'Zunheboto','Nagaland',NULL,NULL),(950,'Anandapur','Orissa',NULL,NULL),(951,'Anugul','Orissa',NULL,NULL),(952,'Asika','Orissa',NULL,NULL),(953,'Balangir','Orissa',NULL,NULL),(954,'Balasore','Orissa',NULL,NULL),(955,'Baleshwar','Orissa',NULL,NULL),(956,'Bamra','Orissa',NULL,NULL),(957,'Barbil','Orissa',NULL,NULL),(958,'Bargarh','Orissa',NULL,NULL),(959,'Bargarh','Orissa',NULL,NULL),(960,'Baripada','Orissa',NULL,NULL),(961,'Basudebpur','Orissa',NULL,NULL),(962,'Belpahar','Orissa',NULL,NULL),(963,'Bhadrak','Orissa',NULL,NULL),(964,'Bhawanipatna','Orissa',NULL,NULL),(965,'Bhuban','Orissa',NULL,NULL),(966,'Bhubaneswar','Orissa',NULL,NULL),(967,'Biramitrapur','Orissa',NULL,NULL),(968,'Brahmapur','Orissa',NULL,NULL),(969,'Brajrajnagar','Orissa',NULL,NULL),(970,'Byasanagar','Orissa',NULL,NULL),(971,'Cuttack','Orissa',NULL,NULL),(972,'Debagarh','Orissa',NULL,NULL),(973,'Dhenkanal','Orissa',NULL,NULL),(974,'Gunupur','Orissa',NULL,NULL),(975,'Hinjilicut','Orissa',NULL,NULL),(976,'Jagatsinghapur','Orissa',NULL,NULL),(977,'Jajapur','Orissa',NULL,NULL),(978,'Jaleswar','Orissa',NULL,NULL),(979,'Jatani','Orissa',NULL,NULL),(980,'Jeypur','Orissa',NULL,NULL),(981,'Jharsuguda','Orissa',NULL,NULL),(982,'Joda','Orissa',NULL,NULL),(983,'Kantabanji','Orissa',NULL,NULL),(984,'Karanjia','Orissa',NULL,NULL),(985,'Kendrapara','Orissa',NULL,NULL),(986,'Kendujhar','Orissa',NULL,NULL),(987,'Khordha','Orissa',NULL,NULL),(988,'Koraput','Orissa',NULL,NULL),(989,'Malkangiri','Orissa',NULL,NULL),(990,'Nabarangapur','Orissa',NULL,NULL),(991,'Paradip','Orissa',NULL,NULL),(992,'Parlakhemundi','Orissa',NULL,NULL),(993,'Pattamundai','Orissa',NULL,NULL),(994,'Phulabani','Orissa',NULL,NULL),(995,'Puri','Orissa',NULL,NULL),(996,'Rairangpur','Orissa',NULL,NULL),(997,'Rajagangapur','Orissa',NULL,NULL),(998,'Raurkela','Orissa',NULL,NULL),(999,'Rayagada','Orissa',NULL,NULL),(1000,'Sambalpur','Orissa',NULL,NULL),(1001,'Soro','Orissa',NULL,NULL),(1002,'Sunabeda','Orissa',NULL,NULL),(1003,'Sundargarh','Orissa',NULL,NULL),(1004,'Talcher','Orissa',NULL,NULL),(1005,'Titlagarh','Orissa',NULL,NULL),(1006,'Umarkote','Orissa',NULL,NULL),(1007,'Karaikal','Pondicherry',NULL,NULL),(1008,'Mahe','Pondicherry',NULL,NULL),(1009,'Kolhapur','Maharashtra',NULL,NULL),(1010,'Yanam','Pondicherry',NULL,NULL),(1011,'Ahmedgarh','Punjab',NULL,NULL),(1012,'Amritsar','Punjab',NULL,NULL),(1013,'Barnala','Punjab',NULL,NULL),(1014,'Batala','Punjab',NULL,NULL),(1015,'Bathinda','Punjab',NULL,NULL),(1016,'Bhagha Purana','Punjab',NULL,NULL),(1017,'Budhlada','Punjab',NULL,NULL),(1018,'Chandigarh','Punjab',NULL,NULL),(1019,'Dasua','Punjab',NULL,NULL),(1020,'Dhuri','Punjab',NULL,NULL),(1021,'Dinanagar','Punjab',NULL,NULL),(1022,'Faridkot','Punjab',NULL,NULL),(1023,'Fazilka','Punjab',NULL,NULL),(1024,'Firozpur','Punjab',NULL,NULL),(1025,'Firozpur Cantt.','Punjab',NULL,NULL),(1026,'Giddarbaha','Punjab',NULL,NULL),(1027,'Gobindgarh','Punjab',NULL,NULL),(1028,'Gurdaspur','Punjab',NULL,NULL),(1029,'Hoshiarpur','Punjab',NULL,NULL),(1030,'Jagraon','Punjab',NULL,NULL),(1031,'Jaitu','Punjab',NULL,NULL),(1032,'Jalalabad','Punjab',NULL,NULL),(1033,'Jalandhar','Punjab',NULL,NULL),(1034,'Jalandhar Cantt.','Punjab',NULL,NULL),(1035,'Jandiala','Punjab',NULL,NULL),(1036,'Kapurthala','Punjab',NULL,NULL),(1037,'Karoran','Punjab',NULL,NULL),(1038,'Kartarpur','Punjab',NULL,NULL),(1039,'Khanna','Punjab',NULL,NULL),(1040,'Kharar','Punjab',NULL,NULL),(1041,'Kot Kapura','Punjab',NULL,NULL),(1042,'Kurali','Punjab',NULL,NULL),(1043,'Longowal','Punjab',NULL,NULL),(1044,'Ludhiana','Punjab',NULL,NULL),(1045,'Malerkotla','Punjab',NULL,NULL),(1046,'Malout','Punjab',NULL,NULL),(1047,'Mansa','Punjab',NULL,NULL),(1048,'Maur','Punjab',NULL,NULL),(1049,'Moga','Punjab',NULL,NULL),(1050,'Mohali','Punjab',NULL,NULL),(1051,'Morinda','Punjab',NULL,NULL),(1052,'Mukerian','Punjab',NULL,NULL),(1053,'Muktsar','Punjab',NULL,NULL),(1054,'Nabha','Punjab',NULL,NULL),(1055,'Nakodar','Punjab',NULL,NULL),(1056,'Nangal','Punjab',NULL,NULL),(1057,'Nawanshahr','Punjab',NULL,NULL),(1058,'Pathankot','Punjab',NULL,NULL),(1059,'Patiala','Punjab',NULL,NULL),(1060,'Patran','Punjab',NULL,NULL),(1061,'Patti','Punjab',NULL,NULL),(1062,'Phagwara','Punjab',NULL,NULL),(1063,'Phillaur','Punjab',NULL,NULL),(1064,'Qadian','Punjab',NULL,NULL),(1065,'Raikot','Punjab',NULL,NULL),(1066,'Rajpura','Punjab',NULL,NULL),(1067,'Rampura Phul','Punjab',NULL,NULL),(1068,'Rupnagar','Punjab',NULL,NULL),(1069,'Samana','Punjab',NULL,NULL),(1070,'Sangrur','Punjab',NULL,NULL),(1071,'Sirhind Fatehgarh Sahib','Punjab',NULL,NULL),(1072,'Sujanpur','Punjab',NULL,NULL),(1073,'Sunam','Punjab',NULL,NULL),(1074,'Talwara','Punjab',NULL,NULL),(1075,'Tarn Taran','Punjab',NULL,NULL),(1076,'Urmar Tanda','Punjab',NULL,NULL),(1077,'Zira','Punjab',NULL,NULL),(1078,'Zirakpur','Punjab',NULL,NULL),(1079,'Bali','Rajastan',NULL,NULL),(1080,'Banswara','Rajastan',NULL,NULL),(1081,'Ajmer','Rajasthan',NULL,NULL),(1082,'Alwar','Rajasthan',NULL,NULL),(1083,'Bandikui','Rajasthan',NULL,NULL),(1084,'Baran','Rajasthan',NULL,NULL),(1085,'Barmer','Rajasthan',NULL,NULL),(1086,'Bikaner','Rajasthan',NULL,NULL),(1087,'Fatehpur','Rajasthan',NULL,NULL),(1088,'Jaipur','Rajasthan',NULL,NULL),(1089,'Jaisalmer','Rajasthan',NULL,NULL),(1090,'Jodhpur','Rajasthan',NULL,NULL),(1091,'Kota','Rajasthan',NULL,NULL),(1092,'Lachhmangarh','Rajasthan',NULL,NULL),(1093,'Ladnu','Rajasthan',NULL,NULL),(1094,'Lakheri','Rajasthan',NULL,NULL),(1095,'Lalsot','Rajasthan',NULL,NULL),(1096,'Losal','Rajasthan',NULL,NULL),(1097,'Makrana','Rajasthan',NULL,NULL),(1098,'Malpura','Rajasthan',NULL,NULL),(1099,'Mandalgarh','Rajasthan',NULL,NULL),(1100,'Mandawa','Rajasthan',NULL,NULL),(1101,'Mangrol','Rajasthan',NULL,NULL),(1102,'Merta City','Rajasthan',NULL,NULL),(1103,'Mount Abu','Rajasthan',NULL,NULL),(1104,'Nadbai','Rajasthan',NULL,NULL),(1105,'Nagar','Rajasthan',NULL,NULL),(1106,'Nagaur','Rajasthan',NULL,NULL),(1107,'Nargund','Rajasthan',NULL,NULL),(1108,'Nasirabad','Rajasthan',NULL,NULL),(1109,'Nathdwara','Rajasthan',NULL,NULL),(1110,'Navalgund','Rajasthan',NULL,NULL),(1111,'Nawalgarh','Rajasthan',NULL,NULL),(1112,'Neem-Ka-Thana','Rajasthan',NULL,NULL),(1113,'Nelamangala','Rajasthan',NULL,NULL),(1114,'Nimbahera','Rajasthan',NULL,NULL),(1115,'Nipani','Rajasthan',NULL,NULL),(1116,'Niwai','Rajasthan',NULL,NULL),(1117,'Nohar','Rajasthan',NULL,NULL),(1118,'Nokha','Rajasthan',NULL,NULL),(1119,'Pali','Rajasthan',NULL,NULL),(1120,'Phalodi','Rajasthan',NULL,NULL),(1121,'Phulera','Rajasthan',NULL,NULL),(1122,'Pilani','Rajasthan',NULL,NULL),(1123,'Pilibanga','Rajasthan',NULL,NULL),(1124,'Pindwara','Rajasthan',NULL,NULL),(1125,'Pipar City','Rajasthan',NULL,NULL),(1126,'Prantij','Rajasthan',NULL,NULL),(1127,'Pratapgarh','Rajasthan',NULL,NULL),(1128,'Raisinghnagar','Rajasthan',NULL,NULL),(1129,'Rajakhera','Rajasthan',NULL,NULL),(1130,'Rajaldesar','Rajasthan',NULL,NULL),(1131,'Rajgarh (Alwar)','Rajasthan',NULL,NULL),(1132,'Rajgarh (Churu','Rajasthan',NULL,NULL),(1133,'Rajsamand','Rajasthan',NULL,NULL),(1134,'Ramganj Mandi','Rajasthan',NULL,NULL),(1135,'Ramngarh','Rajasthan',NULL,NULL),(1136,'Ratangarh','Rajasthan',NULL,NULL),(1137,'Rawatbhata','Rajasthan',NULL,NULL),(1138,'Rawatsar','Rajasthan',NULL,NULL),(1139,'Reengus','Rajasthan',NULL,NULL),(1140,'Sadri','Rajasthan',NULL,NULL),(1141,'Sadulshahar','Rajasthan',NULL,NULL),(1142,'Sagwara','Rajasthan',NULL,NULL),(1143,'Sambhar','Rajasthan',NULL,NULL),(1144,'Sanchore','Rajasthan',NULL,NULL),(1145,'Sangaria','Rajasthan',NULL,NULL),(1146,'Sardarshahar','Rajasthan',NULL,NULL),(1147,'Sawai Madhopur','Rajasthan',NULL,NULL),(1148,'Shahpura','Rajasthan',NULL,NULL),(1149,'Shahpura','Rajasthan',NULL,NULL),(1150,'Sheoganj','Rajasthan',NULL,NULL),(1151,'Sikar','Rajasthan',NULL,NULL),(1152,'Sirohi','Rajasthan',NULL,NULL),(1153,'Sojat','Rajasthan',NULL,NULL),(1154,'Sri Madhopur','Rajasthan',NULL,NULL),(1155,'Sujangarh','Rajasthan',NULL,NULL),(1156,'Sumerpur','Rajasthan',NULL,NULL),(1157,'Suratgarh','Rajasthan',NULL,NULL),(1158,'Taranagar','Rajasthan',NULL,NULL),(1159,'Todabhim','Rajasthan',NULL,NULL),(1160,'Todaraisingh','Rajasthan',NULL,NULL),(1161,'Tonk','Rajasthan',NULL,NULL),(1162,'Udaipur','Rajasthan',NULL,NULL),(1163,'Udaipurwati','Rajasthan',NULL,NULL),(1164,'Vijainagar','Rajasthan',NULL,NULL),(1165,'Gangtok','Sikkim',NULL,NULL),(1166,'Calcutta','West Bengal',NULL,NULL),(1167,'Arakkonam','Tamil Nadu',NULL,NULL),(1168,'Arcot','Tamil Nadu',NULL,NULL),(1169,'Aruppukkottai','Tamil Nadu',NULL,NULL),(1170,'Bhavani','Tamil Nadu',NULL,NULL),(1171,'Chengalpattu','Tamil Nadu',NULL,NULL),(1172,'Port Blair','Andaman and Nicobar Islands',NULL,NULL),(1173,'Chinna salem','Tamil nadu',NULL,NULL),(1174,'Coimbatore','Tamil Nadu',NULL,NULL),(1175,'Coonoor','Tamil Nadu',NULL,NULL),(1176,'Cuddalore','Tamil Nadu',NULL,NULL),(1177,'Dharmapuri','Tamil Nadu',NULL,NULL),(1178,'Dindigul','Tamil Nadu',NULL,NULL),(1179,'Erode','Tamil Nadu',NULL,NULL),(1180,'Gudalur','Tamil Nadu',NULL,NULL),(1181,'Gudalur','Tamil Nadu',NULL,NULL),(1182,'Gudalur','Tamil Nadu',NULL,NULL),(1183,'Kanchipuram','Tamil Nadu',NULL,NULL),(1184,'Karaikudi','Tamil Nadu',NULL,NULL),(1185,'Karungal','Tamil Nadu',NULL,NULL),(1186,'Karur','Tamil Nadu',NULL,NULL),(1187,'Kollankodu','Tamil Nadu',NULL,NULL),(1188,'Lalgudi','Tamil Nadu',NULL,NULL),(1189,'Madurai','Tamil Nadu',NULL,NULL),(1190,'Nagapattinam','Tamil Nadu',NULL,NULL),(1191,'Nagercoil','Tamil Nadu',NULL,NULL),(1192,'Namagiripettai','Tamil Nadu',NULL,NULL),(1193,'Namakkal','Tamil Nadu',NULL,NULL),(1194,'Nandivaram-Guduvancheri','Tamil Nadu',NULL,NULL),(1195,'Nanjikottai','Tamil Nadu',NULL,NULL),(1196,'Natham','Tamil Nadu',NULL,NULL),(1197,'Nellikuppam','Tamil Nadu',NULL,NULL),(1198,'Neyveli','Tamil Nadu',NULL,NULL),(1199,'OValley','Tamil Nadu',NULL,NULL),(1200,'Oddanchatram','Tamil Nadu',NULL,NULL),(1201,'P.N.Patti','Tamil Nadu',NULL,NULL),(1202,'Pacode','Tamil Nadu',NULL,NULL),(1203,'Padmanabhapuram','Tamil Nadu',NULL,NULL),(1204,'Palani','Tamil Nadu',NULL,NULL),(1205,'Palladam','Tamil Nadu',NULL,NULL),(1206,'Pallapatti','Tamil Nadu',NULL,NULL),(1207,'Pallikonda','Tamil Nadu',NULL,NULL),(1208,'Panagudi','Tamil Nadu',NULL,NULL),(1209,'Panruti','Tamil Nadu',NULL,NULL),(1210,'Paramakudi','Tamil Nadu',NULL,NULL),(1211,'Parangipettai','Tamil Nadu',NULL,NULL),(1212,'Pattukkottai','Tamil Nadu',NULL,NULL),(1213,'Perambalur','Tamil Nadu',NULL,NULL),(1214,'Peravurani','Tamil Nadu',NULL,NULL),(1215,'Periyakulam','Tamil Nadu',NULL,NULL),(1216,'Periyasemur','Tamil Nadu',NULL,NULL),(1217,'Pernampattu','Tamil Nadu',NULL,NULL),(1218,'Pollachi','Tamil Nadu',NULL,NULL),(1219,'Polur','Tamil Nadu',NULL,NULL),(1220,'Ponneri','Tamil Nadu',NULL,NULL),(1221,'Pudukkottai','Tamil Nadu',NULL,NULL),(1222,'Pudupattinam','Tamil Nadu',NULL,NULL),(1223,'Puliyankudi','Tamil Nadu',NULL,NULL),(1224,'Punjaipugalur','Tamil Nadu',NULL,NULL),(1225,'Rajapalayam','Tamil Nadu',NULL,NULL),(1226,'Ramanathapuram','Tamil Nadu',NULL,NULL),(1227,'Rameshwaram','Tamil Nadu',NULL,NULL),(1228,'Rasipuram','Tamil Nadu',NULL,NULL),(1229,'Salem','Tamil Nadu',NULL,NULL),(1230,'Sankarankoil','Tamil Nadu',NULL,NULL),(1231,'Sankari','Tamil Nadu',NULL,NULL),(1232,'Sathyamangalam','Tamil Nadu',NULL,NULL),(1233,'Sattur','Tamil Nadu',NULL,NULL),(1234,'Shenkottai','Tamil Nadu',NULL,NULL),(1235,'Sholavandan','Tamil Nadu',NULL,NULL),(1236,'Sholingur','Tamil Nadu',NULL,NULL),(1237,'Sirkali','Tamil Nadu',NULL,NULL),(1238,'Sivaganga','Tamil Nadu',NULL,NULL),(1239,'Sivagiri','Tamil Nadu',NULL,NULL),(1240,'Sivakasi','Tamil Nadu',NULL,NULL),(1241,'Srivilliputhur','Tamil Nadu',NULL,NULL),(1242,'Surandai','Tamil Nadu',NULL,NULL),(1243,'Suriyampalayam','Tamil Nadu',NULL,NULL),(1244,'Tenkasi','Tamil Nadu',NULL,NULL),(1245,'Thammampatti','Tamil Nadu',NULL,NULL),(1246,'Thanjavur','Tamil Nadu',NULL,NULL),(1247,'Tharamangalam','Tamil Nadu',NULL,NULL),(1248,'Tharangambadi','Tamil Nadu',NULL,NULL),(1249,'Theni Allinagaram','Tamil Nadu',NULL,NULL),(1250,'Thirumangalam','Tamil Nadu',NULL,NULL),(1251,'Thirunindravur','Tamil Nadu',NULL,NULL),(1252,'Thiruparappu','Tamil Nadu',NULL,NULL),(1253,'Thirupuvanam','Tamil Nadu',NULL,NULL),(1254,'Thiruthuraipoondi','Tamil Nadu',NULL,NULL),(1255,'Thiruvallur','Tamil Nadu',NULL,NULL),(1256,'Thiruvarur','Tamil Nadu',NULL,NULL),(1257,'Thoothukudi','Tamil Nadu',NULL,NULL),(1258,'Thuraiyur','Tamil Nadu',NULL,NULL),(1259,'Tindivanam','Tamil Nadu',NULL,NULL),(1260,'Tiruchendur','Tamil Nadu',NULL,NULL),(1261,'Tiruchengode','Tamil Nadu',NULL,NULL),(1262,'Tiruchirappalli','Tamil Nadu',NULL,NULL),(1263,'Tirukalukundram','Tamil Nadu',NULL,NULL),(1264,'Tirukkoyilur','Tamil Nadu',NULL,NULL),(1265,'Tirunelveli','Tamil Nadu',NULL,NULL),(1266,'Tirupathur','Tamil Nadu',NULL,NULL),(1267,'Tirupathur','Tamil Nadu',NULL,NULL),(1268,'Tiruppur','Tamil Nadu',NULL,NULL),(1269,'Tiruttani','Tamil Nadu',NULL,NULL),(1270,'Tiruvannamalai','Tamil Nadu',NULL,NULL),(1271,'Tiruvethipuram','Tamil Nadu',NULL,NULL),(1272,'Tittakudi','Tamil Nadu',NULL,NULL),(1273,'Udhagamandalam','Tamil Nadu',NULL,NULL),(1274,'Udumalaipettai','Tamil Nadu',NULL,NULL),(1275,'Unnamalaikadai','Tamil Nadu',NULL,NULL),(1276,'Usilampatti','Tamil Nadu',NULL,NULL),(1277,'Uthamapalayam','Tamil Nadu',NULL,NULL),(1278,'Uthiramerur','Tamil Nadu',NULL,NULL),(1279,'Vadakkuvalliyur','Tamil Nadu',NULL,NULL),(1280,'Vadalur','Tamil Nadu',NULL,NULL),(1281,'Vadipatti','Tamil Nadu',NULL,NULL),(1282,'Valparai','Tamil Nadu',NULL,NULL),(1283,'Vandavasi','Tamil Nadu',NULL,NULL),(1284,'Vaniyambadi','Tamil Nadu',NULL,NULL),(1285,'Vedaranyam','Tamil Nadu',NULL,NULL),(1286,'Vellakoil','Tamil Nadu',NULL,NULL),(1287,'Vellore','Tamil Nadu',NULL,NULL),(1288,'Vikramasingapuram','Tamil Nadu',NULL,NULL),(1289,'Viluppuram','Tamil Nadu',NULL,NULL),(1290,'Virudhachalam','Tamil Nadu',NULL,NULL),(1291,'Virudhunagar','Tamil Nadu',NULL,NULL),(1292,'Viswanatham','Tamil Nadu',NULL,NULL),(1293,'Agartala','Tripura',NULL,NULL),(1294,'Badharghat','Tripura',NULL,NULL),(1295,'Dharmanagar','Tripura',NULL,NULL),(1296,'Indranagar','Tripura',NULL,NULL),(1297,'Jogendranagar','Tripura',NULL,NULL),(1298,'Kailasahar','Tripura',NULL,NULL),(1299,'Khowai','Tripura',NULL,NULL),(1300,'Pratapgarh','Tripura',NULL,NULL),(1301,'Udaipur','Tripura',NULL,NULL),(1302,'Achhnera','Uttar Pradesh',NULL,NULL),(1303,'Adari','Uttar Pradesh',NULL,NULL),(1304,'Agra','Uttar Pradesh',NULL,NULL),(1305,'Aligarh','Uttar Pradesh',NULL,NULL),(1306,'Allahabad','Uttar Pradesh',NULL,NULL),(1307,'Amroha','Uttar Pradesh',NULL,NULL),(1308,'Azamgarh','Uttar Pradesh',NULL,NULL),(1309,'Bahraich','Uttar Pradesh',NULL,NULL),(1310,'Ballia','Uttar Pradesh',NULL,NULL),(1311,'Balrampur','Uttar Pradesh',NULL,NULL),(1312,'Banda','Uttar Pradesh',NULL,NULL),(1313,'Bareilly','Uttar Pradesh',NULL,NULL),(1314,'Chandausi','Uttar Pradesh',NULL,NULL),(1315,'Dadri','Uttar Pradesh',NULL,NULL),(1316,'Deoria','Uttar Pradesh',NULL,NULL),(1317,'Etawah','Uttar Pradesh',NULL,NULL),(1318,'Fatehabad','Uttar Pradesh',NULL,NULL),(1319,'Fatehpur','Uttar Pradesh',NULL,NULL),(1320,'Fatehpur','Uttar Pradesh',NULL,NULL),(1321,'Greater Noida','Uttar Pradesh',NULL,NULL),(1322,'Hamirpur','Uttar Pradesh',NULL,NULL),(1323,'Hardoi','Uttar Pradesh',NULL,NULL),(1324,'Jajmau','Uttar Pradesh',NULL,NULL),(1325,'Jaunpur','Uttar Pradesh',NULL,NULL),(1326,'Jhansi','Uttar Pradesh',NULL,NULL),(1327,'Kalpi','Uttar Pradesh',NULL,NULL),(1328,'Kanpur','Uttar Pradesh',NULL,NULL),(1329,'Kota','Uttar Pradesh',NULL,NULL),(1330,'Laharpur','Uttar Pradesh',NULL,NULL),(1331,'Lakhimpur','Uttar Pradesh',NULL,NULL),(1332,'Lal Gopalganj Nindaura','Uttar Pradesh',NULL,NULL),(1333,'Lalganj','Uttar Pradesh',NULL,NULL),(1334,'Lalitpur','Uttar Pradesh',NULL,NULL),(1335,'Lar','Uttar Pradesh',NULL,NULL),(1336,'Loni','Uttar Pradesh',NULL,NULL),(1337,'Lucknow','Uttar Pradesh',NULL,NULL),(1338,'Mathura','Uttar Pradesh',NULL,NULL),(1339,'Meerut','Uttar Pradesh',NULL,NULL),(1340,'Modinagar','Uttar Pradesh',NULL,NULL),(1341,'Muradnagar','Uttar Pradesh',NULL,NULL),(1342,'Nagina','Uttar Pradesh',NULL,NULL),(1343,'Najibabad','Uttar Pradesh',NULL,NULL),(1344,'Nakur','Uttar Pradesh',NULL,NULL),(1345,'Nanpara','Uttar Pradesh',NULL,NULL),(1346,'Naraura','Uttar Pradesh',NULL,NULL),(1347,'Naugawan Sadat','Uttar Pradesh',NULL,NULL),(1348,'Nautanwa','Uttar Pradesh',NULL,NULL),(1349,'Nawabganj','Uttar Pradesh',NULL,NULL),(1350,'Nehtaur','Uttar Pradesh',NULL,NULL),(1351,'NOIDA','Uttar Pradesh',NULL,NULL),(1352,'Noorpur','Uttar Pradesh',NULL,NULL),(1353,'Obra','Uttar Pradesh',NULL,NULL),(1354,'Orai','Uttar Pradesh',NULL,NULL),(1355,'Padrauna','Uttar Pradesh',NULL,NULL),(1356,'Palia Kalan','Uttar Pradesh',NULL,NULL),(1357,'Parasi','Uttar Pradesh',NULL,NULL),(1358,'Phulpur','Uttar Pradesh',NULL,NULL),(1359,'Pihani','Uttar Pradesh',NULL,NULL),(1360,'Pilibhit','Uttar Pradesh',NULL,NULL),(1361,'Pilkhuwa','Uttar Pradesh',NULL,NULL),(1362,'Powayan','Uttar Pradesh',NULL,NULL),(1363,'Pukhrayan','Uttar Pradesh',NULL,NULL),(1364,'Puranpur','Uttar Pradesh',NULL,NULL),(1365,'Purquazi','Uttar Pradesh',NULL,NULL),(1366,'Purwa','Uttar Pradesh',NULL,NULL),(1367,'Rae Bareli','Uttar Pradesh',NULL,NULL),(1368,'Rampur','Uttar Pradesh',NULL,NULL),(1369,'Rampur Maniharan','Uttar Pradesh',NULL,NULL),(1370,'Rasra','Uttar Pradesh',NULL,NULL),(1371,'Rath','Uttar Pradesh',NULL,NULL),(1372,'Renukoot','Uttar Pradesh',NULL,NULL),(1373,'Reoti','Uttar Pradesh',NULL,NULL),(1374,'Robertsganj','Uttar Pradesh',NULL,NULL),(1375,'Rudauli','Uttar Pradesh',NULL,NULL),(1376,'Rudrapur','Uttar Pradesh',NULL,NULL),(1377,'Sadabad','Uttar Pradesh',NULL,NULL),(1378,'Safipur','Uttar Pradesh',NULL,NULL),(1379,'Saharanpur','Uttar Pradesh',NULL,NULL),(1380,'Sahaspur','Uttar Pradesh',NULL,NULL),(1381,'Sahaswan','Uttar Pradesh',NULL,NULL),(1382,'Sahawar','Uttar Pradesh',NULL,NULL),(1383,'Sahjanwa','Uttar Pradesh',NULL,NULL),(1384,'\"Saidpur',' Ghazipur\"',NULL,NULL),(1385,'Sambhal','Uttar Pradesh',NULL,NULL),(1386,'Samdhan','Uttar Pradesh',NULL,NULL),(1387,'Samthar','Uttar Pradesh',NULL,NULL),(1388,'Sandi','Uttar Pradesh',NULL,NULL),(1389,'Sandila','Uttar Pradesh',NULL,NULL),(1390,'Sardhana','Uttar Pradesh',NULL,NULL),(1391,'Seohara','Uttar Pradesh',NULL,NULL),(1392,'\"Shahabad',' Hardoi\"',NULL,NULL),(1393,'\"Shahabad',' Rampur\"',NULL,NULL),(1394,'Shahganj','Uttar Pradesh',NULL,NULL),(1395,'Shahjahanpur','Uttar Pradesh',NULL,NULL),(1396,'Shamli','Uttar Pradesh',NULL,NULL),(1397,'\"Shamsabad',' Agra\"',NULL,NULL),(1398,'\"Shamsabad',' Farrukhabad\"',NULL,NULL),(1399,'Sherkot','Uttar Pradesh',NULL,NULL),(1400,'\"Shikarpur',' Bulandshahr\"',NULL,NULL),(1401,'Shikohabad','Uttar Pradesh',NULL,NULL),(1402,'Shishgarh','Uttar Pradesh',NULL,NULL),(1403,'Siana','Uttar Pradesh',NULL,NULL),(1404,'Sikanderpur','Uttar Pradesh',NULL,NULL),(1405,'Sikandra Rao','Uttar Pradesh',NULL,NULL),(1406,'Sikandrabad','Uttar Pradesh',NULL,NULL),(1407,'Sirsaganj','Uttar Pradesh',NULL,NULL),(1408,'Sirsi','Uttar Pradesh',NULL,NULL),(1409,'Sitapur','Uttar Pradesh',NULL,NULL),(1410,'Soron','Uttar Pradesh',NULL,NULL),(1411,'Suar','Uttar Pradesh',NULL,NULL),(1412,'Sultanpur','Uttar Pradesh',NULL,NULL),(1413,'Sumerpur','Uttar Pradesh',NULL,NULL),(1414,'Tanda','Uttar Pradesh',NULL,NULL),(1415,'Tanda','Uttar Pradesh',NULL,NULL),(1416,'Tetri Bazar','Uttar Pradesh',NULL,NULL),(1417,'Thakurdwara','Uttar Pradesh',NULL,NULL),(1418,'Thana Bhawan','Uttar Pradesh',NULL,NULL),(1419,'Tilhar','Uttar Pradesh',NULL,NULL),(1420,'Tirwaganj','Uttar Pradesh',NULL,NULL),(1421,'Tulsipur','Uttar Pradesh',NULL,NULL),(1422,'Tundla','Uttar Pradesh',NULL,NULL),(1423,'Unnao','Uttar Pradesh',NULL,NULL),(1424,'Utraula','Uttar Pradesh',NULL,NULL),(1425,'Varanasi','Uttar Pradesh',NULL,NULL),(1426,'Vrindavan','Uttar Pradesh',NULL,NULL),(1427,'Warhapur','Uttar Pradesh',NULL,NULL),(1428,'Zaidpur','Uttar Pradesh',NULL,NULL),(1429,'Zamania','Uttar Pradesh',NULL,NULL),(1430,'Almora','Uttarakhand',NULL,NULL),(1431,'Bazpur','Uttarakhand',NULL,NULL),(1432,'Chamba','Uttarakhand',NULL,NULL),(1433,'Dehradun','Uttarakhand',NULL,NULL),(1434,'Haldwani','Uttarakhand',NULL,NULL),(1435,'Haridwar','Uttarakhand',NULL,NULL),(1436,'Jaspur','Uttarakhand',NULL,NULL),(1437,'Kashipur','Uttarakhand',NULL,NULL),(1438,'kichha','Uttarakhand',NULL,NULL),(1439,'Kotdwara','Uttarakhand',NULL,NULL),(1440,'Manglaur','Uttarakhand',NULL,NULL),(1441,'Mussoorie','Uttarakhand',NULL,NULL),(1442,'Nagla','Uttarakhand',NULL,NULL),(1443,'Nainital','Uttarakhand',NULL,NULL),(1444,'Pauri','Uttarakhand',NULL,NULL),(1445,'Pithoragarh','Uttarakhand',NULL,NULL),(1446,'Ramnagar','Uttarakhand',NULL,NULL),(1447,'Rishikesh','Uttarakhand',NULL,NULL),(1448,'Roorkee','Uttarakhand',NULL,NULL),(1449,'Rudrapur','Uttarakhand',NULL,NULL),(1450,'Sitarganj','Uttarakhand',NULL,NULL),(1451,'Tehri','Uttarakhand',NULL,NULL),(1452,'Muzaffarnagar','Uttarpradesh',NULL,NULL),(1453,'\"Adra',' Purulia\"',NULL,NULL),(1454,'Alipurduar','West Bengal',NULL,NULL),(1455,'Arambagh','West Bengal',NULL,NULL),(1456,'Asansol','West Bengal',NULL,NULL),(1457,'Baharampur','West Bengal',NULL,NULL),(1458,'Bally','West Bengal',NULL,NULL),(1459,'Balurghat','West Bengal',NULL,NULL),(1460,'Bankura','West Bengal',NULL,NULL),(1461,'Barakar','West Bengal',NULL,NULL),(1462,'Barasat','West Bengal',NULL,NULL),(1463,'Bardhaman','West Bengal',NULL,NULL),(1464,'Bidhan Nagar','West Bengal',NULL,NULL),(1465,'Chinsura','West Bengal',NULL,NULL),(1466,'Contai','West Bengal',NULL,NULL),(1467,'Cooch Behar','West Bengal',NULL,NULL),(1468,'Darjeeling','West Bengal',NULL,NULL),(1469,'Durgapur','West Bengal',NULL,NULL),(1470,'Haldia','West Bengal',NULL,NULL),(1471,'Howrah','West Bengal',NULL,NULL),(1472,'Islampur','West Bengal',NULL,NULL),(1473,'Jhargram','West Bengal',NULL,NULL),(1474,'Kharagpur','West Bengal',NULL,NULL),(1475,'Kolkata','West Bengal',NULL,NULL),(1476,'Mainaguri','West Bengal',NULL,NULL),(1477,'Mal','West Bengal',NULL,NULL),(1478,'Mathabhanga','West Bengal',NULL,NULL),(1479,'Medinipur','West Bengal',NULL,NULL),(1480,'Memari','West Bengal',NULL,NULL),(1481,'Monoharpur','West Bengal',NULL,NULL),(1482,'Murshidabad','West Bengal',NULL,NULL),(1483,'Nabadwip','West Bengal',NULL,NULL),(1484,'Naihati','West Bengal',NULL,NULL),(1485,'Panchla','West Bengal',NULL,NULL),(1486,'Pandua','West Bengal',NULL,NULL),(1487,'Paschim Punropara','West Bengal',NULL,NULL),(1488,'Purulia','West Bengal',NULL,NULL),(1489,'Raghunathpur','West Bengal',NULL,NULL),(1490,'Raiganj','West Bengal',NULL,NULL),(1491,'Rampurhat','West Bengal',NULL,NULL),(1492,'Ranaghat','West Bengal',NULL,NULL),(1493,'Sainthia','West Bengal',NULL,NULL),(1494,'Santipur','West Bengal',NULL,NULL),(1495,'Siliguri','West Bengal',NULL,NULL),(1496,'Sonamukhi','West Bengal',NULL,NULL),(1497,'Srirampore','West Bengal',NULL,NULL),(1498,'Suri','West Bengal',NULL,NULL),(1499,'Taki','West Bengal',NULL,NULL),(1500,'Tamluk','West Bengal',NULL,NULL),(1501,'Tarakeswar','West Bengal',NULL,NULL),(1502,'Chikmagalur','Karnataka',NULL,NULL),(1503,'Davanagere','Karnataka',NULL,NULL),(1504,'Dharwad','Karnataka',NULL,NULL),(1505,'Gadag','Karnataka',NULL,NULL),(1506,'Chennai','Tamil Nadu',NULL,NULL),(1507,'Coimbatore','Tamil Nadu',NULL,NULL),(1508,'Barrackpur','unknown',NULL,NULL),(1509,'Barwani','unknown',NULL,NULL),(1510,'Basna','unknown',NULL,NULL),(1511,'Bawal','unknown',NULL,NULL),(1512,'Beawar','unknown',NULL,NULL),(1513,'Berhampur','unknown',NULL,NULL),(1514,'Bhajanpura','unknown',NULL,NULL),(1515,'Bhandara','unknown',NULL,NULL),(1516,'Bharatpur','unknown',NULL,NULL),(1517,'Bharthana','unknown',NULL,NULL),(1518,'Bhilai','unknown',NULL,NULL),(1519,'Bhilwara','unknown',NULL,NULL),(1520,'Bhinmal','unknown',NULL,NULL),(1521,'Bhiwandi','unknown',NULL,NULL),(1522,'Bhusawal','unknown',NULL,NULL),(1523,'Bidar','unknown',NULL,NULL),(1524,'Bijnaur','unknown',NULL,NULL),(1525,'Bilara','unknown',NULL,NULL),(1527,'Budaun','unknown',NULL,NULL),(1528,'Bulandshahr','unknown',NULL,NULL),(1529,'Burla','unknown',NULL,NULL),(1532,'Chakeri','unknown',NULL,NULL),(1533,'Champawat','unknown',NULL,NULL),(1534,'Chandil','unknown',NULL,NULL),(1535,'Chandrapur','unknown',NULL,NULL),(1536,'Chapirevula','unknown',NULL,NULL),(1537,'Charkhari','unknown',NULL,NULL),(1538,'Charkhi Dadri','unknown',NULL,NULL),(1539,'Chhindwara','unknown',NULL,NULL),(1540,'Chiplun','unknown',NULL,NULL),(1541,'Chitrakoot','unknown',NULL,NULL),(1542,'Churu','unknown',NULL,NULL),(1543,'Dalkhola','unknown',NULL,NULL),(1544,'Damoh','unknown',NULL,NULL),(1545,'Daund','unknown',NULL,NULL),(1546,'Dehgam','unknown',NULL,NULL),(1547,'Devgarh','unknown',NULL,NULL),(1548,'Dhulian','unknown',NULL,NULL),(1549,'Dumdum','unknown',NULL,NULL),(1550,'Dwarka1','unknown',NULL,NULL),(1551,'Etah','unknown',NULL,NULL),(1552,'Faizabad','unknown',NULL,NULL),(1553,'Falna','unknown',NULL,NULL),(1554,'Farrukhabad','unknown',NULL,NULL),(1555,'Fatehgarh','unknown',NULL,NULL),(1556,'Fatehpur Chaurasi','unknown',NULL,NULL),(1557,'Fatehpur Sikri','unknown',NULL,NULL),(1558,'Firozabad','unknown',NULL,NULL),(1559,'Gadchiroli','unknown',NULL,NULL),(1560,'Gandhidham','unknown',NULL,NULL),(1561,'Ganjam','unknown',NULL,NULL),(1562,'Ghatampur','unknown',NULL,NULL),(1563,'Ghatanji','unknown',NULL,NULL),(1564,'Ghaziabad','unknown',NULL,NULL),(1565,'Ghazipur','unknown',NULL,NULL),(1566,'Goa Velha','unknown',NULL,NULL),(1567,'Gokak','unknown',NULL,NULL),(1568,'Gondiya','unknown',NULL,NULL),(1569,'Gorakhpur','unknown',NULL,NULL),(1571,'Guna','unknown',NULL,NULL),(1572,'Hanumangarh','unknown',NULL,NULL),(1573,'Harda','unknown',NULL,NULL),(1574,'Harsawa','unknown',NULL,NULL),(1575,'Hastinapur','unknown',NULL,NULL),(1576,'Hathras','unknown',NULL,NULL),(1579,'Jagadhri','unknown',NULL,NULL),(1580,'Jais','unknown',NULL,NULL),(1581,'Jaitaran','unknown',NULL,NULL),(1582,'Jalgaon','unknown',NULL,NULL),(1583,'Jalore','unknown',NULL,NULL),(1584,'Jhabua','unknown',NULL,NULL),(1585,'Jhalawar','unknown',NULL,NULL),(1586,'Jhunjhunu','unknown',NULL,NULL),(1588,'Junnar','unknown',NULL,NULL),(1589,'Kailaras','unknown',NULL,NULL),(1590,'Kalburgi','unknown',NULL,NULL),(1591,'Kalimpong','unknown',NULL,NULL),(1592,'Kamthi','unknown',NULL,NULL),(1593,'Kanpur','unknown',NULL,NULL),(1594,'Karad','unknown',NULL,NULL),(1595,'Keylong','unknown',NULL,NULL),(1596,'Kheri','unknown',NULL,NULL),(1598,'Khurai','unknown',NULL,NULL),(1600,'Kodad','unknown',NULL,NULL),(1601,'Konnagar','unknown',NULL,NULL),(1602,'Krishnanagar','unknown',NULL,NULL),(1603,'Kuchinda','unknown',NULL,NULL),(1605,'Madhyamgram','unknown',NULL,NULL),(1606,'Mahabaleswar','unknown',NULL,NULL),(1608,'Mahoba','unknown',NULL,NULL),(1609,'Mahwa','unknown',NULL,NULL),(1614,'Manesar','unknown',NULL,NULL),(1615,'Mangalagiri','unknown',NULL,NULL),(1616,'Mira-Bhayandar','unknown',NULL,NULL),(1617,'Mirzapur','unknown',NULL,NULL),(1618,'Mithapur','unknown',NULL,NULL),(1619,'Mohania','unknown',NULL,NULL),(1620,'Mokama','unknown',NULL,NULL),(1621,'Moradabad','unknown',NULL,NULL),(1622,'Mukatsar','unknown',NULL,NULL),(1623,'Nagalapuram','unknown',NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_college`
--

LOCK TABLES `college_event_college` WRITE;
/*!40000 ALTER TABLE `college_event_college` DISABLE KEYS */;
INSERT INTO `college_event_college` VALUES (1,1,1,'PONNAIYAH RAMAJAYAM INSTITUTE OF SCIENCE AND TECHNOLOGY (PRIST) UNIVERSITY'),(2,1,1,'SRI VENKATESHWARAA COLLEGE OF ENGINEERING & TECHNOLOGY'),(3,1,1,'RAAK COLLEGE OF ENGINEERING AND TECHNOLOGY'),(4,6,1,'INDIRA GANDHI POLYTECHNIC COLLEGE, MAHE'),(5,1,1,'KARAIKAL POLYTECHNIC COLLEGE'),(6,1,1,'CHRIST COLLEGE OF ENGINEERING AND TECHNOLOGY'),(7,1,1,'SRI MANAKULA VINAYAGAR ENGINEERING COLLEGE'),(8,1,1,'ACHARIYA COLLEGE OF ENGINEERING TECHNOLOGY'),(9,1,1,'SHRI KRISHNAA COLLEGE OF ENGINEERING AND TECHNOLOGY'),(10,1,1,'DR. S.J.S. PAUL MEMORIAL COLLEGE OF ENGINEERING AND TECHNOLOGY'),(11,6,1,'WOMEN\'S POLYTECHNIC COLLEGE'),(12,1,1,'ALPHA COLLEGE OF ENGINEERING & TECHNOLOGY'),(13,1,1,'SRI GANESH COLLEGE OF ENGINEERING AND TECHNOLOGY'),(14,1,1,'AVVAIYAR COLLEGE OF ENGINEERING AND TECHNOLOGY FOR WOMEN'),(15,6,1,'HAYAGRIVA POLYTECHNIC COLLEGE'),(16,1,1,'REGENCY INSTITUTE OF TECHNOLOGY'),(17,1,1,'BHARATHIYAR COLLEGE OF ENGINEERING AND TECHNOLOGY'),(18,1,1,'RAJIV GANDHI COLLEGE OF ENGINEERING AND TECHNOLOGY'),(19,1,1,'PERUNTHANALAIVAR KAMARAJAR INSTITUTE OF ENGINEERING AND TECHNOLOGY'),(20,6,1,'WOMEN\'S POLYTECHNIC COLLEGE (GOVT. OF PUDUCHERRY)'),(21,1,1,'PONDICHERRY ENGINEERING COLLEGE'),(22,1,1,'MANAKULA VINAYAGAR INSTITUTE OF TECHNOLOGY'),(23,6,1,'SRI MANAKULA VINAYAGAR POLYTECHNIC COLLEGE'),(24,1,1,'RVS COLLEGE OF ENGINEERING &TECHNOLOGY'),(25,1,1,'DR.B.R.AMBEDKAR POLYTECHNIC COLLEGE'),(26,1,1,'MOTILAL NEHRU GOVERNMENT POLYTECHNIC COLLEGE'),(27,1,325,'MAHARAJA AGRASEN INSTITUTE OF TECHNOLOGY'),(28,1,325,'CHHOTU RAM RURAL INSTITUTE OF TECHNOLOGY'),(29,1,325,'INTEGRATED INSTITUTE OF TECHNOLOGY'),(30,1,325,'TERI UNIVERSITY'),(31,1,325,'AMITY SCHOOL OF ENGINEERING & TECHNOLOGY'),(32,1,325,'MAHARAJA SURAJMAL INSTITUTE OF TECHNOLOGY'),(33,1,325,'G. B. PANT POLYTECHNIC'),(34,1,325,'DELHI INSTITUTE OF TOOL ENGINEERING'),(35,1,325,'AMBEDKAR INSTITUTE OF ADVANCED COMMUNICATION TECHNOLOGIES AND RESEARCH'),(36,6,325,'GURU NANAK DEV POLYTECHNIC'),(37,1,325,'CH. BRAHM PRAKASH GOVERNMENT ENGINEERING COLLEGE'),(38,1,325,'ADITYA INSTITUTE OF TECHNOLOGY'),(39,1,325,'HMR INSTITUTE OF TECHNOLOGY AND MANAGEMENT'),(40,6,325,'INTERNATIONAL POLYTECHNIC FOR WOMEN'),(41,6,325,'BSF POLYTECHNIC'),(42,1,325,'MARATHWADA INSTITUTE OF TECHNOLOGY'),(43,1,325,'MEERABAI INSTITUTE OF TECHNOLOGY'),(44,1,325,'DELHI COLLEGE OF ENGINEERING'),(45,1,325,'BHARATI VIDYAPEETH\'S COLLEGE OF ENGINEERING'),(46,6,325,'ARYABHAT POLYTECHNIC'),(47,6,325,'GURU TEGH BAHADUR POLYTECHNIC INSTITUTE'),(48,4,325,'SAFDARJUNG HOSPITAL AND VMMC'),(49,1,325,'GURU GOBIND SINGH INDRAPRASTHA UNIVERSITY'),(50,4,325,'BABA HARIDASS COLLEGE OF PHARMACY & TECHNOLOGY'),(51,1,325,'NETAJI SUBHAS INSTITUTE OF TECHNOLOGY'),(52,1,325,'NATIONAL POWER TRAINING INSTITUTE (NORTHERN REGION)'),(53,1,325,'NORTHERN INDIA ENGINEERING COLLEGE'),(54,6,325,'PUSA POLYTECHNIC'),(55,1,325,'JAMIA MILLIA ISLAMIA (A CENTRAL UNIVERSITY)'),(56,6,325,'KASTURBA POLYTECHNIC FOR WOMEN'),(57,1,325,'GURU TEGH BAHADUR INSTITUTE OF TECHNOLOGY'),(58,1,325,'G.B. PANT GOVT. ENGINEERING COLLEGE'),(59,1,325,'MIRAMBIKA RESEARCH CENTRE OF INTEGRAL EDUCATION AND HUMAN VALUES');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_collegedepartment`
--

LOCK TABLES `college_event_collegedepartment` WRITE;
/*!40000 ALTER TABLE `college_event_collegedepartment` DISABLE KEYS */;
INSERT INTO `college_event_collegedepartment` VALUES (1,3),(6,6),(7,7),(8,9),(5,31),(2,67),(3,75),(4,98);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_collegedepartment_college`
--

LOCK TABLES `college_event_collegedepartment_college` WRITE;
/*!40000 ALTER TABLE `college_event_collegedepartment_college` DISABLE KEYS */;
INSERT INTO `college_event_collegedepartment_college` VALUES (1,1,27),(2,2,27),(3,3,27),(4,4,27),(5,5,27),(6,6,27),(7,7,27),(9,8,27);
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
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_department`
--

LOCK TABLES `college_event_department` WRITE;
/*!40000 ALTER TABLE `college_event_department` DISABLE KEYS */;
INSERT INTO `college_event_department` VALUES (1,'MCA'),(3,'COMMUNICATION ENGINEERING AND SIGNAL PROCESSING'),(4,'COMPUTER SCIENCE & ENGINEERING'),(5,'COMPUTER SCIENCE AND ENGINEERING'),(6,'ELECTRICAL AND COMPUTER ENGINEERING'),(7,'ELECTRICAL AND ELECTRONICS ENGINEERING'),(8,'ELECTRONICS & COMMUNICATION ENGG'),(9,'ELECTRONICS AND COMMUNICATIONS ENGINEERING'),(10,'INFORMATION TECHNOLOGY'),(11,'MECHANICAL AND AUTOMATION ENGINEERING'),(12,'MECHANICAL ENGINEERING'),(13,'SOFTWARE ENGINEERING'),(18,''),(19,'ADVANCED MATERIALS TECHNOLOGY'),(20,'ARCHITECTURAL ASSISTANTSHIP'),(21,'AUTOMOBILE ENGINEERING'),(22,'BIOCHEMICAL ENGINEERING'),(23,'BIOINFORMATICS'),(24,'BIOTECHNOLOGY'),(25,'CAD CAM'),(26,'CHEMICAL ENGINEERING'),(27,'CIVIL (PUBLIC HEALTH & ENVIRONMENT) ENGINEERING'),(28,'CIVIL ENGINEERING'),(29,'COMMUNICATION ENGINEERING AND SIGNAL PROCESSING'),(30,'COMPUTER ENGINEERING'),(31,'COMPUTER SCEINCE & ENGINEERING'),(32,'COMPUTER SCIENCE & ENGINEERING'),(33,'COMPUTER SCIENCE AND ENGINEERING'),(34,'COMPUTER TECHNOLOGY AND APPLICATIONS'),(35,'CONSTRUCTION ENGINEERING'),(36,'CONTROL AND INSTRUMENTATION'),(37,'COSMETOLOGY AND HEALTH'),(38,'DIGITAL COMMUNICATION'),(39,'DIGITAL COMMUNICATIONS'),(40,'DIGITAL ELECTRONICS'),(41,'DIGITAL ELECTRONICS & MICROPROCESSOR'),(42,'DIPLOMA MEDICAL LAB TECHNOLOGY'),(43,'EARTHQUAKE ENGINEERING'),(44,'ELECTRICAL AND COMPUTER ENGINEERING'),(45,'ELECTRICAL AND ELECTRONICS ENGINEERING'),(46,'ELECTRICAL ENGINEERING'),(47,'ELECTRICAL POWER SYSTEMS'),(48,'ELECTRONICS & COMMUNICATION ENGG'),(49,'ELECTRONICS & COMMUNICATION ENGG(INDUSTRY INTEGRATED)'),(50,'ELECTRONICS AND COMMUNICATION ENGINEERING (SANDWICH)'),(51,'ELECTRONICS AND COMMUNICATIONS ENGINEERING'),(52,'ELECTRONICS ENGINEERING (DIGITAL ELECTRONICS)'),(53,'EMBEDDED SYSTEM AND VLSI'),(54,'ENGINEERING EDUCATION'),(55,'ENVIRONMENT ENGINEERING'),(56,'ENVIRONMENTAL ENGINEERING'),(57,'ENVIRONMENTAL ENGINEERING AND MANAGEMENT'),(58,'ENVIRONMENTAL SCIENCE AND ENGINEERING'),(59,'FASHION DESIGNING'),(60,'FOOD PROCESSING TECHNOLOGY'),(61,'GARMENT FABRICATION'),(62,'GEOTECHNICAL ENGINEERING'),(63,'HYDRAULICS & FLOOD CONTROL'),(64,'INDUSTRIAL ELECTRONICS'),(65,'INFORMATION SECURITY'),(66,'INFORMATION SYSTEMS'),(67,'INFORMATION TECHNOLOGY'),(68,'INFORMATION TECHNOLOGY ENABLED SERVICES AND MANAGEMENT'),(69,'INSTRUMENTATION & CONTROL ENGINEERING'),(70,'INSTRUMENTATION AND CONTROL ENGINEERING'),(71,'LIBRARY AND INFORMATION SCIENCE'),(72,'MANUFACTURING PROCESS & AUTOMATION ENGINEERING'),(73,'MASTER OF SCIENCE IN SOFTWARE ENGINEERING'),(74,'MASTERS IN ENGINEERING AND MANAGEMENT'),(75,'MECHANICAL AND AUTOMATION ENGINEERING'),(76,'MECHANICAL ENGINEERING'),(77,'MECHANICAL ENGINEERING (MAINTENANCE)'),(78,'MECHATRONICS'),(79,'MEDICAL ELECTRONICS'),(80,'MEDICAL LAB TECHNOLOGY'),(81,'MEDICAL LABORATORY TECHNOLOGY'),(82,'MICROWAVE & OPTICAL COMMUNICATION'),(83,'NANO SCIENCE & TECHNOLOGY'),(84,'NANO TECHNOLOGY'),(85,'PLASTIC ENGINEERING'),(86,'PLASTICS ENGINEERING'),(87,'POLYMER SCIENCE & CHEMICAL TECHNOLOGY'),(88,'POLYMER TECHNOLOGY'),(89,'POWER ENGINEERING'),(90,'POWER SYSTEMS'),(91,'PRINTING TECHNOLOGY'),(92,'PROCESS CONTROL'),(93,'PRODUCTION AND INDUSTRIAL ENGINEERING'),(94,'PRODUCTION ENGINEERING'),(95,'RADIO FREQUENCY AND MICROWAVE ENGINEERING'),(96,'REFRIGERATION AND AIR CONDITIONING'),(97,'SIGNAL PROCESSING'),(98,'SOFTWARE ENGINEERING'),(99,'STRUCTURAL ENGINEERING'),(100,'TEXTILE DESIGNING'),(101,'THERMAL ENGINEERING'),(102,'TOOL & DIE MAKING'),(103,'TOOL ENGINEERING'),(104,'VLSI DESIGN AND EMBEDDED SYSTEMS'),(105,'WATER RESOURCE ENGINEERING');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_feedback`
--

LOCK TABLES `college_event_feedback` WRITE;
/*!40000 ALTER TABLE `college_event_feedback` DISABLE KEYS */;
INSERT INTO `college_event_feedback` VALUES (1,'sastha','sastha@globalensolutions.com','sample content test',0);
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
  `organizer_name` varchar(50) NOT NULL,
  `organizer_mobile` bigint(20) NOT NULL,
  `organizer_email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_organizer`
--

LOCK TABLES `college_event_organizer` WRITE;
/*!40000 ALTER TABLE `college_event_organizer` DISABLE KEYS */;
INSERT INTO `college_event_organizer` VALUES (1,'Jeevan Mammen Stephen:',9895714082,'sdgsdggs@gmail.com'),(2,' Balavishnu V J',9171635252,'balavishnu06@gmail.com'),(3,'Pratiksha Mohanty',9632696203,'carnival@alliance.edu.in'),(4,'sdfsdf',2342342341,'sdfgsd@aas.com'),(5,'Deepanwita Tripathy',9853702299,'www.sldcnitr.in'),(6,'CSE',9852013647,'CSE@gmail.com'),(7,'sdafsad',4874578451,'sadfsadf@gmail.com');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_postevent`
--

LOCK TABLES `college_event_postevent` WRITE;
/*!40000 ALTER TABLE `college_event_postevent` DISABLE KEYS */;
INSERT INTO `college_event_postevent` VALUES (1,'dhanak2015','saisasthaa@gmail.com',1234567890,'Regular Capoeira classes','2015-10-24','2015-10-31',1,1,'Dhanak is the annual cultural fest of the Indian Institute of Space Science & Technology, Trivandrum. It is a four-day long event held in the odd semester  each year and is attended by students from across South India and some parts of North India. With events ranging from literary & music-art-dance to visual arts & film-making, it presents the perfect platform to expose the participants to healthy competition and also bag prizes while they are at it.','\r\nClosest Airport - Trivandrum Internation Airport ','Tamilnadu','pondicherry','manakula','Computer science','static/img/party-music-hd-wallpaper-1920x1200-3850.jpg',1,0),(2,'Pretheev','pretheevraj@gmail.com',8754405589,'Qubit\'15 (technoVIT\'15)','2015-10-14','2015-10-16',1,6,'Qubit\'15 is an event presented by Computing Science and Engineering . And technoVIT\'15 is the overall fest conducted by VIT Chennai.','Vandalur, Kelambakkam Road, Chennai, Tamil Nadu 600127','Tamilnadu','Chennai','VIT University Chennai Campus','cse','static/img/11953199_1640028686253445_335380266701552541_n.jpg',1,0),(3,'Pretheev','pretheevraj@gmail.com',8754405589,'Fiesta de Mercadeo 15','2015-10-14','2015-10-15',5,7,'A national level techno-management-Law & cultural Fest events to be held on 14th and 15th of OCTOBER at Alliance University.','Chikkahagade Cross, Chandapura - Anekal Main Road, Anekal\r\nBengaluru – 562 106, Karnataka, India.',' Karnataka','Bengaluru','Fiesta de Mercadeo 15','MBA, Commerce, Law, BBA','static/img/galeria_flyer_1_r7_c1.jpg',1,0),(6,'Pradeepa','rpradeepa812@gmail.com',9789761928,'Student Led Design Conference','2015-10-30','2015-11-01',1,4,'AMERICAN SOCIETY OF MECHANICAL ENGINEERS INDIA’S STUDENT LED DESIGN CONFERENCE (SLDC 2015)\r\n\r\nIS A ZONAL LEVEL CONFERENCE TO BE HELD FOR THE FIRST TIME IN NIT, ROURKELA.\r\n\r\nSLDC BRINGS THIS INNOVISION (30TH OCT-1ST NOV, 2015), A SYMPOSIUM ALONG WITH A PLATFORM TO\r\n\r\nSHOWCASE ONE\'S ABILITIES AND A CHANCE TO BRING INTO ACTION ALL THE IDEAS.','Rourkela ','Bangalore','Rourkela ','ASME NIT','MECHANICAL ENGINEERING','/events/static/img/logo.png',0,0),(7,'priya','avbmail93@gmail.com',8148456121,'technical event','2015-10-13','2015-10-14',1,1,'workshop on NS2 ','Sree sowdambika college of engineering ,\r\nMadurai','Tamil Nadu','Madurai','SSCE','CSE','/events/gallery7-2.jpg',1,0),(8,'AnonymousUser','asdff@dsadf.com',7845784578,'asdfsadf','2015-10-16','2015-10-22',1,2,'asdfsadf','sadfsda','asdfsadf','sadfsadf','sdafasd','asdfasdf','/events/2015-Historic-Dodgertown-College-and-High-School-Spring-Training2.jpg',0,0);
/*!40000 ALTER TABLE `college_event_postevent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_event_postevent_organizer`
--

DROP TABLE IF EXISTS `college_event_postevent_organizer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college_event_postevent_organizer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `postevent_id` int(11) NOT NULL,
  `organizer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `postevent_id` (`postevent_id`,`organizer_id`),
  KEY `college_event_postevent_organizer_c5c7cdeb` (`postevent_id`),
  KEY `college_event_postevent_organizer_8b4cd99f` (`organizer_id`),
  CONSTRAINT `organizer_id_refs_id_84b7e48f` FOREIGN KEY (`organizer_id`) REFERENCES `college_event_organizer` (`id`),
  CONSTRAINT `postevent_id_refs_id_9a3b7958` FOREIGN KEY (`postevent_id`) REFERENCES `college_event_postevent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_postevent_organizer`
--

LOCK TABLES `college_event_postevent_organizer` WRITE;
/*!40000 ALTER TABLE `college_event_postevent_organizer` DISABLE KEYS */;
INSERT INTO `college_event_postevent_organizer` VALUES (1,1,1),(4,2,2),(5,3,3),(7,7,2);
/*!40000 ALTER TABLE `college_event_postevent_organizer` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_premiumpriceinfo`
--

LOCK TABLES `college_event_premiumpriceinfo` WRITE;
/*!40000 ALTER TABLE `college_event_premiumpriceinfo` DISABLE KEYS */;
INSERT INTO `college_event_premiumpriceinfo` VALUES (1,0,'INR','free',30),(2,1000,'INR','paid',30);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_subcategory`
--

LOCK TABLES `college_event_subcategory` WRITE;
/*!40000 ALTER TABLE `college_event_subcategory` DISABLE KEYS */;
INSERT INTO `college_event_subcategory` VALUES (1,'subcategory/icon/workshop_2.png','subcategory/icon/workshop_hover_2.png','Workshop'),(2,'subcategory/icon/seminar_1.png','subcategory/icon/seminar_hover_1.png','Seminar'),(3,'subcategory/icon/online_events_1.png','subcategory/icon/online_events_hover_1.png','onlineevents'),(4,'subcategory/icon/conference_1.png','subcategory/icon/conference_hover_1.png','Conferences'),(5,'subcategory/icon/youth_submit_1.png','subcategory/icon/youth_submit_hover_1.png','Youthsubmit'),(6,'subcategory/icon/technical_1.png','subcategory/icon/technical_hover_1.png','Technical'),(7,'subcategory/icon/culturals_1.png','subcategory/icon/culturals_hover_1.png','Culturals'),(8,'subcategory/icon/literary_1.png','subcategory/icon/literary_hover_1.png','Literary'),(9,'subcategory/icon/symposium_1.png','subcategory/icon/symposium_hover_1.png','Symposium');
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_event_subcategory_category`
--

LOCK TABLES `college_event_subcategory_category` WRITE;
/*!40000 ALTER TABLE `college_event_subcategory_category` DISABLE KEYS */;
INSERT INTO `college_event_subcategory_category` VALUES (1,1,1),(2,1,2),(3,1,4),(4,2,1),(5,2,2),(6,2,4),(7,3,1),(8,3,2),(9,3,3),(10,3,4),(11,3,5),(12,4,1),(13,4,2),(14,4,4),(15,5,3),(16,6,1),(17,6,2),(22,7,1),(23,7,2),(24,7,3),(25,7,5),(26,8,3),(27,9,1),(28,9,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=132 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-10-10 20:05:51',1,21,'1','Mainbanner object',1,''),(2,'2015-10-10 20:06:35',1,21,'2','Mainbanner object',1,''),(3,'2015-10-10 20:07:41',1,21,'3','Mainbanner object',1,''),(4,'2015-10-10 20:09:32',1,21,'4','Mainbanner object',1,''),(5,'2015-10-10 20:13:35',1,20,'1','bottom',1,''),(6,'2015-10-10 20:14:06',1,20,'2','left',1,''),(7,'2015-10-10 20:14:20',1,20,'3','right',1,''),(8,'2015-10-10 20:15:07',1,19,'1','',1,''),(9,'2015-10-10 20:20:43',1,7,'1','Engineering',1,''),(10,'2015-10-10 20:21:05',1,7,'2','Arts & Science',1,''),(11,'2015-10-10 20:21:44',1,7,'3','Management',1,''),(12,'2015-10-10 20:22:05',1,7,'4','Medical',1,''),(13,'2015-10-10 20:22:19',1,7,'5','Others',1,''),(14,'2015-10-10 20:24:28',1,8,'1','Workshop',1,''),(15,'2015-10-10 20:25:03',1,8,'2','Seminar',1,''),(16,'2015-10-10 20:25:54',1,8,'3','onlineevents',1,''),(17,'2015-10-10 20:26:50',1,8,'4','Conferences',1,''),(18,'2015-10-10 20:27:55',1,8,'5','Youthsubmit',1,''),(19,'2015-10-10 20:28:49',1,8,'6','Technical',1,''),(20,'2015-10-10 20:29:20',1,8,'7','Cultural',1,''),(21,'2015-10-10 20:29:37',1,8,'7','Culturals',2,'Changed name.'),(22,'2015-10-10 20:30:35',1,8,'8','Literary',1,''),(23,'2015-10-10 20:31:11',1,8,'9','Symposium',1,''),(24,'2015-10-10 20:32:33',1,13,'1','free',1,''),(25,'2015-10-10 20:33:16',1,13,'2','paid',1,''),(26,'2015-10-10 20:48:34',1,10,'1','PONNAIYAH RAMAJAYAM INSTITUTE OF SCIENCE AND TECHNOLOGY (PRIST) UNIVERSITY',1,''),(27,'2015-10-10 20:48:53',1,10,'2','SRI VENKATESHWARAA COLLEGE OF ENGINEERING & TECHNOLOGY',1,''),(28,'2015-10-10 20:49:19',1,10,'3','RAAK COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(29,'2015-10-10 20:49:48',1,7,'6','POLYTECHNIC',1,''),(30,'2015-10-10 20:50:16',1,10,'4','INDIRA GANDHI POLYTECHNIC COLLEGE, MAHE',1,''),(31,'2015-10-10 20:50:36',1,10,'5','KARAIKAL POLYTECHNIC COLLEGE',1,''),(32,'2015-10-10 20:51:11',1,10,'6','CHRIST COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(33,'2015-10-10 20:52:20',1,10,'7','SRI MANAKULA VINAYAGAR ENGINEERING COLLEGE',1,''),(34,'2015-10-10 20:52:41',1,10,'8','ACHARIYA COLLEGE OF ENGINEERING TECHNOLOGY',1,''),(35,'2015-10-10 20:53:13',1,10,'9','SHRI KRISHNAA COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(36,'2015-10-10 20:53:39',1,10,'10','DR. S.J.S. PAUL MEMORIAL COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(37,'2015-10-10 20:57:11',1,10,'11','WOMEN\'S POLYTECHNIC COLLEGE',1,''),(38,'2015-10-10 20:57:39',1,10,'12','ALPHA COLLEGE OF ENGINEERING & TECHNOLOGY',1,''),(39,'2015-10-10 20:58:04',1,10,'13','SRI GANESH COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(40,'2015-10-10 20:58:27',1,10,'14','AVVAIYAR COLLEGE OF ENGINEERING AND TECHNOLOGY FOR WOMEN',1,''),(41,'2015-10-10 21:05:19',1,10,'15','HAYAGRIVA POLYTECHNIC COLLEGE',1,''),(42,'2015-10-10 21:05:45',1,10,'16','REGENCY INSTITUTE OF TECHNOLOGY',1,''),(43,'2015-10-10 21:06:07',1,10,'17','BHARATHIYAR COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(44,'2015-10-10 21:06:23',1,10,'18','RAJIV GANDHI COLLEGE OF ENGINEERING AND TECHNOLOGY',1,''),(45,'2015-10-10 21:06:43',1,10,'19','PERUNTHANALAIVAR KAMARAJAR INSTITUTE OF ENGINEERING AND TECHNOLOGY',1,''),(46,'2015-10-10 21:07:52',1,10,'20','WOMEN\'S POLYTECHNIC COLLEGE (GOVT. OF PUDUCHERRY)',1,''),(47,'2015-10-10 21:08:10',1,10,'21','PONDICHERRY ENGINEERING COLLEGE',1,''),(48,'2015-10-10 21:15:08',1,14,'2','International Winter Internship and Training',1,''),(49,'2015-10-10 21:21:29',1,19,'1','',3,''),(50,'2015-10-10 21:22:38',1,19,'2','',1,''),(51,'2015-10-10 21:25:27',1,19,'3','',1,''),(52,'2015-10-10 21:26:12',1,19,'4','',1,''),(53,'2015-10-10 21:28:31',1,19,'5','',1,''),(54,'2015-10-10 21:33:51',1,19,'6','',1,''),(55,'2015-10-10 21:34:30',1,19,'7','',1,''),(56,'2015-10-10 21:58:03',1,10,'22','MANAKULA VINAYAGAR INSTITUTE OF TECHNOLOGY',1,''),(57,'2015-10-10 21:58:29',1,10,'23','SRI MANAKULA VINAYAGAR POLYTECHNIC COLLEGE',1,''),(58,'2015-10-10 21:58:49',1,10,'24','RVS COLLEGE OF ENGINEERING &TECHNOLOGY',1,''),(59,'2015-10-10 21:59:15',1,10,'25','DR.B.R.AMBEDKAR POLYTECHNIC COLLEGE',1,''),(60,'2015-10-10 21:59:40',1,10,'26','MOTILAL NEHRU GOVERNMENT POLYTECHNIC COLLEGE',1,''),(61,'2015-10-10 23:36:48',1,15,'1','Jeevan Mammen Stephen:',1,''),(62,'2015-10-10 23:37:35',1,14,'1','Regular Capoeira classes',1,''),(63,'2015-10-10 23:48:28',1,17,'1','sastha',2,'Changed city and confirmation_code.'),(64,'2015-10-10 23:48:53',1,4,'2','sastha',2,'Changed is_staff.'),(65,'2015-10-11 07:01:21',1,15,'2',' Balavishnu V J',1,''),(66,'2015-10-11 07:05:06',1,14,'2','Qubit\'15 (technoVIT\'15)',1,''),(67,'2015-10-11 07:05:18',1,14,'2','Qubit\'15 (technoVIT\'15)',2,'No fields changed.'),(68,'2015-10-11 07:15:58',1,14,'2','Qubit\'15 (technoVIT\'15)',2,'Changed poster.'),(69,'2015-10-11 11:33:55',1,15,'3','Pratiksha Mohanty',1,''),(70,'2015-10-11 11:34:57',1,14,'3','Fiesta de Mercadeo 15',1,''),(71,'2015-10-11 12:48:08',1,4,'9','deepak',3,''),(72,'2015-10-11 12:59:21',1,4,'10','wasdfa',3,''),(73,'2015-10-11 19:20:37',1,14,'5','test',2,'Changed organizer and admin_status.'),(74,'2015-10-11 19:25:24',1,14,'5','test',3,''),(75,'2015-10-11 19:25:24',1,14,'4','test',3,''),(76,'2015-10-11 19:26:21',1,4,'12','asdfsadf',3,''),(77,'2015-10-11 19:26:21',1,4,'13','asdfsd',3,''),(78,'2015-10-11 19:26:21',1,4,'15','ewtrrwe',3,''),(79,'2015-10-11 19:26:21',1,4,'11','fdsfgdsf',3,''),(80,'2015-10-11 19:26:21',1,4,'14','fsdfsdfg',3,''),(81,'2015-10-11 19:26:21',1,4,'6','jsjjsjs',3,''),(82,'2015-10-11 19:26:21',1,4,'18','kalai',3,''),(83,'2015-10-11 19:26:21',1,4,'19','qwert',3,''),(84,'2015-10-11 19:26:21',1,4,'16','sdfsadfsd',3,''),(85,'2015-10-11 19:34:23',1,4,'22','eventswat',3,''),(86,'2015-10-12 07:22:06',1,14,'7','technical event',2,'Changed organizer and admin_status.'),(87,'2015-10-12 07:48:19',1,9,'1624','Delhi',1,''),(88,'2015-10-12 07:52:02',1,9,'1624','Delhi',3,''),(89,'2015-10-12 07:55:18',1,10,'27','MAHARAJA AGRASEN INSTITUTE OF TECHNOLOGY',1,''),(90,'2015-10-12 07:59:08',1,12,'1','COMMUNICATION ENGINEERING AND SIGNAL PROCESSING',1,''),(91,'2015-10-12 07:59:44',1,12,'2','INFORMATION TECHNOLOGY',1,''),(92,'2015-10-12 08:01:22',1,12,'3','MECHANICAL AND AUTOMATION ENGINEERING',1,''),(93,'2015-10-12 08:02:22',1,12,'4','SOFTWARE ENGINEERING',1,''),(94,'2015-10-12 08:05:18',1,12,'5','COMPUTER SCEINCE & ENGINEERING',1,''),(95,'2015-10-12 08:07:00',1,12,'6','ELECTRICAL AND COMPUTER ENGINEERING',1,''),(96,'2015-10-12 08:07:57',1,12,'7','ELECTRICAL AND ELECTRONICS ENGINEERING',1,''),(97,'2015-10-12 08:08:34',1,12,'8','ELECTRONICS AND COMMUNICATIONS ENGINEERING',1,''),(98,'2015-10-12 08:09:24',1,12,'8','ELECTRONICS AND COMMUNICATIONS ENGINEERING',2,'No fields changed.'),(99,'2015-10-12 08:10:45',1,10,'28','CHHOTU RAM RURAL INSTITUTE OF TECHNOLOGY',1,''),(100,'2015-10-12 08:12:22',1,10,'29','TERI UNIVERSITY',1,''),(101,'2015-10-12 08:12:44',1,10,'29','INTEGRATED INSTITUTE OF TECHNOLOGY',2,'Changed college_name.'),(102,'2015-10-12 08:13:58',1,10,'30','TERI UNIVERSITY',1,''),(103,'2015-10-12 08:15:24',1,10,'31','AMITY SCHOOL OF ENGINEERING & TECHNOLOGY',1,''),(104,'2015-10-12 08:16:28',1,10,'32','MAHARAJA SURAJMAL INSTITUTE OF TECHNOLOGY',1,''),(105,'2015-10-12 08:19:07',1,10,'33','G. B. PANT POLYTECHNIC',1,''),(106,'2015-10-12 08:19:58',1,10,'34','DELHI INSTITUTE OF TOOL ENGINEERING',1,''),(107,'2015-10-12 08:20:58',1,10,'35','AMBEDKAR INSTITUTE OF ADVANCED COMMUNICATION TECHNOLOGIES AND RESEARCH',1,''),(108,'2015-10-12 08:22:34',1,10,'36','GURU NANAK DEV POLYTECHNIC',1,''),(109,'2015-10-12 08:23:58',1,10,'37','CH. BRAHM PRAKASH GOVERNMENT ENGINEERING COLLEGE',1,''),(110,'2015-10-12 08:25:21',1,10,'38','ADITYA INSTITUTE OF TECHNOLOGY',1,''),(111,'2015-10-12 08:26:18',1,10,'39','HMR INSTITUTE OF TECHNOLOGY AND MANAGEMENT',1,''),(112,'2015-10-12 08:26:51',1,10,'40','INTERNATIONAL POLYTECHNIC FOR WOMEN',1,''),(113,'2015-10-12 08:27:29',1,10,'41','BSF POLYTECHNIC',1,''),(114,'2015-10-12 08:28:17',1,10,'42','MARATHWADA INSTITUTE OF TECHNOLOGY',1,''),(115,'2015-10-12 08:29:25',1,10,'43','MEERABAI INSTITUTE OF TECHNOLOGY',1,''),(116,'2015-10-12 08:29:48',1,10,'44','DELHI COLLEGE OF ENGINEERING',1,''),(117,'2015-10-12 08:30:28',1,10,'45','BHARATI VIDYAPEETH\'S COLLEGE OF ENGINEERING',1,''),(118,'2015-10-12 08:31:16',1,10,'46','ARYABHAT POLYTECHNIC',1,''),(119,'2015-10-12 08:31:46',1,10,'47','GURU TEGH BAHADUR POLYTECHNIC INSTITUTE',1,''),(120,'2015-10-12 08:32:46',1,10,'48','SAFDARJUNG HOSPITAL AND VMMC',1,''),(121,'2015-10-12 08:33:05',1,10,'49','GURU GOBIND SINGH INDRAPRASTHA UNIVERSITY',1,''),(122,'2015-10-12 08:33:30',1,10,'50','BABA HARIDASS COLLEGE OF PHARMACY & TECHNOLOGY',1,''),(123,'2015-10-12 08:33:48',1,10,'51','NETAJI SUBHAS INSTITUTE OF TECHNOLOGY',1,''),(124,'2015-10-12 08:34:09',1,10,'52','NATIONAL POWER TRAINING INSTITUTE (NORTHERN REGION)',1,''),(125,'2015-10-12 08:34:28',1,10,'53','NORTHERN INDIA ENGINEERING COLLEGE',1,''),(126,'2015-10-12 08:34:46',1,10,'54','PUSA POLYTECHNIC',1,''),(127,'2015-10-12 08:35:45',1,10,'55','JAMIA MILLIA ISLAMIA (A CENTRAL UNIVERSITY)',1,''),(128,'2015-10-12 08:36:48',1,10,'56','KASTURBA POLYTECHNIC FOR WOMEN',1,''),(129,'2015-10-12 08:38:07',1,10,'57','GURU TEGH BAHADUR INSTITUTE OF TECHNOLOGY',1,''),(130,'2015-10-12 08:38:43',1,10,'58','G.B. PANT GOVT. ENGINEERING COLLEGE',1,''),(131,'2015-10-12 08:39:22',1,10,'59','MIRAMBIKA RESEARCH CENTRE OF INTEGRAL EDUCATION AND HUMAN VALUES',1,'');
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
INSERT INTO `django_session` VALUES ('1gugon7lf7r6x8s7q5aap3n0p92ja98y','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-26 04:59:54'),('21okufdmji9cniuuew0661c6pr7j50ns','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-10-25 09:44:08'),('3cz76tx5hawcvmk3d60ds2dofq04fxiy','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 20:04:30'),('5jtpne8w9czhmmvefcydkli6hovqp3b6','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 14:30:32'),('5rfs9uw3ncv0in6torioestp50b17ed8','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-26 03:18:07'),('a5pffvwmnrfc9ysg3i7fr4ht2cd8evwg','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 14:19:39'),('ad72cpydg3lrym3kds32gnchreo5m215','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 06:15:09'),('azmq9en6lf0ris99p3uunpisvp5v36lh','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 05:45:50'),('dlxsel5zz6d0vgxi02db397x7kl5ynhz','NmYzM2Y1MWVjOWVmNWQyNzI3ZGIzODViZWJjZTJiZGMxMzhiNmYxODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MTZ9','2015-10-25 14:30:33'),('f8qocdo3iw93sxd4imncajlfrtn9md38','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 14:30:32'),('hyoauyhqeea04g1fiy2wh43widf01go9','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 15:57:28'),('i9uk7bvnt22wo8g238wsp4673nw74k5q','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 19:28:07'),('icuj4b9coqlou109y1j6ovv8p5j0560r','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 14:30:32'),('il0eq5ry56tgla5httpy9jg50bbivfq1','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-26 09:01:44'),('jyuqsnvi3tm34jraeb97rj3kd01e8epo','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-10-26 08:15:34'),('lecisvmt9dueeh3znifeh4bhflpxvyet','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-10-26 07:40:08'),('ls1ne5n07xz2ztx5nnc025x904vpivmj','OWVjYTA0MGFlOWFhYjhjNzkyZGRmNmU4M2Q5NjY1MGZjYmY2ZWEzMjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MjF9','2015-10-25 17:02:43'),('nneqzxoewshtqy1upyt26pyes4sgswyp','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 17:54:24'),('pvou2dscopxur7d1kicot1al3yw4shsu','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-26 07:24:28'),('ryeqeu9x2pwct5cuizgjtwh0dkwqqsg9','MWM2NDY3OTI1YTFlYmE4Zjg4YzE0Y2YwODUyNTNjYTIyZjBkMDE3Yjp7fQ==','2015-10-25 16:56:18'),('xqbb3fszvc9bn7ju01jt3xf6o35u00bv','NDE3YTY5NTA5N2M0ZTYwMmUwMWIyNmYzZjFhMThiNzAwYTI4Zjc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-10-24 20:03:42');
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_userprofile`
--

LOCK TABLES `events_userprofile` WRITE;
/*!40000 ALTER TABLE `events_userprofile` DISABLE KEYS */;
INSERT INTO `events_userprofile` VALUES (1,2,'9786243201','1230',0,0,NULL,1,NULL,NULL),(2,3,'8489923344','',0,0,NULL,NULL,NULL,NULL),(3,4,'1234567890','',0,0,NULL,NULL,NULL,NULL),(4,5,'8754405589','',0,0,NULL,NULL,NULL,NULL),(6,7,'7845729671','',0,0,NULL,NULL,NULL,NULL),(7,8,'7845729671','',0,0,NULL,NULL,NULL,NULL),(16,17,'7845729671','',0,0,NULL,NULL,NULL,NULL),(19,20,'9500376377','',0,0,NULL,NULL,NULL,NULL),(20,21,'7845784512','',0,0,NULL,NULL,NULL,NULL),(22,23,'7845784578','',0,0,NULL,NULL,NULL,NULL),(23,24,'9999999999','',0,0,NULL,NULL,NULL,NULL),(24,25,'9789761928','',0,0,NULL,NULL,NULL,NULL),(25,26,'7891023654','',0,0,NULL,NULL,NULL,NULL);
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-12  2:06:06
