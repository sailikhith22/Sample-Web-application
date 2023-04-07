from src.logger import logging
from src.exceptions import CustomException
import os, sys 


def get_questions():
    questions = {1:"A bench comprising Chief Justice D Y Chandrachud and Justice J B Pardiwala said that laying down general guidelines without having relation to facts of a case will be dangerous",
                        2:"The plea alleged an alarming rise in the use of coercive criminal processes against opposition political leaders and other citizens exercising their fundamental right to dissent.",
                        3:"The Supreme Court on Wednesday refused to entertain a plea by 14 parties, led by the Congress, alleging arbitrary use of central probe agencies against opposition leaders and seeking guidelines for the future",
                        4:'He is someone I adore, and have great affection and respect for. Bommai mama stood by me during my difficult times," said Sudeep, addressing the media with the chief minister beside him.',
                        5:"A bench comprising Chief Justice D Y Chandrachud and Justice J B Pardiwala said that “laying down general guidelines without having relation to facts of a case will be dangerous",
                        6:"The plea alleged an alarming rise in the use of coercive criminal processes against opposition political leaders and other citizens exercising their fundamental right to dissent.",
                        7:"The Supreme Court on Wednesday refused to entertain a plea by 14 parties, led by the Congress, alleging arbitrary use of central probe agencies against opposition leaders and seeking guidelines for the future",
                        8:"The Supreme Court on Wednesday refused to entertain a plea by 14 parties, led by the Congress, alleging arbitrary use of central probe agencies against opposition leaders and seeking guidelines for the future",
                        9:'He is someone I adore, and have great affection and respect for. Bommai mama stood by me during my difficult times," said Sudeep, addressing the media with the chief minister beside him.',
                        10:"A bench comprising Chief Justice D Y Chandrachud and Justice J B Pardiwala said that “laying down general guidelines without having relation to facts of a case will be dangerous",
                        11:"The plea alleged an alarming rise in the use of coercive criminal processes against opposition political leaders and other citizens exercising their fundamental right to dissent.",
                        12:"The Supreme Court on Wednesday refused to entertain a plea by 14 parties, led by the Congress, alleging arbitrary use of central probe agencies against opposition leaders and seeking guidelines for the future",
                        13:'He is someone I adore, and have great affection and respect for. Bommai mama stood by me during my difficult times," said Sudeep, addressing the media with the chief minister beside him.',
                        14:"A bench comprising Chief Justice D Y Chandrachud and Justice J B Pardiwala said that “laying down general guidelines without having relation to facts of a case will be dangerous",
                        15:"The plea alleged an alarming rise in the use of coercive criminal processes against opposition political leaders and other citizens exercising their fundamental right to dissent."}
    
    logging.info("Questions generated\n".format(questions))
    return questions 

def get_answers():
    answers = {1:13, 2: 3, 3: 4, 4: 5, 5: 6, 6:3 , 7:5, 8: 6, 9:7, 10:8, 11:9, 12:10, 13:11, 14:12, 15:3}

    logging.info("Answers generated\n".format(answers))
    return answers
