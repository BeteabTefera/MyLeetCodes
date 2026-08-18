# Last updated: 8/18/2026, 2:50:48 PM
from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            U: answer order doesn't matter, group the anagrams together from a list of words
               what is an anagram? two words with the same letter makeup
            M: What method is good to approach this problem in the most simpler manner?
            two words are anagrams when the letters sorted are equal
                
                Example: 
                    Input: strs = ["eat","tea","tan","ate","nat","bat"]
                    inside strs 'eat' and 'tea' when sorted are both equal to 'aet'

            P: Plan is to loop throught the words in list and turn them into a mini list and 
               sort then proceed to join them
                and save them in a set 
               then put them back to a list and use default dict to collect the anagrams
               return list of dict values

            I: During actual implementation i learned that we don't need sets, dict
               will use its own iteration for strings to match key and pairs

        '''
        d = defaultdict(list)
        for i in strs:
            d[(''.join(sorted(list(i))))].append(i)

        return (list(d.values()))