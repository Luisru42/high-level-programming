# 🎬 SQL Data Operations: Users, Genres & Geography

This repository contains a curated set of SQL scripts designed to explore user management, genre classification, and geographic data analysis. Each file targets a specific operation, making it ideal for practicing relational queries, joins, subqueries, and constraints.

## 📁 File Breakdown

### 🔐 User & Privilege Management
- `0-privileges.sql` — Grant or inspect user privileges
- `1-create_user.sql` — Create a new database user
- `2-create_read_user.sql` — Create a user with read-only access

### 🎭 Genre & Show Analysis
- `2-genre_id_by_show.sql` — Retrieve genre ID for a specific show
- `11-genre_id_all_shows.sql` — List genre IDs for all shows
- `12-no_genre.sql` — Identify shows without assigned genres
- `13-count_shows_by_genre.sql` — Count shows grouped by genre
- `14-my_genres.sql` — List genres associated with a specific user or show
- `15-comedy_only.sql` — Filter shows that are strictly comedies
- `16-shows_by_genre.sql` — Join shows with their genre metadata
- `101-not_a_comedy.sql` — Exclude comedy shows from results

### 🧩 Data Integrity & Constraints
- `3-force_name.sql` — Enforce non-null names in table entries
- `4-never_empty.sql` — Prevent empty values in critical fields
- `5-unique_id.sql` — Ensure unique identifiers across records

### 🗺️ Geographic Data Queries
- `6-states.sql` — List all states in the dataset
- `7-cities.sql` — List all cities
- `8-cities_of_california_subquery.sql` — Use subquery to find California cities
- `9-cities_by_state_join.sql` — Join cities with their respective states

## 🚀 How to Use

Run each script individually using your SQL client or automate them via CLI:

```bash
mysql -u your_user -p < 13-count_shows_by_genre.sql