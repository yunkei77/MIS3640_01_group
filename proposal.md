1. **The Big Idea**
This is a simple plagiarism detection tool for content creators and students. We see an increasing demand for a free, simple plagiarism checker as most of the ones available online are not free and might not be accurate.

The simple idea here is, for a given body of documents, e.g. a doc., we want to find pairs of documents witth a lot of text in common. To detect plagiarism, We are looking at using a natural language processing library along with the search API to search the result pages of a Google search. 

It is very likely that a plagirizer will take only part of a plagirized document, reorder pieces, or rewords the contents.  Since the determinant of a good plagiarism checker is its accuracy and comprehensiveness, our ultimate goal is to build a checker that can find all such pairs of document in open-access sources without have to compare all documents on the web. Our minimum viable product will be a checker that can first breaks down an entire document into semantically relevant and logical phrases and sentances. then ask the user to input a URL so that the software can start checking for plagiarism into locals portals. 

2. **Learning Goals**
This project will allow us to deepen our understanding of the Python language and  get our hands on the idea of string matching. Plagiarism checker is one of the beginner examples of natural language processing, therefore, we will also gain exposure to the bigger picture. 


3. **Project Implementation Plan**

We will first need to determine a reasonable threshhold of similarity that can define to what degree of similarity will be called plagiarism. This will require research and judgement in the beginning phase.  

In python, we think the following libraries will help: 
from .matcher: import Text, ExtendedMatch, Matcher
import os
import glob
import csv

The Matcher.match funciton will be an essential part of our program. It takes i nan argument and a group of cases to test the argument against. 

4. **Project Schedule**
Since we have roughly 8 weeks to finishe the project, we will disect our project into weekly goals:

Week 1: 
        1.1 Use resources to determine a reasonable threshold for plagiarism
        1.2 Get familiar with Natural Language Processing 
        1.3 Get familiar with Matcher.match 
        1.4 Alway make changes/accomadations to the project plans whenever needed

Week 2:
        1.1 Start writing pseudo code
        1.2 Search and identify useful libraries that will be useful to the project 

Week 3: 
        1.1 Continue improve psedudo code; It's a learning process 

Week 4: 
        1.1 Start writing code

Week 5:
        1.1 By the end of the week, finish the first part of the code where we can take in a document and break it down into smaller logical pieces

Week 6:
        1.1 Start writing the second hald of the code where we aim to match similarity of the two documents

Week 7:
        1.1 A week to take a step back and examine our progress
        1.2 Make adjustment and continue writing our code

Week 8 (Submission 11/30): 
        1.1 Final check, finish all necessary debugging  


5. **Collaboration Plan**
We plan to practice agile development in which the three of us will first split up the tasks that need to be done and finish them separately. Then we will come together to integrate all of the parts. During this process, we will develop our codes in iterations which we make small adjustments and additions each time and test it out every time we make any changes to the previous codes. This way we can increase our efficiency since we will be able to locate and fix any bugs or defects at each iteration. We will also be able to get a sense of how well are the codes working at an early stage and make necessary adjustments and improvements along the way.


6. **Risks**
Since all three of us have no experience in python programming before the class, we would need to do extra researching in order to complete the project. Therefore, one of the risks we might encounter is to find the most suitable code for our project. Furthermore, it might be difficult for us to recognize which part is wrong when we encounter errors. The risks of not knowing how to fix the problems is quite high for us. 


7. **Additional Course Contnet**
As far as the course is going now, all the topics are helpful to our project. The more we know about Python, the more we can use in our coding. Most importantly, we need to know how to utilize the “big data” in order to achieve our goal. As for now, the “iteration” and “Strings” topics would be helpful in organizing our major idea. We would also need to know how to make our checker work more comprehensible and efficiently. 

Introducing more of Natural Language Processing will also be helpful. 

