Title: Detailed Report on Assignment Implementation: SetList, DisjointSet, and Maze Runner Functions

**Introduction**

In this report, I will provide a detailed explanation of my implementation of the SetList, DisjointSet, and Maze Runner functions for the assignment. I will discuss the functions and their purposes, the challenges I encountered during implementation, and the strategies I used to overcome those challenges. The report aims to provide an in-depth understanding of the assignment's requirements, the thought process behind the implementation, and the learning outcomes achieved through the completion of this assignment.

**Table of Contents**

1. Introduction
1. SetList Implementation
   1. Node Class
   1. SetList Class
1. DisjointSet Implementation
1. Maze Runner Function - Recursive
1. Challenges and Solutions
1. Conclusion

**2. SetList Implementation**

The SetList is a doubly linked list used to represent a single set of a disjoint set. It consists of two main components: the Node class and the SetList class.

**2.1 Node Class**

The Node class is declared within the SetList class and stores the following information:

- Data: The data value stored in the node.
- Next Node: A reference to the next node in the SetList.
- Previous Node: A reference to the previous node in the SetList.
- SetList Reference: A reference to the SetList the node belongs to.

The Node class provides several member functions, including **get\_data()**, **get\_next()**, **get\_previous()**, and **get\_set()**, which allow accessing the node's data and its relationships with other nodes in the SetList.

**2.2 SetList Class**

The SetList class represents a set in the disjoint set data structure. It is initialized as an empty list and contains the following member functions:

- **get\_front()**: Returns a reference to the first node in the list.
- **get\_back()**: Returns a reference to the last node in the list.
- **make\_set(data)**: Adds the first value to the SetList object if the list is empty and returns a reference to the newly created Node.
- **union\_set(other\_set)**: Performs a union with the current object and the provided SetList. The elements of the other\_set are transferred to the current object, and other\_set becomes empty in the process. The function returns the number of elements transferred.
- **find\_data(data)**: Returns a reference to the Node containing the specified data. If the data does not exist, None is returned.
- **representative\_node()**: Returns a reference to the node that holds the representative of the SetList. If the SetList is empty, None is returned.
- **representative()**: Returns the data of the representative node of the SetList. If the SetList is empty, None is returned.
- **\_\_len\_\_()**: Returns the number of items within the SetList.

**3. DisjointSet Implementation**

The DisjointSet class represents a disjoint set, which is a set of sets where each element can belong to only one set. The implementation is done in the a1\_partc.py file and includes the following member functions:

- **make\_set(element)**: Adds a new set with the provided element to the DisjointSet. If the element already exists within the DisjointSet, the function does nothing and returns False. Otherwise, it creates a new SetList object containing only one node with the element as the value, adds a dictionary entry with the element as the key and a reference to the node as the value, and returns True.
- **find\_set(element)**: Returns the representative of the set containing the specified element.
- **get\_num\_sets()**: Returns the number of sets in the DisjointSet.
- **union\_sets(element1, element2)**: Performs a union operation on the sets that contain the specified elements. It finds the representatives of the sets, checks if they are different, and performs the union operation using the SetList **union\_set()** function. The function returns True if the union was successful and False otherwise.

The DisjointSet class effectively implements the disjoint set data structure using the SetList and Node classes. It allows efficient operations on sets, such as finding the representative, making sets, and performing unions.

**4. Maze Runner Function - Recursive**

The maze runner function is implemented in the a1\_partd.py file and provides a recursive algorithm to find a path from the starting cell to the destination cell in a given maze. The function takes the maze and the current cell coordinates as input and returns a boolean value indicating whether a path was found.

The recursive maze runner function follows these steps:

1. Check if the current cell is outside the boundaries of the maze. If so, return False.
1. Check if the current cell is the destination cell. If so, return True.
1. Check if the current cell is a wall or has already been visited. If so, return False.
1. Mark the current cell as visited.
1. Recursively call the maze runner function for each adjacent cell (up, down, left, and right) and return True if any of the recursive calls return True.
1. If no adjacent cells lead to a valid path, backtrack by unmarking the current cell and return False.

**5. Challenges and Solutions**

During the implementation of the functions, I encountered several challenges and applied various strategies to overcome them. Here, I will outline some of the major challenges and describe the solutions I employed:

**Challenge 1: Understanding the Disjoint Set Data Structure**

The disjoint set data structure was new to me, so understanding its concepts and the implementation details presented a challenge. I spent time researching and studying the topic to gain a solid understanding of how sets, representatives, and unions are handled.

Solution: To overcome this challenge, I read relevant articles and resources on disjoint sets. I also reviewed the provided code and documentation to understand how the SetList and DisjointSet classes interact. By studying the code and working through examples, I grasped the core concepts and successfully implemented the required functions.

**Challenge 2: Recursive Maze Runner Algorithm**

Implementing the recursive algorithm for the maze runner function required careful planning and consideration of various scenarios. It was challenging to handle the backtracking and ensure the correct traversal of the maze.

Solution: To overcome this challenge, I studied the provided Maze class and understood its structure and methods. I broke down the problem into smaller subproblems and identified the base case for the recursion. I used a recursive helper function to explore different paths and implemented backtracking to backtrack when a path leads to a dead end. I extensively tested the function with different maze configurations to ensure its correctness.

**6. Conclusion**

In conclusion, this report detailed the implementation of the SetList, DisjointSet, and Maze Runner functions for the assignment. I discussed the purpose and functionality of each function, the challenges encountered during implementation, and the strategies employed to overcome those challenges. The implementation of these functions allowed me to gain a deeper understanding of linked lists, disjoint sets, and recursive algorithms. Through this assignment, I enhanced my problem-solving skills and expanded my knowledge in these areas. Overall, the assignment provided a valuable learning experience and helped solidify my understanding of the concepts involved.

