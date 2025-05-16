import mysql.connector

def deploy_change():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='testdb'
    )
    cursor = conn.cursor()

    # Add a new table
    sql = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        role VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    try:
        cursor.execute(sql)
        conn.commit()
        print("Database change deployed successfully.")
    except Exception as e:
        print("Error during deployment:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    deploy_change()
