#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>


void print(long* arr, size_t end) {
	for (size_t i = 0; i < end; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}


void shuffle(long* arr, long len) {
	if (len > 1) {
		for (long i = 0; i < len - 1; i++) {
			long j = i + rand() / (RAND_MAX / (len - i) + 1);
			long t = arr[j];
			arr[j] = arr[i];
			arr[i] = t;
		}
	}
}


void rand_array(long* arr, long len) {
	for (long i = 0; i < len; i++) {
		arr[i] = i;
	}
	shuffle(arr, len);
}


void copy(long* arr1, long* arr2, long len) {
	for (long i = 0; i < len; i++) {
		arr2[i] = arr1[i];
	}
}

void swap(long* ind1, long* ind2) {
	int c = *ind1;
	*ind1 = *ind2;
	*ind2 = c;
}

long* partition_Lomuto(long* start, long* end) {
	if (end - start < 2) {
		return start;
	}
	--end;

	if (*start > *end) {
		long c = *start;
		*start = *end;
		*end = c;
	}

	/*long* pivot_pos = start;
	long pivot = *pivot_pos;*/

	//if (end - start < 2) return start;
	//if (*start > *end) swap(start, end);

	///*long* pivot_pos = start;
	//long pivot = *pivot_pos;*/

	//size_t random_range_size = end - start + 1;
	//size_t elem_ind = start + rand() % random_range_size;

	//if (elem_ind != start) swap(start, elem_ind);

	long* i = start + 1;
	long* j = start + 1;

	while (j != end + 1) {
		if (*j < *start) swap(j, i++);
		j++;
	}
	i--;
	swap(i, start);
		
	return i--;
}


//void quick_sort_Lomuto(long* start, long* end) {
//	long* p = partition_Lomuto(start, end);
//	if (end - start > 2) {
//		quick_sort_Lomuto(start, p);
//		quick_sort_Lomuto(p + 1, end);
//	}
//}

long* partition_Hoare(long* start, long* end) {
	/*if (end - start < 2) {
		return start;
	}
	--end;*/
	if (*start > *end) {
		long c = *start;
		*start = *end;
		*end = c;
	}

	long* pivot_pos = start;
	long pivot = *pivot_pos;

	long* i = start;
	long* j = end;

	while (i <= j) {
		while (*i < pivot) i++;
		while (*j > pivot) j--;
		if (i >= j) break;
		swap(i++, j--);
	}

	return j;
}

//void quick_sort_Hoare(long* start, long* end) {
//	if (start < end) {
//		long* p = partition_Hoare(start, end);
//		quick_sort_Hoare(start, p);
//		quick_sort_Hoare(p + 1, end);
//	}
//}


long* partition_Aleksandresku(long* start, long* end) {

	if (end - start < 2) {
		return start;
	}
	--end;

	if (*start > *end) {
		long c = *start;
		*start = *end;
		*end = c;
	}

	long* pivot_pos = start;
	long pivot = *pivot_pos;
	 
	/*size_t random_range_size = end - start;

	long* pivot_pos = start + rand() % random_range_size;
	long pivot = *pivot_pos;*/

	if (pivot_pos != start) {
		long c = *start;
		*start = *pivot_pos;
		*pivot_pos = c;
		//swap(start, pivot_pos);
	}

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


//void quick_sort_Aleksandresku(long* start, long* end) {
//	long* p = partition_Aleksandresku(start, end);
//	if (end - start > 2) {
//		quick_sort_Aleksandresku(start, p);
//		quick_sort_Aleksandresku(p + 1, end);
//	}
//}

#define QUICK_SORT(name)                                  \
void quick_sort_##name(long* start, long* end) {          \
	if (start < end) {                                    \
		long* p = partition_##name(start, end);           \
		quick_sort_##name(start, p);                      \
		quick_sort_##name(p + 1, end);                    \
	}                                                     \
}                                                         \

QUICK_SORT(Lomuto);
QUICK_SORT(Hoare);
QUICK_SORT(Aleksandresku);



#define TIME_CHECK(sort, message, k)                      \
void time_check_##sort(long* arr, long len) {             \
	clock_t s0 = clock();                                 \
	quick_sort_##sort(arr, arr + len - k);                \
	clock_t s1 = clock();                                 \
	long time = s1 - s0;                                  \
	printf(message);                                      \
	printf("%ld\n", time);                                \
}                                                         \

TIME_CHECK(Lomuto, "Naive Lomuto takes: ", 0);
TIME_CHECK(Hoare, "Hoare takes: ", 1);
TIME_CHECK(Aleksandresku, "Super good Lomuto takes: ", 0);


void main() {

	long len =6000000;
	long* array_1 = (long*)malloc(len * sizeof(long));
	long* array_2 = (long*)malloc(len * sizeof(long));
	long* array_3 = (long*)malloc(len * sizeof(long));

	rand_array(array_1, len);
	copy(array_1, array_2, len);
	copy(array_1, array_3, len);
	/*rand_array(array_2, len);
	rand_array(array_3, len);*/
	//print(array_1, len);

	/*quick_sort_Lomuto(array_1, array_1 + len);
	quick_sort_Hoare(array_2, array_2 + len);
	quick_sort_Aleksandresku(array_3, array_3 + len);
	print(array_1, len);
	print(array_2, len);
	print(array_3, len);*/

	time_check_Lomuto(array_1, len);
	time_check_Hoare(array_2, len);
	time_check_Aleksandresku(array_3, len);
	free(array_1);
	free(array_2);
	free(array_3);
}
