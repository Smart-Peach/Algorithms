#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>


void print(int* arr, size_t end) {
	for (size_t i = 0; i < end; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}


void rand_array(int* arr, long len) {
	for (long i = 0; i < len; i++) {
		arr[i] = rand() % 100;
	}
}


void swap(int* ind1, int* ind2) {
	int c = *ind1;
	*ind1 = *ind2;
	*ind2 = c;
}

long* partition_Lomuto(long* start, long* end) {
	if (end - start < 2) return start;
	if (*start > *end) swap(start, end);

	size_t random_range_size = end - start + 1;
	size_t elem_ind = start + rand() % random_range_size;

	if (elem_ind != start) swap(start, elem_ind);

	int* i = start + 1;
	int* j = start + 1;

	while (j != end + 1) {
		if (*j < *start) swap(j, i++);
		j++;
	}
	i--;
	swap(i, start);
		
	return i;
}


void quick_sort_Lomuto(long* start, long* end) {
	long* p = partition_Lomuto(start, end);
	if (end - start > 2) {
		quick_sort_Lomuto(start, p);
		quick_sort_Lomuto(p + 1, end);
	}
}

void quick_sort_Hoare(long* start, long* end) {
	int* i = start;
	int* j = end;

	size_t random_range_size = end - start + 1;
	//size_t elem_ind = start + rand() % random_range_size;
	int pivot = *(start + rand() % random_range_size);

	while (i < j) {
		while (*i < pivot) i++;
		while (*j > pivot) j--;
		if (i <= j) swap(i++, j--);
	}

	if (i < end) quick_sort_Hoare(i, end);
	if (start < j) quick_sort_Hoare(start, j);
}


long* partition_Aleksandresku(long* start, long* end) {

	if (end - start < 2) {
		return start;
	}
	--end;

	if (*start > *end) {
		int c = *start;
		*start = *end;
		*end = c;
	}

	long* pivot_pos = start;
	int pivot = *start;

	do {
		++start;
	} while (*start < pivot);

	for (long* read = start + 1; read < end; read++) {
		long x = *read;
		long smaller = -(x < pivot);

		long delta = smaller & (read - start);
		start[delta] = *start;
		read[-delta] = x;
		start -= smaller;
	}

	--start;

	*pivot_pos = *start;
	*start = pivot;
	return start;
}


void quick_sort_Aleksandresku(long* start, long* end) {
	long* p = partition_Aleksandresku(start, end);
	if (end - start > 2) {
		quick_sort_Aleksandresku(start, p);
		quick_sort_Aleksandresku(p + 1, end);
	}
}


#define TIME_CHECK(sort, message, k)                      \
void time_check_##sort(int* arr, long len) {              \
	clock_t s0 = clock();                                 \
	quick_sort_##sort(arr, arr + len - k);                \
	clock_t s1 = clock();                                 \
	long time = (s1 - s0) / CLOCKS_PER_SEC;               \
	printf(message);                                      \
	printf("%ld\n", time);                                \
}                                                         \

TIME_CHECK(Lomuto, "Naive Lomuto takes: ", 1);
TIME_CHECK(Hoare, "Hoare takes: ", 1);
TIME_CHECK(Aleksandresku, "Super good Lomuto takes: ", 0);


void main() {

	long len = 1000000;
	int* array_1 = (int*)malloc(len * sizeof(int));
	int* array_2 = (int*)malloc(len * sizeof(int));
	int* array_3 = (int*)malloc(len * sizeof(int));

	rand_array(array_1, len);
	rand_array(array_2, len);
	rand_array(array_3, len);

	time_check_Lomuto(array_1, len);
	time_check_Hoare(array_2, len);
	time_check_Aleksandresku(array_3, len);
	free(array_2);
	free(array_3);
}
