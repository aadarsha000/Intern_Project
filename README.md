# School Management System

A simple Django and Django restframework website. This website contains:-
 - User Access
 - User Role Management
 - User Permission Management
 - User Group Management
 - Social Sign up (Google)
 - API using auth token


### This project contains three diffrent types of user or group with following permission i.e
 - Principal
   - Can view, add, update, delete anything in project
 - Teacher
   - Can view profile, notice, event
   - can add, update, delete the notice, event
 - Student
   - Can view profile, notice, event


### Admin/Principal View 

![Admin view](https://github.com/aadarsha000/Intern_Project/assets/116047355/3e94e8a3-0404-4b43-9b76-a973686a7c40)

### Teacher View

![teacherpanel](https://github.com/aadarsha000/Intern_Project/assets/116047355/3e57da19-fe8c-4c44-90c4-2b9fc19a2d49)

### Student View

![studentpanel](https://github.com/aadarsha000/Intern_Project/assets/116047355/80fd7977-9dea-4d79-87ca-ec55b5921850)

### Login

#### Normal login

![login](https://github.com/aadarsha000/Intern_Project/assets/116047355/b2b74156-6a96-4221-bacc-a9b6e603a2bf)

#### Social login

![Screenshot 2023-06-01 155917](https://github.com/aadarsha000/Intern_Project/assets/116047355/53f6ae33-ca26-40e6-8bed-bf8055f0c2c5)
![sociallogin2](https://github.com/aadarsha000/Intern_Project/assets/116047355/c4022bfe-88dd-458e-acd9-e3402d4b2000)

### Signup
![singup](https://github.com/aadarsha000/Intern_Project/assets/116047355/faa23a54-521e-482d-b606-d00f92b9acb6)
![singup2](https://github.com/aadarsha000/Intern_Project/assets/116047355/d5d138be-6907-40ea-99e1-7d0c05800c3e)

### Assign Teacher To Subject
Only the user role Principal and group Principal can assign the teacher to their respective subjects
![assignteacher](https://github.com/aadarsha000/Intern_Project/assets/116047355/1e171ec6-52ea-4ed0-93b8-9b8e136dc2e0)

### Enroll Student To Course
Only the user role Principal and group Principal can enroll the students to their respective course
![enrollteacher](https://github.com/aadarsha000/Intern_Project/assets/116047355/4c3381cb-84e2-4614-bd17-0ca165f72f24)

### Teacher list
Only the user role Principal and group Principal can view the list of teacher
![teacherlist](https://github.com/aadarsha000/Intern_Project/assets/116047355/52ef1fb6-392b-49f8-864b-ef2c1140280a)

### Student List
Only the user role Principal and group Principal can view the list of Students
![studentlist](https://github.com/aadarsha000/Intern_Project/assets/116047355/a34c8df6-4293-4308-9699-40e1f815ff33)

### Events
 - User with role principal and teacher both can view, add, edit, delete the events
 - User with role student can only view
![Screenshot 2023-06-01 154650](https://github.com/aadarsha000/Intern_Project/assets/116047355/474faed2-b45e-4168-ad44-f22583ea43e6)
![Screenshot 2023-06-01 154725](https://github.com/aadarsha000/Intern_Project/assets/116047355/2fede8d1-cacc-43e6-ade9-b73c55e9be81)

### Notice
 - User with role principal and teacher both can view, add, edit, delete the events
 - User with role student can only view
![Screenshot 2023-06-01 154803](https://github.com/aadarsha000/Intern_Project/assets/116047355/3eb96197-79b3-4fce-bef8-376ee1b0fd2b)
![Screenshot 2023-06-01 154841](https://github.com/aadarsha000/Intern_Project/assets/116047355/1507086b-8d90-40bd-a772-71e9e034663e)

### Course
 - User with role principal  can view, add, edit, delete the course
 - User with role student can only view course
 ![Screenshot 2023-06-01 155116](https://github.com/aadarsha000/Intern_Project/assets/116047355/f405355c-8bc5-4e4b-b0c9-37ec619e4052)
 ![Screenshot 2023-06-01 155236](https://github.com/aadarsha000/Intern_Project/assets/116047355/677e451e-1d1c-42a1-82e0-7c2de9e72633)
 
### Subjects
 - User with role principal  can view, add, edit, delete the subjects
 - user with role studen can only view subjects
 ![Screenshot 2023-06-01 155310](https://github.com/aadarsha000/Intern_Project/assets/116047355/5cc44ae5-fa6f-4689-9797-ac987f7e4b93)
![Screenshot 2023-06-01 155401](https://github.com/aadarsha000/Intern_Project/assets/116047355/0ef5fed5-780f-49b3-8ddd-d6273d54bfef)

### API
- To access the API user should pass authorization token with login credential
- if authorization token with login credential is no provide following error is shown
![restapi2](https://github.com/aadarsha000/Intern_Project/assets/116047355/984c7526-e260-4590-8e34-a97ea365ea52)
- if authorization token with login credential is provide then result is recived
![restapi](https://github.com/aadarsha000/Intern_Project/assets/116047355/1b61f386-1e66-436f-ac51-0a8ddeff963a)
