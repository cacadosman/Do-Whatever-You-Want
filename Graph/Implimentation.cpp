#include <iostream>
#include <queue>
using namespace std;

void printDFS(int **edges, int n, int sv, bool *visited){
	cout << sv << endl;
	visited[sv] = true;
	for(int i = 0; i < n; i++){
		if(i == sv){
			continue;
		}
		if(edges[sv][i]){
			if(visited[i]){
				continue;
			}
			printDFS(edges, n, i, visited);
		}
	}
}

void printBFS(int **edges, int n, int sv, bool *visited){
	queue<int> q;
	q.push(sv);
	visited[sv] = true;
	while(!q.empty()){
		int val = q.front();
		cout << val << " ";
		q.pop();
		for(int i = 0; i < n; i++){
			if(i == val){
				continue;
			}
			if(edges[val][i] != 0 && !visited[i]){
				q.push(i);
				visited[i] = true;
			}
		}
	}
}

void BFS(int **edges, int n){
	bool *visited = new bool[n];
	for(int i = 0; i < n; i++){
		visited[i] = false;
	}
	for(int i = 0; i < n; i++){
		if(!visited[i]){
			printBFS(edges, n, i, visited);
		}
	}
	delete[] visited;
}

void DFS(int **edges, int n){
	bool *visited = new bool[n];
	for(int i = 0; i < n; i++){
		visited[i] = false;
	}
	for(int i = 0; i < n; i++){
		if(!visited[i]){
			printDFS(edges, n, i, visited);
		}
	}
	delete[] visited;
}

bool hasPath(int **edges, int n, int v1, int v2){
	bool *visited = new bool[n];
	for(int i = 0; i < n; i++){
		visited[i] = false;
	}
	queue<int> q;
	q.push(v1);
	visited[v1] = true;
	while(!q.empty()){
		int val = q.front();
		if(val == v2){
			return true;
		}
		q.pop();
		for(int i = 0; i < n; i ++){
			if(i == val){
				continue;
			}
			if(edges[val][i] && !visited[i]){
				q.push(i);
				visited[i] = true;
			}
		}
	}
	return false;
}

int main(){
	int n, e;
	cin >> n >> e;
	int **edges = new int*[n];
	for(int i = 0; i < n; i++){
		edges[i] = new int[n];
		for(int j = 0; j < n; j++){
			edges[i][j] = 0;
		}
	}
	while(e --){
		int n1, n2;
		cin >> n1 >> n2;
		edges[n1][n2] = 1;
		edges[n2][n1] = 1;
	}
	cout << "DFS" << endl;
	DFS(edges, n);
	cout << "BFS" << endl;
	BFS(edges, n);
	for(int i = 0; i < n; i++){
		delete[] edges[i];
	}
}







