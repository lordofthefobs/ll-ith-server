CREATE TABLE history (
     id BIGINT NOT NULL AUTO_INCREMENT,
     device_id BIGINT NOT NULL,
     startTime DATETIME default NULL,
     endTime DATETIME default NULL,
     PRIMARY KEY (id)
);