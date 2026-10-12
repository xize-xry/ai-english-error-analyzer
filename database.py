import os

import pymysql
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    return pymysql.connect(
        host="127.0.0.1",
        port=3366,
        user="root",
        password=os.getenv("MYSQL_PASSWORD") or "",
        database="ai_english",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
        read_timeout=10,
        write_timeout=10,
    )


def save_result(question, student_answer, correct_answer, result, student_id):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO wrong_questions (
                    question, student_answer, correct_answer,
                    error_type, reason, suggestion, student_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                question,
                student_answer,
                correct_answer,
                result["error_type"],
                result["reason"],
                result["suggestion"],
                student_id,
            ))
            record_id = cursor.lastrowid
        connection.commit()
        return record_id
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def get_wrong_questions(student_id, limit=20, error_type=None):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT *
                FROM wrong_questions
                WHERE student_id = %s
            """
            values = [student_id]

            if error_type is not None:
                sql += " AND error_type = %s"
                values.append(error_type)

            sql += " ORDER BY id DESC LIMIT %s"
            values.append(limit)

            cursor.execute(sql, tuple(values))
            return list(cursor.fetchall())
    finally:
        connection.close()


def get_profile(student_id):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT error_type, COUNT(*) AS count
                FROM wrong_questions
                WHERE student_id = %s
                GROUP BY error_type
                ORDER BY count DESC, error_type ASC
            """, (student_id,))
            rows = list(cursor.fetchall())

        total = sum(row["count"] for row in rows)

        for row in rows:
            row["percentage"] = round(row["count"] / total * 100, 1)

        return {
            "student_id": student_id,
            "total_questions": total,
            "error_stats": rows,
        }
    finally:
        connection.close()