// The Maximum Subarray
// a.k.a. Kadane's Algorithm (Maximum Sum Subarray)
// Time complexity: O(n)
// https://www.hackerrank.com/challenges/maxsubarray/problem

#include <bits/stdc++.h>
using namespace std;

pair<int, int> max_subarray_and_subsequence(vector<int>& v) {
    int max_subarray_so_far = v[0];
    int max_subarray_ending_here = 0; // Max sum of array.

    for (int i = 0; i < v.size(); i++) {
        max_subarray_ending_here += v[i];
        // If the contiguous element is greater.
        if (max_subarray_so_far < max_subarray_ending_here) {
            max_subarray_so_far = max_subarray_ending_here;
        }
        if (max_subarray_ending_here < 0) {
            max_subarray_ending_here = 0;
        }
    }
    int max_subsequence = 0;
    int max_subsequence_aux = v[0];
    for (int i = 0; i < v.size(); i++) {
        if (v[i] > 0){
            max_subsequence += v[i];
        }
        if (v[i] > max_subsequence_aux){
            max_subsequence_aux = v[i];
        }
    }
    max_subsequence = max_subsequence > 0 ? max_subsequence : max_subsequence_aux;
    return make_pair(max_subarray_so_far, max_subsequence);
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        vector<int> v;
        int n;
        cin >> n;
        for (int j = 0; j < n; ++j) {
            int x;
            cin >> x;
            v.push_back(x);
        }
        pair<int, int> r = max_subarray_and_subsequence(v);
        cout << r.first << ' ' << r.second << endl;
    }

    return 0;
}