USE [master]
GO
/****** Object:  Database [WAREHOUSE]    Script Date: 5/29/2025 14:51:22 ******/
CREATE DATABASE [WAREHOUSE]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'WAREHOUSE', FILENAME = N'D:\Application\SQL server 2022\SQL2022\MSSQL16.SQLEXPRESS\MSSQL\DATA\WAREHOUSE.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'WAREHOUSE_log', FILENAME = N'D:\Application\SQL server 2022\SQL2022\MSSQL16.SQLEXPRESS\MSSQL\DATA\WAREHOUSE_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [WAREHOUSE] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [WAREHOUSE].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [WAREHOUSE] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [WAREHOUSE] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [WAREHOUSE] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [WAREHOUSE] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [WAREHOUSE] SET ARITHABORT OFF 
GO
ALTER DATABASE [WAREHOUSE] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [WAREHOUSE] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [WAREHOUSE] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [WAREHOUSE] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [WAREHOUSE] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [WAREHOUSE] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [WAREHOUSE] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [WAREHOUSE] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [WAREHOUSE] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [WAREHOUSE] SET  ENABLE_BROKER 
GO
ALTER DATABASE [WAREHOUSE] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [WAREHOUSE] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [WAREHOUSE] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [WAREHOUSE] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [WAREHOUSE] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [WAREHOUSE] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [WAREHOUSE] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [WAREHOUSE] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [WAREHOUSE] SET  MULTI_USER 
GO
ALTER DATABASE [WAREHOUSE] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [WAREHOUSE] SET DB_CHAINING OFF 
GO
ALTER DATABASE [WAREHOUSE] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [WAREHOUSE] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [WAREHOUSE] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [WAREHOUSE] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [WAREHOUSE] SET QUERY_STORE = ON
GO
ALTER DATABASE [WAREHOUSE] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [WAREHOUSE]
GO
/****** Object:  Table [dbo].[account]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[account](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](50) NOT NULL,
	[fullname] [nvarchar](255) NULL,
	[password] [nvarchar](255) NOT NULL,
	[role_id] [int] NULL,
	[created_at] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[category]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[category](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[created_at] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[inventory]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[inventory](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[product_id] [int] NULL,
	[quantity] [int] NOT NULL,
	[updated_at] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[order]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[order](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[partner_id] [int] NULL,
	[type] [bit] NOT NULL,
	[status] [int] NOT NULL,
	[order_date] [datetime] NULL,
	[staff_id] [int] NULL,
	[total_cost] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[order_item]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[order_item](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[order_id] [int] NULL,
	[product_id] [int] NULL,
	[unit] [nvarchar](10) NOT NULL,
	[quantity] [int] NOT NULL,
	[unit_cost] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[partner]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[partner](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[description] [nvarchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[product]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[product](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[category_id] [int] NULL,
	[created_at] [datetime] NULL,
	[unit] [nvarchar](10) NOT NULL,
	[export_cost] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[role]    Script Date: 5/29/2025 14:51:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[role](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[account] ON 

INSERT [dbo].[account] ([id], [username], [fullname], [password], [role_id], [created_at]) VALUES (1, N'admin', N'admin', N'1234', 1, CAST(N'2025-05-24T15:25:27.113' AS DateTime))
INSERT [dbo].[account] ([id], [username], [fullname], [password], [role_id], [created_at]) VALUES (2, N'trungnd', N'Nguyễn Đức Trung', N'1234', 2, CAST(N'2025-05-25T21:00:42.350' AS DateTime))
SET IDENTITY_INSERT [dbo].[account] OFF
GO
SET IDENTITY_INSERT [dbo].[category] ON 

INSERT [dbo].[category] ([id], [name], [created_at]) VALUES (10, N'đồ uống', CAST(N'2025-05-28T09:57:08.470' AS DateTime))
INSERT [dbo].[category] ([id], [name], [created_at]) VALUES (11, N'thực phẩm khô', CAST(N'2025-05-28T09:57:19.797' AS DateTime))
INSERT [dbo].[category] ([id], [name], [created_at]) VALUES (12, N'văn phòng phẩm', CAST(N'2025-05-28T09:58:02.360' AS DateTime))
INSERT [dbo].[category] ([id], [name], [created_at]) VALUES (13, N'điện lạnh', CAST(N'2025-05-28T09:59:13.017' AS DateTime))
INSERT [dbo].[category] ([id], [name], [created_at]) VALUES (14, N'vật liệu xây dựng', CAST(N'2025-05-28T09:59:33.503' AS DateTime))
SET IDENTITY_INSERT [dbo].[category] OFF
GO
SET IDENTITY_INSERT [dbo].[inventory] ON 

INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (4, 13, 130, CAST(N'2025-05-28T11:47:44.607' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (5, 14, 238, CAST(N'2025-05-28T10:29:12.970' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (6, 15, 468, CAST(N'2025-05-28T10:30:21.447' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (7, 16, 120, CAST(N'2025-05-28T10:30:41.097' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (8, 17, 50, CAST(N'2025-05-28T10:32:38.567' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (9, 18, 110, CAST(N'2025-05-29T11:08:39.687' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (10, 19, 34, CAST(N'2025-05-28T10:35:57.780' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (11, 20, 563, CAST(N'2025-05-28T10:36:30.910' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (12, 21, 293, CAST(N'2025-05-28T10:37:32.487' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (13, 22, 49, CAST(N'2025-05-28T10:38:13.773' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (14, 23, 23, CAST(N'2025-05-28T11:47:44.610' AS DateTime))
INSERT [dbo].[inventory] ([id], [product_id], [quantity], [updated_at]) VALUES (15, 24, 123, CAST(N'2025-05-28T10:40:01.053' AS DateTime))
SET IDENTITY_INSERT [dbo].[inventory] OFF
GO
SET IDENTITY_INSERT [dbo].[order] ON 

INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (2, 1, 0, 0, CAST(N'2025-05-28T11:12:07.743' AS DateTime), 2, 279900000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (3, 3, 0, 0, CAST(N'2025-05-28T11:25:36.090' AS DateTime), 2, 784420000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (4, 1, 0, 2, CAST(N'2025-05-28T11:26:33.483' AS DateTime), 2, 130000000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (5, 1, 0, 0, CAST(N'2025-05-28T11:28:44.987' AS DateTime), 2, 806000000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (6, 1, 0, 1, CAST(N'2025-05-28T11:30:55.133' AS DateTime), 2, 13000000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (7, 4, 1, 0, CAST(N'2025-05-28T11:32:22.117' AS DateTime), 2, 13300000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (8, 5, 0, 2, CAST(N'2025-05-28T11:41:13.117' AS DateTime), 2, 14650000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (9, 10, 1, 0, CAST(N'2025-05-28T11:42:06.707' AS DateTime), 2, 27220000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (10, 12, 1, 0, CAST(N'2025-05-28T11:43:32.270' AS DateTime), 2, 16200000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (11, 4, 1, 0, CAST(N'2025-05-28T11:47:27.160' AS DateTime), 2, 123000000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (12, 5, 1, 2, CAST(N'2025-05-28T11:48:38.423' AS DateTime), 2, 4080000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (13, 5, 1, 1, CAST(N'2025-04-28T11:49:23.497' AS DateTime), 2, 10350000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (15, 1, 0, 2, CAST(N'2025-05-29T00:35:39.877' AS DateTime), 2, 500000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (16, 3, 0, 0, CAST(N'2025-05-29T11:02:49.993' AS DateTime), 2, 400000)
INSERT [dbo].[order] ([id], [partner_id], [type], [status], [order_date], [staff_id], [total_cost]) VALUES (17, 12, 1, 0, CAST(N'2025-05-29T11:08:21.990' AS DateTime), 2, 9000000)
SET IDENTITY_INSERT [dbo].[order] OFF
GO
SET IDENTITY_INSERT [dbo].[order_item] ON 

INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (2, 2, 13, N'thùng', 200, 130000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (3, 2, 14, N'bao', 250, 230000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (4, 2, 16, N'thùng', 120, 220000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (5, 2, 15, N'thùng', 500, 340000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (6, 3, 17, N'thùng', 50, 160000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (7, 3, 18, N'thùng', 122, 430000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (8, 3, 19, N'hộp', 34, 100000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (9, 3, 20, N'thùng', 563, 580000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (10, 3, 21, N'hộp', 344, 180000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (11, 3, 24, N'thùng', 123, 2700000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (12, 4, 13, N'thùng', 1000, 130000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (13, 5, 23, N'chiếc', 34, 11500000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (14, 5, 22, N'chiếc', 50, 8300000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (15, 6, 13, N'thùng', 100, 130000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (16, 7, 13, N'thùng', 50, 130000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (17, 7, 15, N'thùng', 20, 340000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (18, 8, 18, N'thùng', 5, 430000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (19, 8, 19, N'hộp', 125, 100000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (20, 9, 18, N'thùng', 12, 450000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (21, 9, 15, N'thùng', 12, 360000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (22, 9, 21, N'hộp', 45, 200000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (23, 9, 22, N'chiếc', 1, 8500000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (24, 10, 21, N'hộp', 6, 200000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (25, 10, 23, N'chiếc', 1, 12000000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (26, 10, 14, N'bao', 12, 250000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (27, 11, 13, N'thùng', 20, 150000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (28, 11, 23, N'chiếc', 10, 12000000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (29, 12, 19, N'hộp', 34, 120000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (30, 13, 18, N'thùng', 23, 450000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (32, 15, 13, N'thùng', 10, 500000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (33, 16, 18, N'thùng', 20, 20000)
INSERT [dbo].[order_item] ([id], [order_id], [product_id], [unit], [quantity], [unit_cost]) VALUES (34, 17, 18, N'thùng', 20, 450000)
SET IDENTITY_INSERT [dbo].[order_item] OFF
GO
SET IDENTITY_INSERT [dbo].[partner] ON 

INSERT [dbo].[partner] ([id], [name], [description]) VALUES (1, N'Công ty A', N'')
INSERT [dbo].[partner] ([id], [name], [description]) VALUES (3, N'Công ty B', N'')
INSERT [dbo].[partner] ([id], [name], [description]) VALUES (4, N'Nguyễn Văn C', N'')
INSERT [dbo].[partner] ([id], [name], [description]) VALUES (5, N'Phạm Thị N', N'')
INSERT [dbo].[partner] ([id], [name], [description]) VALUES (10, N'Peter parker', N'')
INSERT [dbo].[partner] ([id], [name], [description]) VALUES (12, N'Lê Thị Z', N'')
SET IDENTITY_INSERT [dbo].[partner] OFF
GO
SET IDENTITY_INSERT [dbo].[product] ON 

INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (13, N'mì tôm hảo hảo chua cay', 11, CAST(N'2025-05-28T10:27:33.000' AS DateTime), N'thùng', 150000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (14, N'gạo XL25', 11, CAST(N'2025-05-28T10:29:12.970' AS DateTime), N'bao', 250000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (15, N'bia lon tiger bạc', 10, CAST(N'2025-05-28T10:30:21.447' AS DateTime), N'thùng', 360000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (16, N'coca cola lon', 10, CAST(N'2025-05-28T10:30:41.097' AS DateTime), N'thùng', 240000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (17, N'trà xanh không độ', 10, CAST(N'2025-05-28T10:32:38.567' AS DateTime), N'thùng', 180000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (18, N'giấy A4', 12, CAST(N'2025-05-28T10:35:36.813' AS DateTime), N'thùng', 450000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (19, N'bút bi thiên long', 12, CAST(N'2025-05-28T10:35:57.780' AS DateTime), N'hộp', 120000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (20, N'tập vở campus', 12, CAST(N'2025-05-28T10:36:30.910' AS DateTime), N'thùng', 600000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (21, N'bút chì màu', 12, CAST(N'2025-05-28T10:37:32.487' AS DateTime), N'hộp', 200000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (22, N'tủ lạnh samsung', 13, CAST(N'2025-05-28T10:38:13.773' AS DateTime), N'chiếc', 8500000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (23, N'điều hòa LG', 13, CAST(N'2025-05-28T10:38:38.040' AS DateTime), N'chiếc', 12000000)
INSERT [dbo].[product] ([id], [name], [category_id], [created_at], [unit], [export_cost]) VALUES (24, N'sơn dulux', 14, CAST(N'2025-05-28T10:40:01.053' AS DateTime), N'thùng', 2800000)
SET IDENTITY_INSERT [dbo].[product] OFF
GO
SET IDENTITY_INSERT [dbo].[role] ON 

INSERT [dbo].[role] ([id], [name]) VALUES (1, N'quản trị viên')
INSERT [dbo].[role] ([id], [name]) VALUES (2, N'nhân viên')
SET IDENTITY_INSERT [dbo].[role] OFF
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__account__F3DBC572DA4D81F8]    Script Date: 5/29/2025 14:51:22 ******/
ALTER TABLE [dbo].[account] ADD UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__category__72E12F1BA0B8E7B4]    Script Date: 5/29/2025 14:51:22 ******/
ALTER TABLE [dbo].[category] ADD UNIQUE NONCLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__inventor__47027DF449FE97CB]    Script Date: 5/29/2025 14:51:22 ******/
ALTER TABLE [dbo].[inventory] ADD UNIQUE NONCLUSTERED 
(
	[product_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[account] ADD  DEFAULT (getdate()) FOR [created_at]
GO
ALTER TABLE [dbo].[category] ADD  DEFAULT (getdate()) FOR [created_at]
GO
ALTER TABLE [dbo].[inventory] ADD  DEFAULT (getdate()) FOR [updated_at]
GO
ALTER TABLE [dbo].[order] ADD  DEFAULT (getdate()) FOR [order_date]
GO
ALTER TABLE [dbo].[product] ADD  DEFAULT (getdate()) FOR [created_at]
GO
ALTER TABLE [dbo].[account]  WITH CHECK ADD FOREIGN KEY([role_id])
REFERENCES [dbo].[role] ([id])
GO
ALTER TABLE [dbo].[inventory]  WITH CHECK ADD FOREIGN KEY([product_id])
REFERENCES [dbo].[product] ([id])
GO
ALTER TABLE [dbo].[order]  WITH CHECK ADD FOREIGN KEY([partner_id])
REFERENCES [dbo].[partner] ([id])
GO
ALTER TABLE [dbo].[order]  WITH CHECK ADD FOREIGN KEY([staff_id])
REFERENCES [dbo].[account] ([id])
GO
ALTER TABLE [dbo].[order_item]  WITH CHECK ADD FOREIGN KEY([order_id])
REFERENCES [dbo].[order] ([id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[order_item]  WITH CHECK ADD FOREIGN KEY([product_id])
REFERENCES [dbo].[product] ([id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[product]  WITH CHECK ADD FOREIGN KEY([category_id])
REFERENCES [dbo].[category] ([id])
GO
ALTER TABLE [dbo].[order]  WITH CHECK ADD CHECK  (([status]>=(0) AND [status]<=(2)))
GO
USE [master]
GO
ALTER DATABASE [WAREHOUSE] SET  READ_WRITE 
GO
