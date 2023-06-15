from Flask import Flask,render_template,url_for,request,redirect
from src.utils import store_examdata, store_surveydata, get_dataframe
import os, sys
from src.logger import logging
from src.exceptions import CustomException
from src.extractinginfo import get_questions
from src.pipelines.predict_pipeline import PredictPipeline

application = Flask(__name__)

app = application

@app.route("/")
def welcomepage():
    return render_template("Welcomepage.html")

@app.route("/homepage", methods=["GET", "POST"])
def homepage():
    data = """Donald Trump turned his head toward photographers as he sat, stone-faced with shoulders rounded, at the defense table in a downtown Manhattan courtroom. “Not guilty,” he said in a firm voice during a historic appearance before a judge Tuesday. Trump became the first US president ever to be charged with a crime.
              Prosecutors state in a 34-count felony indictment that Trump conspired to illegally influence the 2016 presidential election through hush money payments to two women, including a porn performer, who said they had sexual encounters with him.
             """

    return render_template("homepage.html",data= data)

@app.route("/survey",methods=["POST","GET"])
def survey():
    try:
        if request.method == 'POST':
            Q1 = request.form.get("Question1")
            Q2 = request.form.get("Question2")
            Q3 = request.form.get("Question3")
            Q4 = request.form.get("Question4")
            Q5 = request.form.get("Question5")
            Q6 = request.form.get("Question6")
            Q7 = request.form.get("Question7")
            Q8 = request.form.get("Question8")
            Q9 = request.form.get("Question9")
            Q10 = request.form.get("Question10")
            Q11 = request.form.get("Question11")
            #store_surveydata(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11)
            return "<h2 align='center'>Data has been saved successfully</h2>", {"Refresh": "5; url=homepage"}
        else:
            return render_template("survey.html")
    except Exception as e:
        logging.error(e,sys)    


@app.route("/examtest/<message>",methods=["GET","POST"])
def examtest(message):
    try:
        questions = get_questions()
        if request.method == "POST":
            if request.form.get("button") == "Start Exam":
                name = request.form.get("name")
                age = request.form.get("age")
                gender = request.form.get("gender")
                
                if any(val=="" or val=="None" for val in [name,age,gender]):
                    return render_template("testexam.html",  questions=questions)
                else:
                    details = {}   
                    #store_persondetails(name,age,gender)
                    details["name"] = name
                    details["age"] = int(age)
                    details["gender"] = gender
                    print("Messages dict from 1st block",details)
                    print("message received ", message)
                    
                   #return redirect(url_for("examtest", message = details)+"#exam-id")
                    #return redirect(url_for("examtest", message = details)+"#exam-id")
                    return redirect(url_for("examtest", message = details)+"#exam-id")
            elif request.form.get("button") == "End Exam":
                # Capture all the answers and store them to answers dictionary
                               
                Q1 = request.form.get("answer1")
                Q2 = request.form.get("answer2")
                Q3 = request.form.get("answer3")
                Q4 = request.form.get("answer4")
                Q5 = request.form.get("answer5")
                Q6 = request.form.get("answer6")
                Q7 = request.form.get("answer7")
                Q8 = request.form.get("answer8")
                Q9 = request.form.get("answer9")
                Q10 = request.form.get("answer10")
                Q11 = request.form.get("answer11")
                Q12 = request.form.get("answer12")
                Q13 = request.form.get("answer13")
                Q14 = request.form.get("answer14")
                Q15 = request.form.get("answer15")
                #print("from the desired block name,age,gender values are: ", message )
                questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15]
                #print("before questions ",questions)
                for ind in range(len(questions)):
                    if type(questions[ind]) == str and len(questions[ind])==0:
                        questions[ind] = 0
                questions = list(map(int, questions))
                #print("From app questions before sending ",questions)
                
                generated_data = store_examdata(message, questions)
                logging.info("Generate data {}".format(generated_data))
                generated_dataframe = get_dataframe(generated_data).iloc[:,:-1]
                logging.info("inside the app generated data is {}".format(generated_dataframe))
                logging.info("Dataframe shape {}".format(generated_dataframe.shape))
                #return redirect(url_for("thankspage", data=generated_data))
                predictpipe = PredictPipeline()
                test_result = predictpipe.predict(generated_dataframe)
                
                return "<h2 align='center'>Having dyslexia is {}</h2>".format(test_result)#, {"Refresh": "5; url=homepage"}
            else:
                return "<h3> Got inside the third block</h3>"
        else:
            
            
            return render_template("testexam.html", questions=questions)
    except Exception as e:
        logging.error(e,sys)

@app.route("/thankspage", methods=["GET", "POST"])
def thankspage():
    try:
        
        return render_template("thankspage.html")
    except Exception as e:
        return "<h2>Some thing went wrong in passing the data from the testpage</h2>" ,  {"Refresh": "5; url=homepage"}

if __name__=="__main__":
    app.run(host="0.0.0.0")
