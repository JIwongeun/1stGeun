#define _CRT_SECURE_NO_WARNINGS_
#include<stdio.h>
#include<stdlib.h>

typedef struct {
	int heap[100001];
	int heap_size;
}Heap;

void init_heap(Heap* h) {

	h->heap_size = 0;

}
void insert_node(Heap* h, int n) {

	int cur = ++(h->heap_size);

	while (cur != 1 && h->heap[cur / 2] < n) {
		h->heap[cur] = h->heap[cur / 2];
		cur /= 2;
	}

	h->heap[cur] = n;
}

int delete_node(Heap* h) {

	int parent, child, item, temp;

	if (h->heap_size == 0)
		return 0;

	parent = 1;
	child = 2;
	item = h->heap[1];
	temp = h->heap[(h->heap_size)--];

	while (child <= h->heap_size) {
		
		if (child<h->heap_size && h->heap[child]< h->heap[child + 1]) {
			child++;
		}

		if (temp > h->heap[child]) break;

		h->heap[parent] = h->heap[child];
		parent = child;
		child *= 2;
	}

	h->heap[parent] = temp;
	return item;
}	


int main(void) {

	Heap* heap = (Heap*)malloc(sizeof(Heap));

	init_heap(heap);

	int t,n;

	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d" ,&n);
		
		if (n == 0) {
			printf("%d\n", delete_node(heap));
		}
		else {
			insert_node(heap, n);
		}

	}


	return 0;
}