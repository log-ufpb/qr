## Vector

**They store a group of elements, sequentially.**

- [Part of the C++ STL](https://cplusplus.com/reference/vector/vector/)
- Implementation: Arrays that can be reallocated in case they exceed a specific size.
- Time complexity for the main operations:
   - Insertion of elements at the end of the vector: \\(O(1)\\)
   - Insertion of elements in the middle of the vector: \\(O(n)\\)
   - Removal of elements  at the end of the vector: \\(O(1)\\)
   - Removal of elements in the middle of the vector: \\(O(n)\\)
   - Search for an element in a certain position: \\(O(1)\\)
   - Search for an element with a certain value: \\(O(n)\\)

***

## Priority queues

**They store a group of elements sequentially, and efficiently obtain its maximum or minimum value.**

- [Part of the C++ STL](https://cplusplus.com/reference/queue/priority_queue/)
- Implementation: Max/Min Heap
- Time complexity for the main operations:
  - Insertion of any element: \\(O(\log n)\\)
  - Removal of any element: \\(O(\log n)\\)
  - Search for the maximum/minimum value: \\(O(1)\\)

***

## Set

**They efficiently store a group of non-repeating elements.**

- [Part of the C++ STL](https://cplusplus.com/reference/set/set/)
- Implementation: Binary Search Trees
- Time complexity for the main operations:
  - Insertion of any element: \\(O(\log n)\\)
  - Removal of any element: \\(O(\log n)\\)
  - Search for an element with a certain value: \\(O(\log n)\\)

***

## Map

**They store elements of type `<key, value>` efficiently avoiding key repetition (repetition of values is possible).**

- [Part of the C++ STL](https://cplusplus.com/reference/map/map/)
- Implementation: Binary Search Trees
- Time complexity for the main operations:
  - Insertion of any element: \\(O(\log n)\\)
  - Removal of any element: \\(O(\log n)\\)
  - Search for an element with a certain key: \\(O(\log n)\\)

***

## Disjoint Set Union

**This data structure stores a collection of sets without element overlap. It allows for efficient operations to create and join sets, as well as checking if two elements are part of the same set. Disjoint Set Union is used in efficient implementations of the Kruskal algorithm for finding the Minimum Spanning Tree of a graph.**

- Not a part of the C++ STL
- Implementation: Vectors or Arrays
- Time complexity for the main operations:
   - Create a set: \\(O(1)\\)
   - Join two sets: \\(\approx O(1)\\)
   - Search for a set of a certain element: \\(\approx O(1)\\)
   - Check if two elements are part of the same set: \\(\approx O(1)\\)
***

**Example:**

<img src="https://cp-algorithms.com/data_structures/DSU_example.png" align="center">

```C++
#include <iostream>
#include <vector>

using namespace std;

class Disjointed_set_union{
private:
    struct Element{
        int root;
        int rank;

        Element() = default;
        Element(int root) : root(root), rank(1){}
    };

    vector<Element> map;
public:
    Disjointed_set_union(int total_elements){
        map.resize(total_elements);
    }

    void make_set(int value){
        int last_idx = map.size();
        map[value] = Element(value);
    }

    int find(int value){
        if(map[value].root == value){
            return value;
        }
        return map[value].root = find(map[value].root);
    }

    void union_sets(int value_1, int value_2){
        int root_1 = find(value_1);
        int root_2 = find(value_2);

        if (root_1 != root_2){
            int rank_1 = map[root_1].rank;
            int rank_2 = map[root_2].rank;

            if(rank_1 > rank_2){
                map[root_2].root = root_1;
            }else if(rank_1 < rank_2){
                map[root_1].root = root_2;
            }else{
                map[root_2].root = root_1;
                map[root_1].rank++;
            }
        }
    }

    bool is_same_set(int value_1, int value_2){
        return find(value_1) == find(value_2);
    }
};

int main(){
    // The elements are numbered from 1 to 4 to match the figure above
    int max_elements = 5;
    Disjointed_set_union dsu(max_elements); // Max of elements is 4
    dsu.make_set(1);
    dsu.make_set(2);
    dsu.make_set(3);
    dsu.make_set(4);

    for(int i = 1; i < max_elements; ++i){
        for(int j = i+1; j < max_elements; ++j){
            if (dsu.is_same_set(i, j)){
                printf("%d and %d are in the same set\n", i, j);
            }else{
                printf("%d and %d are not in the same set\n", i, j);
            }
        }
    }
    printf("\n ------------- \n\n");

    dsu.union_sets(1, 2);

    for(int i = 1; i < max_elements; ++i){
        for(int j = i+1; j < max_elements; ++j){
            if (dsu.is_same_set(i, j)){
                printf("%d and %d are in the same set\n", i, j);
            }else{
                printf("%d and %d are not in the same set\n", i, j);
            }
        }
    }
    printf("\n ------------- \n\n");

    dsu.union_sets(3, 4);

    for(int i = 1; i < max_elements; ++i){
        for(int j = i+1; j < max_elements; ++j){
            if (dsu.is_same_set(i, j)){
                printf("%d and %d are in the same set\n", i, j);
            }else{
                printf("%d and %d are not in the same set\n", i, j);
            }
        }
    }
    printf("\n ------------- \n\n");

    dsu.union_sets(1, 3);

    for(int i = 1; i < max_elements; ++i){
        for(int j = i+1; j < max_elements; ++j){
            if (dsu.is_same_set(i, j)){
                printf("%d and %d are in the same set\n", i, j);
            }else{
                printf("%d and %d are not in the same set\n", i, j);
            }
        }
    }
    return 0;
}
```

It is possible to use `unordered_map` instead of `vector` for a more general implementation.

## Graphs (adjacency list)

**They represent sparse graphs when it is necessary to know which arcs touch a certain vertex. This data structure is efficient in memory spaces when compared to other implementations (e.g., adjacency matrix). Moreover, they can be more efficient, time-wise, for algorithms such as breadth-first search and depth-first search.**

- Not a part of the C++ STL
- Implementation: Vector of vectors
- Time complexity for the main operations:
   - Insertion of elements at the end of the vector: \\(O(1)\\)
   - Removal of elements  at the end of the vector: \\(O(1)\\)
   - Check the existence of an arc between any two vertices: \\(O(n)\\)

**Example:**

<img src="https://www.techiedelight.com/wp-content/uploads/Eulerian-Cycle-in-Directed-Graph.png" align="center" width=33% height=33%>

```C++
#include<cstdio>
#include<vector>
using namespace std;

int main(){
    int total_nodes = 4;
    vector<vector<int>> graph(total_nodes); // initialise with 4 empty vectors

    graph[0].push_back(1); // adds an arc from 0 to 1
    graph[1].push_back(2); // adds an arc from 1 to 2
    graph[1].push_back(4); // adds an arc from 1 to 4
    graph[2].push_back(3); // adds an arc from 2 to 3
    graph[3].push_back(0); // adds an arc from 3 to 0
    graph[3].push_back(1); // adds an arc from 3 to 1
    graph[4].push_back(3); // adds an arc from 4 to 3


    // iterate over the arcs from each vertex
    for(int i = 0; i < total_nodes; ++i){
        for(auto j : graph[i]){
            printf("There is an arc from %d to %d\n", i, j);
        }
    }
    return 0;
}
```

***

## Graphs (adjacency matrix)

**They represent dense graphs when it is necessary to know if there is an arc between any two vertices or its cost in weighted graphs.**

- Not a part of the C++ STL
- Implementation: Array of arrays or vector of vectors. It is important it is a matrix \\(n \times n\\).
- Time complexity for the main operations:
   - Insertion of an arc: \\(O(1)\\)
   - Removal of an arc: \\(O(1)\\)
   - Changing an arc: \\(O(1)\\)
   - Check the existence of an arc between any two vertices: \\(O(1)\\)
   - Obtain the cost of an arc between any two vertices: \\(O(1)\\)
   - Insertion of a vertex costs the same as a matrix reallocation for an array of arrays or the vertex insertion in each vector when implementing this structure as a vector of vectors.

**Example:**

<img src="https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/" align="center" width=33% height=33%>

```C++
#include<cstdio>
#include<vector>
using namespace std;

int main(){
    int total_nodes = 5;
    int graph_arr[total_nodes][total_nodes] = {
                                           {0, 3, 0, 7, 8},
                                           {3, 0, 1, 4, 0},
                                           {0, 1, 0, 2, 0},
                                           {7, 4, 2, 0, 3},
                                           {8, 0, 0, 3, 0}
                                          };

    // iterate over the vertices
    for(int i = 0; i < total_nodes; ++i){
       for(int j = i+1; j < total_nodes; ++j){
           if(graph_arr[i][j])
              printf("There is an edge from %d to %d with cost: %d\n", i, j, graph_arr[i][j]);
        }
    }
    printf("\n-----------------------\n\n");
    vector<vector<int>> graph_vec {
                                    {0, 3, 0, 7, 8},
                                    {3, 0, 1, 4, 0},
                                    {0, 1, 0, 2, 0},
                                    {7, 4, 2, 0, 3},
                                    {8, 0, 0, 3, 0}
                                   };

    // iterate over the vertices
    for(int i = 0; i < total_nodes; ++i){
       for(int j = i+1; j < total_nodes; ++j){
           if(graph_vec[i][j])
              printf("There is an edge from %d to %d with cost: %d\n", i, j, graph_vec[i][j]);
        }
    }
    return 0;
}
```
