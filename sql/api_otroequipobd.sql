-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: api_otroequipobd
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comida`
--

DROP TABLE IF EXISTS `comida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comida` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `pais` varchar(100) NOT NULL,
  `precio` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comida`
--

LOCK TABLES `comida` WRITE;
/*!40000 ALTER TABLE `comida` DISABLE KEYS */;
INSERT INTO `comida` VALUES (1,'pizza','italia',5),(2,'tacos','mexico',4),(3,'sushi','japon',8),(4,'croissant','francia',7),(5,'paella','espagna',9),(6,'lasagna ','italia',8),(7,'arepas','venezuela',5),(8,'empanadas','colombia',3),(9,'donas','estados unidos',3),(10,'hamburguesas','alemania',5),(11,'curry','tailandia',9),(12,'crepas','francia',4),(13,'pupusas','el salvador',2),(14,'nasi goreng','indondesia ',8),(15,'burrito','mexico',3);
/*!40000 ALTER TABLE `comida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuadrimotos`
--

DROP TABLE IF EXISTS `cuadrimotos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuadrimotos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo_cuadri` varchar(45) NOT NULL,
  `tamagno` varchar(45) NOT NULL,
  `precio` float NOT NULL,
  `horario_abre` varchar(100) NOT NULL,
  `horario_cierre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuadrimotos`
--

LOCK TABLES `cuadrimotos` WRITE;
/*!40000 ALTER TABLE `cuadrimotos` DISABLE KEYS */;
INSERT INTO `cuadrimotos` VALUES (1,'azhgt456','adulto',15,'08:00:00','16:00:00'),(2,'dsfdsogf','nigno',10,'08:00:00','16:00:00'),(3,'ddasfjs','adulto',15,'08:00:00','16:00:00'),(4,'uysfsdfg','nigno',10,'08:00:00','16:00:00'),(5,'ldfsdfy','adulto',15,'08:00:00','16:00:00');
/*!40000 ALTER TABLE `cuadrimotos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurante`
--

DROP TABLE IF EXISTS `restaurante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurante` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `horario_inicio` varchar(100) NOT NULL,
  `horario_cierre` varchar(100) NOT NULL,
  `precio_promedio` float NOT NULL,
  `distancia_hotel` float NOT NULL,
  `calificacion_cliente` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurante`
--

LOCK TABLES `restaurante` WRITE;
/*!40000 ALTER TABLE `restaurante` DISABLE KEYS */;
INSERT INTO `restaurante` VALUES (1,'restaurante1','09:00:00','18:00:00',15,5,9),(2,'restaurante2','11:00:00','21:00:00',13,7,8.5),(3,'restaurante3','10:30:00','23:00:00',18,9,8),(4,'restaurante4','12:00:00','20:00:00',16,3,9.5),(5,'restaurante5','08:00:00','20:00:00',20,10,8.75);
/*!40000 ALTER TABLE `restaurante` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-07 10:04:21
