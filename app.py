from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
mysqlConnection = mysql.connector.connect(host="localhost", user="root", password="root", database="testdb", port=3306)


@app.route('/')
def frontend():
    return render_template('frontend.html')


mysqlCursor = mysqlConnection.cursor()


@app.route('/save_employee', methods=['POST'])
def save_employee():
    data = request.get_json()
    tupleFromDict = tuple(data.values())
    print(f"tupleFromDict:{tupleFromDict}")
    empid = request.form.get('empid')
    empname = request.form.get('empname')
    empsal = request.form.get('empsal')
    sql = "INSERT INTO employee (empid, empname,empsal) VALUES (%s, %s,%s)"
    mysqlCursor.execute(sql, tupleFromDict)

    mysqlConnection.commit()

    print(mysqlCursor.rowcount, "record inserted.")
    # Process and save employee data (modify this part based on your needs)

    response = {
        'message': 'Employee information saved successfully',
        'empid': empid,
        'empname': empname,
        'empsal': empsal
    }

    return jsonify(response)


if __name__ == '__main__':
    # Run Flask app on a remote host and port
    app.run(host='0.0.0.0', port=5000, debug=True)
