def analyzeMsg(message, counter, session):
    if counter == 1:
        return handleCounter1()
    elif counter == 2:
        return handleCounter2(message, session)
    elif counter == 3:
        return handleCounter3(message, session)
    elif counter == 4:
        return handleCounter4(message, session)
    elif counter ==5:
        return handleCounter4(message, session)
    return clearSess(session)

def clearSess(session):
    session.clear()
    session["counter"] = 1
    return handleCounter1()

def handleCounter1():
    return "Hello Aron! Would you like to access your appointments, portal, or learn about us? (appointments, portal, about)"

def handleCounter2(message, session):
    try:
        session["first"] = message
        if message == "appointments":
            return "Your next appointment is on Wednesday at 2:30pm with Dr. Lewis! Would you like to schedule an appointment, or go back to the main menu? (appt, menu)"
        elif message == "portal":
            return "What would you like to see? (medications, tests, vitals, visits, insurance, allergies, immunizations, notes)"
        elif message == "about":
            session.clear()
            return "Hey there! Gogo Health Portal is a unique app that lets you access your health portal via texting. This way, you won't have to worry about getting an internet connection or some fancy smart phone!"
        return clearSess(session)
    except:
        return clearSess(session)

def handleCounter3(message, session):
    try:
        if session["first"] == "appointments":
            if message == "appt":
                return "Soonest avaliability is 10/22/2017 at 3:00pm. Does this work for an appointment? (no, yes, cancel)"
        elif session["first"] == "portal":
            if message == "medications":
                return "Your current prescription is: prozac. Your past perscriptions in the last 6 months were: galantamine, celecoxib. (back)"
            elif message == "tests":
                return "Your latest test: prostate examination was negative. Your previous test: STI screening was negative. (back)"
            elif message == "vitals":
                return "Your latest measured height: 70.00 in, weight: 215.00 lbs, BMI: 30.85 kg/meter(2), BMI percentile: 96, and blood pressure: 104/62 mm[Hg] (back)"
            elif message == "visits":
                return "Your previous visit was on 05/27/2016 with Dr. Lewis concerning your back pains. (back)"
            elif message == "insurance":
                return "Your insurance provider: CaresourceJust4Me, insurance type: critical illness (back)"
            elif message == "allergies":
                return "You are alergic to pollen, peanutbutter, and soy. Dr. Lewis has previously recommend you carry an Epipen at all times. (back)"
            elif message == "immunizations":
                return "Your past immunizations have been: chicken pox on 01/01/1998, MMR on 05/16/2003, and varicella on 06/23/2014. (back)"
            elif message == "notes":
                return "Dr. Lewis recommends that you carry an Epipen at all times. Dr. Lewis also recommends coming back for a checkup every other week. (back)"
        return clearSess(session)
    except:
        return clearSess(session)

def handleCounter4(message, session):
    try:
        if session["first"] == "appointments":
            if message == "no":
                return "Okay, what date/time works for you? (m/d/y/time, example 4/3/2017/4:30pm)"
            if message == "yes":
                return "Great! You are scheduled for 10/22/2017 at 3:00pm and you will recieve a notification 24 hours in advance."
        return clearSess(session)
    except:
        return clearSess(session)


def handleCounter5(message, session):
    try:
        if session["first"] == "appointments":
            return "Okay, your appointment has been scheduled for " + message + " you will recieve a notification 24 hours in advance."
        return clearSess(session)
    except:
        return clearSess(session)



