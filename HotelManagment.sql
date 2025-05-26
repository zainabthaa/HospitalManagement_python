-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 26, 2025 at 07:26 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `HotelManagment`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_ID` int(11) NOT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `mname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_ID`, `fname`, `mname`, `lname`, `address`) VALUES
(101, 'John', 'Michael', 'Doe', '123 Palm Street'),
(102, 'Sara', 'Lynn', 'Smith', '456 Ocean Avenue'),
(103, 'Ali', 'Yousef', 'Khan', '789 Sunset Blvd'),
(104, 'Emily', 'Jane', 'Brown', '321 Lakeview Road');

-- --------------------------------------------------------

--
-- Table structure for table `dependents`
--

CREATE TABLE `dependents` (
  `dependent_ID` int(11) NOT NULL,
  `emp_ID` int(11) DEFAULT NULL,
  `dependent_name` varchar(50) DEFAULT NULL,
  `DoB` date DEFAULT NULL,
  `gender` enum('Male','Female','Other') DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `relation` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dependents`
--

INSERT INTO `dependents` (`dependent_ID`, `emp_ID`, `dependent_name`, `DoB`, `gender`, `role`, `relation`) VALUES
(1, 1, 'Layla Hassan', '2010-05-15', 'Female', NULL, 'Daughter'),
(2, 2, 'Youssef Saleh', '2012-08-22', 'Male', NULL, 'Son'),
(3, 4, 'Omar Fahad', '2008-11-30', 'Male', NULL, 'Nephew');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_ID` int(11) NOT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `mname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `shifts` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_ID`, `fname`, `mname`, `lname`, `role`, `shifts`) VALUES
(1, 'Ahmed', 'Ali', 'Hassan', 'Manager', 'Morning'),
(2, 'Fatima', 'Omar', 'Saleh', 'Receptionist', 'Evening'),
(3, 'Khalid', 'Hussein', 'Nasser', 'Housekeeper', 'Night'),
(4, 'Noura', 'Sami', 'Fahad', 'Chef', 'Morning');

-- --------------------------------------------------------

--
-- Table structure for table `food_and_beverage`
--

CREATE TABLE `food_and_beverage` (
  `item_ID` int(11) NOT NULL,
  `booking_ID` int(11) DEFAULT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `item_price` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food_and_beverage`
--

INSERT INTO `food_and_beverage` (`item_ID`, `booking_ID`, `item_name`, `quantity`, `item_price`) VALUES
(1, 501, 'Club Sandwich', 2, 25.00),
(2, 501, 'Orange Juice', 2, 10.00),
(3, 502, 'Chicken Biryani', 1, 35.00),
(4, 503, 'Pasta Alfredo', 1, 30.00),
(5, 503, 'Lemonade', 1, 8.00);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `room_ID` int(11) NOT NULL,
  `availability` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_ID`, `availability`) VALUES
(201, 1),
(202, 0),
(203, 1),
(204, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_ID`);

--
-- Indexes for table `dependents`
--
ALTER TABLE `dependents`
  ADD PRIMARY KEY (`dependent_ID`),
  ADD KEY `emp_ID` (`emp_ID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`emp_ID`);

--
-- Indexes for table `food_and_beverage`
--
ALTER TABLE `food_and_beverage`
  ADD PRIMARY KEY (`item_ID`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dependents`
--
ALTER TABLE `dependents`
  MODIFY `dependent_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `food_and_beverage`
--
ALTER TABLE `food_and_beverage`
  MODIFY `item_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dependents`
--
ALTER TABLE `dependents`
  ADD CONSTRAINT `dependents_ibfk_1` FOREIGN KEY (`emp_ID`) REFERENCES `employee` (`emp_ID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
