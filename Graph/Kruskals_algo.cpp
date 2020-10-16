#include <iostream>
#include <algorithm>
using namespace std;

class Edges{
public:
	int src, dest, weight;
};

bool compare(Edges e1, Edges e2){
	return e1.weight < e2.weight;
}

int getParent(int v, int *parent){
	if(parent[v] == v){
		return v;
	}
	return getParent(parent[v], parent);
}

Edges *kruskalsAlgo(Edges *arr, int v, int e){
	Edges *output = new Edges[v - 1];
	int count = 0;
	int *parent = new int[v];
	for(int i = 0; i < v; i++){
		parent[i] = i;
	}
	int i = 0;
	while(count < v - 1){
		Edges curr_Edge = arr[i];
		int srcParent = getParent(curr_Edge.src, parent);
		int destParent = getParent(curr_Edge.dest, parent);
		if(srcParent != destParent){
			output[count] = curr_Edge;
			count ++;
			parent[srcParent] = destParent;
		}
		i++;
	}
	delete[] parent;
	return output;
}

int main(){
	int v, e;
	cin >> v >> e;
	Edges *arr = new Edges[e];
	for(int i = 0; i < e; i++){
		cin >> arr[i].src >> arr[i].dest >> arr[i].weight;
	}
	sort(arr, arr + e, compare);
	Edges *output = kruskalsAlgo(arr, v, e);
	for(int i = 0; i < (v - 1); i++){
		if(output[i].src < output[i].dest){
			cout << output[i].src << " " << output[i].dest << " " << output[i].weight << endl;
		}
		else {
			cout << output[i].dest << " " << output[i].src << " " << output[i].weight << endl;
		}
	}
	delete[] arr;
	delete[] output;
	return 0;
}