
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.phone_numbers = []

class Phonebook():

    def __init__(self):
        self.root = TrieNode()
        self.filename = 'contacts.txt'
        self._load_contacts_from_file()

    def _load_contacts_from_file(self) -> None:
        """
        Loads contacts from the file into the Trie structure.
        """
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, number = line.strip().split(',')
                    self._add_contact_to_trie(name, number)
        except FileNotFoundError:
            pass

    def _add_contact_to_trie(self, name: str, number: str) -> None:
        """
        Adds a contact to the Trie structure.

        :param name: Contact name
        :param number: Contact phone number
        """
        node = self.root
        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        if number not in node.phone_numbers:
            node.phone_numbers.append(number)

    def add_contact(self, name: str, number: str) -> bool:
        """
        Adds a new contact to the file and the Trie structure.

        :param name: Contact name
        :param number: Contact phone number
        :return: True if the contact was added successfully, False if the contact already exists.
        """
        if self.search_contact(name, is_end_of_word=True):
            return False

        # Add to the file
        with open(self.filename, 'a') as file:
            file.write(f"{name},{number}\n")

        # Add to the Trie
        self._add_contact_to_trie(name, number)
        return True

    def search_contact(self, name: str, is_end_of_word: bool = False) -> list[str]:
        """
        Searches for contacts by prefix or full name.

        :param name: The name or prefix to search for
        :param is_end_of_word: If True, searches for an exact match
        :return: A list of phone numbers matching the search criteria
        """
        node = self.root
        for char in name:
            if char not in node.children:
                return []
            node = node.children[char]
        
        if is_end_of_word:
            return node.phone_numbers if node.is_end_of_word else []
        
        return self._collect_numbers(node)

    def _collect_numbers(self, node: TrieNode) -> list[str]:
        """
        Recursively collects phone numbers from the Trie.

        :param node: The Trie node to collect numbers from
        :return: A list of phone numbers found under the node
        """
        results = []
        if node.is_end_of_word:
            results.extend(node.phone_numbers)
        for child_node in node.children.values():
            results.extend(self._collect_numbers(child_node))
        return results