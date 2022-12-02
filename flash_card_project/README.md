# Day 31 Flash Card Practice 

Current file set up is set to practice the 100 most frequent words in the French language.
Can be easily configured to support any language by updating the constant variables PRACTICE_LANGUAGE and LANGUAGE
and then adding a csv into the data folder with a column row structure shown below.

|  Language 1   |   Language 2  |
| ------------- | ------------- |
|     word      |  translation  |
|     word      |  translation  |

### Current Features (Dec 1st 2022)
* Displays a random word from the list of words to learn for 3 seconds and then reveals the correct translation
  User then checks the corresponding button to indicate whether they knew the word or did not no the word.
  If word if known then it is removed from the word list and the save file is updated. On subsequent runs the program
  will use the save file words_to_learn.csv which contains only words that still need to be mastered.
  
### Planned Features 
* Start screen explaining game play
* Ability to reset game which will reintroduce all words from original word list 
* On screen tracker of how many words have been learned and how many are remaining
