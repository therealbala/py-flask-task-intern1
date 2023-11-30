from flask import Flask, render_template, request  

app = Flask(__name__)
 
@app.route("/", methods=['GET','POST']) 
def post_method():    
    if request.method == 'GET': 
       return render_template("contact.html")   
    else: 
       name =  user = request.form['name'] 
       email =  user = request.form['email']  
       message =  user = request.form['message']   

       ###### SMTP CODES GOES HERE ###### 
       ''' 
       import smtplib 
       subject = 'Python Email'
       body = 'This email is sent using python'
       message = f'Subject: {subject}\n\n{body}'
       server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
       server.login("username", "password")
       i = 1 
       while i < 11: 
            server.sendmail("from email address", 
                            "to email address", message) 
            i += 1 
       server.quit()  
       ''' 

       return render_template("success.html",name=name,email=email,message=message)    
  

if __name__=="__main__":
    app.run(debug=True)  
    


