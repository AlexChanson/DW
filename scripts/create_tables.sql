CREATE TABLE `chart_entry` (
	`streams` INT UNSIGNED NOT NULL,
	`country_id` varchar(7) NOT NULL,
	`track_id` CHAR(22) NOT NULL,
	`week_id` INT UNSIGNED NOT NULL,
	`entryNb` TINYINT UNSIGNED NOT NULL DEFAULT '1',
	`rank` SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (`country_id`, `track_id`, `week_id`)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `track` (
	`track_id` CHAR(22) NOT NULL,
	`album` VARCHAR(255) NOT NULL,
	`title` VARCHAR(255) NOT NULL,
	`genre` VARCHAR(127) NOT NULL,
	`release_year` DATE NOT NULL,
	PRIMARY KEY (`track_id`)
)
ENGINE=InnoDB
;

CREATE TABLE `artist` (
	`artist_id` CHAR(22) NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`followers` INT(10) UNSIGNED NOT NULL,
	`genre` VARCHAR(127) NOT NULL,
	`country_id` SMALLINT(5) UNSIGNED NOT NULL,
	PRIMARY KEY (`artist_id`)
)
ENGINE=InnoDB
;

CREATE TABLE `plays` (
	`artist_id` CHAR(22) NOT NULL,
	`track_id` CHAR(22) NOT NULL,
	PRIMARY KEY (`artist_id`, `track_id`)
)
ENGINE=InnoDB
;

CREATE TABLE `country` (
	`country_id` varchar(7) NOT NULL,
	`name` VARCHAR(64) NOT NULL,
	`region` VARCHAR(64) NOT NULL,
	PRIMARY KEY (`country_id`)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `week` (
	`week_id` INT(10) UNSIGNED NOT NULL,
	`start_day` DATE NOT NULL,
	`month` TINYINT(3) UNSIGNED NOT NULL,
	`decade` SMALLINT(5) UNSIGNED NOT NULL,
	`year` YEAR NOT NULL,
	PRIMARY KEY (`week_id`)
)
ENGINE=InnoDB
;

CREATE TABLE `song_feature` (
	`track_id` CHAR(22) NOT NULL,
	`danceability` FLOAT NOT NULL,
	`length_ms` INT(10) UNSIGNED NOT NULL,
	`tempo` FLOAT NOT NULL,
	PRIMARY KEY (`track_id`)
)
ENGINE=InnoDB
;

