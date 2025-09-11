# 📊 SQL Exercises & Database Operations

This repository contains a structured set of SQL scripts designed to reinforce foundational and intermediate database concepts. Each file targets a specific operation, ranging from basic database listing to more advanced data manipulation and aggregation tasks.

## 🗂 File Overview

| Filename                      | Description                                      |
|------------------------------|--------------------------------------------------|
| 0-list_databases.sql         | List all available databases                     |
| 1-create_database_if_missing.sql | Create a database only if it doesn't exist     |
| 2-remove_database.sql        | Safely remove a specified database               |
| 3-list_tables.sql            | Display all tables within a database             |
| 4-first_table.sql            | Create the first table with basic structure      |
| 5-full_table.sql             | Create a table with full schema and constraints  |
| 6-list_values.sql            | Retrieve all values from a table                 |
| 7-insert_value.sql           | Insert a new record into a table                 |
| 8-count.sql                  | Count records in a table                         |
| 9-full_creation.sql          | Full setup: database, tables, and initial data   |
| 10-top_score.sql             | Query for the highest score                      |
| 11-best_score.sql            | Retrieve the best score per student              |
| 12-no_cheating.sql           | Enforce integrity: exclude cheating cases        |
| 13-change_class.sql          | Update student class assignments                 |
| 14-average.sql               | Calculate average scores                         |
| 15-groups.sql                | Group data by class or category                  |
| 16-no_link.sql               | Identify records without foreign key links       |


## 🧠 Purpose

This collection is ideal for:
- Practicing SQL syntax and logic
- Understanding relational database operations
- Preparing for technical interviews or certifications
- Automating common database tasks

## 🚀 Usage

You can run each script individually using your preferred SQL client or batch them via CLI tools. For example, in MySQL:

```bash
mysql -u username -p < 0-list_databases.sql