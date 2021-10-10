import pyttsx3
friend=pyttsx3.init()
friend.setProperty('rate', 150)
friend.say("To prevent the spread of COVID-19 Clean your hands often. Use soap and water, or an alcohol-based hand "
           "rub.Maintain a safe distance from anyone who is coughing or sneezing. Wear a mask when physical "
           "distancing is not possible.Don’t touch your eyes, nose or mouth. Cover your nose and mouth with your bent "
           "elbow or a tissue when you cough or sneeze.")
friend.runAndWait()

friend2=pyttsx3.init()
friend2.say("If you have a fever, cough and difficulty breathing , press one (Round Button) and , if not press zero(Square Button)")
friend2.runAndWait()
n=int(input())
if n==1:
    friend2.say("Stay home. Most people with COVID-19 have mild illness and can recover at home without medical care. "
                "Do not leave your home, except to get medical care. Do not visit public areas.Take care of yourself. "
                "Get rest and stay hydrated. Take over-the-counter medicines, such as acetaminophen, to help you feel "
                "better.Stay in touch with your doctor. Call before you get medical care. Be sure to get care if you "
                "have trouble breathing, or have any other emergency warning signs, or if you think it is an "
                "emergency.Avoid public transportation, ride-sharing, or taxis.")
    friend2.runAndWait()
elif n==0:
    friend2.say("That's great. take care and follow all the precautions ")
    friend2.runAndWait()


friend.say("Thankyou for your attention")
friend.runAndWait()
