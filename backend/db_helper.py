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


# Function to get the next available order_id
def get_next_order_id():
    cursor = cnx.cursor()

    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1
    

# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()
        # Calling the stored procedure
        query = f"Select item_id FROM food_items WHERE LOWER(name) = '{food_item.lower()}';"
        cursor.execute(query)
        item_id = cursor.fetchone()[0]
        # print(order_id, item_id, quantity)
        cursor.callproc('insert_order_item', (order_id, item_id, quantity))
        cnx.commit()
        cursor.close()
        # print("Order item inserted successfully!")
        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        cnx.rollback()
        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return -1
    

def get_total_order_price(order_id):
    cursor = cnx.cursor()
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    cnx.commit()
    cursor.close()