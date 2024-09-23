# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:02:31 2024

@author: Mustafa-Sameer
"""

users_data = {
    'ahmad': {
        'password': "ah@#1234567890md",
        "currently_logged_in":False,
        'courses': {'math':12},
    },

}



def  run_the_system( ):
  while True:
    print("*"*20)  
    print("1.register_new_user: 1")
    print("2.login:2")
    print("3.exit:3")
    print("*"*20)
    Enter=input("enter: ")
    def new( ):
         while True:
             username=input('username: ').lower()
             if username in users_data :
                 print("Name exists. Try again.")

             else:
                 break
         Password=input("(Enter Password:(16 characters.,two special characters and two digits. ,Cannot contain the username. ) ").lower()
         number=0
         special_characters=0
         while True:
           for i in Password:
               if i in "123456789":
                 number+=1
               elif i in "@#$%^&*?!_*()[]{}":
                 special_characters+=1
           if   len(Password)==16 and  number>=2 and   special_characters>=2 and  Password.find( username)==-1 :
               print("The password is correct")
               Password= Password
               break
           else:
               print("The password is wrong")
               Password=input("Password: ")
         users_data[username]={'password':Password, "currently_logged_in":False,'courses':{}}      
         print("The registration process has been completed.")     
    def log( ):
        
        username=input('username: ').lower()
        Password=input("Password: ")
        if  username in users_data and Password==users_data[ username]["password"]:
          users_data[username]["currently_logged_in"]  =True
          while True:  
            print("1.add_new_user_course:1 ")
            print("2.Retrieve registered courses:2 ")
            print("3.Calculate average grade for the courses:3 ")
            print("4.See the total number of users in the system:4 ")
            print("5.Edit_chorus_tags:5")
            print("6.Delete the user account:6")
            print("7.Log out :7")
            Enter=input("enter: ")
            def new_course():
               number_new_course=int(input("number_new_course: "))
               for i in range(number_new_course):
                 
                   new_course=input("enter new_course: ").lower()
                   users_data[username]["courses"] [new_course]=0
               print("The course has been added successfully") 
            def   Retrieve_registered_courses():
                if  users_data[username]["courses"]=={}:
                   print("NO courses registered") 
                    
                else:
                    
                   print( users_data[username]["courses"])
               
            def average_grade_for_the_courses():
                sum_grade_for_the_courses=0
                number_for_the_courses=0
                for i in users_data[username]["courses"].keys():
                    print(i)
                    sum_grade_for_the_courses+=users_data[username]["courses"] [i]
                    number_for_the_courses+=1
                if   number_for_the_courses !=0:  
                 average_grade_for_the_courses=sum_grade_for_the_courses/ number_for_the_courses
                 print("average_grade_for_the_courses: ",average_grade_for_the_courses)
                else:
                    print("No average_grade_for_the_courses")
              
            def    total_number_of_users():
                number_of_users=0
                for i in users_data.keys():
                    print(i)
                    number_of_users+=1
                print('total_number_of_users: ',number_of_users)
            def Edit_chorus_tags():
                
                if  users_data[username]["courses"]=={}:
                   print("NO courses ") 
                    
                else:
                    Retrieve_registered_courses()
                    edit=input("Edit_chorus_tags:")
                    if edit in users_data[username]["courses"]:
                     x=int(input("enter grade:"))
                     users_data[username]["courses"][edit]=x
                    else:
                        print("An error in writing the course")
            def Delete_the_user():
               del users_data[username]
               
            def Log_out():
               users_data[username]["currently_logged_in"]  =False
                 
            if  Enter=="1":
                new_course()
            if  Enter=="2":
               Retrieve_registered_courses()
            if  Enter=="3":
                average_grade_for_the_courses()
            if  Enter=="4": 
                 total_number_of_users()
            if  Enter=="5":  
                Edit_chorus_tags()
            if  Enter=="6":   
               return  Delete_the_user()
            if Enter =="7":
                return Log_out()
    if Enter=="1":
        new()     
    elif Enter =="2":
       log() 
    elif Enter=="3":
        return 
    else:
        print("Typing error")
  
run_the_system( )
















