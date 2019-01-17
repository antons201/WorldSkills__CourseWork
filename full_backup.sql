-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.10.1

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
-- Table structure for table `Championships`
--

DROP TABLE IF EXISTS `Championships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Championships` (
  `id` int(11) NOT NULL,
  `name` text,
  `region` varchar(45) DEFAULT NULL,
  `user_amount` int(11) DEFAULT NULL,
  `time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Championships`
--

LOCK TABLES `Championships` WRITE;
/*!40000 ALTER TABLE `Championships` DISABLE KEYS */;
INSERT INTO `Championships` VALUES (1,'НазваниеЧемпионата1','Регион',3,'2019-05-05'),(2,'НазваниеЧемпионата2','Регион',0,'2020-05-05');
/*!40000 ALTER TABLE `Championships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ChampionshipsResults`
--

DROP TABLE IF EXISTS `ChampionshipsResults`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ChampionshipsResults` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_championship` int(11) DEFAULT NULL,
  `id_competence` int(11) DEFAULT NULL,
  `id_module` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `result` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ChampionshipsResults_1_idx` (`id_competence`),
  KEY `fk_ChampionshipsResults_2_idx` (`id_championship`),
  CONSTRAINT `fk_ChampionshipsResults_1` FOREIGN KEY (`id_competence`) REFERENCES `Competence` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ChampionshipsResults_2` FOREIGN KEY (`id_championship`) REFERENCES `Championships` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ChampionshipsResults`
--

LOCK TABLES `ChampionshipsResults` WRITE;
/*!40000 ALTER TABLE `ChampionshipsResults` DISABLE KEYS */;
INSERT INTO `ChampionshipsResults` VALUES (1,1,1,1,2,1),(2,1,1,2,2,10);
/*!40000 ALTER TABLE `ChampionshipsResults` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ChampionshipsUsers`
--

DROP TABLE IF EXISTS `ChampionshipsUsers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ChampionshipsUsers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_championship` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Championships_Users_1_idx` (`id_championship`),
  CONSTRAINT `fk_Championships_Users_1` FOREIGN KEY (`id_championship`) REFERENCES `Championships` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ChampionshipsUsers`
--

LOCK TABLES `ChampionshipsUsers` WRITE;
/*!40000 ALTER TABLE `ChampionshipsUsers` DISABLE KEYS */;
INSERT INTO `ChampionshipsUsers` VALUES (1,1,2),(2,1,5),(3,1,6),(4,1,7),(5,1,8),(6,2,9),(7,1,12),(8,1,13),(9,1,16),(10,1,17),(11,1,18),(17,1,25),(23,1,32),(25,1,34),(28,1,37),(31,1,41),(34,1,44),(38,1,48),(39,1,49),(40,1,50),(41,1,51),(42,1,52),(43,1,53),(44,1,54),(45,1,55),(46,1,56),(47,1,58);
/*!40000 ALTER TABLE `ChampionshipsUsers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Competence`
--

DROP TABLE IF EXISTS `Competence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Competence` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `discription` text,
  `plan` text,
  `schedule` text,
  `infrastructure` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nameCompetence_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Competence`
--

LOCK TABLES `Competence` WRITE;
/*!40000 ALTER TABLE `Competence` DISABLE KEYS */;
INSERT INTO `Competence` VALUES (1,'WEB','Описание веба','картинка','ссылка на расписание','ссылка на ифраструктуру'),(2,'Проганье','Описание проганья','картинка','ссылка на расписание','ссылка на ифраструктуру'),(3,'Инженерия','Описание инженерии','картинка','ссылка на расписание','ссылка на ифраструктуру'),(4,'Хирургия','Описание хирургии','картинка','ссылка на расписание','ссылка на ифраструктуру'),(999,'Все','Все','Все','Все','Все');
/*!40000 ALTER TABLE `Competence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CompetenceSponsors`
--

DROP TABLE IF EXISTS `CompetenceSponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CompetenceSponsors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_competence` int(11) DEFAULT NULL,
  `id_sponsor` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Competence_Sposors_1_idx` (`id_sponsor`),
  KEY `fk_Competence_Sponsors_1_idx` (`id_competence`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CompetenceSponsors`
--

LOCK TABLES `CompetenceSponsors` WRITE;
/*!40000 ALTER TABLE `CompetenceSponsors` DISABLE KEYS */;
INSERT INTO `CompetenceSponsors` VALUES (1,2,1),(2,2,2),(3,2,3);
/*!40000 ALTER TABLE `CompetenceSponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CompetenceVolunteer`
--

DROP TABLE IF EXISTS `CompetenceVolunteer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CompetenceVolunteer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_competence` int(11) DEFAULT NULL,
  `id_volunteer` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Competence_Volunteer_1_idx` (`id_competence`),
  KEY `fk_Competence_Volunteer_2_idx` (`id_volunteer`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CompetenceVolunteer`
--

LOCK TABLES `CompetenceVolunteer` WRITE;
/*!40000 ALTER TABLE `CompetenceVolunteer` DISABLE KEYS */;
INSERT INTO `CompetenceVolunteer` VALUES (3,2,1),(7,2,1),(8,1,0),(9,1,0),(10,1,0),(11,1,0),(12,1,0),(13,1,14);
/*!40000 ALTER TABLE `CompetenceVolunteer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sponsors`
--

DROP TABLE IF EXISTS `Sponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sponsors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `region` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sponsors`
--

LOCK TABLES `Sponsors` WRITE;
/*!40000 ALTER TABLE `Sponsors` DISABLE KEYS */;
INSERT INTO `Sponsors` VALUES (1,'хуй','рег','М'),(2,'имя','Россия','Ж'),(3,'тест','Рус','Ж');
/*!40000 ALTER TABLE `Sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserTypes`
--

DROP TABLE IF EXISTS `UserTypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserTypes` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserTypes`
--

LOCK TABLES `UserTypes` WRITE;
/*!40000 ALTER TABLE `UserTypes` DISABLE KEYS */;
INSERT INTO `UserTypes` VALUES (1,'Admin'),(2,'Competitor'),(3,'Coordinator'),(4,'Expert');
/*!40000 ALTER TABLE `UserTypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `id_number` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `birth` date DEFAULT NULL,
  `region` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `id_type` int(11) NOT NULL,
  `competence` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idNumber_UNIQUE` (`id_number`),
  KEY `fk_Users_1_idx` (`id_type`),
  KEY `fk_Users_2_idx` (`competence`),
  CONSTRAINT `fk_Users_1` FOREIGN KEY (`id_type`) REFERENCES `UserTypes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_2` FOREIGN KEY (`competence`) REFERENCES `Competence` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Администратор','М','админ','1','2000-01-01','Регион','Почта',1,999),(2,'Участник','М','юзер','1','2000-01-01','Регион','Почта',2,1),(3,'Координатор','М','коор','1','2000-01-01','Регион','Почта',3,999),(4,'Эксперт','M','эксперт','1','2000-01-01','Регион','Почта',4,2),(5,'Участник','М','юзер2','1','2000-01-02','Регион','Почта',2,2),(6,'Участник','М','юзер3','1','2000-01-03','Регион','Почта',2,3),(7,'Участник','М','юзер4','1','2000-01-04','Регион','Почта',2,4),(8,'Участник','М','юзер5','1','2000-01-05','Регион','Почта',2,1),(9,'Участник','М','юзер6','1','2000-01-07','Регион','Почта',2,1),(10,'эксперт','Ж','логин','пароль','1990-01-01','Регион','почта@почта',4,1),(12,'эксперт','Ж','хуилва','пароль','1990-01-01','Регион','почта@почта',4,1),(13,'эксперт','Ж','вамв','пароль','1990-01-01','Регион','почта@почта',4,1),(15,'эксперт','Ж','вавфысвы','пароль','1990-01-01','Регион','почта@почта',4,1),(16,'эксперт','Ж','ygsuvjs','пароль','1990-01-01','Регион','почта@почта',4,1),(17,'эксперт','Ж','ygfdfds','пароль','1990-01-01','Регион','почта@почта',4,1),(18,'эксперт','Ж','19831132','пароль','1983-01-01','Регион','почта@почта',4,1),(25,'эксперт','Ж','19901542','пароль','1990-01-01','Регион','почта@почта',4,1),(32,'эксперт','Ж','19901532','пароль','1990-01-01','Регион','почта@почта',4,2),(34,'эксперт','Ж','19901442','пароль','1990-01-01','Регион','почта@почта',4,1),(37,'заебало','Ж','19902332','пароль','1990-01-01','Регион','почта@почта',2,2),(41,'заебало','Ж','19902342','пароль','1990-01-01','Регион','почта@почта',2,2),(44,'заебало','Ж','19902272','пароль','1990-01-01','Регион','почта@почта',2,2),(48,'звдалмь','Ж','199алв72','пароль','1990-01-01','Регион','почта@почта',2,2),(49,'заебало','Ж','19902292','пароль','1990-01-01','Регион','почта@почта',2,2),(50,'заебало','Ж','19902992','пароль','1990-01-01','Регион','почта@почта',2,2),(51,'заебало','Ж','19902402','пароль','1990-01-01','Регион','почта@почта',2,2),(52,'эксперт','Ж','19902514','пароль','1990-01-01','Регион','почта@почта',4,2),(53,'уч','Ж','19902972','пароль','1990-01-01','Регион','почта@почта',2,2),(54,'корди','Ж','19902203','пароль','1990-01-01','Регион','почта@почта',3,999),(55,'уч','Ж','19902892','пароль','1990-01-01','Регион','почта@почта',2,2),(56,'заебало','Ж','19902142','пароль','1990-01-01','Регион','почта@почта',2,2),(58,'заебало','Ж','19902852','пароль','1990-01-01','Регион','почта@почта',2,2);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Volunteer`
--

DROP TABLE IF EXISTS `Volunteer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Volunteer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `region` varchar(45) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Volunteer`
--

LOCK TABLES `Volunteer` WRITE;
/*!40000 ALTER TABLE `Volunteer` DISABLE KEYS */;
INSERT INTO `Volunteer` VALUES (1,'волонтер','регион','М'),(2,'волонтер','регион','М'),(3,'волонтерfkdl','регион','М'),(4,'вотерfkdlhjbjh','регион','М'),(5,'test','регион','М'),(6,'testff','регион','М'),(7,'testff','регион','М'),(8,'testff','регион','М'),(9,'testff','регион','М'),(10,'testff','регион','М'),(11,'имяволонтера','Россия','М'),(12,'dj','Россия','М'),(13,'имя','Россия','Ж'),(14,'ТЕСТ','Россия','Ж');
/*!40000 ALTER TABLE `Volunteer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mydb'
--

--
-- Dumping routines for database 'mydb'
--
/*!50003 DROP PROCEDURE IF EXISTS `add_competitor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_competitor`(n varchar(45), g varchar(1), r varchar(45), e varchar(45), p varchar(45), b date, c int,
                                l varchar(45), type int, champion int)
begin
  insert into Users(name, gender, id_number, password, birth, region, email, id_type, competence)
  values (n, g, l, p, b, r, e, type, c);
  insert into ChampionshipsUsers(id_championship, id_user)
  values (champion, (select id from Users where id_number = l));
  update Championships set Championships.user_amount = Championships.user_amount + 1 where Championships.id = champion;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_coordinator` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_coordinator`(n varchar(45), g varchar(1), r varchar(45), e varchar(45), p varchar(45), b date,
                                 c int,
                                 l varchar(45), type int,champion int)
begin
  insert into Users(name, gender, id_number, password, birth, region, email, id_type, competence)
  values (n, g, l, p, b, r, e, type, c);
  insert into ChampionshipsUsers(id_championship, id_user)
  values (champion, (select id from Users where id_number = l));
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_expert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_expert`(n varchar(45), g varchar(1), r varchar(45), e varchar(45), p varchar(45), b date, c int,
                            l varchar(45), type int, champion int)
begin
  insert into Users(name, gender, id_number, password, birth, region, email, id_type, competence)
  values (n,g,l,p,b,r,e,type,c);
  insert into ChampionshipsUsers(id_championship, id_user) values (champion, (select id from Users where id_number = l));
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_marks` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_marks`(IN id_u int, IN module int, IN mark int, IN champ int, IN comp int)
begin
  update ChampionshipsResults set result = mark where id_championship = champ and id_module = module and id_user = id_u and id_competence = comp;
  #insert into ChampionshipsResults(id_championship, id_competence, id_module, id_user, result)
  #values (champ, comp, module, id_u, mark);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_sponsor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_sponsor`(IN name varchar(45), IN gender varchar(1), IN region varchar(45), IN competence int)
begin
  insert into Sponsors(name, region, gender) values (name, region, gender);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_sponsor_to_competence` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_sponsor_to_competence`( IN name varchar (45), IN gender varchar (1), IN region varchar (45), IN competence int)
begin
   declare id_vol int default 0;
  set id_vol = (select id
              from Sponsors
              where Sponsors.name = name
                and Sponsors.region = region
                and Sponsors.gender = gender
              limit 1);

  insert into CompetenceSponsors(id_competence, id_sponsor)
  values (competence, id_vol);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_volunteer` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_volunteer`(IN name varchar(45), IN gender varchar(1), IN region varchar(45), IN competence int)
begin
  insert into Volunteer(name, region, gender) values (name, region, gender);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_volunteer_to_competence` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_volunteer_to_competence`(IN name varchar(45), IN gender varchar(1), IN region varchar(45),
                                             IN competence int)
begin
  declare id_v int default 0;
  set id_v = (select id
            from Volunteer
            where Volunteer.name = name
              and Volunteer.region = region
              and Volunteer.gender = gender
            limit 1);

  insert into CompetenceVolunteer(id_competence, id_volunteer) values (competence, id_v);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `change_password` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `change_password`(id_user int,pass varchar(45))
begin
  update Users set Users.password = pass where id = id_user;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `change_vol_competence` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `change_vol_competence`(IN id_vol int, IN id_comp int)
begin
  update CompetenceVolunteer set id_competence = id_comp where id_volunteer = id_vol;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `next_championship` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `next_championship`()
BEGIN
select id,name from Championships where curdate()<time limit 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reg_competitor_result` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reg_competitor_result`(IN n varchar(45), IN g varchar(1), IN r varchar(45), IN e varchar(45),
                                       IN p varchar(45),
                                       IN b date, IN c int, IN l varchar(45), IN type int, IN champion int)
begin
  declare id_u int;
  set id_u = (select id
              from Users
              where name = n
                and gender = g
                and region = r
                and email = e
                and password = p
                and birth = b
                and competence = c
                and id_type = type
                and id_number = l);
  insert into ChampionshipsResults(id_championship, id_competence, id_module, id_user, result)
  values (champion, c, 1, id_u, 0);
  insert into ChampionshipsResults(id_championship, id_competence, id_module, id_user, result)
  values (champion, c, 2, id_u, 0);
  insert into ChampionshipsResults(id_championship, id_competence, id_module, id_user, result)
  values (champion, c, 3, id_u, 0);
  insert into ChampionshipsResults(id_championship, id_competence, id_module, id_user, result)
  values (champion, c, 4, id_u, 0);
  insert into ChampionshipsResults(id_championship, id_competence, id_module, id_user, result)
  values (champion, c, 5, id_u, 0);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_all_marks` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_all_marks`(champ int, comp int)
begin
  select id_user, id_module, result from ChampionshipsResults where champ = id_championship and comp = id_competence;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_competitors` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_competitors`(IN id_champ int, IN id_comp int, IN id_user int, IN type int)
BEGIN
  #id_champ int, id_comp int, id_user int
  #select id_user from ChampionshipsUsers where id_championship = 1;
  declare comp_check int default 0;
  set comp_check = (select count(*) from Competence where id = id_comp limit 1);
  #select comp_check;
  if (comp_check = 0) then
    select distinct Users.id,
                    Users.name,
                    Users.gender,
                    Users.id_number,
                    Users.password,
                    Users.birth,
                    Users.region,
                    Users.email,
                    Users.competence
    from Users
           join
         (select ChampionshipsUsers.id_user from ChampionshipsUsers where id_championship = id_champ) as t
         on t.id_user = Users.id
    where id_type = type
      and Users.id != id_user;
  end if;
  if (comp_check > 0) then
    select distinct Users.id,
                    Users.name,
                    Users.gender,
                    Users.id_number,
                    Users.password,
                    Users.birth,
                    Users.region,
                    Users.email,
                    Users.competence
    from Users
           join
         (select ChampionshipsUsers.id_user from ChampionshipsUsers where id_championship = id_champ) as t
         on t.id_user = Users.id
    where id_type = type
      and Users.id != id_user
      and competence = id_comp;
  end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_marks_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_marks_user`(id_u int, champ int, comp int)
begin
  select id_module, result from ChampionshipsResults where id_u = id_user and champ = id_championship and comp = id_competence;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-17 20:35:55
