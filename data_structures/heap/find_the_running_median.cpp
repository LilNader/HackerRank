// Find the Running Median
// https://www.hackerrank.com/challenges/find-the-running-median/problem

#include <bits/stdc++.h>
using namespace std;

#define max_heap priority_queue<int>
#define min_heap priority_queue<int, vector<int>, greater<int> >

double get_median(max_heap& l_than_med, min_heap& g_than_med){
    if((g_than_med.size() + l_than_med.size()) % 2 == 0){
        return ((double) g_than_med.top() + l_than_med.top()) / 2;
    } else{
        if (l_than_med.size() > g_than_med.size()){
            return l_than_med.top();
        } else{
            return g_than_med.top();
        }
    }
}

void rebalance_heaps(max_heap& l_than_med, min_heap& g_than_med){
    if(g_than_med.size() - l_than_med.size() == 2){
        int x = g_than_med.top();
        g_than_med.pop();
        l_than_med.push(x);
    } else if(l_than_med.size() - g_than_med.size() == 2){
        int x = l_than_med.top();
        l_than_med.pop();
        g_than_med.push(x);
    }
}

void add_to_heap(int x, max_heap& l_than_med, min_heap& g_than_med){
    if(l_than_med.empty() || x <= l_than_med.top()){
        l_than_med.push(x);
    } else{
        g_than_med.push(x);
    }
}

vector<double> get_medians(vector<int>& v){
    vector<double> medians;
    max_heap l_than_med; // Store values greater than the median
    min_heap g_than_med; // Store values less than the median
    for(int i=0; i<v.size(); i++){
        add_to_heap(v[i], l_than_med, g_than_med);
        rebalance_heaps(l_than_med, g_than_med);
        medians.push_back(get_median(l_than_med, g_than_med));
    }
    return medians;
}

int main(){
    int n, x;
    vector<int> v;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> x;
        v.push_back(x);
    }
    cout << setprecision(1) << fixed;

    vector<double> medians = get_medians(v);
    for (int i = 0; i < n; i++){
        cout << medians[i] << endl;
    }
    return 0;
}