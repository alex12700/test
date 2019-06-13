def test_fib(x1,x2):
    temp = 1 
    y = z = b = 1
    while (b <= x1 or b <= x2):
        z = y
        y = b
        b = z + y
        if (b == x):
            q = 1

    if (q == 1):
        return True    
    else:
        return False


int main()
{
    double x;
    int i,y,z,b;
    bool q;
    cout << "Vvedite chislo:" << endl;
    cin >> x;
    y = z = b = 1;
    q = 0;

    for (i = 1; i < x; i++)
    {   z = y; 
        y = b;
        b = z + y;
        if (b == x)  { q = 1; }
    }
    if (q) {cout << x << " eto chislo fib-chi." << endl; } 
        else {cout << x << " ne chislo fib-chi" << endl; };
    system ("pause");
    return 0;
}