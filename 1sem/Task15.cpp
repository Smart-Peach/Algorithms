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


class Dynarr {
	int* data;
	size_t len;
	size_t cap;

	public:
		Dynarr() {
			data = NULL;
			len = 0;
			cap = 0;
		}

		int elem(int i) {
			if (i >= len) {
				printf("Index out of range!\n");
				return -1;
			}
			return data[i];
		}

		void add(int value) {

			if (data == NULL) {
				data = new int;
				cap = 1;
			}

			if (len == cap) {
				data = (int*)realloc(data, (cap * 2) * sizeof(int));  //Didn't understand how to do it with "new"
				nullCheck(data);
				cap = cap * 2;
			}

			data[len] = value;
			len++;
		}

		void pop() {

			if (len == 0) {
				printf("You can't delete an element from empty array!\n");
				return;
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

	Dynarr arr;
	arr.print();

	arr.add(9);
	arr.add(78);
	arr.add(34);
	arr.print();
	arr.add(56);
	arr.add(123);
	arr.print();
	arr.pop();
	arr.pop();
	arr.pop();
	arr.print();
	arr.elem(8);
	arr.pop();
	arr.pop();
	arr.pop();
}
