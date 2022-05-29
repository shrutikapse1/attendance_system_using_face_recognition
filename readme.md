
#  Attendance System Using Face Recognition

### Requirements
- Editor - Visual studio code
- Database - MySql
- Python 3.6+ 


### What steps you have to follow to run code??
- Download or clone my Repository to your device
- Type `pip install -r requirements.txt` in command prompt(this will install required package for project)
- Create a `data`, `college_images` and `Attendance_Report` folder in a project folder.
- Add `attendance.csv` in `Attendance_Report` folder.
- Add `main.py`, `student.py`, `train.py`, `help.py`, `face_recognitionl.py`, `developerl.py`, `haarcascade_frontalface_default`,`tempCodeRunnerFile.py`, `setup.py`, `classifier.xml`, `favicon.ico` in project folder
- Create database and table in MYSQL workbench:
  Queries Used 
  - CREATE DATABASE face_recognition;
  - USE face_recognition;
  - CREATE TABLE student
    (
        Dep varchar(45),
        course varchar(45),
        Year varchar(45),
        Semester varchar(45),
        id varchar(45) PRIMARY KEY,
        Name varchar(45),
        Division varchar(45),
        Roll varchar(45),
        Gender varchar(45),
        Dob varchar(45),
        Email varchar(45),
        Phone varchar(45),
        Address varchar(45),
        Teacher varchar(45),
        PhotoSample varchar(45)
    );
- Run `main.py` file using `python main.py`
- For `conn=mysql.connector.connect(user="root",password="root123",host="localhost",database="face_recognition")`
  present in `student.py` and `face_recognitionl.py` replace password with your MYSQL password.  
   
### Specifications
- `Student Details` 
- `Train Image` 
- `Face Detector`
- `Attendance Details`
- `Photos`
- `Developer`
- `Help Desk`
- `Exit` 

### Project flow & explaination

- After you run the project first of all register student face and other information so that system can identify student, so click on register Student Details
- Register the student by filling details of `current course` and `student information`. It contains 5 buttons providing operation
  `Save`, `Update`,`Delete`,`Reset`,`Take Photo Sample`.  
  (To perform this operation database should be created whose queries mention in steps to follow section and connection code should be updated as mention in steps to follow section)

- After clicking `Take Photo Sample` button. A camera window will pop up and it will detect your Face and take upto 100 Images and stored in the folder named `data`. more you give the image to system, the better it will perform while recognising the face.

- At right side of panel you can see saved information in database 

- Then you have to close `Student Details` window and click on `Train Image` button, It will train the model and convert all the Image into numeric format so that computer can understand. we are training the image so that next time when we will show the same face to the computer it will easily identify the face.
   
- After training model close `Train Image` and click on `Face Detector`, after that click on `Face Recognition` button after which A camera window will pop up and it will detect student Face and display student details and attence will mark for particular student in `attendance.csv` file
  to close pop up window of camera press `enter` button.
  (connection code should be updated as mention in steps to follow section)

- After that close `Student Details` window and click on `Attendance Details` button which has 3 buttons 
  - `Import CSV` which will display attendance details of student marked in csv to right panel in tabular format.
  - `Export CSV` using this button you can export data of daily attendance to other csv file (shruti.csv)
  - `Reset` which will clear entry fields 

- `Photos` section will redirect you to folder where captured images are stored.

- `Developer` contains my short introduction, 
   `Help Desk` has the details to contact me and by selecting `Exit` you can exit through application.

### Links

[Desktop Application Link](https://drive.google.com/drive/folders/17bkaevr7t6f91EAtZG-fFj78Kpe-2s-H?usp=sharing)

### TECHNOLOGY USED:

- tkinter for whole GUI
- OpenCV for taking images and face recognition (cv2.face.LBPHFaceRecognizer_create())
  CSV, Numpy, Pandas, datetime etc. for other purposes.
 

