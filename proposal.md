1. **The Big Idea**
This is a simple plagiarism detection tool for content creators and students. We see an increasing demand for a free, simple plagiarism checker as most of the ones available online are not free and might not be accurate.

The simple idea here is, for a given body of documents, e.g. a doc., we want to find pairs of documents witth a lot of text in common. To detect plagiarism, We are looking at using a natural language processing library along with the search API to search the result pages of a Google search. 

It is very likely that a plagirizer will take only part of a plagirized document, reorder pieces, or rewords the contents.  Since the determinant of a good plagiarism checker is its accuracy and comprehensiveness, our ultimate goal is to build a checker that can find all such pairs of document in open-access sources without have to compare all documents on the web. Our minimum viable product will be a checker that can first breaks down an entire document into semantically relevant and logical phrases and sentances. then ask the user to input a URL so that the software can start checking for plagiarism into locals portals. 

2. **Learning Goals**
This project will allow us to deepen our understanding of the Python language and  get our hands on the idea of string matching. Plagiarism checker is one of the beginner examples of natural language processing, therefore, we will also gain exposure to the bigger picture. 

补充ind. learning goal

3. **Project Implementation Plan**

We will first need to determine a threshhold of plagiarism 

from .matcher: import Text, ExtendedMatch, Matcher
import os
import glob
import csv

The Matcher.match funciton will be an essential part of our program. It takes i nan argument and a group of cases to test the argument against. 

