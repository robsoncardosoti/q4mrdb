create database repositorio;
use repositorio;
-- MySQL dump 10.13  Distrib 5.5.21, for Win64 (x86)
--
-- Host: localhost    Database: repositorio
-- ------------------------------------------------------
-- Server version	5.5.21

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
-- Table structure for table `tme`
--

DROP TABLE IF EXISTS `tme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tme` (
  `serial` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `oai_set` varchar(255) DEFAULT NULL,
  `dispquery` enum('false','true') NOT NULL COMMENT 'Dispon¡vel para consulta externa',
  `dc_title` varchar(255) DEFAULT NULL,
  `dc_creator` text,
  `dc_subject` varchar(255) DEFAULT NULL,
  `dc_description` text,
  `dc_contributor` varchar(255) DEFAULT NULL,
  `dc_publisher` varchar(255) DEFAULT NULL,
  `dc_date` date DEFAULT NULL,
  `dc_type` varchar(255) DEFAULT NULL,
  `dc_format` varchar(255) DEFAULT NULL,
  `dc_identifier` varchar(255) DEFAULT NULL,
  `dc_source` varchar(255) DEFAULT NULL,
  `dc_language` varchar(255) DEFAULT NULL,
  `dc_relation` varchar(255) DEFAULT NULL,
  `dc_coverage` varchar(255) DEFAULT NULL,
  `dc_rights` varchar(255) DEFAULT NULL,
  `loginbd` varchar(15) NOT NULL COMMENT 'Login do banco de dados',
  `passwordbd` varchar(15) NOT NULL COMMENT 'Senha de acesso ao banco de dados',
  PRIMARY KEY (`serial`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tme`
--

LOCK TABLES `tme` WRITE;
/*!40000 ALTER TABLE `tme` DISABLE KEYS */;
INSERT INTO `tme` VALUES (1,'http://localhost/website/xyzsystem/database/oai','http://localhost/website/xyzsystem/','admname@xyz.com','http://localhost/website/system/systemname','true','imdb_pt','IMDB Inc','filmes, séries, atores, papéis, diretores, genêros, episodios.','Contém registros dos filmes, séries de TV e episódios, os atores e diretores de cada filme, os diversos gêneros de cada filme bem como sua avaliação.','XYZ','Amazon','2020-08-28','Database- MySQL','SGBDR','imdb_pt','AB','por','CD','EF','GH','root','1234');
/*!40000 ALTER TABLE `tme` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-28  7:36:01
