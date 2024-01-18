from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
mysqlConnection = mysql.connector.connect(host="localhost", user="root", password="root", database="testdb", port=3306)


@app.route('/')
def frontend():
    return render_template('frontend.html')


mysqlCursor = mysqlConnection.cursor()


from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
mysqlConnection = mysql.connector.connect(host="localhost", user="root", password="new_password", database="testdb", port=3306)


@app.route('/')
def frontend():
    return render_template('frontend.html')


mysqlCursor = mysqlConnection.cursor()


@app.route('/save_employee', methods=['POST'])
def save_employee():
    try:
        data = request.get_json()
        print(f"JSON Data: {data}")

        empid = data.get('empid')
        empname = data.get('empname')
        empsal = data.get('empsal')

        # Validate and process the data as needed

        # Assuming you have a MySQL connection and cursor defined earlier
        sql = "INSERT INTO employees (empid, empname, empsal) VALUES (%s, %s, %s)"
        mysqlCursor.execute(sql, (empid, empname, empsal))
        mysqlConnection.commit()

        print(mysqlCursor.rowcount, "record inserted.")

        response = {
            'message': 'Employee information saved successfully',
            'empid': empid,
            'empname': empname,
            'empsal': empsal
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

