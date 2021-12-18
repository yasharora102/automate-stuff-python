## Practice Questions
### 1. What is the function that creates Regex objects?
```python
re.compile()
```
### 2. Why are raw strings often used when creating Regex objects?
```
Raw strings are used so that backslashes do not have to be escaped.
```
### 3. What does the search() method return?
```
It returns Match objects.
```
### 4. How do you get the actual strings that match the pattern from a Match object?
```python
group()
```
### 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
```
Group 0: Entire match
Group 1: First set of parentheses
Group 2: Second set of parentheses
```
### 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
```
By backslash (\)
```
### 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
```
No groups: list of strings returned. 
Groups present: list of tuples of strings returned.
```
### 8. What does the | character signify in regular expressions?
```
Signifies matching “either, or” between two groups.
```

### 9. What two things does the ? character signify in regular expressions?
```
It means 'match zero or one of the preceding group' or signify nongreedy matching.
```
### 10. What is the difference between the + and * characters in regular expressions?
```
+ matches one or more
* matches zero or more
```
### 11. What is the difference between {3} and {3,5} in regular expressions?
```
{3}:   matches exactly three instances of the preceding group.
{3,5}: matches between three and five instances.
```
### 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
```
 \d : single digit 
 \w : single word
 \s : single space character
```
### 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
```
\d : not a single digit 
\w : not a single word 
\s : not a single space character
```
### 14. What is the difference between .* and .*??
```
.* : performs greedy match 
.*?: performs nongreedy match
```
### 15. What is the character class syntax to match all numbers and lowercase letters?
```python
[a-z0-9]
```
### 16. How do you make a regular expression case-insensitive?
```
By passing re.IGNORECASE or re.I to re.compile()
```
### 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
```
. matches any chracter except the newline .
If re.DOTALL is passed as the second argument to re.compile() it will also match the newline characters.
```
### 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
```python
'X drummers, X pipers, five rings, X hens'
```
### 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
```
Add space and comments to the string passed.
```
### 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
```python
'42'
'1,234'
'6,368,745'
```
but not the following:
```
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
```
### Answer
#
```python
re.compile(r'^\d{1,3}(,\d{3})*$') 
```
### 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
```python
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
```
but not the following:
```
'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
```
### Answer
#
```python
re.compile(r'[A-Z](?:\w)+\sWatanabe')
```
### 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
```python
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
```
but not the following:
```
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'
```
### Answer
#
```python
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.IGNORECASE)
```
