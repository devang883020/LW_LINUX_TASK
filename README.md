# LW_LINUX_TASK
this is the repository for linux task:
1.Install docker inside docker:-
Installing Docker inside Docker (often referred to as "Docker in Docker" or "DinD") on a Red Hat Linux system involves setting up Docker and configuring it to run Docker containers within Docker containers.

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_inside_docker_1.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_inside_docker_2.jpg)



2.How can we use the linux as a Zoom kind platform for video streaming.
install node.js
create a nodejs project
install express socket.io
create server.js file
create index.html file for the client
run the server
install the jitsi meet from this repository:-https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-quickstart/

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_jitsi_meet.jpg)


![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_jitsi_meet_2.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_jitsi_meet_3.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_jitsi_meet_4.jpg)


3. How to launch the webserver in the docker container:
using systemctl start the docker container
create a Dockerfile
create an nginx configuration file
make a index file
build the docker image
run the docker container


![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/docker_webserver.png)



 4. Find out the command to do Email from the linux terminal:
sudo apt update
sudo apt install mailutils
sudo yum install mailx
echo "This is the body of the email." | mail -s "This is the subject" user@example.com
    

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/email_output.jpg)





5. How to run linux cli terminal in the web browser:



![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_cgi_bin_1.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_cgi_bin_2.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_cgi_bin_3.jpg)




6.Find out the command to do whatsapp message from the linux terminal:
yum install nodejs
yum install groupinstall "Development Tools"
npm install -g mudslide  login
npx mudslide send phone_number "message"


![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_whatsapp_1.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_whatsapp_2.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_whatsapp_3.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_whatsapp_4.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/linux_whatsapp_5.jpg)



7. Find the command to get the output of any command from the speaker:
    cal | espeak-ng

   
![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/text_to_speak.png)



8. how to launch the webserver in the docker container:
using systemctl start the docker container
create a Dockerfile
create an nginx configuration file
make a index file
build the docker image
run the docker container

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/web_browser_cgibin_docker_1.jpg)

![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/web_browser_cgibin_docker_2.jpg)




9.How to run linux cli terminal in the web browser:


![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/web_browser_cli.png)



10.
![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/webserver_linux.jpg)
GitHub
![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/GitHub)



11. Find out the command to do SMS from the linux terminal:
Yum install curl
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/your_account_sid/Messages.json" \
--data-urlencode "To=+1234567890" \
--data-urlencode "From=+0987654321" \
--data-urlencode "Body=Hello, this is a test message!" \
-u your_account_sid:your_auth_token
import cv2
from PIL import Image
import numpy as np

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture image from webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if not ret:
    print("Failed to capture image")
    exit()

# Convert the captured image to a format suitable for PIL
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(image)

# Detect faces in the image
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Load the sunglasses image
sunglass = Image.open("new black glass.png")

# Loop over detected faces and overlay sunglasses
for (x, y, w, h) in faces:
    # Resize the sunglasses to fit the face width
    sunglass_width = w
    sunglass_height = int(sunglass_width * sunglass.size[1] / sunglass.size[0])
    sunglass_resized = sunglass.resize((sunglass_width, sunglass_height), Image.LANCZOS)

    # Calculate position to overlay sunglasses
    y_offset = int(y + h / 4)
    x_offset = x

    # Create a mask and overlay the sunglasses
    mask = sunglass_resized.convert("RGBA")
    image_pil.paste(sunglass_resized, (x_offset, y_offset), mask)

# Convert the result back to OpenCV format and display it
result = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
cv2.imshow("Sunglass Filter", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
from PIL import Image
import numpy as np

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture image from webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if not ret:
    print("Failed to capture image")
    exit()

# Convert the captured image to a format suitable for PIL
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(image)

# Detect faces in the image
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Load the sunglasses image
sunglass = Image.open("new black glass.png")

# Loop over detected faces and overlay sunglasses
for (x, y, w, h) in faces:
    # Resize the sunglasses to fit the face width
    sunglass_width = w
    sunglass_height = int(sunglass_width * sunglass.size[1] / sunglass.size[0])
    sunglass_resized = sunglass.resize((sunglass_width, sunglass_height), Image.LANCZOS)

    # Calculate position to overlay sunglasses
    y_offset = int(y + h / 4)
    x_offset = x

    # Create a mask and overlay the sunglasses
    mask = sunglass_resized.convert("RGBA")
    image_pil.paste(sunglass_resized, (x_offset, y_offset), mask)

# Convert the result back to OpenCV format and display it
result = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
cv2.imshow("Sunglass Filter", result)
cv2.waitKey(0)
cv2.destroyAllWindows()




12.How can we make a post in telegram,instagram,facebook, discord from the linux terminal:
https://api.telegram.org/bot7439985955:AAF_bwFrD8JbAHdbj-N-eMjM-SpJS2UFI0Q/getUpdates
curl -s -X POST https://api.telegram.org/bot7326363154:AAE2TIOwBmJSuLlg7IHVYgC0ECLbnO0g4Sw/sendMessage -d chat_id=-1002231978174 -d text="qwertyui"
