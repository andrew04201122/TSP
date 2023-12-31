# Dynamic Programming: 

Please use C++/C or python to write a dynamic programming program for travelling salesman problem (TSP)

For input format, we need to enter a graph. Let’s use the following simple description:

```
edgeIndex  edgeWeight  nameOfVertexU  nameOfVertexV
e1  1  v1 v2
e2  4  v1 v5
e3  5  v2  v5
e4  2  v1 v6
e5  3  v6 v5
e6  2  v6 v4
e7  6  v6 v3
e8  1  v3  v4
e9  5  v5  v3
e10 8  v4 v2
```

For output format, you have to print out the shortest path and the cost of going around.

For this example, the shortest path is 1, 2, 5, 3, 4, 6, 1, and the cost of most efficient tour = 16. 


## The way to run this code:
just run command below:

```
python TSP.py
```


## Other testcase 

```
e1  1  v1 v2
e2  4  v1 v5
e3  5  v2 v5
e4  2  v1 v6
e5  3  v6 v5
e6  2  v6 v4
e7  6  v6 v3
e8  1  v3  v4
e9  5  v5  v3
e10 8  v4 v2
e11  3 v7 v8
e12  4  v6  v7
e13  2  v7  v9
e14  1  v7  v1
e15  2  v7  v5
e16  10  v8  v1
e17  4   v8  v3
e18  2  v8  v6
e20  3  v9  v1
e21  4  v8  v2
e22  2  v9  v3
e23  8  v9  v5
```

```
e1  1  v1 v2
e2  4  v1 v5
e3  5  v2 v5
e4  2  v1 v6
e5  3  v6 v5
e6  2  v6 v4
e7  6  v6 v3
e8  1  v3  v4
e9  5  v5  v3
e10 8  v4 v2
e11  3 v7 v8
e12  4  v6  v7
e13  2  v7  v9
e14  1  v7  v1
e15  2  v7  v5
e16  10  v8  v1
e17  4   v8  v3
e18  2  v8  v6
e20  3  v9  v1
e21  4  v8  v2
e22  2  v9  v3
e23  8  v9  v5
e24  1  v10  v1
e25  2  v10  v3
e26  13  v10  v6
e27  3   v10  v5
e28  4  v10 v8
e29  3  v11 v2
e30  4  v11 v4
e31  5  v11 v6
e32  6  v11 v8
e33  1  v7  v2
```
