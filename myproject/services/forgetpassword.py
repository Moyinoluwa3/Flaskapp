from flask import jsonify, request
from .utils import sendmail
from flask_restful import Resource
from database.models import User
#from flask_jwt_extended import create_access_token, get_jwt_identity, decode_token
import datetime
from itsdangerous import URLSafeTimedSerializer  as Serializer

#http://blog/changepassword/<token>/
class ForgetPassword(Resource):

    def post(self):
        
            
        
        try:
            body = request.get_json()
            email = body.get('email')
            
            if not email:
                return {"status": "email does not exist"},404
            user = User.objects.get(email=body.get('email'))
            if not user:
                return{"status":"you dont own an email in this api"}
            
            if not user:
                return {"satue": "you are amddd"}, 200

            expiration_time = str(datetime.datetime.now() + datetime.timedelta(seconds=120))
            print(expiration_time)
            s = Serializer("kbshgbjsbgjsbgjfsbjb")
            
            token = s.dumps({'email': user.email, "expiration_time":expiration_time})
            
            url = f"{request.host_url}api/auth/changepassword?token={token}"
            
                        
            status = sendmail(email = email, url = url)
            
            if status == 1:
                return {"message": "Reset link successfully sent to your mail" }, 200
            return {"message": "Mail failed, kindly retry"}
                
        except:
            return {"status": "User does not exist"}, 404    


class Changepassword(Resource):
    def post(self):
        token = request.args.get('token')
        s = Serializer('kbshgbjsbgjsbgjfsbjb')
        try:
            print(s.loads(token))
            email = s.loads(token)['email']
            expiration_time = s.loads(token)['expiration_time']
            print(email)
            print(expiration_time)
            if ( datetime.datetime.now() < datetime.datetime.fromisoformat(expiration_time)):
                body = request.get_json()
                password = body.get("password")
                confirm_password = body.get("confirm_password")
                if password != confirm_password:
                    return jsonify({"message": "Password Mismatch"})
                user = User.objects.get(email=email)
                user.modify(password = password)
                user.hash_password()
                user.save()
                return jsonify({"message": "Password Successfully Updated"})
            return jsonify({"message": "Expired Token"})
        except:
            return  jsonify({"message": "Invalid token or Wrong Token"})





