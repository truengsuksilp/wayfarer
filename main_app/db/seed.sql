-- PSQL 

-- Delete tables
DELETE FROM main_app_posts;
DELETE FROM main_app_city;
DELETE FROM main_app_profile;

-- IMPORT CSV command examples

COPY main_app_profile FROM '/Users/truengsuksilp/sei/projects/project_wayfarer/main_app/db/seed_profiles.csv' DELIMITER ',' CSV HEADER;

COPY main_app_city FROM '/Users/truengsuksilp/sei/projects/project_wayfarer/main_app/db/seed_cities.csv' DELIMITER ',' CSV HEADER;

COPY main_app_post FROM '/Users/truengsuksilp/sei/projects/project_wayfarer/main_app/db/seed_posts.csv' DELIMITER ',' CSV HEADER;