# What is it?
A **Regex** (short for _regular expression_) is a sequence of characters that specifies another sequence, pattern, or category of characters in a text.

Regular expressions are widely used in programming and text processing, appearing in many applications such as internet search engines, text and code editors, lexers, linters, parsers, and more.

# How to test it?
To test regular expressions, you can use online tools such as [Replit](https://replit.com/languages/julia) or [regex101](https://regex101.com/). Replit allows you to run code online, while regex101 provides a visual interface to test regular expressions on sample text.

# When to use it?
A programmer has likely had to scan through text to find or extract a sequence or pattern of information, or to process text input that may be in an invalid format. These tasks often involve gathering data as part of a larger process, so being able to correctly do them is essential. The problem comes from the scope of the task - if there are more requirements to be analyzed, it can greatly increase the complexity of it.

Let's give a more detailed description of the mentioned tasks before:
1. Retrieve all date occurrences from a text. Date fields are separated by a forward slash (/). Day and month fields can be with or without preceding 0, for values between 1-9, and year field can be with 1 to 4 digits.
2. Retrieve the digits from a phone number. The phone number is from Brazil. Country code is not necessary. Parentheses for area code, space between fields and dash (-) before the last 4 digits are optional.

Here are two implementations in Julia, using Regex, of how to solve the tasks above.

Task 1:
```julia
text = """
    Source Text/File.
    Matching examples:
    12/02/2012
    1/10/984
    07/4/2
    Non-matching examples:
    123/4/2000
    3/499/567
    10/10/10101
"""
re = Regex("\\s(\\d{1,2}/\\d{1,2}/\\d{1,4})\\s")
for m in eachmatch(re, text)
    println(m[1])
end
```
Task 2:
```julia
text = """
    Source Phone.
    Matching examples:
    (88) 88888-8888
    99 99999 9999
    12123451234
    Non-matching examples:
    (88( 88888-8888
    99 9999 9999
    121234123
"""
re = Regex("\\(?(\\d{2})\\)? ?(\\d{5})[- ]?(\\d{4})")
for m in eachmatch(re, text)
    println(string(m[1], m[2], m[3]))
end
```
In these cases, we successfully avoided performing complex character-by-character string checks to find what we need, while still allowing for some flexibility. However, a regular expression might be very complex to write and debug, especially for more advanced patterns.

We can define some of its benefits and drawbacks:
## Benefits
- Time-saving: With Regex, you can automate tasks that would take a lot of time manually.
- Precision: Regex allows you to select exactly the information you need, without selecting irrelevant information.
- Portability: Regex is supported by most programming languages, so you can use the same pattern to search or replace information in different languages.
- Flexibility: Regex can be used to search for different patterns in different types of data.

## Drawbacks
- Steep learning curve: Regex has its own syntax, which can be difficult to learn and master, especially for beginners.
- Complexity: Regex can be very complex, especially for large or complicated patterns.
- Performance: Depending on the size of the input data and the complexity of the pattern, Regex can be slower than other methods of text processing.

In the end, as the complexity of the task at hand can vary greatly, it's up to the programmer to decide whether using Regex it is the best approach or not.