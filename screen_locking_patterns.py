"""
https://www.codewars.com/kata/585894545a8a07255e0002f1
https://www.codewars.com/kata/screen-locking-patterns/train/python

DESCRIPTION:
Screen Locking Patterns
You might already be familiar with many smartphones that allow you to use a geometric pattern as a security measure.
To unlock the device, you need to connect a sequence of dots/points in a grid by swiping your finger without lifting
it as you trace the pattern through the screen. The image below has an example pattern of 7 dots/points:
[A, B, I, E, D, G, C].

lock_example.png

For this kata, your job is to implement the function countPatternsFrom(firstPoint, length);
where firstPoint is a single-character string corresponding to the point in the grid (i.e.: 'A')
and length is an integer indicating the length of the pattern. The function must return the number of combinations
starting from the given point, that have the given length.

Take into account that dots can only be connected with straight directed lines either:

horizontally (like A to B)
vertically (like D to G),
diagonally (like I and E, as well as B and I), or
passing over a point that has already been 'used' like (G and C passing over E).
The sample tests have some examples of the number of combinations for some cases to help you check your code.

Optional Extra:

Out of curiosity, in case you're wondering, for the Android lock screen, valid patterns must have between 4 and 9 dots,
and there are 389112 possible valid combinations in total.

"""

# DATA STRUCTURE: Adjacency list. Connection graph

# dir: points from where to go directly
# ind: points where it Can go if has passed first through key:
# ind example: It can go from 'corner' point to 'G' if the way has passed over 'D' first

graph = {
    'A': {'dir': ['B', 'D', 'E', 'F', 'H'],
          'ind': [('D', 'G'), ('E', 'I'), ('B', 'C')]
          },
    'B': {'dir': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
          'ind': [('E', 'H')]
          },
    'C': {'dir': ['B', 'D', 'E', 'F', 'H'],
          'ind': [('E', 'G'), ('F', 'I'), ('B', 'A')]
          },
    'D': {'dir': ['A', 'B', 'E', 'G', 'H', 'C', 'I'],
          'ind': [('E', 'F')]
          },
    'E': {'dir': ['A', 'B', 'C', 'D', 'G', 'F', 'H', 'I'],
          'ind': []
          },
    'F': {'dir': ['B', 'C', 'E', 'H', 'I', 'A', 'G'],
          'ind': [('E', 'D')]
          },
    'G': {'dir': ['D', 'E', 'H', 'F', 'B'],
          'ind': [('D', 'A'), ('E', 'C'), ('H', 'I')]
          },
    'H': {'dir': ['D', 'E', 'F', 'G', 'I', 'A', 'C'],
          'ind': [('E', 'B')]
          },
    'I': {'dir': ['B', 'D', 'E', 'F', 'H'],
          'ind': [('H', 'G'), ('E', 'A'), ('F', 'C')]
          },
}


def count_patterns_from(firstPoint, length):
    """
    Count the number of combinations starting from the given point, that have the given length.
    :param string firstPoint: Node from which the locking patterns starts
    :param int length: Length of the locking pattern
    :return int: number of possible combinations
    """

    return 0 if length < 0 or length > 10 else count_patterns_recursive(stack='',
                                                                        node=firstPoint,
                                                                        length=length)


def count_patterns_recursive(stack, node, length):
    """
    Search recursively (deep first search) the possible paths to follow
    :param str stack: string where the visited nodes are saved
    :param str node: last_visited node
    :param int length: length of the path
    :return result: number of combinations
    """

    if length == 1:
        return 1

    # Add the visited node to the stack
    stack += node
    # Ask for node candidates to go from node
    candidates = node_candidates(stack=stack)
    result = 0
    for node in candidates:
        result += count_patterns_recursive(stack=stack, node=node, length=length-1)

    return result


def node_candidates(stack):
    """
    Return a list with the nodes candidates of the last node in the stack
    :param stack: list of nodes already visited
    :return: list of nodes that can be visited
    """
    candidates = []
    node = stack[-1]
    for n_dir in graph[node]['dir']:
        if n_dir not in stack:
            candidates.append(n_dir)

    for n_ind in graph[node]['ind']:
        if n_ind[0] in stack and n_ind[1] not in stack:
            candidates.append(n_ind[1])
    return candidates


# Test in Codewars
print(count_patterns_from('A', 3)) # 31
print(count_patterns_from('E', 4)) # 256
