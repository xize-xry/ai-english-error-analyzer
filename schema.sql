CREATE DATABASE IF NOT EXISTS ai_english
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE ai_english;

CREATE TABLE IF NOT EXISTS wrong_questions (
    id INT NOT NULL AUTO_INCREMENT,
    question TEXT NOT NULL,
    student_answer VARCHAR(255) NOT NULL,
    correct_answer VARCHAR(255) NOT NULL,
    error_type VARCHAR(255) DEFAULT NULL,
    reason TEXT,
    suggestion TEXT,
    student_id VARCHAR(64) NOT NULL DEFAULT 'legacy',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    INDEX idx_student_id (student_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;