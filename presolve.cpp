#include <bits/stdc++.h>
#define endl '\n'
#define pll pair<ll, ll>
#define tll tuple<ll, ll, ll>
#define pii pair<int, int>
#define tii tuple<int, int, int>
#define vi vector<int>
#define vl vector<ll>
#define x first
#define y second
#define all(a) a.begin() + 1, a.end()
#define rep(i, j, k) for (int i = (j); i <= (k); i++)
#define per(i, j, k) for (int i = (j); i >= (k); i--)
#define int ll
#define ios ios::sync_with_stdio(false), std::cin.tie(0), std::cout.tie(0)
typedef long long ll;
const ll maxn = 2e5 + 10;
const ll mod = 998244353;
const ll inf32 = 1e9 + 10;
const ll inf64 = 1e18 + 10;

void solve()
{
    std::ifstream file("D:/workSpace/20231019/data/credit/credit.csv"); 
    if (!file.is_open())
    {
        std::cout << "无法打开文件！" << endl;
        return;
    }

    std::vector<std::vector<std::string>> data;

    std::string line;
    while (std::getline(file, line))
    {
        std::stringstream ss(line);
        std::string cell;
        std::vector<std::string> row;
        while (std::getline(ss, cell, ','))
            row.push_back(cell);
        data.push_back(row);
    }
    file.close();
    std::string istr[] = {"checking_balance", "credit_history", "purpose", "savings_balance", "employment_length", "personal_status",
                            "other_debtors", "property", "installment_plan", "housing", "job", "telephone", "foreign_worker"};
    std::vector<std::set<std::string>> s(14);
    for (size_t col = 0; col < data[0].size(); col++)
    {
        for (int i = 0; i < 13; ++i)
        {
            if (data[0][col].substr(1, data[0][col].length() - 2) == istr[i]){
                //std::cout << "Column " << col + 1 << ":" << endl;
                for (size_t row = 1; row < data.size(); row++)
                {
                    s[i].insert(data[row][col]);
                    //std::cout << data[row][col] << endl;
                }
            }
        }
        //std::cout << endl;
    }
    std::cout << "col_dict = {" << endl;
    for (int i = 0; i < 13; ++i){
        int tot = 0;
        std::cout << '\"'<< istr[i] << '\"' << " : {";
        for (auto str : s[i]){
            std::cout << str << " : " << tot++ << ", "[str == (*s[i].rbegin())];
        }
        std::cout << "}" << ", "[i == 12];
        std::cout << endl;
    }
    std::cout << "}" << endl;
    return;
}

signed main()
{
    std::ios;
    // freopen("sample.txt", "r", stdin);
    freopen("resout.txt", "w", stdout);
    int t = 1;
    // std::cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}