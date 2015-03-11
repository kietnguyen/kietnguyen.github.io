# Text Processing

## Applications of Text

* **Documents**: written in plain text and/or in a _markup language_ (e.g. LaTex, Markdown, etc.)
* **Web pages**: written in HTML (Hypertext Markup Language) or XML (Extensible Markup Language)
* **Email**: contains header (source of the message), body (content of the message), attachment (converted into text presentation)
* **Printer output**: as plain text or PostScript (if contains graphics)
* **Program source code**

## Manipulating Text

### cat

* To concatenate files and print on the standard output

  ```
  -A  --show-all        
        Display non-printing characters (^ and M- notation), TAB (^I), EOL ($)
        
  -n  --number          
        Display line number

  -s  --squeeze-blank   
        Suppress repeated blank lines
  ```

  **Example**

  ```bash
  # Simple word processor
  cat > foo.txt
  # Type some text with TAB and multiple newlines
  cat -A foo.txt
  cat -ns foo.txt
  ```

### sort

### Slicing & Dicing

#### cut

To extract a section of text from a line and output the extracted section to standard output

    -c char_list

## Comparing Text

### diff

* To detect the differences between files or source trees

  ```
  diff file1.txt file2.txt
  ```

  `diff` change commands

  ```
  r1ar2     Append the lines at the position r2 in the second file to the position r1 in the first file.
  r1cr2     Change (replace) the lines at position r1 with the lines at the position r2 in the second file.
  r1dr2     Delete the lines in the first file at position r1, which would have appeared at range r2 in the second file
  ```

  ```
  diff -u file1.txt file2.txt
  ```

  _diff_ Unified Format Change 

  ```
  blank     Is shared by both files
  -         Was removed from the first file
  +         Was added to the first file
  ```

### patch

* To apply changes to text files
* Benefits:

  * The _diff_ file is very small
  * The _diff_ file concisely shows the change being made

* To prepare for a patch: `diff -Naur old_file new_file > diff_file`

  ```
  -N  --new-file  
          Treat absent files as empty

  -a  --text      
          Treat all files as text

  -r  --recursive
          Support recursion of a directory ree
  ```

  ```
  diff -Naur file1.txt file2.txt > patchfile.txt
  ```
  
* To apply a patch: `patch < diff_file`

  ```
  patch < patchfile.txt
  ```

## Editing on-the-fly

### sed

* Short for stream editor
  
  ```
  echo front | sed 's/front/back/'
