# CalculateGPA
This a backend project to calculate the cumulative GPA and save the subjects degrees and make some statistics to the student.



to run this program on your machine 

1. If you don't have Python first install it and add it to the path then go to the next

   - can install from : https://www.python.org/

   - **Remember**: To Add Python To Path in the Installation

   - 32-bit version:

     https://www.python.org/ftp/python/3.10.10/python-3.10.10.exe

     64-bit version:

     https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe 



**then you need to open cmd in the project file**



2. install all modules that required to run this project, all of them in requirements.txt file in the project

   - ```shell
     pip install -r requirements.txt
     ```

3. then you need to create the database, write the next code in cmd 

   - ```shell
     py manage.py migrate
     # or 
     python manage.py migrate
     ```

4. you want to run the local server

   - ```shell
     py manage.py runserver 7000
     ```

5. open your browser and write this link : http://127.0.0.1:7000/
