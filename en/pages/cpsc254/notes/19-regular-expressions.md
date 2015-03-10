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

      -i  --ignore-case           Ignore case
      -v  --invert-match          Invert match
      -c  --count                 Print the number of matches
      -l  --files-with-matches    Print the name of each file that contains a match
      -L  --files-without-match   Print the names of files that do not contain matches
      -n  --line-number           Prefix each matching line with the number of the line within the file
      -h  --no-filename           Suppress the output of filenames for multi-file searches

  Examples

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
* **Metacharacters**: `^ $ . [ ] { } - ? * + ( ) | \` to specify more complex matches

#### Any Character

To match any character: `.`

  ```
  # Match any line that has 4+ characters and matches the regex
  grep -h '.zip' ls*
  ```

#### Anchors

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

  _A crossword puzzle helper_
  For example: What's a five-letter word whose third leter is 'j' and last letter is 'r' that means...?

  ```
  grep -i '^..j.r$' /usr/share/dict/words
  ```

#### Bracket Expressions

To match a single character from a set of characters: `[[character...]]`

  # Match any line contains the string "bzip" or "gzip"
  grep -h '[bg]zip' ls*
  ```

#### Negation
To match a single character NOT from a set of characters: `[^[character...]]`

  ```
  # Match any line contains the string "zip" NOT preceded by "b" or "g"
  grep -h '[^bg]zip' ls*
  ```

#### Traditional character ranges

  ```
  # Match any line contains strings beginning with an uppercase character
  grep -h '^[A-Z]' ls*
  ```

Notice the difference meaning between above and below

  ```
  # Match any line contains strings contains - (dash), A, Z
  grep -h '[-AZ]' ls*
  ```

#### POSIX Character Classes

POSIX was a IEEE standard to unify all the various UNIX forks and UNIX-like systems in 1988.

  ```
  ls /usr/sbin/[A-Z]*
  ```

  ```
  # Check for language
  echo $LANG
  # If it's en_US.UTF-8, system uses dictionary order aAbB..zZ;
  #   if it's POSIX, system uses collation order AB..Zab..Z.
  #   Change LANG to desired setting: export LANG=POSIX
  ```

### Quantifiers

#### `?` - Match an element zero or 1 time

We want to match 2 forms: `(nnn) nnn-nnnn` and `nnn nnn-nnnn`, where "n" is a numberal. Regex would be `^\(?[0-9][0-9][0-9]\)? [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$`

  ```
  # "(555) 123-4567"
  echo "(555) 123-4567" | grep -E '^\(?[0-9][0-9][0-9]\)? [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$'

  # "555 123-4567"
  echo "555 123-4567" | grep -E '^\(?[0-9][0-9][0-9]\)? [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$'

  # Nothing
  echo "AAA 123-4567" | grep -E '^\(?[0-9][0-9][0-9]\)? [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$'
  ```

#### `*` - Match an element 0 or more times

  ```
  # "This works."
  echo "This works." | grep -E '[[:upper:]][[:upper:][:lower:] ]*\.'

  # "This Works."
  echo "This Works." | grep -E '[[:upper:]][[:upper:][:lower:] ]*\.'

  # Nothing
  echo "this does not" | grep -E '[[:upper:]][[:upper:][:lower:] ]*\.'
  ```

#### `+` - Match and element 1 or more times

  ```
  # "This that"
  echo "This that" | grep -E '^([[:alpha:]]+ ?)+$'

  # "a b c"
  echo "a b c" | grep -E '^([[:alpha:]]+ ?)+$'

  # Nothing b/c number 9
  echo "a b 9" | grep -E '^([[:alpha:]]+ ?)+$'

  # Nothing b/c 2 spaces between c and d
  echo "abc  d" | grep -E '^([[:alpha:]]+ ?)+$'
  ```

#### `{}` - Match an element a specific number of times

    {n}     Match the preceding element if it occurs exactly n times.
    {n,m}   Match the preceding element if it occurs at least n times, but no more than m times.
    {n,}    Match the preceding element if it occurs n or more times.
    {,m}    Match the preceding element if it occurs no more than m times.

  ```
  # "(555) 123-4567"
  echo "(555) 123-4567" | grep -E '^\(?[0-9]{3}\)? [0-9]{3}-[0-9]{4}$'

  # "555 123-4567"
  echo "555 123-4567" | grep -E '^\(?[0-9]{3}\)? [0-9]{3}-[0-9]{4}$'

  # Nothing
  echo "AAA 123-4567" | grep -E '^\(?[0-9]{3}\)? [0-9]{3}-[0-9]{4}$'
  ```

### Putting regular expressions to work

  ```
  # Randomize phone list
  for i in {1..10}; do echo "(${RANDOM:0:3}) ${RANDOM:0:3}-${RANDOM:0:4}" >> phonelist.txt; done
  ```

#### Searching for text with less


#### Searching for text with vim
