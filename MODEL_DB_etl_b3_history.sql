-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: etl_b3_history
-- ------------------------------------------------------
-- Server version	5.7.31

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
-- Table structure for table `asset_data_history`
--

DROP TABLE IF EXISTS `asset_data_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset_data_history` (
  `id_asset_data_history` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_registro` int(11) NOT NULL,
  `data_pregao` date NOT NULL,
  `cod_bdi` decimal(20,2) NOT NULL,
  `cod_negociacao` varchar(20) NOT NULL,
  `tipo_mercado` int(11) NOT NULL,
  `nome_empresa` varchar(250) NOT NULL,
  `especificacao_papel` varchar(10) NOT NULL,
  `prazo_dias_merc_termo` varchar(10) NOT NULL,
  `moeda_referencia` varchar(10) NOT NULL,
  `preco_abertura` decimal(20,2) NOT NULL,
  `preco_maximo` decimal(20,2) NOT NULL,
  `preco_minimo` decimal(20,2) NOT NULL,
  `preco_medio` decimal(20,2) NOT NULL,
  `preco_ultimo_negocio` decimal(20,2) NOT NULL,
  `preco_melhor_oferta_compra` decimal(20,2) NOT NULL,
  `preco_melhor_oferta_venda` decimal(20,2) NOT NULL,
  `numero_negocios` bigint(20) NOT NULL,
  `quantidade_papeis_negociados` bigint(20) NOT NULL,
  `volume_total_negociado` decimal(20,2) NOT NULL,
  `preco_exercicio` decimal(20,2) NOT NULL DEFAULT '0.00',
  `indicador_correcao_precos` decimal(20,2) NOT NULL DEFAULT '0.00',
  `data_vencimento` date NOT NULL,
  `fator_cotacao` decimal(20,2) NOT NULL DEFAULT '1.00',
  `preco_exercicio_pontos` decimal(20,2) NOT NULL DEFAULT '0.00',
  `codigo_isin` varchar(250) NOT NULL,
  `num_distribuicao_papel` decimal(20,2) NOT NULL,
  `server_date` date NOT NULL,
  PRIMARY KEY (`id_asset_data_history`),
  UNIQUE KEY `id_asset_data_history_UNIQUE` (`id_asset_data_history`),
  UNIQUE KEY `chave_composta` (`data_pregao`,`cod_negociacao`,`tipo_mercado`,`prazo_dias_merc_termo`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_data_history`
--

LOCK TABLES `asset_data_history` WRITE;
/*!40000 ALTER TABLE `asset_data_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `asset_data_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `market_type`
--

DROP TABLE IF EXISTS `market_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `market_type` (
  `id_market_type` int(11) NOT NULL AUTO_INCREMENT,
  `market_type_description` varchar(250) NOT NULL,
  PRIMARY KEY (`id_market_type`),
  UNIQUE KEY `id_market_type_UNIQUE` (`id_market_type`),
  UNIQUE KEY `market_type_description_UNIQUE` (`market_type_description`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `market_type`
--

LOCK TABLES `market_type` WRITE;
/*!40000 ALTER TABLE `market_type` DISABLE KEYS */;
INSERT INTO `market_type` VALUES (10,'MERCADO À VISTA'),(12,'CÓD. 12 - ATUALIZAR DESCRIÇÃO'),(13,'CÓD. 13 - ATUALIZAR DESCRIÇÃO'),(17,'CÓD. 17 - ATUALIZAR DESCRIÇÃO'),(20,'CÓD. 20 - ATUALIZAR DESCRIÇÃO'),(30,'CÓD. 30 - ATUALIZAR DESCRIÇÃO'),(70,'OPÇÕES DE COMPRA'),(80,'OPÇÕES DE VENDA');
/*!40000 ALTER TABLE `market_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_result_asset_data_history`
--

DROP TABLE IF EXISTS `view_result_asset_data_history`;
/*!50001 DROP VIEW IF EXISTS `view_result_asset_data_history`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_result_asset_data_history` AS SELECT 
 1 AS `id_asset_data_history`,
 1 AS `tipo_registro`,
 1 AS `data_pregao`,
 1 AS `cod_bdi`,
 1 AS `cod_negociacao`,
 1 AS `tipo_mercado`,
 1 AS `nome_empresa`,
 1 AS `especificacao_papel`,
 1 AS `prazo_dias_merc_termo`,
 1 AS `moeda_referencia`,
 1 AS `preco_abertura`,
 1 AS `preco_maximo`,
 1 AS `preco_minimo`,
 1 AS `preco_medio`,
 1 AS `preco_ultimo_negocio`,
 1 AS `preco_melhor_oferta_compra`,
 1 AS `preco_melhor_oferta_venda`,
 1 AS `numero_negocios`,
 1 AS `quantidade_papeis_negociados`,
 1 AS `volume_total_negociado`,
 1 AS `preco_exercicio`,
 1 AS `indicador_correcao_precos`,
 1 AS `data_vencimento`,
 1 AS `fator_cotacao`,
 1 AS `preco_exercido_pontos`,
 1 AS `codigo_isin`,
 1 AS `nun_distribuicao_papel`,
 1 AS `server_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'etl_b3_history'
--

--
-- Dumping routines for database 'etl_b3_history'
--

--
-- Final view structure for view `view_result_asset_data_history`
--

/*!50001 DROP VIEW IF EXISTS `view_result_asset_data_history`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kwebs732_tr_op`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_result_asset_data_history` AS select `a`.`id_asset_data_history` AS `id_asset_data_history`,`a`.`tipo_registro` AS `tipo_registro`,`a`.`data_pregao` AS `data_pregao`,`a`.`cod_bdi` AS `cod_bdi`,`a`.`cod_negociacao` AS `cod_negociacao`,`b`.`market_type_description` AS `tipo_mercado`,`a`.`nome_empresa` AS `nome_empresa`,`a`.`especificacao_papel` AS `especificacao_papel`,`a`.`prazo_dias_merc_termo` AS `prazo_dias_merc_termo`,`a`.`moeda_referencia` AS `moeda_referencia`,`a`.`preco_abertura` AS `preco_abertura`,`a`.`preco_maximo` AS `preco_maximo`,`a`.`preco_minimo` AS `preco_minimo`,`a`.`preco_medio` AS `preco_medio`,`a`.`preco_ultimo_negocio` AS `preco_ultimo_negocio`,`a`.`preco_melhor_oferta_compra` AS `preco_melhor_oferta_compra`,`a`.`preco_melhor_oferta_venda` AS `preco_melhor_oferta_venda`,`a`.`numero_negocios` AS `numero_negocios`,`a`.`quantidade_papeis_negociados` AS `quantidade_papeis_negociados`,`a`.`volume_total_negociado` AS `volume_total_negociado`,`a`.`preco_exercicio` AS `preco_exercicio`,`a`.`indicador_correcao_precos` AS `indicador_correcao_precos`,`a`.`data_vencimento` AS `data_vencimento`,`a`.`fator_cotacao` AS `fator_cotacao`,`a`.`preco_exercicio_pontos` AS `preco_exercido_pontos`,`a`.`codigo_isin` AS `codigo_isin`,`a`.`num_distribuicao_papel` AS `nun_distribuicao_papel`,`a`.`server_date` AS `server_date` from (`asset_data_history` `a` join `market_type` `b`) where ((`a`.`tipo_mercado` = `b`.`id_market_type`) and (`a`.`server_date` = curdate())) order by `a`.`id_asset_data_history` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-24 21:06:30
