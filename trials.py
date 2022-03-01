"""Python functions for JavaScript Trials 1."""

'''
// Print each item in the given array.
//
// Ex.:
//   > output_all_items([1, 'hello', True]);
//   1
//   hello
//   true'''
def output_all_items(items):
    for item in items:
        print(item)
    

'''
// Given an array of numbers, return an array of all even numbers.
//
// Ex.:
//   > get_all_evens([7, 8, 10, 1, 2, 2]);
//   [8, 10, 2, 2]
'''
def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

'''
// Given an array, return all elements at odd numbered indices.
//
// Ex.:
//   > get_odd_indices([1, 'hello', True, 500]);
//   ['hello', 500]
'''
def get_odd_indices(items):
    new_list = []
    for i in range(1, len(items), 2):
        new_list.append(items[i])
    return new_list

'''
// Given an array, output a numbered list.
//
// Ex.:
// > print_as_numbered_list([1, 'hello', True]);
// 1. 1
// 2. hello
// 3. true
'''
def print_as_numbered_list(items):
    count = 1
    for item in items:
        print(str(count) + ".", item)
        count += 1
    
'''
// Return an array of numbers in a certain range.
//
// Ex.:
// > get_range(0, 5);
// [0, 1, 2, 3, 4]
//
// > getRange(1, 3);
// [1, 2]
'''
def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)
    return nums

'''
// Given a string, return a string where vowels are replaced with '*'.
//
// Ex.:
//   > censor_vowels('hello world');
//   'h*ll* w*rld'
'''
def censor_vowels(word):
    sensored = []
    for char in word:
        if char in "aeiou":
            sensored.append("*")
        sensored.append(char)
    return "".join(sensored)

'''
// Given a string in snake case, return a string in upper camel case.
//
// Ex.:
//   > snake_to_camel('hello_world');
//   'HelloWorld'
'''
def snake_to_camel(string):
    camel_case = []
    string.split("_")
    for word in string.split("_"):
        camel_case.append(word.capitalize())
    return "".join(camel_case)

'''
// Return the length of the longest word in the given array of words.
//
// Ex.:
//   > longest_word_length(['hello', 'world']);
//   5
//
//   > longestWordLength(['jellyfish', 'zebra']);
//   9
'''
def longest_word_length(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

'''
// Truncate repeating characters into one character.
//
// Ex.:
//   > truncate('aaaabbbbcccca');
//   'abca'
//
//   > truncate('hi***!!!! wooow');
//   'hi*! wow
'''
def truncate(string):
    result = [string[0]]
    count = 1
    while count < len(string):
        if string[count] != string[count - 1]:
            result.append(string[count])
        count += 1
    return "".join(result)

'''
// Return true if all parentheses in a given string are balanced.
//
// Ex.:
// > has_balanced_parens('()');
// true
//
// > has_balanced_parens('((This) (is) (good))');
// true
//
// > has_balanced_parens('(Oh no!)(');
// false
function hasBalancedParens(string) {
  let parens = 0;

  for (const char of string) {
    if (char === "(") {
      parens += 1;
    } else if (char === ")") {
      parens -= 1;

      if (parens < 0) {
        return false;
      }
    }
  }

  return parens === 0;
}
'''
def has_balanced_parens(string):
    parens = 0
    i = 0
    k = -1
    for word in string.split():
        while parens == 0:
            if word[i] == "(":
                if word[k] != ")":
                    parens = 1
        i += 1
        k -= 1


def compress(string):
    pass  # TODO: replace this line with your code
