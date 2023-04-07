-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 13, 2020 at 12:59 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `farmgap`
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

--
-- Dumping data for table `checklist`
--

INSERT INTO `checklist` (`No`, `NameofChecklist`, `Date`, `FarmID`) VALUES
(1, '', '2019-05-11', 1),
(2, '', '2019-05-11', 1),
(3, '', '2019-07-16', 2),
(4, '', '2019-07-16', 2);

-- --------------------------------------------------------

--
-- Table structure for table `checklistdetail`
--

CREATE TABLE `checklistdetail` (
  `C-No` int(11) NOT NULL,
  `Seq` int(5) NOT NULL,
  `Namelist` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `value` varchar(255) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `checklistdetail`
--

INSERT INTO `checklistdetail` (`C-No`, `Seq`, `Namelist`, `value`) VALUES
(1, 2, 'ปริมาณน้ำ', 'เพียงพอ'),
(1, 1, 'แหล่งน้ำที่ใช้', 'No'),
(2, 1, 'การแยกระบบระบายน้ำ', 'แยก'),
(2, 2, 'ความสะอาด', 'สะอาด'),
(2, 3, 'ห้องน้ำ/ห้องสุขา ในบริเวณฟาร์ม', 'ไม่มี'),
(3, 1, 'WaterSource', 'ลำธาร');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Emp_ID` varchar(13) CHARACTER SET utf8mb4 NOT NULL,
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

INSERT INTO `employee` (`Emp_ID`, `FName_th`, `LName_th`, `FName_en`, `LName_en`, `Date`, `Tel`, `LineID`, `Email`, `HouseNo`, `Moo`, `Soi`, `Road`, `Tambon`, `Amphure`, `Province`, `Password`, `FarmID`, `RoleID`) VALUES
('1000000000000', 'วริศ', 'จริยะ', 'Varis', 'Jariya', '1987-10-25', '0954612452', 'varis1877', 'Example@example.com', '187/5', '3', '5', '345', 'บางคูวัด', 'ปทุมธานี', 'ปทุมธานี', '122445', 1, 1),
('2410055662163', 'มีชัย', 'ใจดี', 'MeChai', 'Jaidee', '1979-05-01', '0426513005', NULL, 'Ezy@example.com', '10', '2', NULL, 'สุรี', 'ในเมือง', 'เมือง', 'เมืองไทย', '12345', 9, 1),
('2544155523950', 'ส้ม', 'หยุด', 'Som', 'Yood', '1988-05-26', '0652554451', NULL, 'Somyood@example.com', '155/4', '2', '12', '343', 'บางบัวทอง', 'บางบัวทอง', 'นครปฐม', 'Somyoodja', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `emptype`
--

CREATE TABLE `emptype` (
  `Role-ID` int(10) NOT NULL,
  `Typename` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `responsibility` varchar(50) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `emptype`
--

INSERT INTO `emptype` (`Role-ID`, `Typename`, `responsibility`) VALUES
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
  `FP-No` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`No`, `Date`, `Name`, `Problem`, `FP-No`) VALUES
(1, '2019-07-15 17:00:00', 'ฝนตก', 'ค่า pH ผกผัน', 1),
(2, '2020-01-04 17:00:00', 'มีน้ำเสีย', 'สัตว์น้ำติดเชื้อโรค', 3),
(4, '2012-02-04 17:00:00', 'น้ำท่วม', 'ปลาลอยออกจากบ่อ', 1);

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
(1, 'สวนเพาะเลี้ยงนายวริศ', '', '2315231520', '3', 'บางคูวัด', 'ปทุมธานี', 'ปทุมธานี', '84\'33', '', 'ลงทะเบียน', 'มี', NULL, 20151125, 'เป็นเจ้าของ', 0, 12, 'มี', 0, 0, 'มี', 0, 0, '', 'มี', 'บ่อขุดใหม่', 0, 'เลี้ยง(บ่อ)', 8, 0, '700 KG', 'กำไร', 'กำลังเลี้ยง'),
(2, 'สวนปลาส้มหยุด', '', '1157234690', '2', 'บางบัวทอง', 'บางบัวทอง', 'นครปฐม', '77\'24', '', 'ลงทะเบียน', 'มี', NULL, 20110304, 'เช่า', 0, 7, 'ไม่มี', 0, 0, 'มี', 0, 0, '', 'ไม่มี', 'บ่อเก่า 5 ปี', 0, 'เลี้ยง(กระชัง)', 4, 0, '400 KG', 'เท่าทุน', 'กำลังพักบ่อ'),
(3, 'ส้มหยุดสุดๆ', 'ส้มจ้าส้ม', '7', '7', 'แปด', 'แปด', 'แปด', '8.8888, 8.8888', 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Farm\\Farmplan\\list3-2.png', 'ไม่มี', 'ไม่มี', 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Farm\\Reg Farm document\\list2.png', 2011, 'พื้นที่ส่วนตัว', 0, 10, 'ไม่มี', 0, 0, 'ไม่มี', 0, 0, 'ไม่มี', 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Farm\\SewageSystem\\ER Diagram.png', 'บ่อขุดใหม่', 0, 'กระชัง', 5, 3, '1', 'กำไร', 'กำลังเลี้ยง'),
(4, '', '', '', '', '', '', '', '', 'No', '', '', 'No', 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 'No', '', 0, '', 0, 0, '', '', ''),
(5, '', '', '', '', '', '', '', '', 'No', '', '', 'No', 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 'No', '', 0, '', 0, 0, '', '', ''),
(6, '', '', '', '', '', '', '', '', 'No', '', '', 'No', 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 'No', '', 0, '', 0, 0, '', '', ''),
(7, '', '', '', '', '', '', '', '', 'No', '', '', 'No', 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 'No', '', 0, '', 0, 0, '', '', ''),
(8, '', '', '', '', '', '', '', '', '..\\assets\\Farm\\Farmplan\\7.jpg', '', '', 'No', 0, '', 0, 0, '', 0, 0, '', 0, 0, '', 'No', '', 0, '', 0, 0, '', '', ''),
(9, 'มีชัยใจดีฟาร์ม', 'มีชัย', '70', '3', 'หนองกี่', 'กระทุ่มแบน', 'กาฬสิน', '71\'4555, 51\'55555', 'No', 'ไม่มี', 'ไม่มี', 'No', 2540, 'พื้นที่ส่วนตัว', NULL, 30, 'มี', 10, 10, 'ไม่มี', NULL, NULL, 'ไม่มี', 'No', 'บ่อขุดใหม่', NULL, 'กระชัง', 18, 20, '1', 'กำไร', 'กำลังเลี้ยง');

-- --------------------------------------------------------

--
-- Table structure for table `fishlot`
--

CREATE TABLE `fishlot` (
  `No` int(5) NOT NULL,
  `NumberofDays` int(2) NOT NULL,
  `Round` int(4) NOT NULL,
  `FP-No` int(11) NOT NULL,
  `FirstHarvest` date DEFAULT NULL,
  `SecHarvest` date DEFAULT NULL,
  `ThirdHarvest` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `fishlot`
--

INSERT INTO `fishlot` (`No`, `NumberofDays`, `Round`, `FP-No`, `FirstHarvest`, `SecHarvest`, `ThirdHarvest`) VALUES
(1, 90, 1, 1, '2019-12-20', NULL, NULL),
(2, 30, 3, 3, '2020-01-07', '2020-02-03', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `fishmanagement`
--

CREATE TABLE `fishmanagement` (
  `No` int(5) NOT NULL,
  `Nameofmanage` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `FL-No` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `fishmanagement`
--

INSERT INTO `fishmanagement` (`No`, `Nameofmanage`, `FL-No`) VALUES
(1, 'ให้อาหาร', 1),
(2, 'ให้อาหารเสริม', 1),
(3, 'ให้อาหาร', 2);

-- --------------------------------------------------------

--
-- Table structure for table `fishpond`
--

CREATE TABLE `fishpond` (
  `No` int(11) NOT NULL,
  `PondType` int(1) NOT NULL,
  `Species` int(5) NOT NULL,
  `FarmID` int(10) NOT NULL,
  `Size` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `fishpond`
--

INSERT INTO `fishpond` (`No`, `PondType`, `Species`, `FarmID`, `Size`) VALUES
(1, 1, 1, 1, 4),
(2, 1, 2, 1, 2),
(3, 2, 4, 2, 7);

-- --------------------------------------------------------

--
-- Table structure for table `fishtype`
--

CREATE TABLE `fishtype` (
  `No` int(2) NOT NULL,
  `FishName` varchar(50) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `fishtype`
--

INSERT INTO `fishtype` (`No`, `FishName`) VALUES
(1, 'ปลาดุก'),
(2, 'ปลาสวาย'),
(3, 'ปลาตะเพียน'),
(4, 'ปลาช่อน'),
(5, 'ปลาทู'),
(6, 'ปลาทู'),
(7, 'ปลาทู');

-- --------------------------------------------------------

--
-- Table structure for table `managementlist`
--

CREATE TABLE `managementlist` (
  `Seq` int(2) NOT NULL,
  `FM-No` int(5) NOT NULL,
  `List` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `Date` datetime NOT NULL,
  `Time` varchar(50) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Time period',
  `Volume` int(2) NOT NULL,
  `MT-No` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `managementlist`
--

INSERT INTO `managementlist` (`Seq`, `FM-No`, `List`, `Date`, `Time`, `Volume`, `MT-No`) VALUES
(1, 1, 'ให้อาหาร', '2019-07-16 00:00:00', '', 5, 1),
(1, 3, 'ให้อาหาร', '2020-01-10 00:00:00', '', 3, 1),
(2, 1, 'ให้อาหาร', '2019-07-16 00:00:00', '', 5, 1),
(3, 1, 'ให้อาหารเสริม', '2019-07-16 00:00:00', '', 4, 2);

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

--
-- Dumping data for table `managementtype`
--

INSERT INTO `managementtype` (`No`, `Name`, `NameType`, `Register`, `InspectionResults`, `MonthlyPurchaseRate`, `Startdate`, `Enddate`) VALUES
(1, 'มีแมวต้องไม่มี', 'อาหาร', '43221', 'Pass', 40, '2019-10-08', '2020-10-08'),
(2, 'เสริมแล้วดี', 'อาหารเสริม', '63229', 'Pass', 2, '2019-12-03', '2022-06-03'),
(3, 'ยาน้ำยาเม็ด', 'ยา', '12346', 'Pass', 12, '2019-12-03', '2020-12-05');

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
  `Seq` int(2) NOT NULL,
  `Ev-No` int(10) NOT NULL,
  `Treatment` varchar(300) CHARACTER SET utf8mb4 NOT NULL,
  `TMSdate` date NOT NULL,
  `TMEdate` date NOT NULL,
  `Emp-ID` varchar(13) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `treatment`
--

INSERT INTO `treatment` (`Seq`, `Ev-No`, `Treatment`, `TMSdate`, `TMEdate`, `Emp-ID`) VALUES
(1, 2, 'ทำการแยกขยะออกจากบ่อ โดยการนำสัตว์น้ำแยกไปไว้ในส่วนคัดแยก ทำการปล่อยน้ำทิ้งทำความสะอาดบ่อ ตรวจสอบสัตว์น้ำว่ามีอาการผิดปกติหรือไม่ หากมีจะดำเนินการนำไปตรวจหาอาการ', '2020-01-06', '2020-01-12', '1000000000000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `checklist`
--
ALTER TABLE `checklist`
  ADD PRIMARY KEY (`No`),
  ADD KEY `checklist_farmid` (`FarmID`);

--
-- Indexes for table `checklistdetail`
--
ALTER TABLE `checklistdetail`
  ADD PRIMARY KEY (`C-No`,`Seq`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Emp_ID`),
  ADD KEY `employee_RoleID` (`RoleID`),
  ADD KEY `employee_farmID` (`FarmID`);

--
-- Indexes for table `emptype`
--
ALTER TABLE `emptype`
  ADD PRIMARY KEY (`Role-ID`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`No`),
  ADD KEY `event_fishpond` (`FP-No`);

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
  ADD KEY `fishlot_fishpond` (`FP-No`);

--
-- Indexes for table `fishmanagement`
--
ALTER TABLE `fishmanagement`
  ADD PRIMARY KEY (`No`),
  ADD KEY `fishmanagement_fishlot` (`FL-No`);

--
-- Indexes for table `fishpond`
--
ALTER TABLE `fishpond`
  ADD PRIMARY KEY (`No`),
  ADD KEY `fishpond_Fishtype` (`Species`),
  ADD KEY `fishpond_TypeNo` (`PondType`),
  ADD KEY `fishpond_farmID` (`FarmID`);

--
-- Indexes for table `fishtype`
--
ALTER TABLE `fishtype`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `managementlist`
--
ALTER TABLE `managementlist`
  ADD PRIMARY KEY (`Seq`,`FM-No`),
  ADD KEY `managamentlist_fishmange` (`FM-No`),
  ADD KEY `managamentlist_mangetype` (`MT-No`);

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
  ADD PRIMARY KEY (`Seq`,`Ev-No`),
  ADD KEY `treatment_empID` (`Emp-ID`),
  ADD KEY `treatment_eventNo` (`Ev-No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `checklist`
--
ALTER TABLE `checklist`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `checklistdetail`
--
ALTER TABLE `checklistdetail`
  MODIFY `Seq` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emptype`
--
ALTER TABLE `emptype`
  MODIFY `Role-ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `No` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `farm`
--
ALTER TABLE `farm`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `fishlot`
--
ALTER TABLE `fishlot`
  MODIFY `No` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `fishmanagement`
--
ALTER TABLE `fishmanagement`
  MODIFY `No` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `fishpond`
--
ALTER TABLE `fishpond`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `fishtype`
--
ALTER TABLE `fishtype`
  MODIFY `No` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `managementtype`
--
ALTER TABLE `managementtype`
  MODIFY `No` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pondtype`
--
ALTER TABLE `pondtype`
  MODIFY `No` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `treatment`
--
ALTER TABLE `treatment`
  MODIFY `Seq` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `checklist`
--
ALTER TABLE `checklist`
  ADD CONSTRAINT `checklist_farmid` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_RoleID` FOREIGN KEY (`RoleID`) REFERENCES `emptype` (`Role-ID`),
  ADD CONSTRAINT `employee_farmID` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`);

--
-- Constraints for table `event`
--
ALTER TABLE `event`
  ADD CONSTRAINT `event_fishpond` FOREIGN KEY (`FP-No`) REFERENCES `fishpond` (`No`);

--
-- Constraints for table `fishlot`
--
ALTER TABLE `fishlot`
  ADD CONSTRAINT `fishlot_fishpond` FOREIGN KEY (`FP-No`) REFERENCES `fishpond` (`No`);

--
-- Constraints for table `fishmanagement`
--
ALTER TABLE `fishmanagement`
  ADD CONSTRAINT `fishmanagement_fishlot` FOREIGN KEY (`FL-No`) REFERENCES `fishlot` (`No`);

--
-- Constraints for table `fishpond`
--
ALTER TABLE `fishpond`
  ADD CONSTRAINT `fishpond_Fishtype` FOREIGN KEY (`Species`) REFERENCES `fishtype` (`No`),
  ADD CONSTRAINT `fishpond_TypeNo` FOREIGN KEY (`PondType`) REFERENCES `pondtype` (`No`),
  ADD CONSTRAINT `fishpond_farmID` FOREIGN KEY (`FarmID`) REFERENCES `farm` (`ID`);

--
-- Constraints for table `managementlist`
--
ALTER TABLE `managementlist`
  ADD CONSTRAINT `managamentlist_fishmange` FOREIGN KEY (`FM-No`) REFERENCES `fishmanagement` (`No`),
  ADD CONSTRAINT `managamentlist_mangetype` FOREIGN KEY (`MT-No`) REFERENCES `managementtype` (`No`);

--
-- Constraints for table `treatment`
--
ALTER TABLE `treatment`
  ADD CONSTRAINT `treatment_empID` FOREIGN KEY (`Emp-ID`) REFERENCES `employee` (`Emp_ID`),
  ADD CONSTRAINT `treatment_eventNo` FOREIGN KEY (`Ev-No`) REFERENCES `event` (`No`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
