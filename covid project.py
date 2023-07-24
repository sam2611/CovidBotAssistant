from ast import main
from turtle import color, width
from covid import Covid
import tkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import pyttsx3
from matplotlib import pyplot as plt 
#to scale the data we are importing patches
import matplotlib.patches as mpatches
#importing covid library
from covid import Covid 
#initializing covid library

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('rate', 150) 
engine.setProperty('voice', voices[1].id)
covid=Covid(source="worldometers")



#function which will get covid data and will show it
def showdata():
    # importing matplotlib which will be used to show data

    covid=Covid (source="worldometers") #declaring empty lists to store different data sets

    cases=[]
    confirmed = []
    active = [] 
    deaths = []

    recovered=0

    # using try and except to run program without errors

    try:

        # updating root main.update()

        # getting countries names entered by the user

        countries=data.get() #removing white spaces from the start and end of the string
        country_names = countries.strip() # replacing white spaces with commas inside the string country_names country_names.replace("", "")
        #splitting the string to store names of countries

        # as a list

        country_names=country_names.split(",") # for loop to get all countries data

        for x in country_names:

            # appending countries data one-by-one in cases list # here, the data will be stored as a dictionary
            # for one country i.e. for each country
            # there will be one dictionary in the list
            #which will contain the whole information
            # of that country cases.append(covid.get_status_by_country_name(x))
            #updating the root 
            main.update()

            # for loop to get one country data stored as dict in list cases
        for y in cases:
            # storing every Country's confirmed cases in the confirmed list

            confirmed.append(y["confirmed"]) 

            # storing every Country's cases in the active list
            active.append(y["active"])

            # storing every Country's deaths cases in the deaths list
            deaths.append(y["deaths"]) 
            # storing every Country's recovered cases in the recovered list
            recovered.append(y["recovered"]) 
            # I marking the color information on scaleusing patches
            confirmed_patch= mpatches.Patch(color-'green', label='confirmed')
            recovered_patch=mpatches.Patch(color-'red', label='recovered') 
            active_patch=mpatches.Patch(color-'blue',label='active')
            deaths_patch=mpatches.Patch(color- 'black', label='deaths')

            # plotting the scale on graph using legend()showing the data using graphs

            plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch]) 

            #this whole for loop section is related to matplotlib

            for x in range(len(country_names)):
                plt.bar(country_names[x], confirmed [x], color='green') 
                if recovered[x] > active[x]:
                    plt.bar(country_names[x], recovered[x], color='red')
                    plt.bar(country_names[x], active[x], color='blue')
                else:
                    plt.bar(country_names[x], active[x], color='blue')
                    plt.bar(country_names[x], recovered[x], color-'red') 
                plt.bar(country_names[x], deaths [x], color-'black')
                #setting the title of the graph 
                plt.title('Current Covid Cases')
                # giving label to x direction of graph 
                plt.xlabel('Country Name')
            plt.show()
    except Exception as e:
    # asking user to enter correct details during entering the country names on GUI
    # please differentiate the country names with spaces or comma but not with both
    # otherwise you will come to this section
        data.set("Enter correct details again")

def indv():
    def search(): 
        cname=ctname.get()
        if cname=='':
            return messagebox.showerror('Error', 'Enter country name')
        else:
            data=covid.get_status_by_country_name(cname)
            sta=Toplevel()
            sta.geometry('300x300') 
            sta.title('Status of '+cname)
            Label(sta, text='Status', font='Helvetica 12 bold').grid(row=1,column=2)
            Label(sta, text='Confirmed cases:'+str(data['confirmed'])).grid(row=2,column=1) 
            Label(sta, text='Active cases:' +str(data['active'])).grid(row=3, column=1) 
            Label(sta, text='Deaths:'+ str(data['deaths'])).grid(row=4, column=1) 
            Label(sta, text='Recoveries:' +str(data['recovered'])).grid(row=5, column=1)
            st.destroy()
            ctname=StringVar() 
            st=Toplevel()
            st=Toplevel()
            st.title('Individual Status')
            st.geometry('400x100') 
            Button(st, text='Search', command=search).grid(row=2,column=3)
            Label (st, text='Country wise status', font='Helvetica 12 bold').grid(row=1,column=2)
            Label (st, text='Enter country name:').grid(row=2,column=1) 
            Entry(st,width-15, textvariable=ctname).grid(row=2, column=2)

def hlp():

    ss=Toplevel (main)
    ss.geometry('300x300')
    ss.title('Helpline')
    Label (ss, text='HELPLINE NUMBER:', font='Helvetica 12 bold').grid(row=1, column=2) 
    Label (ss, text='Delhi 011-22307145', font='Helvetica 12 bold').grid(row=2,column=2)
    Label (ss, text='Andhra Pradesh 8866-2410978', font='Helvetica 12 bold').grid(row=3,column=2) 
    Label (ss, text='Arunachal Pradesh 9436055743', font='Helvetica 12 bold').grid(row=4, column=2)
    Label (ss, text='Assam 6913347770', font='Helvetica 12 bold').grid(row=5,column=2)
    Label (ss, text='Bihar 104', font='Helvetica 12 bold').grid(row=6,column=2)
    Label (ss, text='Chhattisgarh 104', font='Helvetica 12 bold').grid(row=7, column=2)
    Label(ss, text='Goa 104', font='Helvetica 12 bold').grid(row=8, column=2)
    Label(ss, text='Rajasthan 0141-2225624', font='Helvetica 12 bold').grid(row=9, column=2)
    Label (ss, text='Uttar Pradesh 18001805145', font='Helvetica 12 bold').grid(row=10, column=2)

def speak():
    engine.say("Hi, I am Glow. I am here to talk to you and aprise you about covid nineteen.Covid nineteen is an infectious disease caused by the SARS-CoV-2 virus. Most people infected with the virus will experience mild to moderate respiratory illness and recover To prevent the spread of COVID-19 Clean your hands often. Use soap and water, or an alcohol-based hand rub.Maintain a safe distance from anyone who is coughing or sneezing. Wear a mask when physical distancing is not possible.Don’t touch your eyes, nose or mouth. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
    engine.runAndWait()
