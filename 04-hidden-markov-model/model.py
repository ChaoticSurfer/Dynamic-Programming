"""
This file contains the representation of a Hidden Markov Model as a Python
class. While this file can't be used directly, the model is used by the Viterbi
algorithm.
"""


class HMM:
    """
    A representation of a Hidden Markov Model, consisting of:

      - A set of possible states
      - A set of possible observations
      - The initial probabilities for the states.
      - The transition probabilities between the states.
      - The emission probabilities for the states and observations.
    """

    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

        # For convenience. This way, the definition of the HMM doesn't need to
        # specify all the states separately.
        #
        # Because our algorithms don't need to loop through all the possible
        # observations, we don't need to store the possible observations.
        self.possible_states = p.keys()


SPEECH_RECOGNITION_HMM = HMM(
    # Initial state probabilities. We can start with 'au' or 'o' with equal
    # probability. All the other syllables only appear in the middle of words.
    {'au': 0.5, 'to': 0, 'o': 0.5, 'tter': 0, 'mo': 0, 'bile': 0},

    # State transition matrix. In this example, we can only form the words
    # 'automobile' and 'otter', and nothing else.
    #
    # For example, 'au' can only be followed by 'to', which can only be
    # followed by 'mo', and so on. Both 'tter' and 'bile' will end their
    # respective words because they can't be followed by anything.
    {
        'au': {'au': 0, 'to': 1, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 0},
        'to': {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 1, 'bile': 0},

        'o': {'au': 0, 'to': 0, 'o': 0, 'tter': 1, 'mo': 0, 'bile': 0},
        'tter': {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 0},

        'mo': {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 1},
        'bile': {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 0},
    },

    # Observation probability matrix.
    #
    # 'au' can produce both 'sound-au' and 'sound-o', but produces the former
    # with higher probability. The same principle applies to 'to', 'o' and
    # 'tter', each of which can produce one of two sounds with different
    # probabilities.
    #
    # 'mo' and 'bile' are unambiguous, as each can only produce a single sound.
    {
        'au': {
            'sound-au': 0.7,
            'sound-o': 0.3,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'to': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0.7,
            'sound-tter': 0.3,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'o': {
            'sound-au': 0.3,
            'sound-o': 0.7,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'tter': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0.3,
            'sound-tter': 0.7,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'mo': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 1,
            'sound-bile': 0
        },

        'bile': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 0,
            'sound-bile': 1
        }
    }
)
