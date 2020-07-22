
 #-*- coding: utf-8 -*-
# @time    : 2020/7/20

from flask import Flask,request,jsonify,Response,make_response
import json
import sys, re,numpy
reload(sys)  
sys.setdefaultencoding('utf8') 



def checkInt(a):
    if a and a.isdigit():
        if ((int(a) > 0) and (int(a) <= 10000) ):
            return True
    return False

def checkStr(b):
    if (b and len(b) <= 16):
        try:
            type(b) == type(" ")
        except:
            return False
        return True
    else:
        return False

def legalStr(b):
    if re.search(r'^[\u4E00-\u9FA5A-Za-z0-9] | \w',b) == None:
        if re.search(r'[~!¥./@#$%^&*()_+{}":;\']+$',b) == None:
            return True
        else:
            return False
    else:
        return False
            


app = Flask(__name__)
@app.route('/shopee/test', methods=['GET'])

def GetPara():
    err_code = 11
    err_msg = "system error"
    a = request.args.get('a')
    b = request.args.get('b')
    refer = ""
    res_dict = {"error_code" : err_code, "error_message" : err_msg,"reference" : refer}
    if checkInt(a) and checkStr(b) and legalStr(b):
        err_code = 0
        err_msg = "success"
        refer = 'NO.{} is {}'.format(a, b)
    else:
        err_code = 21
        err_msg = "empty or wrong params"
    
    res_dict = {}
    res_dict["error_code"] = err_code
    res_dict["error_message"] = err_msg
    res_dict["reference"] = str(refer)
    json.dumps(res_dict)
    return jsonify(res_dict)
if __name__ == '__main__':
    app.run(debug=True,port=5000)
