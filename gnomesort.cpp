#include <iostream>
using namespace std;
//Gnome sort

int main()
{
    int l[5] = { 5, 3 , 1 , 2 , 4};     //initialize data
    int n = sizeof(l)/sizeof(l[0]);          //length of l
    for (int i = 0; i < 5; ++i)
        {
        cout << l[i] << endl;
        }
    for (int i = 1; i <= n; ++i)
        {
        if (l[i] >= l[i-1])
            {
            i++;
            }
        if (l[i] < l[i-1])
            {
            int temp = l[i];
            l[i] = l[i-1];       //swap
            l[i-1] = temp;
            i--;
            }
        }
    for (int i = 0; i < 5; ++i)
        {
        cout << l[i] << endl;
        }
}
