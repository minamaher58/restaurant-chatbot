import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="restaurant-chatbot"
)

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id):
    cursor = cnx.cursor()

    query = f"SELECT status FROM order_tracking WHERE order_id = %s"
    cursor.execute(query, (order_id,))

    result = cursor.fetchone()

    cursor.close()

    if result:
        return result[0]
    else:
        return None
