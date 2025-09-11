-- List all shows contained in the genre with the id 80.
SELECT tv_show.title, tv_show.genres.genre_id
FROM tv_show, tv_show.genres ON tv_show.id = tv_show.genres.tv_show_id
JOIN tv_show.genres ON tv_show.id = tv_show.genres.tv_show_id
WHERE tv_show.genres.genre_id = 80;