from Database import Database
from flask import Flask,jsonify,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "<h1>Welcome to CRUD application</h1>"

@app.route('/getEmployees',methods=['GET'])
def getEmployees():
    db=Database()
    statement="select * from employee_table"
    employees=db.select(statement)
    result=[]

    for (id,name,occupation,age) in employees:
        result.append({
            "id":id,
            "name":name,
            "occupation":occupation,
            "age":age
        })

    return jsonify(result)

@app.route('/getEmployee',methods=['GET'])
def getEmployee():
    id = request.args.get('id')

    statement=f'select * from employee_table where id={id}'
    db=Database()
    employee=db.selectone(statement)

    result={
        "id":employee[0],
        "name":employee[1],
        "occupation":employee[2],
        "age":employee[3]
    }

    return jsonify(result)


@app.route('/addEmployee',methods=['POST'])
def addEmployee():

    name=request.get_json()["name"]
    occupation=request.get_json()["occupation"]
    age=request.get_json()["age"]
    print(name)

    statement=f'insert into employee_table(name,occupation,age) values("{name}","{occupation}",{age})'

    db=Database()
    db.execute(statement)

    return jsonify("Inserted")

@app.route('/updateEmployee',methods=['PUT'])
def updateEmployee():
    id=request.get_json()[0]["id"]
    occupation=request.get_json()["occupation"]
    age=request.get_json()["age"]

    statement=f'update employee_table set occupation="{occupation}", age={age} where id={id}'

    db=Database()
    db.execute(statement)

    return jsonify("Updated")


@app.route('/deleteEmployee',methods=['Delete'])
def deleteEmployee():
    id=request.args.get('id')

    statement=f'delete from employee_table where id={id}'

    db=Database()
    db.execute(statement)

    return jsonify("Deleted")

@app.route('/getEmpData',methods=['GET'])
def getEmpData():
    db = Database()
    statement = "select * from employee_table"
    employees = db.select(statement)
    names=[]
    ages=[]

    for (id, name, occupation, age) in employees:
        names.append(name)
        ages.append(age)

    result = {
        "names": names,
        "ages": ages
    }

    return jsonify(result)

@app.route('/api/userExists',methods=['GET'])
def userExists():
    id = request.args.get('id')
    print(id)
    result = {
        "name": "",
        "email": id,
        "password": "NA"
    }
    return jsonify(result)

@app.route('/api/validatePassword',methods=['POST'])
def validatePassword():
    name=request.get_json()["name"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    print(name)
    print(email)
    print(password)

    return jsonify("Pratik8286")

@app.route('/api/addUser',methods=['POST'])
def addUser():
    name=request.get_json()["name"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    print(name)
    print(email)
    print(password)

    return jsonify(True)


@app.route('/api/verifyEmail',methods=['POST'])
def verifyEmail():
    name=request.get_json()["name"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    print(name)
    print(email)
    print(password)

    return jsonify(True)

@app.route('/api/users/login',methods=['POST'])
def userLogin():
    print(request)
    email=request.get_json()["username"]
    password=request.get_json()["password"]
    print(email)
    print(password)

    # return jsonify("Pratik8286")

    statement=f'select * from users where Email="{email}" AND Password="{password}"'
    db=Database()
    user=db.selectone(statement)

    result={
        "id":user[0],
        "fname":user[1],
        "lname":user[2]
    }
    print(result)

    return jsonify(result)

@app.route('/api/users/register',methods=['POST'])
def userRegister():
    fname = request.get_json()["fname"]
    lname = request.get_json()["lname"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    gender = request.get_json()["gender"]
    mobile = request.get_json()["mobile"]
    country = request.get_json()["country"]

    statement=f'insert into users (FirstName,LastName,Gender,Email,Password,Mobile,Country) ' \
              f'values ("{fname}","{lname}","{gender}","{email}","{password}","{mobile}","{country}");'
    db=Database()
    db.execute(statement)

    return jsonify("Inserted")



app.run()