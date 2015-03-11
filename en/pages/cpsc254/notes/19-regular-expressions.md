# Regular Expressions

## What are Regular Expressions?

* Are symbolic notations used to identify patterns in text
* Are supported by many command line tools and by most programming langulates
* Not all regular expressions are the same
* We will limit ourselves to **POSIX standards**

## grep

* Derived from "**g**lobal **r**egular **e**xpression **p**rint"
* Searches text files for the occurrence of specified regular expression and outputs any line containing a match to standard output
* _Recall_: use `grep` to search for fixed strings

  ```
  # list all the files in the /usr/bin directory whose names contain the substring "zip"
  ls /usr/bin | grep zip
  ```

* Options and arguments: `grep [options] regex [file...]`

  ```
  # Matching control
  -i  --ignore-case
          Ignore  case  distinctions  in  both  the  PATTERN and the input files.

  -v  --invert-match
          Invert the sense of matching, to select non-matching lines.

  # Output control
  -c  --count
          Print a count of matching  lines for  each  input  file

  -l  --files-with-matches
          Print the name of each file that contains a match

  -L  --files-without-match   
          Print the names of files that do not contain matches

  -n  --line-number           
          Prefix each matching line with the number of the line within the file

  -h  --no-filename           
          Suppress the output of filenames for multi-file searches
  ```

  **Example**

  ```
  # SETUP
  mkdir grep_examples && cd $_
  ls /bin > ls-bin.txt
  ls /usr/bin > ls-usr-bin.txt
  ls /sbin > ls-sbin.txt
  ls /usr/sbin > ls-usr-sbin.txt
  ll ls-*
  ```

  ```
  # DEMO
  # - Search string "bzip" in the listed files
  grep bzip ls*

  # - Search string "bzip" in the listed files with line numbers
  grep -n bzip ls*

  # - Search string "bzip" in the listed files without filenames
  grep -h bzip ls*

  # - Search number of matches in the listed files
  grep -c bzip ls*

  # - Search and list files that contain matches
  grep -l bzip ls*

  # - Search and list files that do not contain a match
  grep -L bzip ls*

  ```

## Metacharacters and Literals

* **Literal charaters**: to specify characters in search string
* **Metacharacters** `^ $ . [ ] { } - ? * + ( ) | \ `: to specify more complex matches

### Any Character

* To match any character: `.`

  ```
  # Match any line that has 4+ characters and matches the regex
  grep -h '.zip' ls*
  ```

### Anchors

* To match at the beginning of the line: `^`
* To match at the end of the line: `$`

  ```
  # Match any line contains the string "zip" at the beginning
  grep -h '^zip' ls*
  # Match any line contains the string "zip" at the end
  grep -h 'zip$' ls*
  # Match any line contains the exact string "zip"
  grep -h '^zip$' ls*

  # Match any blank lines w/ line number
  grep -hn '^$' ls*
  ```

  **_A crossword puzzle helper_**
  What's a five-letter word whose 3rd leter is _j_ and last letter is _r_ that means...?

  ```
  grep -i '^..j.r$' /usr/share/dict/words
  ```

### Bracket Expressions and Character Classes

* To match a single character from a set of characters: `[[character...]]`

  ```
  # Match any line contains the string "bzip" or "gzip"
  grep -h '[bg]zip' ls*
  ```

#### Negation

* To match a single character NOT from a set of characters: `[^[character...]]`

  ```
  # Match any line contains the string "zip" NOT preceded by "b" or "g"
  grep -h '[^bg]zip' ls*
  ```

#### Traditional character ranges

* `[A-Z]`, `[a-z]`, `[0-9]`, or any combination

  ```
  # Match any line contains strings beginning with an uppercase character
  grep -h '^[A-Z]' ls*
  ```

#### POSIX Character Classes

* POSIX was a IEEE standard to unify all the various UNIX forks and UNIX-like systems in mid 1980s.

  ```
  # SETUP
  cd posix_example && cd $_
  touch {A..Z} {a..z} {0..9}
  
  # Check for language
  echo $LANG
  # If it's en_US.UTF-8, system uses dictionary order aAbB..zZ;
  #   if it's POSIX, system uses collation order AB..Zab..Z.
  #   Change LANG to desired setting: export LANG=POSIX
  
  # With LANG=en_US.UTF-8
  ls [A-D]
  ls [A-d]

  # Observe when LANG=POSIX
  LANG=POSIX
  ls [A-D]
  ls [a-d]
  ```

See _POSIX Character Classes_ in Table 19-2

### Basic vs. Extended Regular Expressions

POSIX splits into 2 kinds of regular expressions:

1. Basic regular expressions (BRE)
  * Metacharacters: `^ $ . [ ] *`
  * Extra ERE metachracters are literal characters unless escaped with `\ `
  * `grep`, `vim` use BRE

1. Extended regular expressions (ERE)
  * Extra metacharacters: `( ) { } ? + |`
  * `egrep`, `grep -E`, `less` use ERE

### Alternation

* To match a set of strings or other regular expressions

  ```
  # ERE
  grep -Eh '^(bz|gz|zip)' ls*
  
  echo AAA | grep -E 'AAA|BBB'
  echo BBB | grep -E 'AAA|BBB'
  echo CCC | grep -E 'AAA|BBB'

  # BRE
  echo AAA | grep 'AAA\|BBB'
  echo BBB | grep 'AAA\|BBB'
  echo CCC | grep 'AAA\|BBB'
  ```

### Quantifiers

* `?` - Match an element 0 or 1 time
* `*` - Match an element 0 or more times
* `+` - Match and element 1 or more times   
* `{}` - Match an element a specific number of times
  
  ```
  {n}     Match the preceding element if it occurs exactly n times.
  {n,m}   Match the preceding element if it occurs at least n times, but no more than m times.
  {n,}    Match the preceding element if it occurs n or more times.
  {,m}    Match the preceding element if it occurs no more than m times.
  ```

  **Example 1**: Quatifier * 
  
  ```
  # "This works."
  echo "This works." | grep -E '[A-Z][A-Za-z ]*\.'

  # "This Works."
  echo "This Works." | grep -E '[A-Z][A-Za-z ]*\.'

  # Nothing
  echo "this does not" | grep -E '[A-Z][A-Za-z ]*\.'
  ```

  **Example 2**: Quantifier ? +
  ```
  # "This that"
  echo "This that" | grep -E '^([A-Za-z]+ ?)+$'

  # "a b c"
  echo "a b c" | grep -E '^([A-Za-z]+ ?)+$'

  # Nothing b/c of number 9
  echo "a b 9" | grep -E '^([A-Za-z]+ ?)+$'

  # Nothing b/c of 2 spaces between c and d
  echo "abc  d" | grep -E '^([A-Za-z]+ ?)+$'
  ```

  **Example 3**: Match 2 forms: `(nnn) nnn-nnnn` and `nnn-nnn-nnnn`, where "n" is a numberal. Regex might be `^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$`

  ```
  # QUANTIFIER: ? {}
  # "(555) 123-4567"
  echo "(555) 123-4567" | grep -E '^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$'

  # "555-123-4567"
  echo "555 123-4567" | grep -E '^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$'

  # Nothing
  echo "AAA-123-4567" | grep -E '^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$'

  # Seem to work, but...
  echo "(555-123-4567" | grep -E '^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$'
  echo "555)-123-4567" | grep -E '^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$'
  echo "(555)-123-4567" | grep -E '^\(?[0-9]{3}\)?-[0-9]{3}-[0-9]{4}$'

  # Let's use alternation
  echo "(555-123-4567" | grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
  echo "555)-123-4567" | grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
  echo "(555)-123-4567" | grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
  echo "555-123-4567" | grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
  echo "(555) 123-4567" | grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
  ```
