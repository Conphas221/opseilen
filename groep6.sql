CREATE TABLE `scores` (
	`name` VARCHAR(64) NOT NULL DEFAULT 'UnnamedPlayer',
	`wins` INT(11) NOT NULL DEFAULT '0',
	`loses` INT(11) NULL DEFAULT '0',
	PRIMARY KEY (`name`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;
