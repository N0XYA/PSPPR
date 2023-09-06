#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>

using namespace std;


float find_mean(vector<int> coordinate)
{
    float mean;
    for (int coord : coordinate)
    {
        mean+= coord;
    }
    return mean / coordinate.size();
}

vector<float> find_diff(vector<int> coordinate, float mean)
{
    int size = coordinate.size();
    vector<float> diff(size);
    for(int i = 0; i < size; i++)
    {
        diff.at(i) = coordinate.at(i) - mean;
    }
    return diff;
}

vector<float> find_square_diff(vector<float> diff)
{
    int size = diff.size();
    vector<float> sqr_diff(size);
    for(int i = 0; i < size; i++)
    {
        sqr_diff[i] = pow(diff[i], 2);
    }
    return sqr_diff;
}

float find_vec_sum(vector<float> coordinate)
{
    float sum;
    for (int i = 0; i < coordinate.size(); i++)
    {
        sum+=coordinate[i];
    }
    return sum;
}

vector<float> multiply_diffs(vector<float> x, vector<float> y)
{
    int size = x.size();
    vector<float> result(size);
    for(int i = 0; i < size; i++)
    {
        result[i] = x[i] * y[i];
    }
    return result;
}
int main()
{
    float b0, b1;
    string path = "C:\\Users\\user\\PycharmProjects\\PSPPR\\cpp_lin_regression.txt";

    vector<int> x{1, 2, 3, 4, 5};
    vector<int> y{2, 4, 5, 4, 5};

    float xmean = find_mean(x);
    float ymean = find_mean(y);

    vector<float> x_difference = find_diff(x, xmean);
    vector<float> y_differnece = find_diff(y, ymean);

    vector<float> x_sqr_diff = find_square_diff(x_difference);
    float x_sqr_diff_sum = find_vec_sum(x_sqr_diff);
    vector<float> multy_arr = multiply_diffs(x_difference, y_differnece);
    float multy_sum = find_vec_sum(multy_arr);
    b1 = multy_sum / x_sqr_diff_sum;
    b0 = ymean - b1 * xmean;
    cout << b1 << ' ' << b0;

    fstream fs;
    fs.open(path, fstream::out);
    for(int i = 0; i < x.size(); i++)
    {
        fs << x[i] << ',' << y[i] << '\n';
    }
    fs << b0 << ',' << b1;
    fs.close();
    return 0;
}