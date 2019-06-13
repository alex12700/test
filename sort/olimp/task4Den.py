#include "pch.h"

#include <iostream>

#include <vector>

#include <set>

#include <algorithm>

#include <cstdlib>

#include <cassert>

#include <fstream>

using namespace std;

const int huge = 100 * 100 + 1;

int main() {
  ifstream fin("D://input.txt");
  ofstream fout("D://output.txt");
  int N, S, F;
  fin» N» S» F;
  S -= 1;
  F -= 1;

  if (N == 1 || F == S) {
    fout« 0« endl;
    return 0;
  }

  vector < vector < int > > g(N, vector < int > (N, 0));

  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      fin» g[i][j];

  vector < int > d(N, huge);
  d[S] = 0;
  vector < bool > done(N, false);
  vector < int > p(N, -1);

  while (1) {
    int min_dist = huge;
    int v = -1;
    for (int i = 0; i < N; ++i)
      if (!done[i]) {
        if (d[i] >= min_dist) continue;
        min_dist = d[i];
        v = i;
      }
    if (v == -1) break;
    done[v] = true;
    for (int i = 0; i < N; ++i)
      if (!done[i]) {
        if (g[v][i] < 0) continue;
        if (d[i] > d[v] + g[v][i]) {
          d[i] = d[v] + g[v][i];
          p[i] = v;
        }
      }
  }

  if (p[F] == -1) {
    fout« - 1« endl;
  } else {
    int r = 0;
    while (p[F] != -1) {
      r += g[p[F]][F];
      F = p[F];
    }
    fout« r« endl;
  }
  return 0;
}