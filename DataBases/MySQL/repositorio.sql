create database repositorio;
use repositorio;

DROP TABLE IF EXISTS `tme`;

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

LOCK TABLES `tme` WRITE;

INSERT INTO `tme` VALUES (1,'http://localhost/website/xyzsystem/database/oai','http://localhost/website/xyzsystem/','admname@xyz.com','http://localhost/website/system/systemname','true','imdb_pt','IMDB Inc','filmes, séries, atores, papéis, diretores, genêros, episodios.','Contém registros dos filmes, séries de TV e episódios, os atores e diretores de cada filme, os diversos gêneros de cada filme bem como sua avaliação.','XYZ','Amazon','2020-08-28','Database- MySQL','SGBDR','imdb_pt','AB','por','CD','EF','GH','root','1234');

UNLOCK TABLES;
