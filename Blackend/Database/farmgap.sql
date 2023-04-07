-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.13-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for farmgaptest
CREATE DATABASE IF NOT EXISTS `farmgaptest` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `farmgaptest`;

-- Dumping structure for table farmgaptest.checklist
CREATE TABLE IF NOT EXISTS `checklist` (
  `No` int(11) NOT NULL AUTO_INCREMENT,
  `NameofChecklist` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Date` date NOT NULL,
  `FarmID` int(10) NOT NULL,
  PRIMARY KEY (`No`),
  KEY `FK_checklist_farm` (`FarmID`),
  CONSTRAINT `FK_checklist_farm` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.checklistdetail
CREATE TABLE IF NOT EXISTS `checklistdetail` (
  `CNo` int(11) NOT NULL,
  `Seq` int(5) NOT NULL AUTO_INCREMENT,
  `Namelist` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `value` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`CNo`,`Seq`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `Emp_ID` int(11) NOT NULL,
  `FName_th` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `LName_th` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `FName_en` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `LName_en` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Date` date NOT NULL,
  `Tel` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `LineID` varchar(30) CHARACTER SET utf8mb4 DEFAULT NULL,
  `Email` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `HouseNo` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `Moo` varchar(2) CHARACTER SET utf8mb4 NOT NULL,
  `Soi` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Road` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Tambon` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Amphure` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `Province` varchar(20) CHARACTER SET utf8mb4 NOT NULL,
  `Password` varchar(20) CHARACTER SET utf8mb4 NOT NULL,
  `FarmID` int(10) NOT NULL,
  `RoleID` int(10) NOT NULL,
  PRIMARY KEY (`Emp_ID`),
  KEY `roleid` (`RoleID`),
  KEY `FK_employee_farm` (`FarmID`),
  CONSTRAINT `FK_employee_farm` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `roleid` FOREIGN KEY (`RoleID`) REFERENCES `emptype` (`RoleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.emptype
CREATE TABLE IF NOT EXISTS `emptype` (
  `RoleID` int(10) NOT NULL,
  `Typename` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `responsibility` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`RoleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.event
CREATE TABLE IF NOT EXISTS `event` (
  `No` int(10) NOT NULL AUTO_INCREMENT,
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Name` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Problem` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `FPNo` int(11) NOT NULL,
  `EmpID` int(13) NOT NULL,
  PRIMARY KEY (`No`),
  KEY `eventoEmp` (`EmpID`),
  KEY `FK_event_fishpond` (`FPNo`),
  CONSTRAINT `FK_event_fishpond` FOREIGN KEY (`FPNo`) REFERENCES `fishpond` (`No`) ON DELETE CASCADE,
  CONSTRAINT `eventoEmp` FOREIGN KEY (`EmpID`) REFERENCES `employee` (`Emp_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.farm
CREATE TABLE IF NOT EXISTS `farm` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `Farmname` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `FarmOwnName` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `FarmNo` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Moo` varchar(2) CHARACTER SET utf8mb4 NOT NULL,
  `Tambon` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Amphure` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `Province` varchar(20) CHARACTER SET utf8mb4 NOT NULL,
  `Location` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `FarmPlan` varchar(300) CHARACTER SET utf8mb4 NOT NULL,
  `registration` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `Document` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `File` varchar(300) CHARACTER SET utf8mb4 DEFAULT 'No',
  `StartOperation` int(4) NOT NULL,
  `Ownership` varchar(40) CHARACTER SET utf8mb4 NOT NULL,
  `Year` int(4) DEFAULT NULL,
  `Area` int(4) NOT NULL,
  `Clarifier` varchar(40) CHARACTER SET utf8mb4 NOT NULL,
  `NumberofCarifier` int(4) DEFAULT NULL,
  `AreaofCarifier` int(4) DEFAULT NULL,
  `StorageTank` varchar(40) CHARACTER SET utf8mb4 NOT NULL,
  `NumberofStorTank` int(4) DEFAULT NULL,
  `AreaofStorTank` int(4) DEFAULT NULL,
  `Sewage` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `SewageSystem` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Pondbreed` varchar(40) CHARACTER SET utf8mb4 NOT NULL,
  `YearofPondBreed` int(4) DEFAULT NULL,
  `Culture` varchar(20) CHARACTER SET utf8mb4 NOT NULL,
  `CultArea` int(3) NOT NULL,
  `NumofCulture` int(4) NOT NULL,
  `LastYearProduct` varchar(15) CHARACTER SET utf8mb4 NOT NULL,
  `PastInvestment` varchar(40) CHARACTER SET utf8mb4 NOT NULL,
  `FarmStatus` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.fishlot
CREATE TABLE IF NOT EXISTS `fishlot` (
  `No` int(5) NOT NULL AUTO_INCREMENT,
  `NumberofDays` int(2) NOT NULL,
  `Round` int(4) NOT NULL,
  `FPNo` int(11) NOT NULL,
  `FTNo` int(2) NOT NULL,
  `Startdate` date DEFAULT NULL,
  `Enddate` date DEFAULT NULL,
  PRIMARY KEY (`No`),
  KEY `FK_fishlot_fishpond` (`FPNo`),
  KEY `FK_fishlot_fishtype` (`FTNo`),
  CONSTRAINT `FK_fishlot_fishpond` FOREIGN KEY (`FPNo`) REFERENCES `fishpond` (`No`) ON DELETE CASCADE,
  CONSTRAINT `FK_fishlot_fishtype` FOREIGN KEY (`FTNo`) REFERENCES `fishtype` (`No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.fishpond
CREATE TABLE IF NOT EXISTS `fishpond` (
  `No` int(11) NOT NULL AUTO_INCREMENT,
  `PondNo` int(5) NOT NULL,
  `PondType` int(1) NOT NULL,
  `FarmID` int(10) NOT NULL,
  `Size` int(3) NOT NULL,
  PRIMARY KEY (`No`),
  KEY `Fishpondtopondtype` (`PondType`),
  KEY `FK_fishpond_farm` (`FarmID`),
  CONSTRAINT `FK_fishpond_farm` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `Fishpondtopondtype` FOREIGN KEY (`PondType`) REFERENCES `pondtype` (`No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.fishtype
CREATE TABLE IF NOT EXISTS `fishtype` (
  `No` int(2) NOT NULL AUTO_INCREMENT,
  `FishName` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.managefish
CREATE TABLE IF NOT EXISTS `managefish` (
  `FLNo` int(5) NOT NULL,
  `Seq` int(2) NOT NULL AUTO_INCREMENT,
  `MTNo` int(2) NOT NULL,
  `List` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Time` varchar(50) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Time period',
  `Volume` int(2) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`Seq`,`FLNo`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.managementtype
CREATE TABLE IF NOT EXISTS `managementtype` (
  `No` int(2) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `NameType` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Register` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `InspectionResults` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `MonthlyPurchaseRate` int(2) DEFAULT NULL,
  `Startdate` date NOT NULL,
  `Enddate` date NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.pondtype
CREATE TABLE IF NOT EXISTS `pondtype` (
  `No` int(1) NOT NULL,
  `Name` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table farmgaptest.treatment
CREATE TABLE IF NOT EXISTS `treatment` (
  `EvNo` int(10) NOT NULL,
  `Seq` int(2) NOT NULL AUTO_INCREMENT,
  `Treatment` varchar(300) CHARACTER SET utf8mb4 NOT NULL,
  `TMSdate` date NOT NULL,
  `TMEdate` date NOT NULL,
  PRIMARY KEY (`EvNo`,`Seq`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
