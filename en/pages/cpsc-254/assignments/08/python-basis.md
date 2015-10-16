# Assignment 08 - Python Basis

## Description

(10 pts - Nothing to submit) Prepare your development environment for python. Install `python3` (version 3.4.x or newer) and any text editor or IDE of your choice. It does not require to use python in Linux; however I will test your python programs on my Ubuntu machine. So make sure you test yours before submitting.

Execute below command in the terminal to download and uncompress the assignment file:

```
wget -qO- http://j.mp/1k8L15f | tar zxf -
```

You will see the "python-basis" folder in your current working directory. In this folder, there are 7 incomplete python files and a "test.py" file, which contains a simple function to display the test cases' results. In each python file, read the `docstring` (comments) and complete the incomplete functions. I have already created some test cases in the main function of each file. It might not completely cover all cases. You can simply execute the python file to see if you have it correct. For example:

```
./foobar.py
```

```
foobar
 OK  got: '1' - expected: '1'
 OK  got: 'foo' - expected: 'foo'
 OK  got: 'bar' - expected: 'bar'
 OK  got: 'foobar' - expected: 'foobar'
 OK  got: '40' - expected: '40'
```

As you see the check the status at the beginning of each test case. If you have all 'OK', you have passed all existing test cases; otherwise, debug the misbehaved ones, which has a 'X'. Here is a list of problems:

1. (4 pts) hello.py
2. (6 pts) foobar.py
3. (6 pts) sum_exponents.py
4. (6 pts) mix_up.py
5. (6 pts) match_ends.py
6. (6 pts) remove_adjencent: loop
7. (15 pts) twin_primes.py


## Submission
Compress all your python files (*.py) as gzip file and submit it via TITANium. From the directory "python-basis", you can issue the below command and replace "cwid" with your CWID number.:

```
tar cvzf assignment-08_cwid.tar.gz *.py
```


## Grading
This assignment worth total of 62 points including 3 points for submission format.
