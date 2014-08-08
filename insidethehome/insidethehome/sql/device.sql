CREATE TABLE device (
     id BIGINT NOT NULL AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     mac VARCHAR(255) NOT NULL,
     state VARCHAR(255) default 'INACTIVE',
     startTime DATETIME default NULL,
     PRIMARY KEY (id)
);