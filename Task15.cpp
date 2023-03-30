#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>


void nullCheck(int* ptr) {
		if (ptr == NULL) {
				printf("Out of memory!");
				exit(0);
		}
}


struct Dynarr {
	int* data;
	size_t len;
	size_t cap;

	void init() {
		data = NULL;
		len = 0;
		cap = 0;
	}

	void add(int value) {

		if (data == NULL) {
			data = (int*)malloc(sizeof(int));
			nullCheck(data);
			cap = 1;
		}

		if (len == cap) {
			data = (int*)realloc(data, (cap * 2) * sizeof(int));
			nullCheck(data);
			cap = cap * 2;
		}

		data[len] = value;
		len++;
	}

	void pop() {

		if (data == NULL) {
			printf("You can't delete an element from empty array!");
		}

		len--;
		if (cap == len * 4) {
			cap = cap / 2;
		}
	}

	void print() {
		for (size_t i = 0; i < len; i++) {
			printf("%d ", data[i]);
		}
		printf(" length: %zu, capacity: %zu", len, cap);
		printf("\n");
	}
};


void main() {
	Dynarr* arr = (Dynarr*)malloc(sizeof(Dynarr));
	arr->init();

	arr->add(9);
	arr->add(78);
	arr->add(34);
	arr->print();
	arr->add(56);
	arr->add(123);
	arr->print();
	arr->pop();
	arr->pop();
	arr->pop();
	arr->print();
}
