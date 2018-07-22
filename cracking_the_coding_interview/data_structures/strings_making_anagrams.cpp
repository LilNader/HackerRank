#include <bits/stdc++.h>

using namespace std;

int chars_to_remove(vector<int> v1, vector<int> v2) {
    int r = 0;
    for(int i = 0; i<26; i++){
        r += abs(v1[i] - v2[i]);
    }
    return r;
}

vector<int> get_ocurrences(string a) {
    vector<int> occurrences(26);
    for(int i=0; i<a.size(); i++){
        int aux = a[i] - 'a';
        occurrences[aux]++;
    }
    return occurrences;
}

// Complete the makeAnagram function below.
int makeAnagram(string a, string b) {
    vector<int> occurrences_a = get_ocurrences(a);
    vector<int> occurrences_b = get_ocurrences(b);
    return chars_to_remove(occurrences_a, occurrences_b);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
