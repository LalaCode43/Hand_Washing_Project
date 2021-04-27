from flask import Flask, Response, request
import pymongo                                 
import json                                     
from bson.objectid import ObjectId

###############################################################################################################################################################

app = Flask(__name__)

###############################################################################################################################################################

try:
    # mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS = 1000) 
    # db = mongo.Users_Info  
    # mongo.server_info() 
    cluster = pymongo.MongoClient("localhost", port=27017, serverSelectionTimeoutMS=1000)
    db = cluster["handwashing"]
    collection = db["user_info"]
except:
    print("ERROR - Cannot connect to db")

###############################################################################################################################################################

@app.route("/users/signup", methods=["POST"])
def Sign_up():
    try:
        res_info = request.get_json(force=True)
        # user = {"fullname": res_info["fullname"],
        #         "email": res_info["email"],
        #         "password": res_info["password"]}
        # check if the email exists
        Exist = collection.count_documents({"email":res_info['email']})
        print(Exist)

        if Exist:
            return Response(response="User already exist!")
        else:
            collection.insert_one(res_info)
            return Response(response="Registed Scuccessfully!")    
        # duplicate = db.Users.count_documents({"email":user["email"]})
        # if duplicate == 0:
        #     dbResponse = db.Users.insert_one(user)
        #     return Response(response=json.dumps({"Message":"User created","id":f"{dbResponse.inserted_id}"}), status=200, mimetype="application/json")
        # else:
        #     return Response(response=json.dumps({"Message":"User already exist"}), status=200, mimetype="application/json")
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(response="Sorry cannot sign in!")
    

###############################################################################################################################################################

@app.route("/users/signin", methods=["POST"])
def Sign_in():

    try:
        # get informations from client's inputs: email and password
        login_info = request.get_json(force=True)
        email = login_info["email"]
        password = login_info["password"]
        
        # check if the email exists
        Exist = collection.count_documents({"email":email})
        print(Exist)

        if Exist == 1:
            data = collection.find({"email": email})
            for user in data:
                if password == user['password']:
                    return Response(response="Login successfully!")
                    # Response(response=json.dumps({"Message":"Password is not correct."}),status=200,mimetype="application/json")
                else:
                    return Response(response="Password is not correct!") 
                    # Response(response=json.dumps({"Message":"Login successfully!"}),status=200,mimetype="application/json")
        else:
            return Response(response="Account is not exist!")

    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(response="Sorry cannot sign in!")


    #     if Exist == 1: # if 
    #         data = collection.find({"email":login_email})
    #         for user in data:
    #             user["_id"] = str(user["_id"])   
    #         if login_info["password"] == data[0]["password"]:
    #             check = True
    #         else:
    #             check = False
    #         if check:
    #             return "True"
    #         else:
    #             return "False"
    #     else:
    #         return Response(response=json.dumps({"Message":"Account is not exist."}),status=200,mimetype="application/json")
    # except Exception as ex:
    #     print("**********")
    #     print(ex)
    #     print("**********")
    #     return Response(response=json.dumps({"Message":"Sorry cannot sign in."}), status=500, mimetype="application/json")

###############################################################################################################################################################

@app.route("/users/passwordforgot", methods=["GET"])
def Forgot_Password():
    try:
        email = str(request.args.get("email"))
        duplicate = db.Users.count_documents({"email":email})
        if duplicate:
            data = list(db.Users.find({"email":email}))
            for user in data:
                user["_id"] = str(user["_id"])
            userInfo = data[0]
            return userInfo["password"]
        else:
            return Response(response=json.dumps({"Message":"This email is not exist."}), status=200, mimetype="application/json")
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(response=json.dumps({"Message":"Sorry cannot find your password."}), status=500, mimetype="application/json")

###############################################################################################################################################################

@app.route("/users/passwordreset", methods=["PATCH"])
def Reset_Password():
    try:
        user_OldInfo = {"email":request.form["email"], "oldpassword":request.form["oldpassword"],"newpassword":request.form["newpassword"]}
        if db.Users.count_documents({"email":str(user_OldInfo["email"])}):
            data = list(db.Users.find({"email":str(user_OldInfo["email"])}))
            for user in data:
                user["_id"] = str(user["_id"])
            userInfo = data[0]
            if user_OldInfo["oldpassword"]==userInfo["password"]:
                dbResponse = db.Users.update_one({"email":user_OldInfo["email"]},{"$set":{"password":user_OldInfo["newpassword"]}})
                if dbResponse.modified_count == 1:
                    return "Successfully"
                else:
                    return "Fail"
            else:
                return "Wrong Password"
        else:
            return Response(response=json.dumps({"Message":"This account does not exist."}), status=200, mimetype="application/json")
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(response=json.dumps({"Message":"Sorry cannot change your account password."}), status=500, mimetype="application/json")

###############################################################################################################################################################

@app.route("/users/deleteuser", methods=["DELETE", "POST"])
def Delete_Account():
    try:
        userInfo = {"fullname": request.form["fullname"],
                    "email": request.form["email"],
                    "password": request.form["password"]}
        data = list(db.Users.find({"email":str(userInfo["email"])}))
        for user in data:
            user["_id"] = str(user["_id"])
        userIf = {"fullname":data[0]["fullname"],"email":data[0]["email"],"password":data[0]["password"]}
        if userInfo == userIf:
            dbResponse = db.Users.delete_one(userInfo)
            if dbResponse.deleted_count ==1:
                return Response(response=json.dumps({"Message":"User deleted."}), status=200, mimetype="application/json" )
            else:
                return Response(response=json.dumps({"Message":"User cannot found."}),status=200,mimetype="application/json")
        else:
            return Response(response=json.dumps({"Message":"Wrong account information."}),status=200,mimetype="application/json")
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(response=json.dumps({"Message":"Sorry cannot delete your account."}), status=500, mimetype="application/json")

###############################################################################################################################################################          

def Init_Backend():
    db.create_collection("Users")
    db.create_collection("Login_Info")
    db.Users.create_index("email")
    db.Login_Info.create_index("email")
    return

###############################################################################################################################################################

if __name__ == "__main__":
    app.run(debug=True)
    # "host="localhost", port=80, "