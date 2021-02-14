"""
This file contains the implementation of the Viterbi algorithm for finding the
most probable sequence of states that produce some observations. The model from
the `model_04_02.py` file is used as the basis of the algorithm.

This file can be run directly to compare the greedy and Viterbi algorithms:

    python3 viterbi.py
"""


from model import SPEECH_RECOGNITION_HMM


def greedy(hmm, observations):
    """
    Given a Hidden Markov Model and a sequence of algorithm, finds the most
    probable sequence of states that produced the observations.

    Uses the greedy algorithm, looking at each observation in isolation and
    ignoring all transition probabilities.
    """

    return [
        max(hmm.possible_states, key=lambda s: hmm.b[s][observation])
        for observation in observations
    ]


class PathProbabilityWithBackPointer:
    """
    Represents the probability of a path along with a back pointer:

      - Stores the probability of a path ending at a given state at a given
        time. The state and time are not stored because they can be inferred
        from where in the 2D grid this object appears.

      - Also stores the state in the previous time step that led to this
        particular path probability. This is the back pointer from which the
        entire path can be reconstructed.
    """

    def __init__(self, probability, previous_state=None):
        self.probability = probability
        self.previous_state = previous_state


def viterbi(hmm, observations):
    """
    Given a Hidden Markov Model and a sequence of algorithm, finds the most
    probable sequence of states that produced the observations.

    Uses the Viterbi algorithm, which incorporates not only the emission
    probabilities, but also the initial and transition probabilities in order
    to construct a realistic path.
    """

    v_grid = [{} for _ in observations]

    for s in hmm.possible_states:
        v_grid[0][s] = PathProbabilityWithBackPointer(
            hmm.p[s] * hmm.b[s][observations[0]]
        )

    for t in range(1, len(observations)):
        for s in hmm.possible_states:
            possible_transition_probabilities = [
                (
                    v_grid[t - 1][r].probability * hmm.a[r][s],
                    r
                )
                for r in hmm.possible_states
            ]

            max_transition_probability, best_previous_state = max(
                possible_transition_probabilities,
                key=lambda probability_and_state: probability_and_state[0]
            )

            v_grid[t][s] = PathProbabilityWithBackPointer(
                max_transition_probability * hmm.b[s][observations[t]],
                best_previous_state
            )

    max_end_state = max(
        hmm.possible_states,
        key=lambda s: v_grid[-1][s].probability
    )

    path_states = []
    last_state = max_end_state
    for t in range(len(observations) - 1, -1, -1):
        path_states.append(last_state)
        last_state = v_grid[t][last_state].previous_state

    path_states.reverse()

    return path_states


if __name__ == '__main__':
    sound_samples = [
        # Technically, the speaker might have said 'auto', but based on the
        # sounds, it's more likely they said 'otter'. Both the greedy and the
        # Viterbi algorithms will agree.
        ['sound-o', 'sound-tter'],

        # Here, the speaker definitely said 'automobile', but only the Viterbi
        # algorithm can infer that.
        ['sound-o', 'sound-tter', 'sound-mo', 'sound-bile'],
    ]

    for sample in sound_samples:
        greedy_path = greedy(SPEECH_RECOGNITION_HMM, sample)
        viterbi_path = viterbi(SPEECH_RECOGNITION_HMM, sample)

        print(f"SAMPLE:  {'  '.join(sample)}")
        print(f"  GREEDY :  {'  '.join(greedy_path)}")
        print(f"  VITERBI:  {'  '.join(viterbi_path)}")
        print()
