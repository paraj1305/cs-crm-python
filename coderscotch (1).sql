-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2024 at 08:46 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coderscotch`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add client', 6, 'add_client'),
(22, 'Can change client', 6, 'change_client'),
(23, 'Can delete client', 6, 'delete_client'),
(24, 'Can view client', 6, 'view_client'),
(25, 'Can add contacts', 7, 'add_contacts'),
(26, 'Can change contacts', 7, 'change_contacts'),
(27, 'Can delete contacts', 7, 'delete_contacts'),
(28, 'Can view contacts', 7, 'view_contacts'),
(29, 'Can add employee', 8, 'add_employee'),
(30, 'Can change employee', 8, 'change_employee'),
(31, 'Can delete employee', 8, 'delete_employee'),
(32, 'Can view employee', 8, 'view_employee'),
(33, 'Can add project', 9, 'add_project'),
(34, 'Can change project', 9, 'change_project'),
(35, 'Can delete project', 9, 'delete_project'),
(36, 'Can view project', 9, 'view_project'),
(37, 'Can add change request', 10, 'add_changerequest'),
(38, 'Can change change request', 10, 'change_changerequest'),
(39, 'Can delete change request', 10, 'delete_changerequest'),
(40, 'Can view change request', 10, 'view_changerequest'),
(41, 'Can add task', 11, 'add_task'),
(42, 'Can change task', 11, 'change_task'),
(43, 'Can delete task', 11, 'delete_task'),
(44, 'Can view task', 11, 'view_task'),
(45, 'Can add lead', 12, 'add_lead'),
(46, 'Can change lead', 12, 'change_lead'),
(47, 'Can delete lead', 12, 'delete_lead'),
(48, 'Can view lead', 12, 'view_lead'),
(49, 'Can add project file', 13, 'add_projectfile'),
(50, 'Can change project file', 13, 'change_projectfile'),
(51, 'Can delete project file', 13, 'delete_projectfile'),
(52, 'Can view project file', 13, 'view_projectfile'),
(53, 'Can add board', 14, 'add_board'),
(54, 'Can change board', 14, 'change_board'),
(55, 'Can delete board', 14, 'delete_board'),
(56, 'Can view board', 14, 'view_board'),
(57, 'Can add leave request', 15, 'add_leaverequest'),
(58, 'Can change leave request', 15, 'change_leaverequest'),
(59, 'Can delete leave request', 15, 'delete_leaverequest'),
(60, 'Can view leave request', 15, 'view_leaverequest'),
(61, 'Can add leave', 16, 'add_leave'),
(62, 'Can change leave', 16, 'change_leave'),
(63, 'Can delete leave', 16, 'delete_leave'),
(64, 'Can view leave', 16, 'view_leave'),
(65, 'Can add leave admin', 17, 'add_leaveadmin'),
(66, 'Can change leave admin', 17, 'change_leaveadmin'),
(67, 'Can delete leave admin', 17, 'delete_leaveadmin'),
(68, 'Can view leave admin', 17, 'view_leaveadmin'),
(69, 'Can add invoice', 18, 'add_invoice'),
(70, 'Can change invoice', 18, 'change_invoice'),
(71, 'Can delete invoice', 18, 'delete_invoice'),
(72, 'Can view invoice', 18, 'view_invoice'),
(73, 'Can add invoice item', 19, 'add_invoiceitem'),
(74, 'Can change invoice item', 19, 'change_invoiceitem'),
(75, 'Can delete invoice item', 19, 'delete_invoiceitem'),
(76, 'Can view invoice item', 19, 'view_invoiceitem'),
(77, 'Can add superadmin', 7, 'add_superadmin'),
(78, 'Can change superadmin', 7, 'change_superadmin'),
(79, 'Can delete superadmin', 7, 'delete_superadmin'),
(80, 'Can view superadmin', 7, 'view_superadmin'),
(81, 'Can add lead file', 20, 'add_leadfile'),
(82, 'Can change lead file', 20, 'change_leadfile'),
(83, 'Can delete lead file', 20, 'delete_leadfile'),
(84, 'Can view lead file', 20, 'view_leadfile'),
(85, 'Can add client image', 21, 'add_clientimage'),
(86, 'Can change client image', 21, 'change_clientimage'),
(87, 'Can delete client image', 21, 'delete_clientimage'),
(88, 'Can view client image', 21, 'view_clientimage'),
(89, 'Can add employee image', 22, 'add_employeeimage'),
(90, 'Can change employee image', 22, 'change_employeeimage'),
(91, 'Can delete employee image', 22, 'delete_employeeimage'),
(92, 'Can view employee image', 22, 'view_employeeimage'),
(93, 'Can add task file', 23, 'add_taskfile'),
(94, 'Can change task file', 23, 'change_taskfile'),
(95, 'Can delete task file', 23, 'delete_taskfile'),
(96, 'Can view task file', 23, 'view_taskfile'),
(97, 'Can add salary slip', 24, 'add_salaryslip'),
(98, 'Can change salary slip', 24, 'change_salaryslip'),
(99, 'Can delete salary slip', 24, 'delete_salaryslip'),
(100, 'Can view salary slip', 24, 'view_salaryslip');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(16, 'employee', 'leave'),
(15, 'employee', 'leaverequest'),
(5, 'sessions', 'session'),
(14, 'superadmin', 'board'),
(10, 'superadmin', 'changerequest'),
(6, 'superadmin', 'client'),
(21, 'superadmin', 'clientimage'),
(8, 'superadmin', 'employee'),
(22, 'superadmin', 'employeeimage'),
(18, 'superadmin', 'invoice'),
(19, 'superadmin', 'invoiceitem'),
(12, 'superadmin', 'lead'),
(20, 'superadmin', 'leadfile'),
(17, 'superadmin', 'leaveadmin'),
(9, 'superadmin', 'project'),
(13, 'superadmin', 'projectfile'),
(24, 'superadmin', 'salaryslip'),
(7, 'superadmin', 'superadmin'),
(11, 'superadmin', 'task'),
(23, 'superadmin', 'taskfile');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-07 12:33:22.541825'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-06-07 12:33:22.588313'),
(3, 'auth', '0001_initial', '2024-06-07 12:33:22.792449'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-06-07 12:33:22.838337'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-06-07 12:33:22.841578'),
(6, 'auth', '0004_alter_user_username_opts', '2024-06-07 12:33:22.849106'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-06-07 12:33:22.857285'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-06-07 12:33:22.861726'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-06-07 12:33:22.864793'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-06-07 12:33:22.873031'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-06-07 12:33:22.876204'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-06-07 12:33:22.889704'),
(13, 'auth', '0011_update_proxy_permissions', '2024-06-07 12:33:22.889704'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-06-07 12:33:22.898183'),
(15, 'superadmin', '0001_initial', '2024-06-07 12:33:23.411072'),
(16, 'admin', '0001_initial', '2024-06-07 12:33:23.509278'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-06-07 12:33:23.517293'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-07 12:33:23.531798'),
(19, 'sessions', '0001_initial', '2024-06-07 12:33:23.557155'),
(20, 'superadmin', '0002_project_assigned_to_alter_project_employees', '2024-06-10 06:47:45.925064'),
(21, 'superadmin', '0003_alter_project_id', '2024-06-10 08:39:19.239827'),
(22, 'superadmin', '0004_alter_project_employees', '2024-06-10 10:46:39.495673'),
(23, 'superadmin', '0005_project_user', '2024-06-10 11:33:35.870986'),
(24, 'superadmin', '0006_remove_project_user', '2024-06-10 11:33:36.147875'),
(25, 'superadmin', '0007_alter_project_employees', '2024-06-10 11:33:36.158730'),
(26, 'superadmin', '0008_employee_project', '2024-06-11 04:35:26.762879'),
(27, 'superadmin', '0009_remove_employee_project', '2024-06-11 04:39:13.903750'),
(28, 'superadmin', '0010_remove_project_assigned_to', '2024-06-11 04:46:11.375704'),
(29, 'superadmin', '0011_task', '2024-06-17 06:30:55.413895'),
(30, 'superadmin', '0012_lead', '2024-06-18 05:18:33.802618'),
(31, 'superadmin', '0013_projectfile', '2024-06-19 12:25:11.692326'),
(32, 'superadmin', '0014_board_alter_task_status_task_board', '2024-06-20 11:50:11.437829'),
(33, 'superadmin', '0015_remove_task_board', '2024-06-20 11:54:44.718836'),
(34, 'superadmin', '0016_task_board', '2024-06-20 12:14:08.373881'),
(35, 'superadmin', '0017_remove_task_board_delete_board', '2024-06-20 12:14:08.387471'),
(36, 'superadmin', '0018_board', '2024-06-20 12:16:43.579540'),
(37, 'superadmin', '0019_task_board', '2024-06-20 12:18:15.005256'),
(38, 'employee', '0001_initial', '2024-06-24 19:08:40.062541'),
(39, 'employee', '0002_delete_leave_delete_leavetype', '2024-06-24 19:09:36.610832'),
(40, 'superadmin', '0020_alter_board_description', '2024-06-25 04:21:12.151549'),
(41, 'employee', '0003_initial', '2024-06-25 05:37:07.595614'),
(42, 'employee', '0004_delete_leaverequest', '2024-06-25 05:43:03.783971'),
(43, 'employee', '0005_initial', '2024-06-25 05:43:56.322318'),
(44, 'superadmin', '0021_leaveadmin', '2024-06-25 05:45:41.167941'),
(45, 'employee', '0006_leave_end_date_leave_start_date', '2024-06-26 09:46:50.095868'),
(46, 'superadmin', '0022_invoice', '2024-07-01 07:08:26.730028'),
(47, 'superadmin', '0023_invoiceitem', '2024-07-01 07:12:30.249507'),
(48, 'superadmin', '0024_invoice_payment_status', '2024-07-01 07:34:16.935934'),
(49, 'superadmin', '0025_invoiceitem_quantity_invoiceitem_rate', '2024-07-01 07:37:10.862113'),
(50, 'superadmin', '0026_remove_invoiceitem_amount_and_more', '2024-07-01 09:23:09.278926'),
(51, 'superadmin', '0027_client_address_client_company', '2024-07-01 13:21:58.429681'),
(52, 'superadmin', '0028_invoice_tax_percentage', '2024-07-02 04:23:19.864286'),
(53, 'superadmin', '0029_contacts_ifsc_code_contacts_swift_code_contacts_bank_and_more', '2024-07-03 14:14:16.612880'),
(54, 'superadmin', '0030_rename_contacts_superadmin', '2024-07-03 14:18:01.088877'),
(55, 'superadmin', '0031_superadmin_last_login_alter_project_employees_and_more', '2024-07-04 05:44:22.029421'),
(59, 'superadmin', '0032_superadmin_last_login', '2024-07-04 05:49:14.242521'),
(60, 'superadmin', '0033_alter_superadmin_options_superadmin_is_active_and_more', '2024-07-04 05:49:14.429312'),
(61, 'superadmin', '0034_rename_company_superadmin_company_name', '2024-07-04 05:49:14.452986'),
(62, 'superadmin', '0035_alter_project_employees', '2024-07-04 06:01:48.281052'),
(63, 'superadmin', '0036_superadmin_last_login', '2024-07-04 06:03:19.397364'),
(65, 'superadmin', '0037_alter_superadmin_options_remove_superadmin_is_active_and_more', '2024-07-04 07:07:18.862785'),
(66, 'superadmin', '0038_remove_superadmin_last_login', '2024-07-04 07:07:18.879970'),
(67, 'superadmin', '0039_superadmin_groups_superadmin_is_active_and_more', '2024-07-04 07:07:19.413638'),
(68, 'superadmin', '0040_alter_employee_groups_and_more', '2024-07-04 07:17:16.900340'),
(69, 'superadmin', '0041_alter_employee_groups_and_more', '2024-07-04 07:50:02.733896'),
(70, 'superadmin', '0042_alter_superadmin_password', '2024-07-04 09:22:58.840072'),
(71, 'superadmin', '0043_employee_total_leaves_employee_used_leaves_and_more', '2024-07-05 11:21:01.289600'),
(72, 'superadmin', '0044_remove_employee_total_leaves_and_more', '2024-07-05 11:23:31.478936'),
(73, 'superadmin', '0045_remove_employee_total_leaves_and_more', '2024-07-05 11:25:00.026621'),
(74, 'superadmin', '0046_remove_employee_total_leaves_and_more', '2024-07-05 11:33:29.398627'),
(75, 'superadmin', '0047_employee_total_leaves', '2024-07-05 11:33:29.427093'),
(76, 'superadmin', '0048_remove_lead_lead_files_leadfile', '2024-07-08 06:31:28.007757'),
(77, 'superadmin', '0049_remove_client_img_clientimage', '2024-07-08 07:11:25.968685'),
(78, 'superadmin', '0050_remove_employee_img_employeeimage', '2024-07-08 07:53:25.100807'),
(79, 'superadmin', '0051_taskfile', '2024-07-17 07:34:36.150698'),
(80, 'superadmin', '0052_alter_taskfile_file', '2024-07-17 08:47:54.012009'),
(81, 'superadmin', '0053_alter_project_status', '2024-07-24 06:32:20.714685'),
(82, 'employee', '0007_alter_leave_employee', '2024-07-24 06:32:22.312723'),
(83, 'superadmin', '0054_alter_changerequest_hours_alter_client_name_and_more', '2024-07-25 07:01:52.205910'),
(84, 'superadmin', '0055_salaryslip', '2024-07-26 06:53:15.901992'),
(85, 'superadmin', '0056_alter_salaryslip_employee', '2024-07-26 07:20:53.941912'),
(86, 'superadmin', '0057_superadmin_address', '2024-07-26 10:27:00.042036'),
(87, 'superadmin', '0058_alter_salaryslip_tds_and_more', '2024-07-29 07:43:24.665688');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0rcgwmhstj8aq08k35mtmhpr6dscg68d', '.eJxVjbEOgjAURX_FdDak0FbAUWcn3ZvX91qKQmsoDMb475aEQdd77j33zTQss9dLspPuiR1ZWbL9b2gAHzashO4QulhgDPPUm2KtFBtNxSWSHU5b90_gIfm8RiMEd66unDGtlFyKg-CCeC0bEqZUXEjlrFXQIAEqainnghtqFTaugizFOD4hvHSA0WbjOV9OuyvGGf3uZtGHOMSut4l9vr-cR7E:1sZ2Lj:SNMdOBdvj-75G_KSdsXfrxOMTd_o0qP7jmzjz_9t2rA', '2024-08-14 05:58:11.389933'),
('3f57ekb04lguthg0mb5fj9ezfbso3is6', 'e30:1sTvqp:adpX5mSNlQG793ySf7S9Ubgevhr-nosbL6_NPehT2dw', '2024-07-31 04:01:11.755045'),
('kp3baqwnb0gjv8qrxssn5tdxd3b129bt', '.eJxVjs1uwjAQhN_F5wg5IfinRyTuvIE1tteN28RBsalUId4dg4Cmx535ZnYuzOBcBnPOtJjo2QfrWLPWLNw3pbtB02mcf4k2d5NSiQ4lzulF5M3hCeyfkX89A_JQS9QuOOWDllpKUlyLVgQvYXlrgyTyUmghbe-k30Gh407Y3teE59ttp7Wqpa8dj7nd6g5xycUkTFQfHbHga02P-DP3AwoyEipQ5oLRjIQfyrWPN6zu9W-hb9hCE2KK6fMttuJ6AykmauQ:1sZ2FL:dEI-pFE95lv8Bgv8DVxAuQvuFgxraWzBhRrm6fjyVFU', '2024-08-14 05:51:35.944078'),
('l0m2pp5pzn5ydazhhswofs5c3qvvyzma', 'e30:1sWdNn:N-6JWRw5BNyxfdfgrgwDKeD9g9m8A_fQ23UkfQj2XDQ', '2024-08-07 14:54:23.206698'),
('m2de0nxhl51vyefmaflj0x2v5gkotoc6', 'e30:1sWbfC:CXUyHl871SCtbFaw1OAitnhVdcMJ2Js3FvYZG7n10W4', '2024-08-07 13:04:14.450680'),
('m5ntrse0zsmr53uk0j0sitd8syvo9qa7', '.eJxVjEEOwiAQRe_C2hDogAWX7j0DmWFAqgaS0q6Md7dNutDte-__twi4LiWsPc1hYnERWovTLySMz1R3ww-s9yZjq8s8kdwTedgub43T63q0fwcFe9nWkQBUzuOQibwxysAZFLAajWMgbRUYm1Oy6CJjtOx546CIvY0uDyg-XwLtOFc:1sPdxM:pfgnIv5mGj_6Eoe2HZxB60cZ-rlpCzVRdH-3GWp7GMc', '2024-07-19 08:06:12.881050'),
('m695oce8xzxad43krq9gx9tw98nwudxd', '.eJxVjk1uwjAYRO_idYScEPzDEol9b2CN7c-N28SpYoOEEHevIwVKt_NmnubODC5lMJdMi4meHVnHmvfMwn1TWgFNP-N8I9qtkFKJDiXO6dnIu_NWOG2Tf54BeagSdQhO-aCllpIU16IVwUtY3togibwUWkjbO-kPUOi4E7b3deH5ft9prar0-cOEuORiEiaq4g8s-HqnI_7gaUBBRkItlLlgNCPhSpkdO96w-s-_gr5hC02IKabPV9iKxy-912V8:1sWdQ9:p1jocE8PaNvSzOx37DHVGyMNi6ZGNLieSRywnMKATE0', '2024-08-07 14:56:49.529229'),
('mjmfnhnoghadt4l3sve3y59jprnpf38b', 'eyJ1c2VyX2lkIjoxfQ:1sJA7q:nvOljK4ST1FeBVzMDsTTg1Q1CHWGHbM7xlvUuaF6a5A', '2024-07-01 11:02:14.433915'),
('mk5djpzt5y61rslf3963inn849ppgftj', '.eJxVj8tugzAQRf_FawTB2AlkmX1_oBs0tm_BqR8IO5Wiqv9eU0VN2J5z587MNxvplufxlrCO1rAzawWrXqEi_YmwGXOlMMVax5BXq-otUj9sqt-igbs8sruCmdJcptHhpLnSWnNIwRXQQ3SgUy9FqzRxborqWg0SgxoMcXkYhD7KQR4hJJVS-MXFO_B3aCtewIddUx4DeZRN73G1eZd39LQXUHK47-o8TZtqPIylZs9Ts_T1dZnKQI6Z3OhAX0jszA8VKw-af9BWbIUnG2yYnnD4-QWbqHmq:1sMQ1t:vpP2WrYqtd7tExknKzbW6Z4kkKM7Rt6Q7VVCSSbvvuM', '2024-07-10 10:37:33.589192'),
('ph6b2d2xg0sffws3k0pxqv618kbh916i', '.eJxVjs1uwjAQhN_F5wg5IfinRyTuvIE1tteN28RBsalUId4dg4Cmx535ZnYuzOBcBnPOtJjo2QfrWLPWLNw3pbtB02mcf4k2d5NSiQ4lzulF5M3hCeyfkX89A_JQS9QuOOWDllpKUlyLVgQvYXlrgyTyUmghbe-k30Gh407Y3teE59ttp7Wqpa8dj7nd6g5xycUkTFQfHbHga02P-DP3AwoyEipQ5oLRjIQfyrWPN6zu9W-hb9hCE2KK6fMttuJ6AykmauQ:1sWvVD:toYbYmdqjRufXK6KpupWWN5huwdpTxywfOExWU4TxQk', '2024-08-08 10:15:15.926785'),
('q3zhjtbufdg6g0qhdnk7xjemhrvsjatc', 'e30:1sWdLU:zp8M75BRo7bFpuv4E4TvCdb7h87HXwUMA4goVBdMjR8', '2024-08-07 14:52:00.912971'),
('xzxeq6q17glyslj7mvnbci2mvf9f9gwq', 'e30:1sWV9l:-3eIUK-hbGVc1Lno8L2hiEnKs6oVrqC-mrUEvh_G50U', '2024-08-07 06:07:21.021448');

-- --------------------------------------------------------

--
-- Table structure for table `employee_leave`
--

CREATE TABLE `employee_leave` (
  `id` bigint(20) NOT NULL,
  `leave_date` date DEFAULT NULL,
  `leave_reason` varchar(255) NOT NULL,
  `status` varchar(10) NOT NULL,
  `employee_id` bigint(20) NOT NULL,
  `end_date` date NOT NULL,
  `start_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee_leave`
--

INSERT INTO `employee_leave` (`id`, `leave_date`, `leave_reason`, `status`, `employee_id`, `end_date`, `start_date`) VALUES
(18, NULL, 'Consequuntur qui do ut unde officiis', 'approved', 2, '2024-06-28', '2024-06-28'),
(19, NULL, 'Fugit cupiditate qui qui eum non odio', 'approved', 2, '2024-07-31', '2024-07-27'),
(21, NULL, 'ipsa dolor esse distinctio Quisquam', 'approved', 2, '2024-06-29', '2024-06-27'),
(22, NULL, 'wdw', 'cancelled', 2, '2024-07-13', '2024-07-12'),
(25, NULL, 'Consequuntur qui do ut unde officiis', 'cancelled', 2, '2024-07-21', '2024-07-19'),
(26, NULL, 'ipsa dolor esse distinctio Quisquam', 'approved', 2, '2024-10-26', '2024-10-22'),
(27, NULL, 'Dolores eum amet enim libero sed rerum optio ut aliquid enim ratione eu nihil laborum magna', 'pending', 2, '2024-07-27', '2024-07-24'),
(28, NULL, 'Non eveniet atque earum tempor ipsam velit sit sit aliquid et nihil amet sint debitis qui', 'pending', 2, '2024-07-27', '2024-07-25');

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_board`
--

CREATE TABLE `superadmin_board` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_board`
--

INSERT INTO `superadmin_board` (`id`, `name`, `description`) VALUES
(10, 'server', 's'),
(13, 'Lara Buckley', 'Deleniti occaecat bl'),
(14, 'Patricia Sloan', 'Saepe placeat qui m'),
(15, 'Hope Santana', 'Aut in ut magna arch');

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_changerequest`
--

CREATE TABLE `superadmin_changerequest` (
  `id` bigint(20) NOT NULL,
  `task` longtext NOT NULL,
  `hours` varchar(30) NOT NULL,
  `cost` decimal(10,2) NOT NULL,
  `project_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_changerequest`
--

INSERT INTO `superadmin_changerequest` (`id`, `task`, `hours`, `cost`, `project_id`) VALUES
(17, 'Voluptas soluta volu', '2 days', 84.00, 151);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_client`
--

CREATE TABLE `superadmin_client` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `location` varchar(2) NOT NULL,
  `industry` varchar(50) NOT NULL,
  `website` varchar(200) NOT NULL,
  `since` int(10) UNSIGNED NOT NULL CHECK (`since` >= 0),
  `address` longtext DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_client`
--

INSERT INTO `superadmin_client` (`id`, `name`, `email`, `phone`, `location`, `industry`, `website`, `since`, `address`, `company`) VALUES
(1, 'Kaden Gordon', 'diqymolom@mailinator.com', '12345678', 'PW', 'Healthcare', 'https://www.qosaropidaky.org.uk', 1978, NULL, NULL),
(9, 'Hector Woods', 'fofap@mailinator.com', '789654123', 'FI', 'Education', 'https://www.jatyzewicobatoc.org.au', 2018, NULL, NULL),
(10, 'Lacota Cote', 'kadafosin@mailinator.com', '113-206345', 'GQ', 'Education', 'https://www.docavilaqiha.co.uk', 1992, NULL, NULL),
(12, 'Quail Juarez', 'vohagilas@mailinator.com', '789456123', 'GI', 'Tech', 'https://www.fofyxarise.in', 1980, NULL, NULL),
(71, 'Macey Wilkerson2ff2', 'sypufu@mailinator.com', '322233', 'IS', 'Education', 'https://www.zufymoba.com', 1970, 'Reprehenderit et te', 'Dunn and Dotson Associates'),
(73, 'Brandon Brock', 'qamez@mailinator.com', '5656464', 'GI', 'Tech', 'https://www.niq.net', 1998, 'Ipsum repellendus E', 'Mullen Petersen Plc'),
(74, 'Dora Dale', 'regavymidi@mailinator.com', '5654516516', 'AI', 'Education', 'https://www.qypudyxuloxe.tv', 2016, 'Quis et modi qui rec', 'Curry and King Trading'),
(75, 'Tatum Livingston', 'raxany@mailinator.com', '34234', 'CH', 'Finance', 'https://www.teqizydic.cm', 2008, 'Mollit aspernatur qu', 'Savage Shepherd Trading'),
(76, 'Tatum Livingston', 'raxany@mailinator.com', '34234', 'CH', 'Finance', 'https://www.teqizydic.cm', 2008, 'Mollit aspernatur qu', 'Savage Shepherd Trading'),
(77, 'Dara Lyons', 'jasedix@mailinator.com', '53453455', 'PF', 'Education', 'https://www.womikuzipelo.org', 1996, 'Dolor soluta dolores', 'Sanders and Morrison Traders'),
(78, 'Orson Pacheco', 'vymosyso@mailinator.com', '42342342', 'TR', 'Education', 'https://www.gibenadyletu.in', 1985, 'Reprehenderit tenet', 'Mullen and Walter Plc'),
(79, 'Orson Pacheco', 'vymosyso@mailinator.com', '42342342', 'TR', 'Education', 'https://www.gibenadyletu.in', 1985, 'Reprehenderit tenet', 'Mullen and Walter Plc'),
(80, 'Jamalia Brooks u', 'fyzod@mailinator.com', '45353', 'AF', 'Other', 'https://www.kesigomeni.cm', 1981, 'Odit qui quis ea nih', 'Britt Dixon LLC'),
(83, 'paraj Bhatasana', 'kabeby@mailinator.com', '1234567833', 'IN', 'Other', 'http://www.dele.ws', 2024, '8 A\r\nDevkinandAn Sos', 'Mitchell Little Co'),
(84, 'Wang Olsen', 'bekymez@mailinator.com', '5628237898', 'DJ', 'Healthcare', 'https://www.meq.net', 1981, 'Libero temporibus om', 'Vega and Frazier Co'),
(88, 'Benjamin Matthews', 'lexegequz@mailinator.com', '+1 (197) 736-3078', 'TH', 'Education', 'https://www.pohyq.ws', 1972, 'Voluptatem ut volupt', 'Barrera Vang Inc');

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_clientimage`
--

CREATE TABLE `superadmin_clientimage` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `client_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_clientimage`
--

INSERT INTO `superadmin_clientimage` (`id`, `image`, `client_id`) VALUES
(26, 'client_images/b1.jpg', 75),
(27, 'client_images/p9_MQzrFUm.jpg', 78),
(28, 'client_images/b1_pqlkaCN.jpg', 80),
(30, 'client_images/2_GjvTmul.png', 83),
(31, 'client_images/2_tGagBZW.png', 84),
(35, 'client_images/WhatsApp_Image_2024-06-17_at_6.43.37_PM_kq0Z3wp.jpeg', 88);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_employee`
--

CREATE TABLE `superadmin_employee` (
  `id` bigint(20) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `joining_date` date DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `has_reset_password` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `total_leaves` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_employee`
--

INSERT INTO `superadmin_employee` (`id`, `last_login`, `is_superuser`, `first_name`, `last_name`, `email`, `phone`, `joining_date`, `salary`, `designation`, `password`, `has_reset_password`, `is_active`, `is_staff`, `total_leaves`) VALUES
(1, '2024-06-08 06:43:47.202714', 0, 'Aristotle', 'Daniel', 'myzapef@mailinator.com', '12345', '2015-10-28', 9, 'Aut quaerat vero iusto consequatur Anim dolor', 'pbkdf2_sha256$720000$EzPGHEQjwJt8VAT43cEgUE$QFUMB7RIoUlILE/nZWo0Moob9KqE2xcHFM9exqHyby0=', 1, 1, 0, 20),
(2, '2024-07-31 05:51:35.786745', 0, 'Paraj', 'Bhatasana', 'paraj.glsbcs21@gmail.com', '7202920152', '2022-07-19', 4300, 'Eos ab vel nemo perspiciatis beatae beatae similique a', 'pbkdf2_sha256$720000$K2P7oHb2tDO0QisrgE1mjQ$WtTCUJjQ8+tUiTSNIj170Dz03DHJrq+s+t9lAmEayeo=', 1, 1, 0, 20),
(6, NULL, 0, 'niks', 'Aguilar', 'pylypyge@mailinator.com', '7894563221', '2023-05-15', 1400, 'Dolor ut rerum laborum temporibus adipisicing nesciunt dolor dolor voluptas rerum mollitia enim et', 'pbkdf2_sha256$720000$4SFjRL2vvUNio7vku4ymSK$BQAkcidPY/PNWcTUEu+2dyIxaR+ol7CI7w0KVLkhD4M=', 0, 1, 0, 20),
(8, NULL, 0, 'Joelle', 'Mack', 'ciwemo@mailinator.com', '1 894362', '1990-02-16', 77, 'Earum id mollitia aliquip excepteur exercitation iure quas cillum aut autem sed accusamus dicta qui', 'pbkdf2_sha256$720000$UeKpKcf2QoDMAPF9eYhdzL$xNzUyhdfWMv2HB/Aa5+z2UMEMYONWzU2IDpeO4L6hrg=', 0, 1, 0, 20),
(9, NULL, 0, 'Benjamin', 'Horne', 'pajijojyx@mailinator.com', '56556582', '1988-12-07', 87, 'Aliqua Officiis quis accusantium tempor', 'pbkdf2_sha256$720000$RKbPp6dvHjChVEIyDR2nsa$B1abhhpTa9y5eaXUNR1yaX8N/LZZO0fE4ST19ybb2pM=', 0, 1, 0, 20),
(10, NULL, 0, 'Logan', 'Cotton', 'nygijy@mailinator.com', '61899166', '1991-02-14', 46, 'Quia officia fuga Non architecto sint in quaerat eius corporis sint aut totam consectetur', 'pbkdf2_sha256$720000$a6QbG6p7thHwHfdgudxQQu$D16qtYDIJ77GBWrGol3SVl0QwP7RKT73r59WX/kOudQ=', 0, 1, 0, 20),
(11, NULL, 0, 'Mira done', 'Mcguire', 'dory@mailinator.com', '123456799', '2022-05-30', 14, 'Qui eaque deleniti et consequat Iste', 'pbkdf2_sha256$720000$dvQUY13s13WhQqqDhLzcpu$Tb2+j1HO+dhT/jQ2YXoQYWXIWtAIm2srNUdjT8MmkJ8=', 0, 1, 0, 20),
(12, NULL, 0, 'Scarlet', 'Nieves', 'weciv@mailinator.com', '123458', '1979-01-28', 53, 'Sint dolore aut sint in blanditiis possimus Nam', 'pbkdf2_sha256$720000$ZBVxVD4vykUxSU90AEtG54$ECEfEihBL8w+FliQTjdXThL2g4PlH3ZQrWAgr+BczXs=', 0, 1, 0, 20),
(13, NULL, 0, 'Scarlet', 'Nieves', 'wesciv@mailinator.com', '123458', '1979-01-28', 53, 'Sint dolore aut sint in blanditiis possimus Nam', 'pbkdf2_sha256$720000$u9Qd4ivvzk2xDOTDNNSySm$oxIV/r+t4XZDVott28zRgJoMFOrexTQUTl3Ry1DWqk8=', 0, 1, 0, 20),
(14, '2024-06-26 06:21:08.287802', 0, 'Zorita', 'Beasley', 'wfohomig@mailinator.com', '4665616', '1992-12-19', 61, 'Adipisicing accusamus aliquip vero sequi', 'pbkdf2_sha256$720000$sAgur5DPVdJkEghwllAaFU$eCez/MweGAQl1s3iIjn9gTPmbVzNvrU0ZRX6yyqTKN0=', 0, 1, 0, 20),
(19, NULL, 0, 'Malcolm', 'Daugherty', 'xufofoz@mailinator.com', '838383', '2002-11-15', 800, 'Accusantium aliquip ea reprehenderit nihil sed nobis sint inventore', 'pbkdf2_sha256$720000$5bJKChlLi0qR5b3XWS0f1r$FSsh0EFowSAgQ2Tx4Q0oKfol3VbKefjPZhIvnxTAMJE=', 0, 1, 0, 20),
(20, NULL, 0, 'Malcolm', 'Daugherty', 'xufofdsoz@mailinator.com', '838383', '2002-11-15', 30000, 'Accusantium aliquip ea reprehenderit nihil sed nobis sint inventore', 'pbkdf2_sha256$720000$Sc98UAefGP9OOQU6c7fFI0$v6HqCPF7V3r9WnzFy8UbrqyuXZ4Nc81Wnor1ij/eNgU=', 0, 1, 0, 20),
(22, NULL, 0, 'Plato', 'Perry', 'dacilaqap@mailinator.com', '72752272', '1988-08-31', 41000, 'Sit aliquip natus ullam nemo et ex ut', 'pbkdf2_sha256$720000$wOBoB4vZF08OPEP2gOAcwT$7BbOzmgqRaQMkvRkGaGkdHTB8eYHdJV17VRpeCtMrPg=', 0, 1, 0, 20),
(25, NULL, 0, 'Tarik1 new 1', 'Mcknight', 'vywepuqir@mailinator.com', '65656', '1984-07-25', 31000, 'Distinctio Accusamus molestiae et libero qui dolor amet', 'pbkdf2_sha256$720000$sQhx10tqVcLTGilnp1AJsy$wVm2Vpoh58pq/OS3NE/E2Unok+L4+Y8pREZh9cUagVU=', 0, 1, 0, 20),
(33, NULL, 0, 'Merritt', 'Osborn', 'kosobok@mailinator.com', '231312312', '2014-07-28', 25000, 'Labore dolore voluptas quia optio reiciendis', 'pbkdf2_sha256$720000$hKjBIkhofHrI7OmpFrq0Mk$uCW0BEqNtIPz4TwcsQup3CUY6/cvSiPm6qQr3SrdRtM=', 0, 1, 0, 20),
(36, NULL, 0, 'Indigo', 'Moss', 'xezyduzi@mailinator.com', '12345678', '1990-10-31', 5400, 'Sunt eveniet dolor qui vel officia qui autem autem sit id porro enim voluptatem Id vero id qua', 'pbkdf2_sha256$720000$Z1M0gPjj7DU860v9HZkgZ5$hMPZSDB1Mzcolbj0huxYYbiH0b2zMY4HurK9RuqIf/Q=', 0, 1, 0, 20),
(37, NULL, 0, 'Hiroko', 'Holland', 'jaqorec@mailinator.com', 'klllk', '1977-04-17', 50000, 'Numquam impedit veritatis temporibus quibusdam unde harum dolor dignissimos nostrud sint a culpa n', 'pbkdf2_sha256$720000$A7QKjVsc1DcsXdWYwaVM9a$kIvMeJJQDhYm35wfYAnrsF93zDzImYxaRPoDFrr5IY8=', 0, 1, 0, 20),
(38, NULL, 0, 'test', 'Cohen', 'qade@mailinator.com', '+1 (951) 917-7525', '2023-06-14', 15000, 'Labore fugit enim', 'pbkdf2_sha256$720000$gvaatUKI0t4AGal41NXlJA$dtq3M3vS5zoDgCgu7kTtkEGlsKjp4QD/aEecar5vZwk=', 0, 1, 0, 20);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_employeeimage`
--

CREATE TABLE `superadmin_employeeimage` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `employee_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_employeeimage`
--

INSERT INTO `superadmin_employeeimage` (`id`, `image`, `employee_id`) VALUES
(7, 'employee_images/Photo_GRSGjNd.jpg', 37),
(8, 'employee_images/Photo_7rGvhXt.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_employee_groups`
--

CREATE TABLE `superadmin_employee_groups` (
  `id` bigint(20) NOT NULL,
  `employee_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_employee_user_permissions`
--

CREATE TABLE `superadmin_employee_user_permissions` (
  `id` bigint(20) NOT NULL,
  `employee_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_invoice`
--

CREATE TABLE `superadmin_invoice` (
  `id` bigint(20) NOT NULL,
  `invoice_date` date NOT NULL,
  `sent_to_client` tinyint(1) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `tax_percentage` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_invoice`
--

INSERT INTO `superadmin_invoice` (`id`, `invoice_date`, `sent_to_client`, `client_id`, `payment_status`, `tax_percentage`) VALUES
(119, '2023-06-09', 0, 78, 'paid', 10.00),
(131, '2020-07-30', 0, 73, 'paid', 10.00),
(132, '2020-05-20', 0, 12, 'unpaid', 10.00),
(133, '2024-01-30', 0, 75, 'paid', 0.00),
(134, '2024-02-29', 0, 74, 'paid', 0.00),
(135, '2024-06-30', 0, 12, 'paid', 0.00),
(136, '2024-11-30', 0, 12, 'paid', 0.00),
(137, '2023-10-09', 0, 84, 'unpaid', 10.00),
(138, '2024-07-30', 0, 12, 'unpaid', 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_invoiceitem`
--

CREATE TABLE `superadmin_invoiceitem` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `invoice_id` bigint(20) NOT NULL,
  `rate` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_invoiceitem`
--

INSERT INTO `superadmin_invoiceitem` (`id`, `title`, `invoice_id`, `rate`) VALUES
(227, 'Earum et illo praese', 131, 25.00),
(228, 'Ab nemo nisi et anim', 131, 50.00),
(229, 'Culpa necessitatibu', 131, 5000.00),
(235, 'test1', 133, 1000.00),
(236, 'dddd', 133, 32000.00),
(237, 'www', 134, 1500.00),
(238, 'ggg', 134, 50000.00),
(239, 'Ea quibusdam ut ut q', 119, 100.00),
(240, 'swss', 119, 30000.00),
(242, 'ss', 135, 30000.00),
(243, 'ddddd', 136, 10000.00),
(244, 'asd', 137, 1200.00),
(245, 'fgh', 138, 2300.00),
(246, 'Aut ab fugiat ratio', 132, 6200.00);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_lead`
--

CREATE TABLE `superadmin_lead` (
  `id` bigint(20) NOT NULL,
  `project_name` varchar(50) NOT NULL,
  `company` varchar(100) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `project_type` varchar(50) NOT NULL,
  `location` varchar(2) NOT NULL,
  `description` longtext DEFAULT NULL,
  `Timeline` date NOT NULL,
  `budget` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_lead`
--

INSERT INTO `superadmin_lead` (`id`, `project_name`, `company`, `email`, `phone`, `project_type`, `location`, `description`, `Timeline`, `budget`) VALUES
(40, 'Zahir Yang new', 'Rogers and Parker Inc', 'kajuz@mailinator.com', '243242433', 'Tech', 'CO', 'Distinctio Ab velit', '1998-12-11', '3232'),
(41, 'Irma Collins', 'Little and Lee Traders', 'gehahomifa@mailinator.com', '8484515', 'Finance', 'MS', 'Placeat tempora aut', '1999-09-15', '1200'),
(42, 'Ila Wilkins', 'Haley and Leach Plc', 'duzixa@mailinator.com', '15166516', 'Tech', 'BD', 'Sed et totam magnam', '1990-11-07', '1200'),
(45, 'Wanda Frazier', 'Brooks Kelley Plc', 'zocoh@mailinator.com', '+1 (201) 209-5582', 'Healthcare', 'CF', 'Aute sunt voluptate', '2027-05-01', '1200'),
(46, 'Nelle Wynn', 'Olsen and Bush LLC', 'jujedyhat@mailinator.com', '+1 (993) 459-2395', 'Tech', 'HN', 'Excepturi accusantiu', '2024-10-10', '7800');

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_leadfile`
--

CREATE TABLE `superadmin_leadfile` (
  `id` bigint(20) NOT NULL,
  `file` varchar(100) NOT NULL,
  `lead_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_leadfile`
--

INSERT INTO `superadmin_leadfile` (`id`, `file`, `lead_id`) VALUES
(22, 'lead_files/WhatsApp_Image_2024-03-24_at_7.01.24_PM_GNRlXRy.jpeg', 40),
(23, 'lead_files/WhatsApp_Image_2024-07-24_at_10.20.18_AM.jpeg', 42),
(24, 'lead_files/Paraj-1_1.pdf', 42);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_leaveadmin`
--

CREATE TABLE `superadmin_leaveadmin` (
  `leave_id` bigint(20) NOT NULL,
  `admin_notes` longtext NOT NULL,
  `approved_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_leaveadmin`
--

INSERT INTO `superadmin_leaveadmin` (`leave_id`, `admin_notes`, `approved_at`) VALUES
(26, '', '2024-07-22 14:47:17.465045');

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_project`
--

CREATE TABLE `superadmin_project` (
  `id` int(11) NOT NULL,
  `project_title` varchar(60) NOT NULL,
  `priority` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `deadline` date NOT NULL,
  `project_cost` decimal(10,2) NOT NULL,
  `project_files` varchar(100) DEFAULT NULL,
  `client_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_project`
--

INSERT INTO `superadmin_project` (`id`, `project_title`, `priority`, `status`, `start_date`, `deadline`, `project_cost`, `project_files`, `client_id`) VALUES
(137, 'atque labore', 'medium', 'Completed', '2008-09-17', '2004-04-22', 39.00, '', 12),
(138, 'my project', 'low', 'inprogress', '1972-04-08', '1991-03-19', 49.00, '', 71),
(139, 'Enim id tota', 'high', 'Completed', '2016-08-23', '1996-05-25', 8.00, '', 71),
(140, 'abore', 'low', 'inprogress', '2020-05-24', '2005-09-18', 98.00, '', 1),
(142, 'iat qui vel2', 'high', 'Completed', '2003-02-07', '1987-12-15', 68.00, '', 1),
(143, 'Labore labore', 'low', 'Completed', '1987-09-05', '1979-06-18', 99.00, '', 12),
(151, 'sit aut dolore dolores', 'low', 'inprogress', '2024-07-31', '2024-12-31', 93.00, '', 84);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_projectfile`
--

CREATE TABLE `superadmin_projectfile` (
  `id` bigint(20) NOT NULL,
  `file` varchar(100) NOT NULL,
  `project_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_projectfile`
--

INSERT INTO `superadmin_projectfile` (`id`, `file`, `project_id`) VALUES
(43, 'project_files/file_TOFhbQY.jpg', 140),
(47, 'project_files/2_OHStxVX.png', 151),
(54, 'project_files/Paraj-1_Ly6kwpU.pdf', 151),
(55, 'project_files/Paraj-1_1_OvT66eq.pdf', 151);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_project_employees`
--

CREATE TABLE `superadmin_project_employees` (
  `id` bigint(20) NOT NULL,
  `project_id` int(11) NOT NULL,
  `employee_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_project_employees`
--

INSERT INTO `superadmin_project_employees` (`id`, `project_id`, `employee_id`) VALUES
(230, 137, 6),
(229, 137, 10),
(231, 137, 14),
(233, 138, 2),
(232, 138, 25),
(234, 139, 2),
(236, 140, 2),
(237, 140, 6),
(238, 140, 22),
(235, 140, 25),
(240, 142, 8),
(242, 143, 22),
(241, 143, 25),
(254, 151, 2),
(255, 151, 6);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_salaryslip`
--

CREATE TABLE `superadmin_salaryslip` (
  `id` bigint(20) NOT NULL,
  `month` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `professional_tax` decimal(10,2) NOT NULL,
  `TDS` decimal(10,2) NOT NULL,
  `leave_deduction` decimal(10,2) NOT NULL,
  `employee_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_salaryslip`
--

INSERT INTO `superadmin_salaryslip` (`id`, `month`, `year`, `professional_tax`, `TDS`, `leave_deduction`, `employee_id`) VALUES
(20, 11, 2001, 17.00, 80.00, 98.00, 37),
(27, 10, 2011, 2.00, 2.00, 2000.00, 38),
(28, 2, 2022, 3.00, 3.00, 1000.00, 38),
(29, 5, 2024, 4.00, 4.00, 8500.00, 38),
(30, 1, 2020, 10.00, 10.00, 10.00, 36),
(31, 1, 2024, 0.00, 0.00, 0.00, 33),
(32, 6, 2024, 0.00, 0.00, 0.00, 25),
(33, 2, 2024, 0.00, 0.00, 0.00, 22),
(34, 11, 2024, 0.00, 0.00, 0.00, 20);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_superadmin`
--

CREATE TABLE `superadmin_superadmin` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `IFSC_CODE` varchar(100) DEFAULT NULL,
  `SWIFT_CODE` varchar(100) DEFAULT NULL,
  `bank` varchar(100) DEFAULT NULL,
  `bank_no` int(11) DEFAULT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_superadmin`
--

INSERT INTO `superadmin_superadmin` (`id`, `email`, `password`, `IFSC_CODE`, `SWIFT_CODE`, `bank`, `bank_no`, `company_name`, `logo`, `website`, `is_active`, `is_staff`, `is_superuser`, `last_login`, `address`) VALUES
(11, 'bhatasanaparaj@gmail.com', 'pbkdf2_sha256$720000$yb38spb5xL3HiFJdCwq0ev$zgUGBa0XYi1N9W9a7H/WqDKB3Xb9emCuH2arGnYfdOA=', 'H32JHJ07CD', 'HKJKIE43223RW', 'SBI BANK', 83287427, 'Coder Scotch Technologies', 'logo/download.png', 'https://www.wajipisezedy.us', 1, 1, 1, '2024-07-31 05:58:11.371786', 'A1217,Titanium Business Park, Corporate Rd, Prahlad Nagar, Ahmedabad, Gujarat 380051');

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_superadmin_groups`
--

CREATE TABLE `superadmin_superadmin_groups` (
  `id` bigint(20) NOT NULL,
  `superadmin_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_superadmin_user_permissions`
--

CREATE TABLE `superadmin_superadmin_user_permissions` (
  `id` bigint(20) NOT NULL,
  `superadmin_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_task`
--

CREATE TABLE `superadmin_task` (
  `id` bigint(20) NOT NULL,
  `title` varchar(60) NOT NULL,
  `description` longtext NOT NULL,
  `due_date` date NOT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `priority` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `employee_id` bigint(20) NOT NULL,
  `project_id` int(11) NOT NULL,
  `board_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `superadmin_task`
--

INSERT INTO `superadmin_task` (`id`, `title`, `description`, `due_date`, `attachment`, `priority`, `status`, `employee_id`, `project_id`, `board_id`) VALUES
(100, 'Distinctio In quos modi qui cupida', 'Illum et placeat o', '2007-12-18', '', 'medium', 'inprogress', 2, 138, 13),
(101, 'Qui labore nemo neque anim optio', 'Incidunt proident', '2024-05-19', '', 'high', 'todo', 6, 138, 15),
(102, 'Facere iure debitis omn', 'Molestias aliquid fu', '2022-02-12', '', 'high', 'unassigned', 13, 137, 13),
(103, 'Voluptas sint maxime t', 'Ipsum blanditiis vol', '2015-11-20', '', 'high', 'inreview', 2, 139, 14),
(105, 'Architecto itaque', 'Sit tempore dicta', '2012-11-06', '', 'low', 'inprogress', 2, 138, 14),
(106, 'oluptas qui tenetur et in fugit', 'Voluptatum similique', '2010-04-16', '', 'high', 'todo', 2, 140, 15),
(107, 'Odio est non facere fugit quaerat', 'Aut amet magnam eni', '1995-08-18', '', 'high', 'inreview', 22, 137, 14),
(108, 'quidem nostrud itaque qui', 'Explicabo Saepe per', '1982-12-09', '', 'medium', 'inprogress', 19, 140, 10),
(110, 'Proident nostru', 'Voluptas commodi par', '2008-07-18', '', 'low', 'completed', 33, 138, 13),
(111, 'ntium nx velit eum at beatae', 'Cupidatat et fuga I', '2003-01-08', '', 'medium', 'completed', 6, 140, 10),
(114, 'Consequat Aut sunt minima ducimus quia voluptatem beatae q', 'Necessitatibus venia', '1997-09-16', '', 'high', 'inprogress', 2, 138, 14),
(115, 'Eu modi et tempor quas unde', 'Nisi quo molestias s', '1997-05-13', '', 'medium', 'completed', 22, 138, 10),
(116, 'Asperiores culpa enim officia in qui', 'Totam qui omnis iust', '2015-04-10', '', 'low', 'inprogress', 1, 138, 10),
(118, 'Unde proident dolores non molestias quia rerum qui', 'Qui magni consequatu', '1991-07-10', '', 'medium', 'completed', 2, 137, 10),
(119, 'Unde proident dolores non molestias quia rerum qui', 'Qui magni consequatu', '1991-07-10', '', 'medium', 'completed', 2, 137, 10),
(120, 'Unde proident dolores non molestias quia rerum qui', 'Qui magni consequatu', '1991-07-10', '', 'medium', 'completed', 2, 137, 10);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin_taskfile`
--

CREATE TABLE `superadmin_taskfile` (
  `id` bigint(20) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `task_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_superadmin_employee_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employee_leave`
--
ALTER TABLE `employee_leave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_leave_employee_id_60d928f8_fk_superadmin_employee_id` (`employee_id`);

--
-- Indexes for table `superadmin_board`
--
ALTER TABLE `superadmin_board`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `superadmin_changerequest`
--
ALTER TABLE `superadmin_changerequest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_changerequest_project_id_20bd620f_fk` (`project_id`);

--
-- Indexes for table `superadmin_client`
--
ALTER TABLE `superadmin_client`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `superadmin_clientimage`
--
ALTER TABLE `superadmin_clientimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_clientima_client_id_025bb3fd_fk_superadmi` (`client_id`);

--
-- Indexes for table `superadmin_employee`
--
ALTER TABLE `superadmin_employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `superadmin_employeeimage`
--
ALTER TABLE `superadmin_employeeimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_employeei_employee_id_93b4e0fa_fk_superadmi` (`employee_id`);

--
-- Indexes for table `superadmin_employee_groups`
--
ALTER TABLE `superadmin_employee_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `superadmin_employee_groups_employee_id_group_id_c808c824_uniq` (`employee_id`,`group_id`),
  ADD KEY `superadmin_employee_groups_group_id_703f5853_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `superadmin_employee_user_permissions`
--
ALTER TABLE `superadmin_employee_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `superadmin_employee_user_employee_id_permission_i_3fa6e723_uniq` (`employee_id`,`permission_id`),
  ADD KEY `superadmin_employee__permission_id_923133bd_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `superadmin_invoice`
--
ALTER TABLE `superadmin_invoice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_invoice_client_id_ee929d2e_fk_superadmin_client_id` (`client_id`);

--
-- Indexes for table `superadmin_invoiceitem`
--
ALTER TABLE `superadmin_invoiceitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_invoiceit_invoice_id_e82ab1ef_fk_superadmi` (`invoice_id`);

--
-- Indexes for table `superadmin_lead`
--
ALTER TABLE `superadmin_lead`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `superadmin_leadfile`
--
ALTER TABLE `superadmin_leadfile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_leadfile_lead_id_ac5d9114_fk_superadmin_lead_id` (`lead_id`);

--
-- Indexes for table `superadmin_leaveadmin`
--
ALTER TABLE `superadmin_leaveadmin`
  ADD PRIMARY KEY (`leave_id`);

--
-- Indexes for table `superadmin_project`
--
ALTER TABLE `superadmin_project`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_project_client_id_25bf6d20_fk_superadmin_client_id` (`client_id`);

--
-- Indexes for table `superadmin_projectfile`
--
ALTER TABLE `superadmin_projectfile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_projectfi_project_id_6cf5fbb1_fk_superadmi` (`project_id`);

--
-- Indexes for table `superadmin_project_employees`
--
ALTER TABLE `superadmin_project_employees`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `superadmin_project_emplo_project_id_employee_id_5d0b985f_uniq` (`project_id`,`employee_id`),
  ADD KEY `superadmin_project_e_employee_id_cfe01db7_fk_superadmi` (`employee_id`);

--
-- Indexes for table `superadmin_salaryslip`
--
ALTER TABLE `superadmin_salaryslip`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_salarysli_employee_id_6d096ae3_fk_superadmi` (`employee_id`);

--
-- Indexes for table `superadmin_superadmin`
--
ALTER TABLE `superadmin_superadmin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `superadmin_superadmin_email_7121ca0f_uniq` (`email`);

--
-- Indexes for table `superadmin_superadmin_groups`
--
ALTER TABLE `superadmin_superadmin_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `superadmin_superadmin_gr_superadmin_id_group_id_68cd21df_uniq` (`superadmin_id`,`group_id`),
  ADD KEY `superadmin_superadmin_groups_group_id_a29fe961_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `superadmin_superadmin_user_permissions`
--
ALTER TABLE `superadmin_superadmin_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `superadmin_superadmin_us_superadmin_id_permission_c479f527_uniq` (`superadmin_id`,`permission_id`),
  ADD KEY `superadmin_superadmi_permission_id_a4a0ba3a_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `superadmin_task`
--
ALTER TABLE `superadmin_task`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_task_project_id_833589f9_fk_superadmin_project_id` (`project_id`),
  ADD KEY `superadmin_task_board_id_719e8229_fk_superadmin_board_id` (`board_id`),
  ADD KEY `superadmin_task_employee_id_c7e7e93d_fk_superadmin_employee_id` (`employee_id`);

--
-- Indexes for table `superadmin_taskfile`
--
ALTER TABLE `superadmin_taskfile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superadmin_taskfile_task_id_6779eb52_fk_superadmin_task_id` (`task_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `employee_leave`
--
ALTER TABLE `employee_leave`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `superadmin_board`
--
ALTER TABLE `superadmin_board`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `superadmin_changerequest`
--
ALTER TABLE `superadmin_changerequest`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `superadmin_client`
--
ALTER TABLE `superadmin_client`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `superadmin_clientimage`
--
ALTER TABLE `superadmin_clientimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `superadmin_employee`
--
ALTER TABLE `superadmin_employee`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `superadmin_employeeimage`
--
ALTER TABLE `superadmin_employeeimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `superadmin_employee_groups`
--
ALTER TABLE `superadmin_employee_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `superadmin_employee_user_permissions`
--
ALTER TABLE `superadmin_employee_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `superadmin_invoice`
--
ALTER TABLE `superadmin_invoice`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=139;

--
-- AUTO_INCREMENT for table `superadmin_invoiceitem`
--
ALTER TABLE `superadmin_invoiceitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;

--
-- AUTO_INCREMENT for table `superadmin_lead`
--
ALTER TABLE `superadmin_lead`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `superadmin_leadfile`
--
ALTER TABLE `superadmin_leadfile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `superadmin_project`
--
ALTER TABLE `superadmin_project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;

--
-- AUTO_INCREMENT for table `superadmin_projectfile`
--
ALTER TABLE `superadmin_projectfile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `superadmin_project_employees`
--
ALTER TABLE `superadmin_project_employees`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=262;

--
-- AUTO_INCREMENT for table `superadmin_salaryslip`
--
ALTER TABLE `superadmin_salaryslip`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `superadmin_superadmin`
--
ALTER TABLE `superadmin_superadmin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `superadmin_superadmin_groups`
--
ALTER TABLE `superadmin_superadmin_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `superadmin_superadmin_user_permissions`
--
ALTER TABLE `superadmin_superadmin_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `superadmin_task`
--
ALTER TABLE `superadmin_task`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT for table `superadmin_taskfile`
--
ALTER TABLE `superadmin_taskfile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_superadmin_employee_id` FOREIGN KEY (`user_id`) REFERENCES `superadmin_employee` (`id`);

--
-- Constraints for table `employee_leave`
--
ALTER TABLE `employee_leave`
  ADD CONSTRAINT `employee_leave_employee_id_60d928f8_fk_superadmin_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`);

--
-- Constraints for table `superadmin_changerequest`
--
ALTER TABLE `superadmin_changerequest`
  ADD CONSTRAINT `superadmin_changerequest_project_id_20bd620f_fk` FOREIGN KEY (`project_id`) REFERENCES `superadmin_project` (`id`);

--
-- Constraints for table `superadmin_clientimage`
--
ALTER TABLE `superadmin_clientimage`
  ADD CONSTRAINT `superadmin_clientima_client_id_025bb3fd_fk_superadmi` FOREIGN KEY (`client_id`) REFERENCES `superadmin_client` (`id`);

--
-- Constraints for table `superadmin_employeeimage`
--
ALTER TABLE `superadmin_employeeimage`
  ADD CONSTRAINT `superadmin_employeei_employee_id_93b4e0fa_fk_superadmi` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`);

--
-- Constraints for table `superadmin_employee_groups`
--
ALTER TABLE `superadmin_employee_groups`
  ADD CONSTRAINT `superadmin_employee__employee_id_c2c5ea3a_fk_superadmi` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`),
  ADD CONSTRAINT `superadmin_employee_groups_group_id_703f5853_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `superadmin_employee_user_permissions`
--
ALTER TABLE `superadmin_employee_user_permissions`
  ADD CONSTRAINT `superadmin_employee__employee_id_d2a21882_fk_superadmi` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`),
  ADD CONSTRAINT `superadmin_employee__permission_id_923133bd_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `superadmin_invoice`
--
ALTER TABLE `superadmin_invoice`
  ADD CONSTRAINT `superadmin_invoice_client_id_ee929d2e_fk_superadmin_client_id` FOREIGN KEY (`client_id`) REFERENCES `superadmin_client` (`id`);

--
-- Constraints for table `superadmin_invoiceitem`
--
ALTER TABLE `superadmin_invoiceitem`
  ADD CONSTRAINT `superadmin_invoiceit_invoice_id_e82ab1ef_fk_superadmi` FOREIGN KEY (`invoice_id`) REFERENCES `superadmin_invoice` (`id`);

--
-- Constraints for table `superadmin_leadfile`
--
ALTER TABLE `superadmin_leadfile`
  ADD CONSTRAINT `superadmin_leadfile_lead_id_ac5d9114_fk_superadmin_lead_id` FOREIGN KEY (`lead_id`) REFERENCES `superadmin_lead` (`id`);

--
-- Constraints for table `superadmin_leaveadmin`
--
ALTER TABLE `superadmin_leaveadmin`
  ADD CONSTRAINT `superadmin_leaveadmin_leave_id_22cd0525_fk_employee_leave_id` FOREIGN KEY (`leave_id`) REFERENCES `employee_leave` (`id`);

--
-- Constraints for table `superadmin_project`
--
ALTER TABLE `superadmin_project`
  ADD CONSTRAINT `superadmin_project_client_id_25bf6d20_fk_superadmin_client_id` FOREIGN KEY (`client_id`) REFERENCES `superadmin_client` (`id`);

--
-- Constraints for table `superadmin_projectfile`
--
ALTER TABLE `superadmin_projectfile`
  ADD CONSTRAINT `superadmin_projectfi_project_id_6cf5fbb1_fk_superadmi` FOREIGN KEY (`project_id`) REFERENCES `superadmin_project` (`id`);

--
-- Constraints for table `superadmin_project_employees`
--
ALTER TABLE `superadmin_project_employees`
  ADD CONSTRAINT `superadmin_project_e_employee_id_cfe01db7_fk_superadmi` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`),
  ADD CONSTRAINT `superadmin_project_employees_project_id_05b17a0e_fk` FOREIGN KEY (`project_id`) REFERENCES `superadmin_project` (`id`);

--
-- Constraints for table `superadmin_salaryslip`
--
ALTER TABLE `superadmin_salaryslip`
  ADD CONSTRAINT `superadmin_salarysli_employee_id_6d096ae3_fk_superadmi` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`);

--
-- Constraints for table `superadmin_superadmin_groups`
--
ALTER TABLE `superadmin_superadmin_groups`
  ADD CONSTRAINT `superadmin_superadmi_superadmin_id_2cb5f237_fk_superadmi` FOREIGN KEY (`superadmin_id`) REFERENCES `superadmin_superadmin` (`id`),
  ADD CONSTRAINT `superadmin_superadmin_groups_group_id_a29fe961_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `superadmin_superadmin_user_permissions`
--
ALTER TABLE `superadmin_superadmin_user_permissions`
  ADD CONSTRAINT `superadmin_superadmi_permission_id_a4a0ba3a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `superadmin_superadmi_superadmin_id_200bdc5b_fk_superadmi` FOREIGN KEY (`superadmin_id`) REFERENCES `superadmin_superadmin` (`id`);

--
-- Constraints for table `superadmin_task`
--
ALTER TABLE `superadmin_task`
  ADD CONSTRAINT `superadmin_task_board_id_719e8229_fk_superadmin_board_id` FOREIGN KEY (`board_id`) REFERENCES `superadmin_board` (`id`),
  ADD CONSTRAINT `superadmin_task_employee_id_c7e7e93d_fk_superadmin_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `superadmin_employee` (`id`),
  ADD CONSTRAINT `superadmin_task_project_id_833589f9_fk_superadmin_project_id` FOREIGN KEY (`project_id`) REFERENCES `superadmin_project` (`id`);

--
-- Constraints for table `superadmin_taskfile`
--
ALTER TABLE `superadmin_taskfile`
  ADD CONSTRAINT `superadmin_taskfile_task_id_6779eb52_fk_superadmin_task_id` FOREIGN KEY (`task_id`) REFERENCES `superadmin_task` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
