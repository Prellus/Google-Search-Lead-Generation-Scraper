import re

class SearchResults(object):
    '''Stores the search results'''
    def __init__(self, items=None):
        self._results = items or []
    
    def links(self):
        '''Returns the links found in search results'''
        return [row.get('link') for row in self._results]
    
    def titles(self):
        '''Returns the titles found in search results'''
        return [row.get('title') for row in self._results]
    
    def text(self):
        '''Returns the text found in search results'''
        return [row.get('text') for row in self._results]
    
    def hosts(self):
        '''Returns the domains found in search results'''
        return [row.get('host') for row in self._results]
    
    def results(self):
        '''Returns all data found in search results'''
        return self._results
    
    def __getitem__(self, index):
        return self._results[index]
    
    def __len__(self):
        return len(self._results)

    def __str__(self):
        return '<SearchResults ({} items)>'.format(len(self._results))
    
    def append(self, item):
        '''appends an item to the results list.'''
        self._results.append(item)
    
    def extend(self, items):
        '''appends items to the results list.'''
        self._results.extend(items)

    def extract_emails(self):
        '''Extracts and returns emails found in search results text'''
        emails = []
        for row in self._results:
            text = row.get('text', '')
            emails.extend(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text))
        return emails

    def extract_phone_numbers(self):
        '''Extracts and returns phone numbers found in search results text'''
        phone_numbers = []
        for row in self._results:
            text = row.get('text', '')
            phone_numbers.extend(re.findall(r'\b(?:\+?(\d{1,3})[-.\s]?(\d{1,4})?[-.\s]?(\d{1,4})?[-.\s]?(\d{1,9})\b|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})\b', text))
        return phone_numbers
