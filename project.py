import time
#chapter2
from PIL import Image
import cv2
#chapter4
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os,sys

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
#------------------------------------  chapters  --------------------------------------------#
def chapters():
    while True:
        slow_print("\n                        📚 --- Main Menu: Chapters --- 📚\n")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━'┓")
        print("                   ┃    1. 📑 Chapter One   Assignments     ┃")
        print("                   ┃    2. 📑 Chapter Two   Assignments     ┃")
        print("                   ┃    4. 📑 Chapter Four  Assignments     ┃")
        print("                   ┃    5. 📑 Chapter Five  Assignments     ┃")
        print("                   ┃    6. 👥 Group Members                 ┃")
        print("                   ┃    7. ❌ Exit                          ┃")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━'┛")
        chapters = int(input("Enter the chapter number: "))
        if chapters == 1:
            container()
            break
        elif chapters == 2:
            chapter2()
            continue
        elif chapters == 4:
            chapter4()
            continue
        elif chapters == 5:
            chapter5()
            continue
        elif chapters == 6:
            members()
            continue
        elif chapters == 7:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid Input! Please try again.")
            
#----------------------------------  chapter1_container  ------------------------------------#
def container():
    while True:
        print("\n                    🎓 --- Chapter One: Assignments --- 🎓")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃ 1. 🧑‍💻 Part One : User Defined Functions  ")
        print("                   ┃ 2. 🔧 Part Two : Built In Functions      ")
        print("                   ┃ 3. 🔙 Back To Main Menu                  ")
        print("                   ┃ 4. ❌ Exit                               ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━┛")
        chapter1 = int(input("Enter the assignment number: "))
        if chapter1 == 1:
            chapter1_p1()
            break
        elif chapter1 == 2:
            chapter1_p2()
            break
        elif chapter1 == 3:
            chapters()
            break
        elif chapter1 == 4:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid input! Please try again.")
#-chapter1_p1-#
def chapter1_p1():
    while True:
        print("\n                    🎓 --- Chapter One: User Defined Functions --- 🎓")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃  1. 🧮 Assignment One: Calculator        ")
        print("                   ┃  2. 💰 Assignment Two: Murabaha Service  ")
        print("                   ┃  3. 🔙 Back To The Chapter 1 Container   ")
        print("                   ┃  4. 🔙 Back To Main Menu                 ")
        print("                   ┃  5. ❌ Exit                              ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━━┛")
        chapter1_p1 = int(input("Enter the assignment number: "))
        if chapter1_p1 == 1:
            assiment_two()
            break
        elif chapter1_p1 == 2:
            assiment_one()
            break
        elif chapter1_p1 == 3:
            container()
            break
        elif chapter1_p1 == 4:
            chapters()
        elif chapter1_p1 == 5:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid input! Please try again.")
#---Calculator---#
def assiment_two():
    def add(x, y):
        return x + y
    def sub(x, y):
        return x - y
    def mul(x, y):
        return x * y
    def div(x, y):
        if y != 0:
            return x / y
        else:
            print("⚠️ Error: Division by Zero!")
            return None
    def mod(x, y):
        return x % y

    while True:
        print("\n                    ✨ --- Welcome to Assignment One: Basic Calculator --- ✨")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃               Select Operation:               ")
        print("                   ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
        print("                   ┃➤ 1. ➕ Add                                   ")
        print("                   ┃➤ 2. ➖ Subtract                              ")
        print("                   ┃➤ 3. ✖  Multiply                              ")
        print("                   ┃➤ 4. ➗ Divide                                ")
        print("                   ┃➤ 5. ➗ Modulus                               ")
        print("                   ┃➤ 6. 🔙 Back To The Chapter 1 Part 1           ")
        print("                   ┃➤ 7. 🔙 Back To The Chapter 1 Container        ")
        print("                   ┃➤ 8. 🔙 Back To Main Menu                      ")
        print("                   ┃➤ 9. ❌ Exit                                  ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        choice = int(input("\nEnter choice {(1-5) For Calculator & (6-9) For The Data Structure)}: "))
        
        if choice == 6:
            chapter1_p1()
            continue
        elif choice == 7:
            container()
            continue
        elif choice == 8:
            chapters()
            continue
        elif choice == 9:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        
        # Only ask for numbers if the user selects a valid operation (1-5)
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 1:
            result = add(num1, num2)
            op = "+"
        elif choice == 2:
            result = sub(num1, num2)
            op = "-"
        elif choice == 3:
            result = mul(num1, num2)
            op = "*"
        elif choice == 4:
            result = div(num1, num2)
            op = "/"
        elif choice == 5:
            result = mod(num1, num2)
            op = "%"
        else:
            print("❌ Invalid input! Please try again.")
            continue

        if result is not None:
            print(f"\n✅ {num1} {op} {num2} = {result}")
#---Murabaha---#
def assiment_one():
    def murabaha():
        print("\n✨ --- Welcome to Assignment Two: Murabaha Service --- ✨")
        name = input("Enter Customer Name: ")
        address = input("Enter Customer Address: ")
        gender = input("Enter Gender (M/F): ")
        product_name = input("Enter Product Name: ")
        product_price = float(input("Enter Product Price: "))
        months = int(input("Enter the number of months to pay: "))

        if months <= 12:
            EXTRA = 0.06 * product_price
        else:
            EXTRA = 0.12 * product_price
        total_amount = product_price + EXTRA
        monthly_pay = total_amount / months

        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("          📊 Bank Murabaha Service 📊")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🧑 Customer Name: {name}")
        print(f"🏠 Address: {address}")
        print(f"⚧ Gender: {gender}")
        print(f"📦 Product: {product_name}")
        print(f"💰 Product Price: {product_price}")
        print(f"🏦 Bank Charge: {EXTRA}")
        print(f"📆 Number of Months: {months}")
        print(f"💵 Total Price: {total_amount}")
        print(f"📅 Monthly Payment: {monthly_pay:.2f}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        dooro = input("\nWould you like to Calculate other Murabaha ? (y/n): ")
        if dooro.lower() == 'y':
            assiment_one()
        else:
            print("🎉 Returning to Back... 🎉")
            loading_animation()
            chapter1_p1()
    murabaha()   
#-chapter1_p2-#
def chapter1_p2():
    while True:
        print("\n                    🎓 --- Chapter One: Built-In Functions --- 🎓")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃1. 📜 Assignment One: Palindrome Checker     ")
        print("                   ┃2. 📋 Assignment Two: Sorting List of Strings")
        print("                   ┃3. 🔙 Back To The Chapter 1 Container        ")
        print("                   ┃4. 🔙 Back To Main Menu                      ")
        print("                   ┃5. ❌ Exit                                   ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        chapter1_p2 = int(input("Enter the assignment number: "))
        if chapter1_p2 == 1:
            plaindrome()
            break
        elif chapter1_p2 == 2:
            sorting()
            break
        elif chapter1_p2 == 3:
            container()
            break
        elif chapter1_p2 == 4:
            chapters()
        elif chapter1_p2 == 5:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid input! Please try again.")
#---Palindrome---#
def plaindrome():
    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]

    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print(user_input,' is a palindrome.')
    else:
        print(user_input,' is not a palindrome.')
    dooro = input("\nWould you like to check another Plaindrome ? (y/n): ")
    if dooro.lower() == 'y':
        plaindrome()
    else:
        print("🎉 Returning to Back... 🎉")
        time.sleep(1)
        chapter1_p2()
#----Sorting-----#
def sorting():
    def sort(string_list):
        return sorted(string_list)

    my = []
    n = int(input("How many strings do you want to enter? "))
    for i in range(n):
        user_input = input(f"Enter string {i+1}: ")
        my.append(user_input)
    
    sorte = sort(my)
    print("Original list:", my)
    print("Sorted list:", sorte)

    dooro = input("\nWould You Like To Sort Another Strings? (y/n): ")
    if dooro.lower() == 'y':
        sorting()
    else:
        print("🎉 Returning to Back... 🎉")
        time.sleep(1)
        chapter1_p2()
#------------------------------------  chapter2  --------------------------------------------#
def chapter2():
    while True:
        print("\n                    🎓 --- Chapter Two: File And Folder Handling --- 🎓")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃  1. 🖼 Open and Display an Image           ")
        print("                   ┃  2. 🔍 Get Image Properties               ")
        print("                   ┃  3. 🔧 Resize an Image                    ")
        print("                   ┃  4. 💾 Save Image in Different Formats    ")
        print("                   ┃  5. 🎥 Read and Display a Video File      ")
        print("                   ┃  6. 💾 Save Video in Different Format     ")
        print("                   ┃  7. 🔙 Back To Main Menu                  ")
        print("                   ┃  8. ❌ Exit                               ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━━┛")
        choice = int(input("Enter the assignment number: "))
        if choice == 1:
            open_and_display_image()
        elif choice == 2:
            get_image_properties()
        elif choice == 3:
            resize_image()
        elif choice == 4:
            save_image_in_different_format()
        elif choice == 5:
            read_and_display_video()
        elif choice == 6:
            save_video_in_different_format()
        elif choice == 7:
            chapters() 
            break
        elif choice == 8:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid input! Please try again.")

        dooro = input("\nWould you like to perform another operation? (y/n): ")
        if dooro.lower() != 'y':
            print("🎉 Returning to Main Menu... 🎉")
            time.sleep(1)
            chapters()
            break

#-chapter2 codes-#
def open_and_display_image():
    img = Image.open("apple.jpg")
    img.show()
def get_image_properties():
    img = Image.open("apple.jpg")
    print("Format:", img.format)
    print("Mode:", img.mode)
    print("Size (Width x Height):", img.size) 
def resize_image():
    img = Image.open("apple.jpg")
    resized_img = img.resize((200, 200))
    resized_img.show()
    resized_img.save("resized_image.png", format="PNG")
    print("Image resized and saved as resized_image.png")
def save_image_in_different_format():
    img = Image.open("apple.jpg")
    img.save("output_image.jpeg", format="PNG")
    print("Image saved as output_image.png")
def read_and_display_video():
    cap = cv2.VideoCapture('bad.MP4')
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Video Width: {frame_width}, Video Height: {frame_height}")
    # Resize video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Resize frame to 1300x1000
        frame_resized = cv2.resize(frame, (1300, 1000))
        cv2.imshow('Video', frame_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
def save_video_in_different_format():
    cap = cv2.VideoCapture('bad.MP4')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (200, 200))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Resize the frame
        frame_resized = cv2.resize(frame, (200, 200))
        out.write(frame_resized)

    cap.release()
    out.release()
    print("Video saved as output_video.avi")
#------------------------------------  chapter4  --------------------------------------------#
def chapter4():
    while True:
        print("\n                    🎓 --- Chapter Four: Python Sending Email SMTP --- 🎓")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃  1. 📧 Sending Email With Attachment     ")
        print("                   ┃  2. 🔙 Back To The Menu                  ")
        print("                   ┃  3. ❌ Exit                              ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━━┛")
        chapter4n = int(input("Enter the assignment number: "))
        if chapter4n == 1:
            sending_email()
            break
        elif chapter4n == 2:
            chapters()
            break
        elif chapter4n == 3:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid input! Please try again.")
def sending_email():
    sender = input("SENDER EMAIL: ")
    receivers = input("RECEIVER EMAILS (comma-separated): ").split(",")
    subject = input("SUBJECT: ")
    message = input("MESSAGE: ")
    file_path = input("FILE PATH TO ATTACH (leave blank if none): ")

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(receivers)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if file_path and os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            attach = MIMEBase('application', 'octet-stream')
            attach.set_payload(f.read())
            encoders.encode_base64(attach)
            attach.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
            msg.attach(attach)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, "nzwrnrpqrmaofxxt")  # Replace with secure handling
            server.sendmail(sender, receivers, msg.as_string())
        print("Email sent!")
    except Exception as e:
        print("Error:", e)

    #SENDER: abdalapoi223@gmail.com
    #RECEIVER1 EMAIL: imc5825058@gmail.com
    #RECEIVER2 EMAIL: cabdiqaadirkaadir@gmail.com
    #C:\Users\pc\Desktop\acmel pictures\acne.jpg
#------------------------------------  chapter5  --------------------------------------------#
def chapter5():
    while True:
        print("\n                    🎓 --- Chapter Five: Second Highest Marks --- 🎓")
        print("                   ┏━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("                   ┃  1. 📉 Display Second Lowest Marks       ")
        print("                   ┃  2. 🔙 Back To The Menu                  ")
        print("                   ┃  3. ❌ Exit                              ")
        print("                   ┗━━━━━━━━━━━━━━━━━━━━━━━━┛")
        chapter5n = int(input("Enter the assignment number: "))
        if chapter5n == 1:
            second_lowest_marks()
            break
        elif chapter5n == 2:
            chapters()
            break
        elif chapter5n == 3:
            print("❌ Exiting the program. Goodbye! 👋")
            sys.exit()
        else:
            print("❌ Invalid input! Please try again.")
def second_lowest_marks():
    students = []
    for i in range(6):
        details = input(f"Enter Student {i+1} details (ID Name Marks): ").split()
        student_id = details[0]
        student_name = details[1]
        student_marks = float(details[2])
        students.append((student_marks, student_id, student_name))

    students.sort()
    second_lowest = students[1]

    print("\nSecond Lowest Marks Student:")
    print(f"ID: {second_lowest[1]}")
    print(f"Name: {second_lowest[2]}")
    print(f"Marks: {second_lowest[0]}")
    
def members():
    while True:
        print("\n👥 **MEMBERS MENU**")
        print("1. Group A Names")
        print("2. Group A IDs")
        print("3. 🔙 Back To Main Menu")
        print("4. ❌ Exit")
        try:
            choice = int(input("👉 Enter Your Choice: "))
            if choice == 1:
                names()
                break
            elif choice == 2:
                ids()
                continue
            elif choice == 3:
                chapters()
                continue
            elif choice == 4:
                print("❌ Exiting the program. Goodbye! 👋")
                sys.exit()
            else:
                print("❌ Invalid Input! Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def names():
    while True:
        print("\n👥 **GROUP A NAMES**")
        print("1. Abdiqadir Caydiid Abshir")
        print("2. Abdullahi Abdiweli Adam")
        print("3. Ismail Ibrahim Abdirahim")
        print("4. Abdiqadir Mohamed Hassan")
        print("5. Mohamed Abdullahi Salaad")
        print("\n🛠 OPTIONS")
        print("1. 🔙 Back To Members Menu")
        print("2. 🔙 Back To Main Menu")
        print("3. ❌ Exit")
        try:
            choice = int(input("👉 Enter Your Choice: "))
            if choice == 1:
                members()
                break
            elif choice == 2:
                chapters()
                continue
            elif choice == 3:
                print("❌ Exiting the program. Goodbye! 👋")
                sys.exit()
            else:
                print("❌ Invalid Input! Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def ids():
    while True:
        print("\n🔢 **GROUP A IDS**")
        print("🆔 765")
        print("🆔 767")
        print("🆔 816")
        print("🆔 738")
        print("🆔 828")
        print("\n🛠 OPTIONS")
        print("1. 🔙 Back To Members Menu")
        print("2. 🔙 Back To Main Menu")
        print("3. ❌ Exit")
        try:
            choice = int(input("👉 Enter Your Choice: "))
            if choice == 1:
                members()
                break
            elif choice == 2:
                chapters()
                continue
            elif choice == 3:
                print("❌ Exiting the program. Goodbye! 👋")
                sys.exit()
            else:
                print("❌ Invalid Input! Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")
              
# Start the main menu================
chapters()
