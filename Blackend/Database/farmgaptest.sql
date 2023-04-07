-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2020 at 09:37 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `farmgaptest`
--

-- --------------------------------------------------------

--
-- Table structure for table `checklist`
--

CREATE TABLE `checklist` (
  `No` int(11) NOT NULL,
  `NameofChecklist` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Date` date NOT NULL,
  `FarmID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `checklistdetail`
--

CREATE TABLE `checklistdetail` (
  `CNo` int(11) NOT NULL,
  `Seq` int(5) NOT NULL,
  `Namelist` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `value` varchar(255) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(13) NOT NULL,
  `Emp_ID` int(13) NOT NULL,
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
  `RoleID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `Emp_ID`, `FName_th`, `LName_th`, `FName_en`, `LName_en`, `Date`, `Tel`, `LineID`, `Email`, `HouseNo`, `Moo`, `Soi`, `Road`, `Tambon`, `Amphure`, `Province`, `Password`, `FarmID`, `RoleID`) VALUES
(1, 2147483647, 'song', 'สามสาว', 'sas', 'sasas', '2020-07-08', '2525525252', '-', 'd@m', '1', '1', '1', '1', '1', '1', '1', '111', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `emptype`
--

CREATE TABLE `emptype` (
  `RoleID` int(10) NOT NULL,
  `Typename` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `responsibility` varchar(50) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `emptype`
--

INSERT INTO `emptype` (`RoleID`, `Typename`, `responsibility`) VALUES
(1, 'เจ้าของฟาร์ม', 'ดูผลลัพธ์'),
(2, 'ลูกจ้าง', 'ดูแลฟาร์ม');

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `No` int(10) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Name` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Problem` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `FPNo` int(11) NOT NULL,
  `EmpID` int(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `farm`
--

CREATE TABLE `farm` (
  `ID` int(10) NOT NULL,
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
  `FarmStatus` varchar(50) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `farm`
--

INSERT INTO `farm` (`ID`, `Farmname`, `FarmOwnName`, `FarmNo`, `Moo`, `Tambon`, `Amphure`, `Province`, `Location`, `FarmPlan`, `registration`, `Document`, `File`, `StartOperation`, `Ownership`, `Year`, `Area`, `Clarifier`, `NumberofCarifier`, `AreaofCarifier`, `StorageTank`, `NumberofStorTank`, `AreaofStorTank`, `Sewage`, `SewageSystem`, `Pondbreed`, `YearofPondBreed`, `Culture`, `CultArea`, `NumofCulture`, `LastYearProduct`, `PastInvestment`, `FarmStatus`) VALUES
(7, 'songg', 'song', '1', '1', '1', '1', '1', '52525', 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\imgfarm1\\Untitled.png', 'ไม่มี', 'ไม่มี', 'No', 2353, 'พื้นที่ส่วนตัว', NULL, 30, 'ไม่มี', NULL, NULL, 'ไม่มี', NULL, NULL, 'ไม่มี', 'No', 'บ่อขุดใหม่', NULL, 'กระชัง', 30, 30, '30', 'ขาดทุน', 'กำลังเลี้ยง');

-- --------------------------------------------------------

--
-- Table structure for table `fishlot`
--

CREATE TABLE `fishlot` (
  `No` int(5) NOT NULL,
  `NumberofDays` int(2) NOT NULL,
  `Round` int(4) NOT NULL,
  `FPNo` int(11) NOT NULL,
  `FTNo` int(2) NOT NULL,
  `Startdate` date DEFAULT NULL,
  `Enddate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `fishpond`
--

CREATE TABLE `fishpond` (
  `No` int(11) NOT NULL,
  `PondNo` int(5) NOT NULL,
  `PondType` int(1) NOT NULL,
  `FarmID` int(10) NOT NULL,
  `Size` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `fishtype`
--

CREATE TABLE `fishtype` (
  `No` int(2) NOT NULL,
  `FishName` varchar(50) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `managefish`
--

CREATE TABLE `managefish` (
  `FLNo` int(5) NOT NULL,
  `Seq` int(2) NOT NULL,
  `MTNo` int(2) NOT NULL,
  `List` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Time` varchar(50) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Time period',
  `Volume` int(2) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `managementtype`
--

CREATE TABLE `managementtype` (
  `No` int(2) NOT NULL,
  `Name` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `NameType` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Register` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `InspectionResults` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `MonthlyPurchaseRate` int(2) DEFAULT NULL,
  `Startdate` date NOT NULL,
  `Enddate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pondtype`
--

CREATE TABLE `pondtype` (
  `No` int(1) NOT NULL,
  `Name` varchar(10) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `pondtype`
--

INSERT INTO `pondtype` (`No`, `Name`) VALUES
(1, 'บ่อ'),
(2, 'กระชัง');

-- --------------------------------------------------------

--
-- Table structure for table `treatment`
--

CREATE TABLE `treatment` (
  `EvNo` int(10) NOT NULL,
  `Seq` int(2) NOT NULL,
  `Treatment` varchar(300) CHARACTER SET utf8mb4 NOT NULL,
  `TMSdate` date NOT NULL,
  `TMEdate` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `checklist`
--
ALTER TABLE `checklist`
  ADD PRIMARY KEY (`No`),
  ADD KEY `FK_checklist_farm` (`FarmID`);

--
-- Indexes for table `checklistdetail`
--
ALTER TABLE `checklistdetail`
  ADD PRIMARY KEY (`CNo`,`Seq`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `roleid` (`RoleID`),
  ADD KEY `FK_employee_farm` (`FarmID`);

--
-- Indexes for table `emptype`
--
ALTER TABLE `emptype`
  ADD PRIMARY KEY (`RoleID`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`No`),
  ADD KEY `FK_event_fishpond` (`FPNo`),
  ADD KEY `FK_event_employee` (`EmpID`);

--
-- Indexes for table `farm`
--
ALTER TABLE `farm`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `fishlot`
--
ALTER TABLE `fishlot`
  ADD PRIMARY KEY (`No`),
  ADD KEY `FK_fishlot_fishpond` (`FPNo`),
  ADD KEY `FK_fishlot_fishtype` (`FTNo`);

--
-- Indexes for table `fishpond`
--
ALTER TABLE `fishpond`
  ADD PRIMARY KEY (`No`),
  ADD KEY `FK_fishpond_farm` (`FarmID`),
  ADD KEY `Fishpondtopondtype` (`PondType`);

--
-- Indexes for table `fishtype`
--
ALTER TABLE `fishtype`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `managefish`
--
ALTER TABLE `managefish`
  ADD PRIMARY KEY (`Seq`,`FLNo`);

--
-- Indexes for table `managementtype`
--
ALTER TABLE `managementtype`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `pondtype`
--
ALTER TABLE `pondtype`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `treatment`
--
ALTER TABLE `treatment`
  ADD PRIMARY KEY (`EvNo`,`Seq`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `checklist`
--
ALTER TABLE `checklist`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `checklistdetail`
--
ALTER TABLE `checklistdetail`
  MODIFY `Seq` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(13) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `No` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `farm`
--
ALTER TABLE `farm`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `fishlot`
--
ALTER TABLE `fishlot`
  MODIFY `No` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fishpond`
--
ALTER TABLE `fishpond`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fishtype`
--
ALTER TABLE `fishtype`
  MODIFY `No` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `managefish`
--
ALTER TABLE `managefish`
  MODIFY `Seq` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `managementtype`
--
ALTER TABLE `managementtype`
  MODIFY `No` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `treatment`
--
ALTER TABLE `treatment`
  MODIFY `Seq` int(2) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `checklist`
--
ALTER TABLE `checklist`
  ADD CONSTRAINT `FK_checklist_farm` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `FK_employee_farm` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `roleid` FOREIGN KEY (`RoleID`) REFERENCES `emptype` (`RoleID`);

--
-- Constraints for table `event`
--
ALTER TABLE `event`
  ADD CONSTRAINT `FK_event_employee` FOREIGN KEY (`EmpID`) REFERENCES `employee` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_event_fishpond` FOREIGN KEY (`FPNo`) REFERENCES `fishpond` (`No`) ON DELETE CASCADE;

--
-- Constraints for table `fishlot`
--
ALTER TABLE `fishlot`
  ADD CONSTRAINT `FK_fishlot_fishpond` FOREIGN KEY (`FPNo`) REFERENCES `fishpond` (`No`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_fishlot_fishtype` FOREIGN KEY (`FTNo`) REFERENCES `fishtype` (`No`) ON DELETE CASCADE;

--
-- Constraints for table `fishpond`
--
ALTER TABLE `fishpond`
  ADD CONSTRAINT `FK_fishpond_farm` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `Fishpondtopondtype` FOREIGN KEY (`PondType`) REFERENCES `pondtype` (`No`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
