import psycopg2

# Connect to the database
conn = psycopg2.connect(database="chinook")

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Execute a SQL query using the execute() method
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s;', ["Queen"])


# Fetch the results using the fetchall() method
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()