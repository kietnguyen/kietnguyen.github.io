# Assignment 07 - Regular Expression

## Description

You can download the package for this assignment by issuing below command in the terminal:

```
wget -qO- http://j.mp/1LgRkti | tar zxf -
```

The above command will download and uncompress the assignment package. You will see the "regex-exercise" folder in your current directory. In this folder, there is answer template file "assignment-07_123456789.md" and 9 other text files for testing your regular expressions in questions 1 - 9. For your answer template file, correct your CWID, and fill in your answers the following questions.

We want to find the regular expression to match all desired line, which starts with the word "match", and ignore those unwanted lines, which starts with the word "skip". The test files don't include the words "match" or "skip"; however, the result of your command should only display of the desired lines. We will use `grep -Ex [pattern] [file]` command to test our regular expressions, where `-E` is to interpret the pattern as an Extended Regular Expression, and `-x` is to match the whole line. You only need to write the patterns in your final text file.

1. Quantifier

  ```
  match   abc
  match   ac
  skip    bac
  ```

  `$ grep -Ex 'ab?c' abc.txt`

1. (2 pts) Anchor metacharacters

  ```
  match   Mission: successful
  skip    Last Mission: successful
  skip    Mission: successful upon capture of target
  ```

  `$ grep -Ex [regex] mission.txt`

1. (2 pts) Escape metacharacter

  ```
  match   cat.
  match   896.
  match   ?=+.
  skip    c9+
  ```

  `$ grep -Ex [regex] dot.txt`

1. (2 pts) Alternation

  ```
  match   I love cats
  match   I love dogs
  skip    I love logs
  ```

  `$ grep -Ex [regex] love.txt`

1. (2 pts) Character set

  ```
  match   hog
  match   dog
  skip    bog
  ```

  `$ grep -Ex [regex] animals.txt`

1. (2 pts) Character range

  ```
  match   MONDAY
  skip    tuesday
  match   WEDNESDAY
  skip    thursday
  ```

  `$ grep -Ex [regex] day.txt`

1. (2 pts) Character range

  ```
  match    3.14529
  match    -255.34
  match    128
  match    1.9e10
  match    123,340.00
  skip     720p
  ```

  `$ grep -Ex [regex] number.txt`

1. (4 pts) What regular expression can we use to match these 2 following phone patterns `### ### ####` and `###-###-####`, where `#` is a number digit? Below are the expected output, the rest does not match our patterns.

  ```
  110-237-1523
  179 184 2479
  899-277-1014
  ```

  `$ grep -Ex [regex] phone-list.txt`

1. (4 pts) What regular expression would you use to check whether a number is in the range of 0 to 255, with no leading zero? The file `255.txt` contains different numbers, one number per line.

  `$ grep -Ex [regex] 255.txt`

1. (4 pts) What regular expression would we use to check whether a variable is valid? A valid variable must contain alphabets, digits, and underscores, and cannot start with a digit.

1. (4 pts) What regular expression would we use to check whether a username is valid? A valid username must contain alphabets, digits, underscores, and hyphens, and have at least 6 and at most 15 characters.

1. (4 pts) A slug is the end part of a URL which identifies a page using human-readable keywords. It usually contains lowercase English alphabet letters, digits, and hyphens. What regular expression would you use?

1. (4 pts) What regular expression can we use for a SIMPLE email validator? This validator doesn't need to eliminate all the bad email address, so keep it simple. The email is composed of:

  * the username must contain at least 4 lowercase letters, numbers, underscores, dots, or hyphens;
  * the at-sign (@);
  * the domain must contain 2 or more lowercase letters, numbers, underscores, or hyphens;
  * a dot;
  * the extension must contain 2 to 6 lowercase letters or dots.

1. (4 pts) What regular expression would you use to check for a ROMAN number in range of I to X?


## Submission
Submit your final text file via TITANium


## Grading
This assignment is worth total of 44 points including 4 points for submission format.
