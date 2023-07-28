-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: db
-- ------------------------------------------------------
-- Server version       5.7.42

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
-- Table structure for table `clubs`
--

DROP TABLE IF EXISTS `clubs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clubs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `owner_phone` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clubs`
--

LOCK TABLES `clubs` WRITE;
/*!40000 ALTER TABLE `clubs` DISABLE KEYS */;
INSERT INTO `clubs` VALUES (1,'Spades',0,'000999888'),(2,'Matrix',0,'000999888'),(3,'FullHouse',0,'000999888'),(4,'PPC',0,'000999888'),(5,'SevenDeuce',0,'000999888');
/*!40000 ALTER TABLE `clubs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `started` datetime DEFAULT NULL,
  `game_type` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `buyin_string` varchar(255) DEFAULT NULL,
  `is_bounty` tinyint(1) DEFAULT NULL,
  `bounties` int(11) DEFAULT NULL,
  `prize` int(11) DEFAULT NULL,
  `bounty_prize` int(11) DEFAULT NULL,
  `club` varchar(255) DEFAULT NULL,
  `bullets` int(11) DEFAULT NULL,
  `bullet_price` int(11) DEFAULT NULL,
  `total_buyin` int(11) DEFAULT NULL,
  `net_profit` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'2023-07-17 07:50:28','PLO','LUNCH 6MAX','(60+60+12)',1,0,0,0,'Matrix',1,132,132,-132),(3,'2023-07-14 21:51:55','PLO6','NOON HYPER','(50+50+10)',1,1,0,50,'Matrix',1,110,110,-60),(4,'2023-07-14 21:51:55','NL-SAT','1/5 - 333','(73+0)',0,NULL,0,NULL,'Spades',3,73,219,-219),(5,'2023-07-15 07:54:35','NL','MORNING HYPER KO','(35+35+7)',1,0,0,NULL,'Matrix',1,77,77,-77),(6,'2023-07-15 08:02:41','NL','FORMULA 111','(111+11)',0,NULL,0,NULL,'Matrix',1,122,122,-122),(7,'2023-07-15 09:29:09','NL-SAT','1/5 - 220','(44+4)',0,NULL,0,NULL,'Matrix',2,48,96,-96),(8,'2023-07-15 12:52:33','NL','NOON MAIN','(100+100+20)',1,0,0,NULL,'Matrix',1,220,220,-220),(9,'2023-07-15 18:33:32','NL','Mini Main 8-Max','(315+0)',0,NULL,0,NULL,'Spades',1,315,315,-315),(10,'2023-07-15 18:42:32','PLO','WAR 6MAX KO','(75+75+15)',1,0,0,NULL,'Matrix',1,165,165,-165),(11,'2023-07-15 19:44:53','NL','MINI MAIN HIGH ROLLER','(175+75+25)',1,0,0,NULL,'Matrix',1,275,275,-275),(13,'2023-07-16 14:48:56','PLO','LUNCH 6MAX','(60+60+12)',1,1,226,60,'Matrix',1,132,132,154),(14,'2023-07-16 15:04:50','NL','1/5 - 555','(122+0)',0,NULL,555,NULL,'Spades',1,122,122,433),(15,'2023-07-16 16:57:57','NL','1/5 - 555','(122+0)',0,NULL,555,NULL,'Matrix',1,122,122,433),(16,'2023-07-17 05:52:08','NL','CRAZY SUNDAY MAIN 50K','(300+30)',0,NULL,0,NULL,'Matrix',1,330,330,-330),(17,'2023-07-17 05:53:41','PLO','Hyper KO 6-Max','(74+74+17)',1,0,0,NULL,'Spades',1,165,165,-165),(18,'2023-07-17 17:22:59','PLO6','NOON HYPER','(50+50+10)',1,0,0,0,'Spades',1,110,110,-110),(19,'2023-07-17 17:25:04','NL','SHARK ATTACK','(125+12)',0,NULL,0,0,'Matrix',1,137,137,-137),(20,'2023-07-17 18:27:23','NL-SAT','1/5 - 275','(55+5)',0,NULL,275,0,'Matrix',1,60,60,215),(21,'2023-07-17 19:12:33','NL-SAT','1/4 - 444','(122+0)',0,NULL,0,0,'Matrix',1,122,122,-122),(22,'2023-07-18 14:00:43','PLO5','LUCKY 5 KO','(55+55+11)',1,0,0,0,'Matrix',1,121,121,-121),(23,'2023-07-21 19:51:55','PLO6','NOON HYPER','(50+50+10)',1,0,0,0,'Matrix',1,110,110,-110),(24,'2023-07-21 20:51:55','PLO','OMAHA','(100+0)',0,0,0,0,'FullHouse',1,100,100,-100),(25,'2023-07-22 18:42:32','PLO','NOON Turbo KO 6-Max','(74+74+17)',1,0,0,NULL,'Matrix',2,165,330,-330),(26,'2023-07-22 22:42:32','NL','BRANCH 6MAX KO','(60+60+12)',1,0,0,NULL,'Matrix',1,132,132,-132),(27,'2023-07-22 23:01:23','NL-SAT','1/5 - 550','(121+0)',0,NULL,0,0,'Matrix',1,121,121,-121),(28,'2023-07-22 23:30:00','NL-SAT','1/5 - 1100','(240+0)',0,NULL,0,0,'Matrix',1,240,240,-240),(29,'2023-07-23 14:00:43','PLO5','LUCKY 5 KO','(55+55+11)',1,2,0,110,'Matrix',2,121,242,-132);
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-25 13:19:03
