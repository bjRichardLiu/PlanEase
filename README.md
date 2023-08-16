# PlanEase
Simplify college student's weekly planning and optimize sleep schedules<br>
[Demo Video](https://youtu.be/qjd_NjF2NSU)<br>
[Won 4th place in beginner track in DualHacks](https://devpost.com/software/planease?ref_content=my-projects-tab&ref_feature=my_projects)<br>

## Build with
[Flask](https://github.com/pallets/flask)<br>
[Jinjia](https://github.com/pallets/jinja/)<br>
[Flask-Web-App-Tutorial](https://github.com/techwithtim/Flask-Web-App-Tutorial)

## Inspiration

Creating a plan scheduler to tackle the mental health and well-being challenges faced by college students resonates deeply with me. Throughout my time in higher education, We've grappled with the stress that arises from an array of tasks and the uncertainty of where to begin. The pressure to manage multiple responsibilities often leads to overwhelming feelings. This struggle has inspired us to develop a tool that can offer practical solutions. By designing a plan scheduler, we aim to alleviate the exact challenges we've experienced firsthand.


## What it does

The functionality of the web application revolves around a simple yet powerful concept: empowering users to take control of their tasks for the week. Users input their tasks, each accompanied by its estimated duration, deadline, and their own time preferences. Using this information as a foundation, the application constructs a personalized schedule that factors in task priorities and preferred time slots. The underlying mission is to provide students with a dynamic tool that not only aids in the meticulous planning and organization of their tasks but also holds the potential to mitigate the stress and anxiety often associated with academic responsibilities.


## How we built it

For the backend, we utilized Flask and Python. To store the data, we employed SQLalchemy. For the front end, we utilized Jinja2, HTML, and CSS, resulting in a user-friendly interface. Additionally, the schedule processing was handled through the implementation of NumPy, further enhancing the application's performance.

## Challenges we ran into

As beginners in web development, understanding how HTML and CSS work was tough without any prior experience. We had only five days to learn the basics and figure out how to create and style web pages.

Since it was our first time building a web app, we struggled with passing data from the front to the back end and parsing it correctly. This required a lot of trial and error.

Working with a database for the first time wasn't a walk in the park. We encountered issues while storing and retrieving data, but we managed to overcome them with patience and perseverance.

Integrating both login and signup functionalities on the same page forced us to rethink our backend logic. Flask, our framework, didn't have a built-in option to handle multiple buttons individually, so we had to come up with a clever workaround.
Learning to use Git and collaborating with others had its ups and downs. At times, we accidentally lost some code while trying to figure out the best practices for teamwork.

Despite these challenges, we embraced the learning process, and with determination, we successfully built our web application. Each obstacle taught us valuable lessons, and we now feel more confident in our abilities for future projects.

## What we learned

We learned a lot about web development, especially how to combine the front end and back end. We also learned how to store user information in a database, as well as how to correctly retrieve those data and process them at the backend.

## What's next for PlanEase

Our next steps involve leveraging AI to enhance the scheduling process, generating more balanced and personalized schedules for our users. We aim to introduce progress tracking, providing a sense of accomplishment and motivation as tasks are completed. Additionally, we'll offer more input options, such as prioritization, to give users better control over their schedules and help them find the optimal arrangement for different types of tasks. Moreover, we plan to analyze weekly patterns and offer recommendations, such as suggesting more sleep or exercise, to further optimize our users' time management and overall well-being. 

