import re

class KeyMap:
    def __init__(self, configurationFile=None):
        if configurationFile is None:
            configurationFile = "./keymappings"

        self.__keytree = {}
        self.__commandSequence = []
        self.processFile(configurationFile)

    def processFile(self, configurationFile):
        for line in file(configurationFile):
            # Remove everything after the first '#'
            actionline = line.split("#")[0]
            actionline = actionline.strip()

            # Reduce all space collections to 1 (and strip)
            if len(actionline) > 0:
                parts = actionline.split(":")
                assert(len(parts) == 2)

                actions_part = parts[0]
                sequence_part = parts[1]

                actions = re.sub("\s+", "", actions_part).strip()
                sequence = re.sub("\s+", " ", sequence_part).strip().split(" ")

                self.addAction(self.__keytree, sequence, actions)

    def addAction(self, tree, sequence, action):
        # We add the first element of sequence to this tree

        # First, we assert that there isn't already a command
        # at this location
        assert( type(tree.get(sequence[0])) is not type("") )

        if len(sequence) == 1:
            assert( type(tree.get(sequence[0])) is not type({}) )
            tree[sequence[0]] = action
            return

        if sequence[0] not in tree:
            tree[sequence[0]] = {}

        self.addAction(tree[sequence[0]], sequence[1:], action)

    def addCommand(self, ch):
        try: 
            self.__commandSequence.append(ch)
        except:
            pass

    def tree(self):
        return self.__keytree

    def reset(self):
        self.__commandSequence = []

    def translate(self):
        return self.__translateSequence(self.__keytree, self.__commandSequence)

    def __translateSequence(self, tree, sequence):

        for ch in sequence:
            try:
                tree = tree[ch]
            except:
                self.reset()
                return None

        action = tree
        if type(action) == type(""):
            self.reset()
            return action

        return None
