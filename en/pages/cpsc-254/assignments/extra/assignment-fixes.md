# (Extra credits) Assignment Fixes

## Description
The objective of this assignment is to fix any mistake that you had in your old assignments. First, create a new directory to store for this assignment, then create a new directory named "old", in which stores all old assignments you want to fix, and another one named "fixed", in which you will fix your assignments. You will create a patch file, which are the differences between all the files in the directories "old" and "fixed". You can name directories anything you like, but adjust the commands accordingly. To create a patch (diff) file, issue below command in the terminal.

```
diff -Nur old fixed > assignment-fixes.diff
```

To patch all your files in the old directory:

```
patch -d old < assignment-fixes.diff
```

Use `-R` option to reverse the patch:

```
patch -Rd old < assignment-fixes.diff
```

If you already overwrite your old files, you can re-download them from TITANium.

## Submission
Submit your final text file "assignment-fixes.diff" via TITANium.

## Grading
This assignment is for extra credits only and worth up to 64 points. You will gain half of the points that you missed.
