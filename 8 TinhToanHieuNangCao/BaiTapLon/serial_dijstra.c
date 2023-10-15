#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

#define N 7 // number of vertex
#define SOURCE 3
#define MAXINT 9999999

void dijkstra(int graph[N][N], int source) {
	int distance[N];
	int visited[N];
	int i, j, count, nextNode, minDistance;

	for (i = 0; i < N; i++) {
		distance[i] = graph[source][i];
		visited[i] = 0;
	}
	// printf("mang distance la: ");
	// for (i = 0; i < N; i++) {
	// 	if (distance[i] == 9999999) printf("%4s\t", "INFI");
	// 	else printf("%4d\t", distance[i]);
	// }
	// printf("\n mang visited la: ");
	// for (i = 0; i < N; i++) {
	// 	if (visited[i] == 9999999) printf("%4s\t", "INFI");
	// 	else printf("%4d\t", visited[i]);
		
	// }
	printf("\n");
	visited[source] = 1; // check status vertex source
	count = 1; // count of vertex source
	// printf("\n mang visited  sau khi gan la: ");
	// for (i = 0; i < N; i++) {
	// 	if (visited[i] == 9999999) printf("%4s\t", "INFI");
	// 	else printf("%4d\t", visited[i]);
		
	// }

	while (count < N) {
		printf("\n");
		printf("N là: %d", N);
		minDistance = MAXINT;
		printf("\t count là: %d", count);
		// pick vertex min distance
		for (i = 0; i < N; i++) {
			if (distance[i] < minDistance && !visited[i]) {
				minDistance = distance[i];
				nextNode = i;
			}
		}
		// printf("\t nextNode là: %d", nextNode);
		// printf("\t minDistance sau là: %d", minDistance);
		//markup vertex visited
		visited[nextNode] = 1;
		count++;

		// printf("\t visited[nextNode] là: %d", visited[nextNode]);
		// printf("\t count++ là: %d", count++);
		
		//update distance after choose vertex min distance
		for (i = 0; i < N; i++) {
			if (!visited[i] && minDistance + graph[nextNode][i] < distance[i]) {
				distance[i] = minDistance + graph[nextNode][i];
			}
		}
		printf("\ndistance la: ");
		for (i = 0; i < N; i++) {
			if (distance[i] == 9999999) printf("%4s\t", "INFI");
			else printf("%4d\t", distance[i]);
		}
		printf("\n visited la: ");
		for (i = 0; i < N; i++) {
			if (visited[i] == 9999999) printf("%4s\t", "INFI");
			else printf("%4d\t", visited[i]);
		}
		printf("\n=====================================\n");
	}
	// printf("\n");
	// printf("Excuted\n");
	// printf("\nShortest distances from %d to other vertices:\n", source);
    // for (i = 0; i < N; i++) {
	// 	if (i == source) {
    //         printf("Vertex %d: is vertex source\n", i);
    //     } else if (distance[i] == MAXINT) {
    //         printf("Vertex %d: not connect\n", i);
    //     } else {
    //         printf("Vertex %d: %d\n", i, distance[i]);
    //     }
    // }
}

int main(int argc, char *argv[]) {
	//cal time
	double time_start, time_end;
	struct timeval tv;
	struct timezone tz;
	//variable read file
	char fn[255];
	FILE *fi;
	//define matrix
	int weight[N][N];
	
	gettimeofday(&tv, &tz);
	time_start = (double)tv.tv_sec + (double)tv.tv_usec / 1000000.00;
	strcpy(fn, "input7.txt");
	fi = fopen(fn, "r");
	if ((fi = fopen(fn, "r")) == NULL) {
		printf("Can't open the input file: %s\n\n", fn);
		exit(1);
	}
	printf("\nThe adjacency matrix: \n");
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			fscanf(fi, "%d", &weight[i][j]);
			if (weight[i][j] == 9999999) printf("%4s\t", "INFI");
			else printf("%4d\t", weight[i][j]);
		}
	printf("\n");
	}
	// printf("Readed matrix file\n");
	
	dijkstra(weight, SOURCE);

	// printf("\n");
	// gettimeofday(&tv, &tz);
	// time_end = (double)tv.tv_sec + (double)tv.tv_usec / 1000000.00;
	// printf("Time cost is %1f\n", time_end - time_start);
	// printf("\n");

	return 0;
}
